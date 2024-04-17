import pandas as pd
from datetime import datetime, timezone
# Считываем данные из файла input.txt в DataFrame
df = pd.read_csv("input.txt", sep=",", names=[
    "id", "user_id", "timestamp", "billing_period", "billing_total_price_usd"], skiprows=1)


def process(df):
    """_summary_

    Args:
        df (Dateframe): _description_
    """
    if df.empty:
        return 0

    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

    df['end_date'] = df.apply(
        lambda row: row['timestamp'] + pd.Timedelta(days=row['billing_period']), axis=1)
    df['fin_contrib'] = df.apply(
        lambda row: row['billing_total_price_usd'] / row['billing_period'], axis=1)

    def count_days_in_feb(row):
        feb_start = pd.Timestamp(2024, 2, 1)
        feb_end = pd.Timestamp(2024, 3, 1)
        return min(row['end_date'], feb_end) - max(row['timestamp'], feb_start)

    df['days_pay_in_february'] = df.apply(
        count_days_in_feb, axis=1).dt.days
    
    df['fin_contrib_in_february'] = df.apply(
        lambda row: row['days_pay_in_february'] * row['fin_contrib'], axis=1)
    
    # Предположим, что если нет данных за февраль или нет пользователей вообще, вернем 0
    if df['days_pay_in_february'].sum() == 0 or len(df['user_id'].unique()) == 0:
        return 0
    user_contrib = df.groupby('user_id')['fin_contrib_in_february'].sum()
    top_3_users = user_contrib.nlargest(3)
    return round(top_3_users.sum(), 2)


print(process(df))

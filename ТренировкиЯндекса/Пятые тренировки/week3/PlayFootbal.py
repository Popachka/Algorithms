import json
from collections import defaultdict
history = {}
count_goal_players = defaultdict(int)
with open('C:\MyFiles\PyCode\Alg\ТренировкиЯндекса\Пятые тренировки\week3\platfoot.txt', 'r') as file:
    numberline = 1
    count_match = 0
    count_goals = 0
    first_goal = [None, 10**8, None] # [Номер команды, минуиа гола, имя игрока]
    teams = ('team1', 'team2')
    for line in file:
        line = line.strip()

        #Проверяем является ли строка матчем
        if '-' in line:
            count_match += 1
            parts = line.split('-')
            team1 = parts[0].strip()[1:-1]
            tmp_for_team_and_score = parts[1].split()
            team2 = ' '.join(tmp_for_team_and_score[:-1]).strip()[1:-1]
            score = tmp_for_team_and_score[-1].strip().split(':')
            score_team1 = int(score[0])
            score_team2 = int(score[1])
            history[count_match] = {
                'team1': {
                    'name': team1,
                    'players': [],
                    'total_goals': score_team1
                },
                'team2':
                {
                    'name': team2,
                    'players': [],
                    'total_goals': score_team2
                },
                'first_goal': [None, 10**8, None]
            }
            count_goals = score_team1 + score_team2
        #Если у нас была информация, что мы обрабатываем матч, то заносим все в словарь
        elif count_goals != 0:
            team = None
            if len(history[count_match]['team1']['players']) != score_team1: # Проверяем, соответсвуюет ли кол-во игроков, набранным очкам
                parts = line.split()
                player_name = ' '.join(parts[:-1])
                count_goal_players[player_name] += 1
                goal_minute = int(parts[-1].strip()[:-1])
                history[count_match]['team1']['players'].append({
                    'name': player_name,
                    'goal_minute': goal_minute
                })
                count_goals -= 1
                team = team1
            elif len(history[count_match]['team2']['players']) != score_team2: # Проверяем, соответсвуюет ли кол-во игроков, набранным очкам
                parts = line.split()
                player_name = ' '.join(parts[:-1])
                count_goal_players[player_name] += 1

                goal_minute = int(parts[-1].strip()[:-1])
                history[count_match]['team2']['players'].append({
                    'name': player_name,
                    'goal_minute': goal_minute
                })
                count_goals -= 1
                team = team2

            now_goal = [team,goal_minute, player_name]
            first_goal =  min(now_goal, first_goal, key= lambda x: x[1])

            if count_goals == 0:
                history[count_match]['first_goal'] = first_goal
                first_goal = [None, 10**8, None]
        #Если это никакой информации, что мы обрабатываем матч не было, то обрабатываем запрос
        else:
            if 'Total goals for' in line: # Кол-во голов команды за все матчи
                team_name = line.split('Total goals for')[-1].strip()[1:-1]
                total_goals = 0
                for matchnumber,matchinfo in history.items():
                    for team in teams:
                        if matchinfo[team]['name'] == team_name:
                            total_goals += matchinfo[team]['total_goals']
                print(total_goals)
            elif 'Total goals by' in line:
                player_name = line.split('Total goals by')[-1].strip()
                total_goals = count_goal_players[player_name]
                print(total_goals)
            elif 'Mean goals per game for' in line:
                team_name = line.split('Mean goals per game for')[-1].strip()[1:-1]
                total_goals = 0
                count_game_this_team = 0
                for matchnumber,matchinfo in history.items():
                    for team in teams:
                        if matchinfo[team]['name'] == team_name:
                            count_game_this_team += 1
                            total_goals += matchinfo[team]['total_goals']
                if count_game_this_team == 0:
                    print(0)
                else:
                    print(total_goals / count_game_this_team,)

            elif 'Mean goals per game by' in line:
                player_name = line.split('Mean goals per game by')[-1].strip()
                player_team = None
                for matchnumber,matchinfo in history.items():
                    for team in teams:
                        for player in matchinfo[team]['players']:
                            if player['name'] == player_name:
                                player_team = matchinfo[team]['name']
                                break
                total_goals = count_goal_players[player_name]
                total_games_this_team = 0
                for matchnumber,matchinfo in history.items():
                    for team in teams:
                        if matchinfo[team]['name'] == player_team:
                            total_games_this_team += 1

                if total_games_this_team == 0:
                    print(0)
                else:
                    print(total_goals / total_games_this_team,)
            elif 'Goals on minute' in line:
                parts = line.split()
                minute = int(parts[3].strip())
                player_name = ' '.join(parts[5:])
                total_goals = 0
                for _, info in history.items():
                    for team in teams:
                        players = info[team]['players']
                        for player_info in players:
                            if player_info['goal_minute'] == minute and player_info['name'] == player_name:
                                total_goals += 1
                print(total_goals)
            elif 'Goals on first' in line:
                parts = line.split()
                minute = int(parts[3].strip())
                player_name = ' '.join(parts[6:])
                total_goals = 0
                for _, info in history.items():
                    for team in teams:
                        players = info[team]['players']
                        for player_info in players:
                            if player_info['goal_minute'] <= minute and player_info['name'] == player_name:
                                total_goals += 1
                print(total_goals)
            elif 'Goals on last' in line:
                parts = line.split()
                minute = int(parts[3].strip())
                player_name = ' '.join(parts[6:])
                total_goals = 0
                for _, info in history.items():
                    for team in teams:
                        players = info[team]['players']
                        for player_info in players:
                            if (91 - minute <= player_info['goal_minute'] <= 90) and player_info['name'] == player_name:
                                total_goals += 1
                print(total_goals)
            elif 'Score opens by' in line and '"' in line:
                team_name = line.split('Score opens by')[-1].strip()[1:-1]
                total_first_goals = 0
                for matchnumber,matchinfo in history.items():
                    if matchinfo['first_goal'][0] == team_name:
                        total_first_goals += 1
                print(total_first_goals)
            elif 'Score opens by' in line:
                player_name = line.split('Score opens by')[-1].strip()
                total_first_goals = 0
                for matchnumber,matchinfo in history.items():
                    if matchinfo['first_goal'][2] == player_name:
                        total_first_goals += 1
                print(total_first_goals)
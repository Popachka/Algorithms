

def calc_ball(F1,F2,S1,S2,l):
    first_team_count = F1 + S1
    second_team_count = F2 + S2
    needed_ball = 0
    # Check the condition based on the given rules
    if first_team_count > second_team_count:
        needed_ball = 0
    elif first_team_count < second_team_count:
        # Check if the second team won at home or away
        if (l == 1 and F2 >= second_team_count - first_team_count) or (l == 2 and S2 >= F1):
            needed_ball = second_team_count - first_team_count + 1
        else:
            needed_ball = second_team_count - first_team_count
    else:
        # Check if the second team won at home or away
        if (l == 1 and F2 >= S1) or (l == 2 and S2 <= F1):
            needed_ball = 1
        else:
            needed_ball = 0
    # Output the result
    print(needed_ball)

F1,F2 = list(map(int,input().split(':')))
S1,S2 = list(map(int, input().split(':')))
l = int(input())
first_team_count = F1 + S1
second_team_count = F2 + S2
needed_ball = 0
if first_team_count > second_team_count:
    needed_ball = 0
elif first_team_count < second_team_count:
    if (l == 1 and F2 >= S1 + second_team_count - first_team_count) or (l == 2 and S2 >= F1):
        needed_ball = second_team_count - first_team_count + 1
    else:
        needed_ball = second_team_count - first_team_count
else:
    if (l == 1 and F2 >= S1) or (l == 2 and S2 >= F1):
        needed_ball = 1
    else:
        needed_ball = 0
print(needed_ball)
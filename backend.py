from rearr_gantt import rearr_gantt

# Fixture generation code


def arr_rotate(arr):
    x = []
    x.append(arr[-2])
    for i in range(0, len(arr) - 2):
        x.append(arr[i])
    x.append(arr[-1])
    return x


tL = []


def schedule(team_list):
    l = len(team_list)

    rotate = team_list
    team_map = {}
    teams = list(map(str, input("Enter team names: ").split()))
    if (len(teams) % 2 != 0):
        teams.append('bye')

    for i in range(l):
        team_map[i+1] = teams[i]
    for i in range(l-1):
        rotate = arr_rotate(rotate)
        left = 0
        right = l-1

        while(left < right):
            tL.append([team_map[rotate[left]], team_map[rotate[right]]])
            # print(tL)
            left += 1
            right -= 1
    # sendData()


def sendData():
    global tL
    l = range(1, 9)
    schedule(l)
    tL = rearr_gantt(tL)
    return tL

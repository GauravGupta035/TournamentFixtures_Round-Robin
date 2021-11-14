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
    teams = list(map(str, input("Enter ").split()))
    for i in range(l):
        team_map[i+1] = teams[i]
    for i in range(l-1):
        rotate = arr_rotate(rotate)
        left = 0
        right = l-1
        print("-----Round ", i+1, " Fixtures-----")
        while(left < right):
            tL.append([team_map[rotate[left]], team_map[rotate[right]]])
            # print(tL)
            print("Team ", team_map[rotate[left]],
                  " Plays Team ", team_map[rotate[right]])
            left += 1
            right -= 1
    # sendData()


def sendData():
    l = range(1, 9)
    schedule(l)
    return tL

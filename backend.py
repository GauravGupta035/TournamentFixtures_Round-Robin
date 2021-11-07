# Fixture generation code

def arr_rotate(arr):
    x = []
    x.append(arr[-2])
    for i in range(0, len(arr) - 2):
        x.append(arr[i])
    x.append(arr[-1])
    return x


def schedule(team_list):
    l = len(team_list)
    rotate = team_list
    team_map = {1: 'DC', 2: 'PBKS', 3: 'RR', 4: 'KKR',
                5: 'MI', 6: 'RCB', 7: 'SRH', 8: 'CSK'}
    for i in range(l-1):
        rotate = arr_rotate(rotate)
        left = 0
        right = l-1
        print("-----Round ", i+1, " Fixtures-----")
        while(left < right):
            print("Team ", team_map[rotate[left]],
                  " Plays Team ", team_map[rotate[right]])
            left += 1
            right -= 1


l = list(map(int, input("Enter list ").split()))
schedule(l)

import CHaser
#0:なし（床）
#1:相手
#2:ブロック
#3:アイテム
client = CHaser.Client()
#1.벽 확인
#2.9칸 이내 다이아 확인
def checkValue(value): #주위 9칸 탐색
    if 3 in value:
        return 'item'
    elif 1 in value:
        return 'enemy'
    elif 2 in value:
        return 'block'
    value = client.get_ready()
    value = [value[1], value[4], value[6], value[8]]
    if 0 not in value:
        return 'break'
    else:
        return 'print('')'
def main():
    while(True):
        up = 'client.walk_up()'
        down = 'client.walk_down()'
        left = 'client.walk_left()'
        right = 'client.walk_right()'
        moveList = [[[up, left],[left,up]],[up],[[up, right],[right,up]],[left],[right],[[down, left],[left,down]],[down],[[down, right],[right,down]]]

        value = client.get_ready() #ex : [2, 0, 0, 0, 0, 0, 0, 0, 2], chaserEx.png
        print(value)
        if 1 in [value[0], value[3], value[5], value[7]]: #상대 확인
            value = [value[0], value[3], value[5], value[7]]
            enemy = value.index(1)
            if enemy == 0:
                client.put_up()
            elif enemy == 1:
                client.put_left()
            elif enemy == 2:
                client.put_right()
            elif enemy == 3:
                client.put_down()
            else:
                print('error')
                exit()
        else:
            CV = checkValue(value)
            if CV == 'item':
                mainItem = value.index(3)
                if mainItem <= 3:
                    []

if __name__ == "__main__":
    main()
def moveChack(value, MainItem, way):
    MCList = [[0,1,2],[3,5],[7,8,9]]
    waypoint = {'up' : 0, 'middle' : 1, 'down' : 2}
    moveway = MCList[waypoint[way]]
    if MainItem == MCList[waypoint[way]][0]:
        if MainItem == 0:
            if (value[1] == 2 or value[3] == 2):
                if (value[1] == 2 and value[3] == 2):
                    return 'None None'
                elif value[1] == 2:
                    return 'left up'
                else:
                    return 'up left'
            else:
                return 'up left'
        elif MainItem == 1:
            return 'up stop'
        else:
            if (value[1] == 2 or value[5] == 2):
                if (value[1] == 2 and value[5] == 2):
                    return 'None None'
                elif value[1] == 2:
                    return 'right up'
                else:
                    return 'up right'
            else:
                return 'up right'
    elif MainItem == MCList[waypoint[way]][1]:
        if MainItem == 3:
            return 'left stop'
        else:
            return 'right stop'
    else: #대충 손봄(자세히 다시보기)
        if MainItem == 6:
            if (value[7] == 2 or value[3] == 2):
                if (value[7] == 2 and value[3] == 2):
                    return 'None None'
                elif value[7] == 2:
                    return 'left down'
                else:
                    return 'down left'
            else:
                return 'down left'
        elif MainItem == 7:
            return 'down stop'
        else:
            if (value[7] == 2 or value[5] == 2):
                if (value[7] == 2 and value[5] == 2):
                    return 'None None'
                elif value[7] == 2:
                    return 'right down'
                else:
                    return 'down right'
            else:
                return 'down right'

#def moveThink(): #상하좌우 9칸씩 확인
    #valueL = client.look_left()
    #valueR = client.look_right()
    #valueU = client.look_up()
    #valueD = client.look_down()
    #if valueL in 3:
    #    return 'L'
    #elif valueR in 3:
    #    return 'R'
    #elif valueU in 3:
    #    return 'U'
    #elif valueD in 3:
    #    return 'D'
    #else:
    #    return 'N'
#def moveAI():
    #value = moveThink()
    #if value == 'L':
    #    value = client.look_left()
#def canmove(): #상하좌우 나가는 길 탐색
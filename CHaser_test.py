import CHaser
#1.벽 확인
#2.9칸 이내 다이아 확인
def checkValue(value): #주위 9칸 탐색
    if 3 in value:
        return 'item'
    elif 1 in value:
        return 'enemy'
    elif 2 in value:
        return 'break'
    value = [value[1], value[4], value[6], value[8]]
    if 0 not in value:
        return 'break'
    else:
        return 'pass'
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
    else:
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
def main():
    value = []
    lastmove = 'None'
    client = CHaser.Client()
    while(True):
        movemain = {'up' : 'client.walk_up()', 'down' : 'client.walk_down()', 'left' : 'client.walk_left()', 'right' : 'client.walk_right()', 'None' : 'pass'}
        moveList = [[['up', 'left'],['left','up']],['up'],[['up', 'right'],['right','up']],['left'],['right'],[['down', 'left'],['left','down']],['down'],[['down', 'right'],['right','down']]]
        value = client.get_ready() #ex : [2, 0, 0, 0, 0, 0, 0, 0, 2], chaserEx.png
        if 1 in [value[1], value[3], value[5], value[7]]: #상대 확인
            Evalue = [value[1], value[3], value[5], value[7]]
            enemy = Evalue.index(1)
            if enemy == 0:#상단
                value = client.put_up()
                lastmove = 'None'
            elif enemy == 1:#좌측
                value = client.put_left()
                lastmove = 'None'
            elif enemy == 2:#우측
                value = client.put_right()
                lastmove = 'None'
            elif enemy == 3:#하단
                value = client.put_down()
                lastmove = 'None'
            else:
                print('error')
                #exit()
        elif 1 in [value[0],value[2],value[6],value[8]]:#각 모서리에 적이 있으면 -> continue하고 위로
            value = client.look_left()
        else:
            CV = checkValue(value)
            if CV == 'item':
                mainItem = value.index(3)
                if mainItem <= 3:
                    uvalue = client.look_up()
                    mainmove = moveChack(value,mainItem,'up')
                    mmove = mainmove.split(' ')
                    for i in mmove:
                        value = eval(movemain[i])
                        lastmove = i
                elif 4<= mainItem <= 6:
                    if mainItem == 4:
                        lvalue = client.look_left()
                    else:
                        rvalue = client.look_right()
                    mainmove = moveChack(value,mainItem,'middle')
                    mmove = mainmove.split(' ')
                    for i in mmove:
                        value = eval(movemain[i])
                        lastmove = i
                elif mainItem >= 6:
                    dvalue = client.look_down()
                    mainmove = moveChack(value,mainItem,'down')
                    mmove = mainmove.split(' ')
                    for i in mmove:
                        value = eval(movemain[i])
                        lastmove = i
            elif CV == '':
                pass

if __name__ == "__main__":
    main()
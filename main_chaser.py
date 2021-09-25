import CHaser
import random

wayList = ['up','left','down','right']

wayListNum = {'up': '0 1 2', 'left': '0 3 6', 'down': '6 7 8','right': '2 5 8'}

movemain = {'up' : 'client.walk_up()', 'down' : 'client.walk_down()', 'left' : 'client.walk_left()', 'right' : 'client.walk_right()', 'None' : 'pass'}

moveList = [[['up', 'left'],['left','up']],['up'],[['up', 'right'],['right','up']],['left'],['right'],[['down', 'left'],['left','down']],['down'],[['down', 'right'],['right','down']]]

waypoint = {'up':'1','left':'3','right':'5','down':'7'}

Nviewpoint = {'up':'down','left':'right','down':'up','right':'left'}

leftRight = {'up':['3','5'], 'left':['7','1'], 'right':['1','7'], 'down':['5','3']}

diagoline = {'0': ['1','3'], '2': ['1','5'], '6' : ['7','3'], '8': ['5','7']}

toMove = {1 : 'up', 3 : 'left', 5 : 'right', 7 : 'down'}
Moveto = {'up' : 1, 3 : 'left', 'right' : 5, 'down' : 7}
def get_key(val, dic):
    for key, value in dic.items():
        if val == value:
            return key
    return('키가 없습니다')

def main():
    lookbool = None
    firstway = None
    Evalue = None
    enemy = None
    item_loca = None
    lookvalue = None
    space = None
    Exit = None
    lastMove = None
    enemycount = 0
    lookbool = False
    viewpoint = 'None'
    firstmove = False
    value = []
    client = CHaser.Client()
    firstway = random.choice(wayList)
    print(firstway)

    while(True):
        #byunsuDic = f"'viewpoint' : {viewpoint}, 'lastMove' : {lastMove}, 'enemycount' : {enemycount}, 'lookbool' : {lookbool}, 'value' : {value}, 'firstmove' : {firstmove}, 'firstway' : {firstway}, 'Evalue' : {Evalue}, 'enemy' : {enemy}, 'int(wayListNum[firstway[2])' : {int(wayListNum[firstway[2]])}, 'Nviewpoint' : {Nviewpoint}, 'value.index(3)' : {value.index(3)}, 'item_loca' : {item_loca}, 'lookvalue' : {lookvalue}, 'lookbool' : {lookbool}, 'space' : {space}, 'Exit' : {Exit}, 'int(waypoint[viewpoint])' : {int(waypoint[viewpoint])}, 'int[leftRight[viewpoint][1])]' : {int[leftRight[viewpoint][1]]}, 'int[leftRight[viewpoint][0])]' : {int(leftRight[viewpoint][1])}, 'Moveto[Nviewpoint[lastMove]]' : {Moveto[Nviewpoint[lastMove]]}" if firstmove == True else 'sans'
        print('start')
        #print('print variable, ', byunsuDic)
        value = client.get_ready() #ex : [2, 0, 0, 0, 0, 0, 0, 0, 2], chaserEx.png
        print('get ready')

        if 1 in [value[1], value[3], value[5], value[7]]: #상대 확인
            print('enemy')
            Evalue = [value[1], value[3], value[5], value[7]]
            enemy = Evalue.index(1)
            if enemy == 0:#상단
                value = client.put_up()

            elif enemy == 1:#좌측
                value = client.put_left()

            elif enemy == 2:#우측
                value = client.put_right()

            elif enemy == 3:#하단
                value = client.put_down()

            else:
                print('error')
                #exit()

        elif 1 in [value[0],value[2],value[6],value[8]] and enemycount <= 4:#각 모서리에 적이 있으면 + 턴 4번 안지났으면 -> 옆보고 continue하고 위로
            print('enemy_look')
            value = client.look_left()
            enemycount += 1
            continue

        elif enemycount > 4: #턴 4번 넘었을때
            Evalue = [value[1], value[3], value[5], value[7]]
            enemy = Evalue.index(1)
            if enemy == 0:#좌측 상단 적
                if value[5] == 0:
                    value = client.walk_right()
                    enemycount = 0
                elif value[7] == 0:
                    value = client.walk_down()
                    enemycount = 0
                else:
                    value = eval(random.choice(['client.walk_left()', 'client.walk_up()']))
            elif enemy == 2:
                if value[3] == 0:
                    value = client.walk_left()
                    enemycount = 0
                elif value[7] == 0:
                    value = client.walk_down()
                    enemycount = 0
                else:
                    value = eval(random.choice(['client.walk_right()', 'client.walk_up()']))
                    enemycount = 0
            elif enemy == 6:
                if value[1] == 0:
                    value = client.walk_up()
                    enemycount = 0
                elif value[5] == 0:
                    value = client.walk_right()
                    enemycount = 0
                else:
                    value = eval(random.choice(['client.walk_left()', 'client.walk_right()']))
                    enemycount = 0
            elif enemy == 8:
                if value[1] == 0:
                    value = client.walk_up()
                    enemycount = 0
                elif value[3] == 0:
                    value = client.walk_left()
                    enemycount = 0
                else:
                    value = eval(random.choice(['client.walk_right()', 'client.walk_down()']))
                    enemycount = 0

        elif firstmove == False:
            print('first move cheak')
            while value[int(wayListNum[firstway][2])] == 2:
                for i in range(2):
                    if wayList.index(firstway) == 3:
                        firstway = wayList[0]

                    else:
                        firstway = wayList[wayList.index(firstway) + 1]
            value = eval(movemain[firstway])
            firstmove = True
            viewpoint = movemain[firstway][12:][:-2]
            lastMove = movemain[firstway][12:][:-2]
            print('end first moving')
        else:

            print(f'moving, value = {value}')

            if 3 in value:
                print('find item')
                if value[int(waypoint[viewpoint])] == 3:#아이템 정면일때
                    if lookbool == True:#client.look_방향이 된 상태일때
                        if lookvalue[4] == 2:#                          ㄱ
                            if lookvalue[2] == 2 and lookvalue[8] == 2: #아이템 사방이 막혀있을때
                                value = eval(f'client.walk_{viewpoint}()')
                                value = client.get_ready()
                                value = eval(f'client.walk_{Nviewpoint[viewpoint]}()')
                                lastMove = Nviewpoint[viewpoint]
                                viewpoint = Nviewpoint[viewpoint]
                                lookbool = False
                    else:
                        valueBool = type(value.index(3)) == list
                        if valueBool:
                            item_loca = value.index(3)[0]
                        else:
                            item_loca = value.index(3)
                        viewpoint = toMove[item_loca]
                        value = eval(f'client.look_{viewpoint}()')
                        lookvalue = value
                        lookbool = True
                elif value[1] == 3 or value[3] == 3 or value[5] == 3  or value[7] == 3:
                    print('item in UDLR')
                    valueBool = type(value.index(3)) == list
                    if valueBool:
                        item_loca = value.index(3)[0]
                    else:
                        item_loca = value.index(3)
                    viewpoint = toMove[item_loca]
                    value = eval(f'client.look_{viewpoint}()')
                else:#정면이 아닌 다른곳에 아이템이 있을때
                    print('item in not front')
                    valueBool = type(value.index(3)) == list
                    if valueBool:
                        item_loca = value.index(3)[0]
                    else:
                        item_loca = value.index(3)
                    space = None
                    for i in diagoline[item_loca]:
                        if value[i] == 0:
                            space = i
                            return
                        else:
                            continue

                    if item_loca == 0 or item_loca == 2 or item_loca == 6 or item_loca == 8: #아이템이 대각선에 있을때
                        print('item in diagonal')
                        if space != None:
                            value = eval(f'client.walk_{toMove[space]}()')
                            lastMove = toMove[space]
                        else:
                            Exit = None
                            ExitList = [1,3,5,7]
                            for i in ExitList:
                                if value[i] == Moveto[Nviewpoint[lastMove]]:
                                    continue
                                if value[i] == 2:
                                    continue
                                elif value[i] == 0 or value[i] == 3:
                                    Exit = i
                                    break
                                else:
                                    break
                            if Exit != None:
                                value = eval(f'client.walk_{toMove[Exit]}')
                                viewpoint = toMove[Exit]
                                lastMove = toMove[Exit]


            elif value[int(waypoint[viewpoint])] == 2:#바로앞(가는방향)이 벽일때
                print('front is block')

                if value[int(waypoint[viewpoint])-1] == 0 and value[int(leftRight[viewpoint][0])] == 0: #왼쪽과 왼쪽 위 전부 열렸을때
                    print(f'and left and left up open, lastMove : {lastMove}')
                    if toMove[int(leftRight[viewpoint][0])] == Moveto[Nviewpoint[lastMove]]:
                        print(f'but it was already gone way')
                        if int(leftRight[viewpoint][1]) == 0:
                            value = eval(f'client.walk_{toMove[int(leftRight[viewpoint][1])]}()')
                        else:
                            print('but front is block')
                            Exit = None
                            ExitList = [1,3,5,7]
                            for i in ExitList:
                                if value[i] == Moveto[Nviewpoint[lastMove]]:
                                    continue
                                if value[i] == 2:
                                    continue
                                elif value[i] == 0 or value[i] == 3:
                                    Exit = i
                                    break
                                else:
                                    break
                    else:
                        #value = eval(f'client.walk_{lastMove}()')
                        value = eval(f'client.walk_{toMove[int(leftRight[viewpoint][0])]}()')
                        lastMove = toMove[int(leftRight[viewpoint][0])]

                elif value[int(waypoint[viewpoint]) + 1] == 0 and value[int(leftRight[viewpoint][1])] == 0: #오른쪽과 오른쪽 위 전부 열렸을때
                    print(f'and right and right up open, lastMove : {lastMove}')
                    if toMove[int(leftRight[viewpoint][1])] == Moveto[Nviewpoint[lastMove]]:
                        print(f'but it was already gone way')
                        if int(leftRight[viewpoint][1]) == 0:
                            value = eval(f'client.walk_{toMove[int(leftRight[viewpoint][0])]}()')
                        else:
                            print('but front is block')
                            Exit = None
                            ExitList = [1,3,5,7]
                            for i in ExitList:
                                if value[i] == Moveto[Nviewpoint[lastMove]]:
                                    continue
                                if value[i] == 2:
                                    continue
                                elif value[i] == 0 or value[i] == 3:
                                    Exit = i
                                    break
                                else:
                                    break
                            if Exit != None:
                                value = eval(f'client.walk_{toMove[Exit]}()')
                                viewpoint = toMove[Exit]
                                lastMove = toMove[Exit]
                    else:
                        #value = eval(f'client.walk_{lastMove}()')
                        value = eval(f'client.walk_{toMove[int(leftRight[viewpoint][1])]}()')
                        lastMove = toMove[int(leftRight[viewpoint][1])]

                elif value[int(waypoint[viewpoint])] == 2 and value[int(waypoint[viewpoint]) +1] == 2 and value[int(waypoint[viewpoint]) -1] == 2: # 가는 방향 3개 다 막혔을때
                    print(f'and front 3 is all block, lastMove : {lastMove}')
                    Exit = None
                    ExitList = [1,3,5,7]
                    for i in ExitList:
                        if value[i] == Moveto[Nviewpoint[lastMove]]:
                            continue
                        if value[i] == 2:
                            continue
                        elif value[i] == 0 or value[i] == 3:
                            Exit = i
                            break
                        else:
                            break
                    if Exit != None:
                        value = eval(f'client.walk_{toMove[Exit]}()')
                        viewpoint = toMove[Exit]
                        lastMove = toMove[Exit]
                    else:
                        value = eval(f'client.walk_{lastMove}()')
            else: #없을때
                print(f'moving viewpoint, lastMove : {lastMove}')
                value = eval(movemain[viewpoint])
                lastMove = viewpoint


if __name__ == "__main__":
    main()
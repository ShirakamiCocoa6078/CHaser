import CHaser
import random


#ファンインソンが作りました。

wayList = ['up','left','down','right']

wayListNum = {'up': '0 1 2', 'left': '0 3 6', 'down': '6 7 8','right': '2 5 8'}

movemain = {'up' : 'client.walk_up()', 'down' : 'client.walk_down()', 'left' : 'client.walk_left()', 'right' : 'client.walk_right()', 'None' : 'pass'}

moveList = [[['up', 'left'],['left','up']],['up'],[['up', 'right'],['right','up']],['left'],['right'],[['down', 'left'],['left','down']],['down'],[['down', 'right'],['right','down']]]

waypoint = {'up':'1','left':'3','right':'5','down':'7'}

Nviewpoint = {'up':'down','left':'right','down':'up','right':'left'}

leftRight = {'up':['3','5'], 'left':['7','1'], 'right':['1','7'], 'down':['5','3']}

diagoline = {'0': ['1','3'], '2': ['1','5'], '6' : ['7','3'], '8': ['5','7']}

toMove = {1 : 'up', 3 : 'left', 5 : 'right', 7 : 'down'}
Moveto = {'up' : 1, 'left' : 3, 'right' : 5, 'down' : 7}
def get_key(val, dic):
    for key, value in dic.items():
        if val == value:
            return key
    return('키가 없습니다')

def find_index(data, target):
    res = []
    lis = data
    while True:
        try:
            res.append(lis.index(target) + (res[-1]+1 if len(res)!=0 else 0))
            lis = data[res[-1]+1:]
        except:
            break
    return res

def main():
    firstway = None
    Evalue = None
    enemy = None
    item_loca = None
    space = None
    lookbool = False
    lookvalue = None
    Exit = None
    lastMove = None
    enemycount = 0
    viewpoint = 'None'
    firstmove = False
    value = []
    lookDelete = []
    turn = 0
    client = CHaser.Client()
    firstway = random.choice(wayList)
    print(firstway)

    while(True):
        #byunsuDic = f"'viewpoint' : {viewpoint}, 'lastMove' : {lastMove}, 'enemycount' : {enemycount}, 'lookbool' : {lookbool}, 'value' : {value}, 'firstmove' : {firstmove}, 'firstway' : {firstway}, 'Evalue' : {Evalue}, 'enemy' : {enemy}, 'int(wayListNum[firstway[2])' : {int(wayListNum[firstway[2]])}, 'Nviewpoint' : {Nviewpoint}, 'value.index(3)' : {value.index(3)}, 'item_loca' : {item_loca}, 'lookvalue' : {lookvalue}, 'lookbool' : {lookbool}, 'space' : {space}, 'Exit' : {Exit}, 'int(waypoint[viewpoint])' : {int(waypoint[viewpoint])}, 'int[leftRight[viewpoint][1])]' : {int[leftRight[viewpoint][1]]}, 'int[leftRight[viewpoint][0])]' : {int(leftRight[viewpoint][1])}, 'Moveto[Nviewpoint[lastMove]]' : {Moveto[Nviewpoint[lastMove]]}" if firstmove == True else 'sans'
        turn += 1
        print(f'start, turn : {turn}')
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
#-------------------------이동(아이템)----------------------------------------------------------------------------
            if 3 in value:
                print('find item')
                item_loca = find_index(value, 3)
                for i in lookDelete:
                    item_loca.pop(i)
                if value[int(waypoint[viewpoint])] == 3:#아이템 정면일때
                    if lookbool:
                        if lookvalue[Moveto[viewpoint]] == 2 and lookvalue[int(leftRight[viewpoint][0])] == 2 and lookvalue[int(leftRight[viewpoint][1])] == 2: #look한거에 앞옆 벽일때
                            value = eval(f'client.walk{Nviewpoint[viewpoint]}()')
                            lastMove = Nviewpoint[viewpoint]
                        else:
                            value = eval(f'client.walk{viewpoint}()')
                            lookDelete = []
                    else:
                        value = eval(f'client.look_{viewpoint}()')
                        lookvalue = value
                        lookbool = True


#-------------------------이동(공간)----------------------------------------------------------------------------
            elif value[int(waypoint[viewpoint])] == 2:#바로앞(가는방향)이 벽일때
                print('front is block')

                if value[Moveto[viewpoint]] == 2 and value[int(leftRight[viewpoint][0])] == 2 and value[int(leftRight[viewpoint][1])] == 2:#보는 방향 앞 옆 전부 막혔을때
                    if value[Moveto[Nviewpoint[viewpoint]]] != 2: #반대가 벽이 아니라면
                        value = eval(f'client.walk_{Nviewpoint[viewpoint]}()')
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

                elif value[int(waypoint[viewpoint])-1] == 0 and value[int(leftRight[viewpoint][0])] == 0: #왼쪽과 왼쪽 위 전부 열렸을때
                    print(f'and left and left up open, lastMove : {lastMove}')
                    if toMove[int(leftRight[viewpoint][0])] == Moveto[Nviewpoint[lastMove]]: #이미 갔던 길일때
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
                    else:
                        #value = eval(f'client.walk_{lastMove}()')
                        value = eval(f'client.walk_{toMove[int(leftRight[viewpoint][0])]}()')
                        lastMove = toMove[int(leftRight[viewpoint][0])]

                elif value[int(waypoint[viewpoint]) + 1] == 0 and value[int(leftRight[viewpoint][1])] == 0: #오른쪽과 오른쪽 위 전부 열렸을때
                    print(f'and right and right up open, lastMove : {lastMove}')
                    if toMove[int(leftRight[viewpoint][1])] == Moveto[Nviewpoint[lastMove]]:
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
                            if Exit != None:
                                value = eval(f'client.walk_{toMove[Exit]}()')
                                viewpoint = toMove[Exit]
                                lastMove = toMove[Exit]
                    else:
                        #value = eval(f'client.walk_{lastMove}()')
                        value = eval(f'client.walk_{toMove[int(leftRight[viewpoint][1])]}()')
                        lastMove = toMove[int(leftRight[viewpoint][1])]
            else: #없을때
                print(f'moving viewpoint, lastMove : {lastMove}')
                value = eval(movemain[viewpoint])
                lastMove = viewpoint


if __name__ == "__main__":
    main()
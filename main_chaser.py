import CHaser
import random
import time
import logging
import traceback

global f
tm = time.localtime(time.time())
string = time.strftime('%Y-%m-%d_%Ih%Mm%Ss%p', tm)
f = open(f"./start_log/{string}.txt", 'w')

#ファンインソンが作りました。

try:
    wayList = ['up','left','down','right']

    wayListNum = {'up': '0 1 2', 'left': '0 3 6', 'down': '6 7 8','right': '2 5 8'}

    movemain = {'up' : 'client.walk_up()', 'down' : 'client.walk_down()', 'left' : 'client.walk_left()', 'right' : 'client.walk_right()', 'None' : 'pass'}

    moveList = [[['up', 'left'],['left','up']],['up'],[['up', 'right'],['right','up']],['left'],['right'],[['down', 'left'],['left','down']],['down'],[['down', 'right'],['right','down']]]

    waypoint = {'up':'1','left':'3','right':'5','down':'7'}

    Nviewpoint = {'up':'down','left':'right','down':'up','right':'left'}

    changeViewp = {1:'up', 3:'left',5:'right',7:'down'}

    leftRight = {'up':['3','5'], 'left':['7','1'], 'right':['1','7'], 'down':['5','3']}

    diagoline = {0: ['1','3'], 2: ['1','5'], 6 : ['7','3'], 8: ['5','7']}

    viewleftRight = {'up': ['0','2'], 'left' : ['6','0'], 'right' : ['2','8'], 'down': ['8','6']}

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
        lookbool = False
        lookvalue = None
        Exit = None
        lastMove = None
        enemycount = 0
        viewpoint = 'None'
        firstmove = False
        value = []
        lookDelete = []
        global ExitRoof
        ExitRoof = []
        global ExitRoof2
        ExitRoof2 = [] #14턴 양옆
        turn = 0
        client = CHaser.Client()
        firstway = 'up' #random.choice(wayList)
        print(firstway)
        def checkRoof(ExitRoo):
            if [ExitRoo[0], ExitRoo[1]] != [ExitRoo[2], ExitRoo[3]]:
                return False
            else:
                return True
        def checkRoof2(ExitRoo2):
            if len(ExitRoo2) >= 12:
                return True
            else:
                return False
        try:
            logging.basicConfig(filename=f'./start_log/{string}_ERROR.log', level=logging.ERROR)
            print(f"logfile's name = {string}.txt, _ERROR.log")
            while(True):
                #byunsuDic = f"'viewpoint' : {viewpoint}, 'lastMove' : {lastMove}, 'enemycount' : {enemycount}, 'lookbool' : {lookbool}, 'value' : {value}, 'firstmove' : {firstmove}, 'firstway' : {firstway}, 'Evalue' : {Evalue}, 'enemy' : {enemy}, 'int(wayListNum[firstway[2])' : {int(wayListNum[firstway[2]])}, 'Nviewpoint' : {Nviewpoint}, 'value.index(3)' : {value.index(3)}, 'item_loca' : {item_loca}, 'lookvalue' : {lookvalue}, 'lookbool' : {lookbool}, 'space' : {space}, 'Exit' : {Exit}, 'int(waypoint[viewpoint])' : {int(waypoint[viewpoint])}, 'int[leftRight[viewpoint][1])]' : {int[leftRight[viewpoint][1]]}, 'int[leftRight[viewpoint][0])]' : {int(leftRight[viewpoint][1])}, 'Moveto[Nviewpoint[lastMove]]' : {Moveto[Nviewpoint[lastMove]]}" if firstmove == True else 'sans'
                turn += 1
                print(f'start, turn : {turn}')
                f.write(f'start, turn : {turn}\n')
                #print('print variable, ', byunsuDic)
                value = client.get_ready() #ex : [2, 0, 0, 0, 0, 0, 0, 0, 2], chaserEx.png
                print(f'get ready, value = {value}, lastmove = {lastMove}, ExitRoof = {ExitRoof}, ExitRoof2 = {ExitRoof2}')
                f.write(f'get ready, value = {value}, lastmove = {lastMove}\n')
                if 1 in [value[1], value[3], value[5], value[7]]: #상대 확인
                    print('enemy')
                    f.write('enemy\n')
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
                        f.write('error\n')
                        #exit()

                elif 1 in [value[0],value[2],value[6],value[8]] and enemycount <= 4:#각 모서리에 적이 있으면 + 턴 4번 안지났으면 -> 옆보고 continue하고 위로
                    print(f'enemy_look, viewpoint = {viewpoint}, enemycount = {enemycount}')
                    f.write(f'enemy_look, viewpoint = {viewpoint}, enemycount = {enemycount}\n')
                    value = client.look_left()
                    enemycount += 1
                    continue
                elif enemycount > 4 and 1 in value: #턴 4번 넘었을때
                    print('over 4 turn')
                    f.write('over 4 turn\n')
                    Evalue = [value[0], value[2], value[6], value[8]]
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
                    elif enemy == 1:
                        if value[3] == 0:
                            value = client.walk_left()
                            enemycount = 0
                        elif value[7] == 0:
                            value = client.walk_down()
                            enemycount = 0
                        else:
                            value = eval(random.choice(['client.walk_right()', 'client.walk_up()']))
                            enemycount = 0
                    elif enemy == 2:
                        if value[1] == 0:
                            value = client.walk_up()
                            enemycount = 0
                        elif value[5] == 0:
                            value = client.walk_right()
                            enemycount = 0
                        else:
                            value = eval(random.choice(['client.walk_left()', 'client.walk_right()']))
                            enemycount = 0
                    elif enemy == 3:
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
                    f.write('first move cheak\n')
                    if value[Moveto[firstway]] != 2:
                        value = eval(movemain[firstway])
                        firstmove = True
                        viewpoint = movemain[firstway][12:][:-2]
                        lastMove = movemain[firstway][12:][:-2]
                        [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]
                        print('end first moving')
                        f.write('end first moving\n')
                    else:
                        Exit = None
                        ExitList = [1,3,5,7]
                        random.shuffle(ExitList)
                        for i in ExitList:
                            if value[i] == 2:
                                continue
                            elif value[i] == 0 or value[i] == 3:
                                Exit = i
                                break
                        firstway = toMove[Exit]
                        value = eval(movemain[firstway])
                        firstmove = True
                        viewpoint = movemain[firstway][12:][:-2]
                        lastMove = movemain[firstway][12:][:-2]
                        [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]
                        print('end first moving')
                        f.write('end first moving\n')
                else:
                    print(f'moving, value = {value}')
                    f.write(f'moving, value = {value}\n')
        #-------------------------이동(아이템)----------------------------------------------------------------------------
                    if 3 in value: #아이템이 있을때
                        print(f'find item, viewpoint = {viewpoint}')
                        f.write(f'find item, viewpoint = {viewpoint}\n')
                        item_loca3 = find_index(value, 3)
                        item_loca2 = []
                        item_loca = []
                        for i in item_loca3:
                            item_loca2.append(f'{i}')
                        Nloca = ['0','2','6','8']
                        for i in Nloca:
                            try:
                                item_loca2.remove(f'{i}')
                            except:
                                continue
                        for i in lookDelete:
                            try:
                                item_loca2.remove(i)
                            except:
                                continue
                        for i in item_loca2:
                            item_loca.append(int(i))
                        if value[int(waypoint[viewpoint])] == 3:#아이템 정면일때
                            if lookbool:
                                if lookvalue[Moveto[viewpoint]] == 2 and lookvalue[int(leftRight[viewpoint][0])] == 2 and lookvalue[int(leftRight[viewpoint][1])] == 2: #look한거에 앞옆 벽일때
                                    value = eval(f'client.walk_{Nviewpoint[lastMove]}()')
                                    lastMove = Nviewpoint[lastMove]
                                    [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]
                                    viewpoint = Nviewpoint[lastMove]
                                    lookbool = False
                                else:
                                    value = eval(f'client.walk_{viewpoint}()')
                                    lastMove = viewpoint
                                    [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]
                                    lookDelete = []
                                    lookbool = False
                            else:
                                value = eval(f'client.look_{viewpoint}()')
                                lookvalue = value
                                lookbool = True
                        elif value[int(waypoint[viewpoint])] != 3 and (value[int(leftRight[viewpoint][0])] == 3 or value[int(leftRight[viewpoint][1])] == 3 or value[Moveto[Nviewpoint[viewpoint]]] == 3): #아이템이 존재하고 정면이 아닌곳에 아이템이 있을때
                            print('item in LRD')
                            f.write('item in LRD\n')
                            viewpoint = changeViewp[item_loca[0]]
                            value = eval(f'client.look_{viewpoint}()')
                            lookvalue = value
                        #대각선에 아이템이 있을때 대처용 이동
                        elif value[int(waypoint[viewpoint])] == 2:#바로앞(가는방향)이 벽일때
                            print(f'front is block 1, viewpoint = {viewpoint}')
                            f.write(f'front is block 1, viewpoint = {viewpoint}\n')
                            if checkRoof: #반복해서 왔다갔다 할때
                                print('roof1')
                                f.write('roof1')
                                Exit = None
                                ExitList = [1,3,5,7].remove(Moveto[ExitRoof[2]])
                                random.shuffle(ExitList)
                                for i in ExitList:
                                    if value[i] == Moveto[Nviewpoint[lastMove]]:
                                        continue
                                    elif value[i] == 2:
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
                                    [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]
                                    ExitRoof = []
                            elif checkRoof2: #12턴지났을때
                                print('roof2')
                                f.write('root2')
                                count = 0
                                for i in range(12):
                                    if ExitRoof2[i] == ExitRoof2[i+2]:
                                        count +=1
                                        continue
                                    else:
                                        break
                                if count < 12:
                                    return False
                                Exit = None
                                ExitList = [1,3,5,7].remove(Moveto[ExitRoof2[0]])
                                random.shuffle(ExitList)
                                for i in ExitList:
                                    if value[i] == Moveto[Nviewpoint[lastMove]]:
                                        continue
                                    elif value[i] == 2:
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
                                    [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]
                                    ExitRoof2 = []

                            elif value[int(waypoint[viewpoint])] == 2 and value[int(viewleftRight[viewpoint][1])] == 2 and value[int(viewleftRight[viewpoint][0])] == 2: # 가는 방향 3개 다 막혔을때
                                print('left, right, up all block')
                                f.write('left, right, up all block\n')
                                if value[Moveto[Nviewpoint[viewpoint]]] != 2: #반대가 벽이 아니라면
                                    value = eval(f'client.walk_{Nviewpoint[viewpoint]}()')
                                    viewpoint = Nviewpoint[viewpoint]
                                    lastMove = Nviewpoint[viewpoint]
                                    [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]
                            elif value[int(waypoint[viewpoint])] == 2 and value[int(waypoint[viewpoint]) +1] == 2 and value[int(waypoint[viewpoint]) -1] == 2: # 가는 방향 3개 다 막혔을때
                                print(f'and front 3 is all block, lastMove : {lastMove}')
                                f.write(f'and front 3 is all block, lastMove : {lastMove}\n')
                                Exit = None
                                ExitList = [1,3,5,7]
                                random.shuffle(ExitList)
                                for i in ExitList:
                                    if value[i] == Moveto[Nviewpoint[lastMove]]:
                                        continue
                                    elif value[i] == 2:
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
                                    [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]

                            elif value[int(viewleftRight[viewpoint][0])] == 0 and value[int(leftRight[viewpoint][0])] == 0: #왼쪽과 왼쪽 위 전부 열렸을때
                                print(f'and left and left up open, lastMove : {lastMove}')
                                f.write(f'and left and left up open, lastMove : {lastMove}\n')
                                if toMove[int(leftRight[viewpoint][0])] == Moveto[Nviewpoint[lastMove]]: #이미 갔던 길일때
                                    print('but it was already gone way')
                                    f.write('but it was already gone way\n')
                                    if int(leftRight[viewpoint][1]) == 0:
                                        value = eval(f'client.walk_{toMove[int(leftRight[viewpoint][0])]}()')
                                        lastMove = toMove[int(leftRight[viewpoint][0])]
                                        [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]
                                    else:
                                        print('but front is block')
                                        f.write('but front is block\n')
                                        Exit = None
                                        ExitList = [1,3,5,7]
                                        random.shuffle(ExitList)
                                        for i in ExitList:
                                            if value[i] == Moveto[Nviewpoint[lastMove]]:
                                                continue
                                            elif value[i] == 2:
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
                                            [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]
                                else:
                                    value = eval(f'client.walk_{toMove[int(leftRight[viewpoint][0])]}()')
                                    lastMove = toMove[int(leftRight[viewpoint][0])]
                                    [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]

                            elif value[int(viewleftRight[viewpoint][1])] == 0 and value[int(leftRight[viewpoint][1])] == 0: #오른쪽과 오른쪽 위 전부 열렸을때
                                print(f'and right and right up open, lastMove : {lastMove}')
                                f.write(f'and right and right up open, lastMove : {lastMove}\n')
                                if toMove[int(leftRight[viewpoint][1])] == Moveto[Nviewpoint[lastMove]]:
                                    print('but it was already gone way')
                                    f.write('but it was already gone way\n')
                                    if int(leftRight[viewpoint][1]) == 0:
                                        value = eval(f'client.walk_{toMove[int(leftRight[viewpoint][1])]}()')
                                        lastMove = toMove[int(leftRight[viewpoint][1])]
                                        [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]
                                    else:
                                        print('but front is block')
                                        f.write('but front is block\n')
                                        Exit = None
                                        ExitList = [1,3,5,7]
                                        random.shuffle(ExitList)
                                        for i in ExitList:
                                            if value[i] == Moveto[Nviewpoint[lastMove]]:
                                                continue
                                            elif value[i] == 2:
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
                                            [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]
                                else:
                                    value = eval(f'client.walk_{toMove[int(leftRight[viewpoint][1])]}()')
                                    lastMove = toMove[int(leftRight[viewpoint][1])]
                                    [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]
                            else:
                                print('find exit')
                                f.write('find exit')
                                Exit = None
                                ExitList = [1,3,5,7]
                                random.shuffle(ExitList)
                                for i in ExitList:
                                    if value[i] == Moveto[Nviewpoint[lastMove]]:
                                        continue
                                    elif value[i] == 2:
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
                                    [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]
                        else: #없을때
                            print(f'moving viewpoint, lastMove : {lastMove}')
                            f.write(f'moving viewpoint, lastMove : {lastMove}\n')
                            value = eval(movemain[viewpoint])
                            lastMove = viewpoint
                            [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]

        #-------------------------이동(공간)----------------------------------------------------------------------------
                    elif value[int(waypoint[viewpoint])] == 2:#바로앞(가는방향)이 벽일때
                        print(f'front is block 2, viewpoint = {viewpoint}')
                        f.write(f'front is block 2, viewpoint = {viewpoint}\n')

                        if value[Moveto[viewpoint]] == 2 and value[int(leftRight[viewpoint][0])] == 2 and value[int(leftRight[viewpoint][1])] == 2:#보는 방향 앞 옆 전부 막혔을때
                            print('left, right, up all block')
                            f.write('left, right, up all block\n')
                            if value[Moveto[Nviewpoint[viewpoint]]] != 2: #반대가 벽이 아니라면
                                value = eval(f'client.walk_{Nviewpoint[viewpoint]}()')
                                viewpoint = Nviewpoint[viewpoint]
                                lastMove = Nviewpoint[viewpoint]
                                [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]
                        elif value[int(waypoint[viewpoint])] == 2 and value[int(viewleftRight[viewpoint][1])] == 2 and value[int(viewleftRight[viewpoint][0])] == 2: # 가는 방향 3개 다 막혔을때
                            print(f'and front 3 is all block, lastMove : {lastMove}')
                            f.write(f'and front 3 is all block, lastMove : {lastMove}\n')
                            Exit = None
                            ExitList = [1,3,5,7]
                            random.shuffle(ExitList)
                            for i in ExitList:
                                if value[i] == Moveto[Nviewpoint[lastMove]]:
                                    continue
                                elif value[i] == 2:
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
                                [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]

                        elif value[int(viewleftRight[viewpoint][0])] == 0 and value[int(leftRight[viewpoint][0])] == 0: #왼쪽과 왼쪽 위 전부 열렸을때
                            print(f'and left and left up open, lastMove : {lastMove}')
                            f.write(f'and left and left up open, lastMove : {lastMove}\n')
                            if toMove[int(leftRight[viewpoint][0])] == Moveto[Nviewpoint[lastMove]]: #이미 갔던 길일때
                                print(f'but it was already gone way')
                                f.write(f'but it was already gone way\n')
                                if int(leftRight[viewpoint][1]) == 0:
                                    value = eval(f'client.walk_{toMove[int(leftRight[viewpoint][0])]}()')
                                    lastMove = toMove[int(leftRight[viewpoint][0])]
                                    [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]
                                else:
                                    print('but front is block')
                                    f.write('but front is block\n')
                                    Exit = None
                                    ExitList = [1,3,5,7]
                                    random.shuffle(ExitList)
                                    for i in ExitList:
                                        if value[i] == Moveto[Nviewpoint[lastMove]]:
                                            continue
                                        elif value[i] == 2:
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
                                        [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]
                            else:
                                value = eval(f'client.walk_{toMove[int(leftRight[viewpoint][0])]}()')
                                lastMove = toMove[int(leftRight[viewpoint][0])]
                                [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]

                        elif value[int(viewleftRight[viewpoint][1])] == 0 and value[int(leftRight[viewpoint][1])] == 0: #오른쪽과 오른쪽 위 전부 열렸을때
                            print(f'and right and right up open, lastMove : {lastMove}')
                            f.write(f'and right and right up open, lastMove : {lastMove}\n')
                            if toMove[int(leftRight[viewpoint][1])] == Moveto[Nviewpoint[lastMove]]:
                                print('but it was already gone way')
                                f.write('but it was already gone way\n')
                                if int(leftRight[viewpoint][1]) == 0:
                                    value = eval(f'client.walk_{toMove[int(leftRight[viewpoint][1])]}()')
                                    lastMove = toMove[int(leftRight[viewpoint][1])]
                                    [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]
                                else:
                                    print('but front is block')
                                    f.write('but front is block\n')
                                    Exit = None
                                    ExitList = [1,3,5,7]
                                    random.shuffle(ExitList)
                                    for i in ExitList:
                                        if value[i] == Moveto[Nviewpoint[lastMove]]:
                                            continue
                                        elif value[i] == 2:
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
                                        [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]
                            else:
                                value = eval(f'client.walk_{toMove[int(leftRight[viewpoint][1])]}()')
                                lastMove = toMove[int(leftRight[viewpoint][1])]
                                [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]
                        else:
                            print('find exit')
                            f.write('find exit')
                            Exit = None
                            ExitList = [1,3,5,7]
                            random.shuffle(ExitList)
                            for i in ExitList:
                                if value[i] == Moveto[Nviewpoint[lastMove]]:
                                    continue
                                elif value[i] == 2:
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
                                [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]
                    else: #없을때
                        print(f'moving viewpoint, lastMove : {lastMove}')
                        f.write(f'moving viewpoint, lastMove : {lastMove}\n')
                        value = eval(movemain[viewpoint])
                        lastMove = viewpoint
                        [x.append(lastMove) for x in (ExitRoof, ExitRoof2)]
        except OSError:
            logging.error(traceback.format_exc())
            f.write('game is done\n')
            f.close()
        except WindowsError:
            pass
        except:
            logging.error(traceback.format_exc())
            f.write('error\n')
        finally:
            f.write('game is close')
            f.close()


    if __name__ == "__main__":
        main()
except:
    logging.error(traceback.format_exc())
    f.write('game is close')
    f.close()
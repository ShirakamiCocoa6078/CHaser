import CHaser
import random

wayList = ['up','left','down','right']

wayListNum = {'up': '0 1 2', 'left': '0 3 6', 'down': '6 7 8','right': '2 5 8'}

viewpoint = 'None'

lookbool = False

movemain = {'up' : 'client.walk_up()', 'down' : 'client.walk_down()', 'left' : 'client.walk_left()', 'right' : 'client.walk_right()', 'None' : 'pass'}

moveList = [[['up', 'left'],['left','up']],['up'],[['up', 'right'],['right','up']],['left'],['right'],[['down', 'left'],['left','down']],['down'],[['down', 'right'],['right','down']]]

waypoint = {'up':'1','left':'3','right':'5','down':'7'}

leftRight = {'up':['3','5'], 'left':['7','1'], 'right':['1','7'], 'down':['5','3']}

diagoline = {'0': ['1','3'], '2': ['1','5'], '6' : ['7','3'], '8': ['5','7']}

toItem = {1 : 'up', 3 : 'left', 5 : 'right', 7 : 'down'}

def get_key(val, dic):
    for key, value in dic.items():
        if val == value:
            return key
    return('키가 없습니다')

def main():
    value = []
    firstmove = False
    client = CHaser.Client()
    firstway = random.choice(wayList)
    print(firstway)

    while(True):
        print('start')
        value = client.get_ready() #ex : [2, 0, 0, 0, 0, 0, 0, 0, 2], chaserEx.png

        if 1 in [value[1], value[3], value[5], value[7]]: #상대 확인
            print('enemy')
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

        elif 1 in [value[0],value[2],value[6],value[8]]:#각 모서리에 적이 있으면 -> 옆보고 continue하고 위로
            print('enemy_look')
            value = client.look_left()
            continue

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
            viewpoint = firstway
            print('end first moving')
        else:

            print('moving')

            if value in 3:
                print('find item')
                if value[int(waypoint[viewpoint])] == 3:#아이템 정면일때
                    if lookbool == True:
                        if lookvalue[4] == 2:
                            if lookvalue[2] == 2 and lookvalue[8] == 2: #아이템 사방이 막혀있을때
                                value = eval('')
                                lookbool = False
                    value = eval(movemain[viewpoint])
                else:#정면이 아닌 다른곳에 아이템이 있을때
                    print('item in not front')
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
                            value = eval(f'client.walk_{toItem[space]}()')
                        else:
                            pass
                    else:
                        viewpoint = toItem[item_loca]
                        value = eval(f'client.look_{viewpoint}()')
                        lookvalue = value
                        lookbool = True


            elif value[int(waypoint[viewpoint])] == 2:#바로앞(가는방향)이 벽일때
                print('front is block')

                if value[int(waypoint[viewpoint])-1] == 0: #왼쪽 위가 열렸으면
                    print('and left up is open')

                    if value[int(leftRight[viewpoint][0])] == 0: #왼쪽과 왼쪽 위 전부 열렸을때
                        print('and left and left up open')
                        value = eval(f'client.walk_{get_key(value[int(leftRight[viewpoint][0])], waypoint)}()')

                    else:
                        continue

                elif value[int(waypoint[viewpoint]) + 1] == 0: #오른쪽 위가 열렸으면
                    print('and right up is open')

                    if value[int(leftRight[viewpoint][1])] == 0: #오른쪽과 오른쪽 위 전부 열렸을때
                        print('and right and right up open')
                        value = eval(f'client.walk_{get_key(value[int(leftRight[viewpoint][1])], waypoint)}()')

                    else:
                        continue

                elif value[int(waypoint[viewpoint])] == 2 and value[int(waypoint[viewpoint]) +1] == 2 and value[int(waypoint[viewpoint]) -1] == 2: # 가는 방향 3개 다 막혔을때
                    print('and front 3 is all block')

                    if value[int(leftRight[viewpoint][0])] == 0:#가는 방향 기준 왼쪽이 비었을때
                        print('and left is open')
                        value = eval(f'client.walk_{get_key(value[int(leftRight[viewpoint][0])], waypoint)}()')

                    elif value[int(leftRight[viewpoint][1])]:#가는 방향 기준 오른쪽이 비었을때
                        print('and right is open')
                        value = eval(f'client.walk_{get_key(value[int(leftRight[viewpoint][1])], waypoint)}()')

                    else: #앞이 완전벽일때(방향전환)
                        print('and all block the front')
                        if value[int(leftRight[viewpoint][0])] == 0:#가는 방향 기준 왼쪽 빔
                            value = eval(f'client.walk_{get_key(value[int(leftRight[viewpoint][0])], waypoint)}()')
                            viewpoint = get_key(value[int(leftRight[viewpoint][0])], waypoint)

                        elif value[int(leftRight[viewpoint][1])] == 0:#가는 방향 기준 왼쪽 빔
                            value = eval(f'client.walk_{get_key(value[int(leftRight[viewpoint][1])], waypoint)}()')
                            viewpoint = get_key(value[int(leftRight[viewpoint][1])], waypoint)
                        else:
                            pass
            else: #없을때
                value = eval(movemain[viewpoint])


if __name__ == "__main__":
    main()
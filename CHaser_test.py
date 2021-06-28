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
#def moveThink(): #상하좌우 9칸씩 확인
    valueL = client.look_left()
    valueR = client.look_right()
    valueU = client.look_up()
    valueD = client.look_down()
    if valueL in 3:
        return 'L'
    elif valueR in 3:
        return 'R'
    elif valueU in 3:
        return 'U'
    elif valueD in 3:
        return 'D'
    else:
        return 'N'
#def moveAI():
    value = moveThink()
    if value == 'L':
        value = client.look_left()
#def canmove(): #상하좌우 나가는 길 탐색
    value = client.get_ready()
    value = [value[1], value[4], value[6], value[8]]
    if 0 not in value:
        return 'break'
    else:
        return 'print('')'
def main():
    while(True):
        value = client.walk_up()
        value = client.walk_down()
        value = client.walk_left()
        value = client.walk_right()
        RU = ['client.walk_right()','client.walk_up()']
        UR = ['client.walk_up()','client.walk_right()']
        RD = ['client.walk_right()','client.walk_down()']
        DR = ['client.walk_down()','client.walk_right()']
        LU = ['client.walk_left()','client.walk_up()']
        UL = ['client.walk_up()','client.walk_left()']
        LD = ['client.walk_left()','client.walk_down()']
        DL = ['client.walk_down()','client.walk_left()']
        value = client.get_ready()
        if 1 in [value[1], value[4], value[6], value[8]]:
            value = [value[1], value[4], value[6], value[8]]
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
                pass


if __name__ == "__main__":
    main()

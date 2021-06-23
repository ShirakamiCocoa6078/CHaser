import CHaser
import random

client = CHaser.Client()

def checkValue(value): #주위 9칸이 다이아가 있는가 확인
    count = 0
    for i in value:
        if i == 3:
            return 'ok'
        else:
            count += 1
    return count
def moveThink(): #상하좌우 9칸씩 확인
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
def moveAI():
    value = moveThink()
    if value == 'L':
        value = client.look_left()
def canmove(): #상하좌우 나가는 길 탐색
    value = client.get_ready()
    value = [value[1], value[4], value[6], value[8]]
    if 0 not in value:
        return 'break'
    else:
        return 'print('')'
def main():
    while(True):
        eval(canmove())
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

        if checkValue(value) != 'ok': #9칸 전부 다이아가 없을때
            value = client.look_right()
            if value[4] == 0:
                moveThink()
        else:
            pass #정상적인거
if __name__ == "__main__":
    main()
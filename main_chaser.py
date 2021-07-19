import CHaser
import random
wayList = ['up','left','down','right']
wayListNum = {'up': '0 1 2', 'left': '0 3 6', 'down': '6 7 8','right': '2 5 8'}
def main():
    value = []
    client = CHaser.Client()
    firstway = random.choice(wayList)
    while(True):
        value = client.get_ready()
        for i in range(4):
            for e in range(3):
                WNum = [wayListNum[firstway].split(' ')]
                if value[WNum[e]] in 0:
                    firstway = random.choice(wayList)


if __name__ == "__main__":
    main()
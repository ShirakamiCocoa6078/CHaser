import CHaser
import random
wayList = ['up','left','down','right']
def main():
    value = []
    client = CHaser.Client()
    firstway = random.choice(wayList)
    while(True):
        value = client.get_ready()


if __name__ == "__main__":
    main()
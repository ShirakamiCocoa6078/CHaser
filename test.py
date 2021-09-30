import CHaser

def main():
    value = []
    client = CHaser.Client()
    while True:
        value = client.get_ready()
        print(value)
        value = client.walk_right()


if __name__ == "__main__":
    main()
import CHaser

def main():
    value = []
    client = CHaser.Client()
    value = client.get_ready()
    print(value)
    value = client.walk_right()
    value = client.walk_right()
    value = client.walk_right()
    value = client.walk_right()
    value = client.walk_right()

if __name__ == "__main__":
    main()
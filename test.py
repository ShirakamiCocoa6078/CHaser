import CHaser

def main():
    value = []
    client = CHaser.Client()
    value = client.get_ready()
    print(value)

if __name__ == "__main__":
    main()
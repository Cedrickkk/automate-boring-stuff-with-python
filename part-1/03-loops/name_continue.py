def main() -> None:
    while True:
        print("Who are you?")
        name = input("> ").lower()

        if name != 'joe':
            continue
            
        print("Hello, Joe. What is the password? (It is a fish.)")
        password = input("> ").lower()

        if password == 'swordfish':
            break

    print("Access granted.")


if __name__ == '__main__':
    main()
def main() -> None:
    while True:
        print("Please input your name: ")
        name = input("> ").lower()

        if name == 'cedrick':
            break

    print(f"Thank you, {name}")

if __name__ == '__main__':
    main()
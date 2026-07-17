def main() -> None:
    name = ''

    while name != 'cedrick':
        print('Please type your name: ')
        name = input("> ").lower()
    
    print(f"Thank you, {name}.")

if __name__ == '__main__':
    main()
def main():
    print("Hello from flow-control!")

    code_block()

def code_block():
    username = 'Mary'
    password = 'swordfish'

    if username == 'Mary':
        print('Hello, Mary!')
        if password == 'swordfish':
            print('Access granted.')
        else:
            print('Wrong password')

if __name__ == "__main__":
    main()

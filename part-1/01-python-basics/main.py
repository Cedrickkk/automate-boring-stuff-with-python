def main():
    print("Hello, Python world!")
    print("What is your name?")
    name = input("> ")
    print("It is good to meet you " + name)
    print("The length of your name is: ")
    name_length = len(name)
    print("What is your age? ")
    age = input("> ")
    print("You will be " + str(int(age) + 1) + " in a year.")

if __name__ == "__main__":
    main()

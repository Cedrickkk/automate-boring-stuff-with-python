def main():
    print("Hello, Python world!")
    print("What is your name?")
    name = input("> ")
    print("It is good to meet you " + name)
    name_length = len(name)
    print("The length of your name is: " + name_length)
    print("What is your age? ")
    age = input("> ")
    print("You will be " + str(int(age) + 1) + " in a year.")

    print("\nNumber Methods in Python: ")
    number_methods()

def number_methods():
    print("\nround() method:")
    print(round(3.14))
    print(round(7.7))
    print(round(-2.2))

    print(round(3.14, 1))
    print(round(7.7777, 3))

    print("\nabs() method:")
    print(abs(25))  
    print(abs(-25))
    print(abs(-3.14))
    print(abs(0))


if __name__ == "__main__":
    main()

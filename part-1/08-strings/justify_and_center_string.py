def main() -> None:
    # justifying strings
    spam: str = "Hello"
    print(spam.rjust(20))

    spam: str = "Hello, world!"
    print(spam.rjust(20))

    spam: str = "Hello"
    print(spam.ljust(20))

    print(spam.rjust(20, "*"))
    print(spam.ljust(20, "-"))

    # centering strings
    print(spam.center(20))
    print(spam.center(20, "="))

if __name__ == "__main__":
    main()
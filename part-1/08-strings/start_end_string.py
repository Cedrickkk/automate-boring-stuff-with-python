def main() -> None:
    spam: str = "Hello, world!"

    # starts with
    print(spam.startswith("Hello"))

    # ends with
    print(spam.endswith("world!"))

    print(spam.startswith("Hello, world!"))
    print(spam.endswith("Hello, world!"))

if __name__ == "__main__":
    main()
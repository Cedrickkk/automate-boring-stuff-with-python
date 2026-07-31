def main() -> None:
    """index() returns the index of the given value"""
    spam: list[str] = ["hello", "hi", "howdy", "heyas"]
    print(spam.index("hello"))
    print(spam.index("hello hello hello")) # throws a ValueError

if __name__ == "__main__":
    main()
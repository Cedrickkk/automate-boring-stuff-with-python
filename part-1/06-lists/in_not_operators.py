def main() -> None:
    """in and not operators"""
    greetings: list[str] = ["hello", "hi", "howdy", "heyas"]

    # in operator
    print("howdy" in greetings)
    print("cat" in greetings)

    # not operator
    print("howdy" not in greetings)
    print("cat" not in greetings)

if __name__ == "__main__":
    main()
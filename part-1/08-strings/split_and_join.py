def main() -> None:
    spam: list[str] = ["cats", "rats", "bats"]

    # join with comma
    print(", ".join(spam))

    print(" ".join(["My", "name", "is", "Cedric"]))

    # split
    print("My name is Cedrick".split())

    letter: str = """
        Dear Alice,
        There is a milk bottle in the fridge
        that is labeled 'Milk Experiment.'
        Please do not drink it.
        Sincerely,
        Bob
    """

    print(letter.split("\n"))


if __name__ == "__main__":
    main()
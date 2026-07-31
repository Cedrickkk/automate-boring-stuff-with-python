def main() -> None:
    """
    Negative Indices

    Gets an item from the end of the list using a negative index
    """
    spam: list[str] = ["cat", "bat", "rat", "elephant"]
    print(spam[-1]) # last index
    print(spam[-3]) # third to the last index
    print(f"The {spam[-1]} is afraid of the {spam[-3]}")

if __name__ == "__main__":
    main()
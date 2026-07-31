def main() -> None:
    # Negative Indexes
    spam: list[str] = ["cat", "bat", "rat", "elephant"]
    print(spam[-1]) # last index
    print(spam[-3]) # third to the last index
    print(f"The {spam[-1]} is afraid of the {spam[-3]}")

if __name__ == "__main__":
    main()
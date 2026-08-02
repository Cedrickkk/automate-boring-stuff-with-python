def main() -> None:
    spam: list[str] = ["cat", "bat", "dog"]

    if spam[0] == "cat":
        print("A cat is the first item.")
    else:
        print("The first item is not a cat.")

    spam: list[str] = []

    if len(spam) > 0 and spam[0] == "cat":
        print("A cat is the first item.")
    else:
        print("The first item is not a cat.")

if __name__ == "__main__":
    main()
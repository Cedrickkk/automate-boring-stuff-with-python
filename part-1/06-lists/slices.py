def main() -> None:
    """
    Slices
    Gets a several value from a list, in the form of a new list.
    """
    spam: list[str] = ["spam", "bat", "rat", "elephant"]
    print(spam[0:4])
    print(spam[1:3])
    print(spam[0:-1])

    # Leaving out one or both of the indexes on either side of the colon
    print(spam[:2])
    print(spam[1:])
    print(spam[:])
    

if __name__ == "__main__":
    main()
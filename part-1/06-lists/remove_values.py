def main() -> None:
    """Removing items in a list"""
    spam: list[str] = ["cat", "bat", "rat", "elephant"]
    spam.remove("cat")
    print(spam)
    

if __name__ == "__main__":
    main()

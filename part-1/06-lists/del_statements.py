def main() -> None:
    """Delete statements"""
    spam: list[str] = ["cat", "bat", "rat", "elephant"]
    del spam[2]
    print(spam)
    del spam[2]
    print(spam)

if __name__ == "__main__":
    main()
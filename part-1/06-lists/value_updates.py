def main() -> None:
    """Value Updates"""
    spam: list[str] = ["cat", "bat", "rat", "elephant"]
    spam[1] = "aardvark"  
    print(spam)
    spam[2] = spam[1]
    print(spam)
    spam[-1] = str(12345)
    print(spam)

if __name__ == "__main__":
    main()
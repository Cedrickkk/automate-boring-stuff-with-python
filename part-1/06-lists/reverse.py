def main() -> None:
    """Reverses a list"""
    spam: list[str] = ["cat", "dog", "moose"]
    spam.reverse()
    print(spam)

if __name__ == "__main__":
    main()
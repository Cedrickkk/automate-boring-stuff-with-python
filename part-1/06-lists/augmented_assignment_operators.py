def main() -> None:
    """Augmented assignment operators"""
    # Addition
    spam: int = 42
    spam = spam + 1
    print(spam)
    spam += 1

    # Subtraction
    spam: int = 43
    spam = spam - 1
    print(spam)
    spam -= 1

    # Multiplication
    spam: int = 43
    spam = spam * 1
    print(spam)
    spam *= 1

    # Division
    spam: int = 43
    spam = spam // 1
    print(spam)
    spam //= 1

    # Modulo
    spam: int = 43
    spam = spam % 1
    print(spam)
    spam &= 1
    

if __name__ == "__main__":
    main()
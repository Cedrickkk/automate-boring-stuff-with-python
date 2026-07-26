def main() -> None:
    try:
        print(spam(2))
        print(spam(12))
        print(spam(0))
        print(spam(4))
    except ZeroDivisionError:
        print("Error: Invalid argument.")

def spam(divide_by: float) -> float:
    return 42 / divide_by

if __name__ == "__main__":
    main()
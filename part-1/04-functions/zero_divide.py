def main() -> None:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(4))

def spam(divide_by: float) -> float | None:
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print("Error: Invalid argument.")

if __name__ == "__main__":
    main()
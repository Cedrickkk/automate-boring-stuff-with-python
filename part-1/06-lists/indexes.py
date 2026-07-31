from typing import Any

def main() -> None:
    spam = ["cat", "bat", "rat", "elephant"]

    print(spam[0])
    print(spam[1])
    print(spam[2])
    print(spam[3])

    print(f"The {spam[1]} ate the {spam[0]}")

    matrix:list[list[Any]] = [["cat", "bat"], [10, 20, 30, 40, 50]]
    print(matrix[0])
    print(matrix[0][1])
    print(matrix[1][4])

if __name__ == "__main__":
    main()
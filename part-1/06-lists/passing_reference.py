from typing import Any

def main() -> None:
    spam: list[int] = [1, 2, 3, 4, 5]
    eggs(spam)
    print(spam)
            
def eggs(some_parameter: list[Any]):
    some_parameter.append("hello")

if __name__ == "__main__":
    main()
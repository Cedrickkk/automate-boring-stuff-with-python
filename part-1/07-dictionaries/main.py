from typing import Any

def main():
    # dictionary example
    spam: dict[Any, Any] = {
        12345: "Luggage Combination",
        42: "The answer",
    }

    print(spam[12345])
    print(spam[42])


if __name__ == "__main__":
    main()

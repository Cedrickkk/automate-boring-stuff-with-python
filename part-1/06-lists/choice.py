from random import choice

def main() -> None:
    """choice - random selection from a list"""
    pets: list[str] = ["Dog", "Cat", "Mouse"]

    print(choice(pets))
    print(choice(pets))
    print(choice(pets))

if __name__ == "__main__":
    main()
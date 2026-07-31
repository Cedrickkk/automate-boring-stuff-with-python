from random import shuffle

def main() -> None:
    """shuffle - reorder items in a list in place"""
    people: list[str] = ["Alice", "Bob", "Charlie", "David"]    
    print(people)
    shuffle(people)
    print(people)
    ...

if __name__ == "__main__":
    main()
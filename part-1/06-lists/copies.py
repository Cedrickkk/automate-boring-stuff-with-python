from copy import copy, deepcopy

def main() -> None:
    spam: list[str] = ["A", "B", "C"] 
    cheese = copy(spam) # Creates a duplicate copy of the list
    cheese[1] = "E" # Changes only `cheese`
    print(f"Cheese = {cheese}")
    print(f"Spam = {spam}")
    print(spam is cheese)

    spam_deep: list[str | list[str]] = ["A", ["B", "C"], "D"]
    cheese_deep = deepcopy(spam_deep)
    cheese_deep[1] = ["C", "B"]
    print(f"Cheese Deep = {cheese_deep}")
    print(f"Spam Deep = {spam_deep}")

if __name__ == "__main__":
    main()
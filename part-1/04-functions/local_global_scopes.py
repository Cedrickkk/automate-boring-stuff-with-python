eggs = 'global'

def main() -> None:
    spam()
    print(eggs)

def spam() -> None:
    global eggs
    eggs = 'spam' # Uses and reassign the global variable `eggs`

def bacon() -> None:
    eggs = 'bacon' # Local variable only

def ham() -> None:
    print(eggs) # Uses the global `eggs` variable

if __name__ == "__main__":
    main()


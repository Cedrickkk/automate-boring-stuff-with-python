eggs = "global"

def main() -> None:
    spam()
    print(eggs)

def spam() -> None:
    global eggs # `global` modifies a global variable from within a function 
    eggs = "spam"

if __name__ == "__main__":
    main()
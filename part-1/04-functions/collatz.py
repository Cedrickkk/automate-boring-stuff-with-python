def main() -> None:
    print("Enter a number: ")
    num = int(input("> "))

    while num != 1:
        num = collatz(num)
        

def collatz(num: int) -> int:
    if num % 2 == 0:
        print(num // 2)
        return num // 2
    else:
        print(3 * num + 1)   
        return 3 * num + 1

if __name__ == "__main__":
    main()
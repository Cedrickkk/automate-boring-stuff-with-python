from random import randint

def main() -> None:
    # Perform 100 coin flips
    for _ in range(100): 
        result = "H" if randint(0, 1) == 0 else "T"
        print(result)

    print()

if __name__ == "__main__":
    main()
from random import random, randint, choice
from time import sleep
from sys import exit

WIDTH: int = 70

def main() -> None:
    columns = [0] * WIDTH
    try:
        while True:
            for i in range(WIDTH):
                if random() < 0.02:
                    columns[i] = randint(4, 14)

                if columns[i] == 0: 
                    print(".", end="")
                else:
                    print(choice([0, 1]), end="")
                    columns[i] -= 1
                    
            print()
            sleep(0.1)

    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    main()
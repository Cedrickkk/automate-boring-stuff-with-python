import sys

from random import randint

def main() -> None:
    print("ROCK, PAPER, SCISSORS")

    wins: int = 0
    losses: int = 0
    ties: int = 0

    player: str | None = None
    computer: str | None = None

    while True:
        print(f"{wins} Wins {losses} Losses {ties} Ties")
        while True:
            print("Enter your move: \n(r) rock \n(p) paper \n(s) scissors \n(q) quit")
            player = input("> ")
    
            if player == 'q':
                sys.exit()
    
            if player == 'r' or player == 'p' or player == 's':
                break
    
            print("Type one of r, p, s, or q.")
            
        if player == 'r':
            print("ROCK versus ...")
        elif player == 'p':
            print("PAPER versus ...")
        elif player == 's':
            print("SCISSORS versus ...")
    
        random_number = randint(1, 3)
    
        if random_number == 1:
            computer = 'r'
            print("ROCK")
        elif random_number == 2:
            computer = 'p'
            print("PAPER")
        elif random_number == 3:
            computer = 's'
            print("SCISSORS")

        if player == computer:
            print("It is a tie!")
            ties += 1
        elif player == 'r' and computer == 's':
            print("You win!")
            wins += 1
        elif player == 'p' and computer == 'r':
            print("You win!")
            wins += 1
        elif player == 's' and computer == 'p':
            print("You win!")
            wins += 1
        elif player == 'r' and computer == 'p':
            print("You lose!")
            losses -= 1
        elif player == 'p' and computer == 's':
            print("You lose!")
            losses -= 1
        elif player == 's' and computer == 'r':
            print("You lose!")
            losses -= 1
        
        
if __name__ == "__main__":
    main()
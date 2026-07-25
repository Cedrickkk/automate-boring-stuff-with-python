import sys

from random import choice

MOVES = {
    "r": "ROCK",
    "p": "PAPER",
    "s": "SCISSORS"
}

def main() -> None:
    print("ROCK, PAPER, SCISSORS")

    wins: int = 0
    losses: int = 0
    ties: int = 0

    while True:
        print(f"{wins} Wins {losses} Losses {ties} Ties")
        player = get_player_move()
        computer = get_computer_move()  
        print(f"{MOVES[player]} versus {MOVES[computer]}")
        
        result =  determine_round_result(player, computer)

        if result == "tie":
            print("It is a tie!")
            ties += 1
        elif result == "win":
            print("You win!")
            wins += 1
        else:
            print("You lose!") 
            losses += 1

def get_player_move() -> str:
    while True:
        print("Enter your move: \n(r) rock \n(p) paper \n(s) scissors \n(q) quit")
        move = input("> ")

        if move == 'q':
            sys.exit()

        if move in MOVES:
            return move

        print("Type one of r, p, s, or q.")
            
def get_computer_move() -> str:
    return choice(['r', 'p', 's'])

def determine_round_result(player: str, computer: str) -> str:
    if player == computer:
        return "tie" 

    wins_against = {
        ("r", "s"),
        ("p", "r"),
        ("s", "p")
    }

    if (player, computer) in wins_against:
        return "win"

    return "lose"

if __name__ == "__main__":
    main()
from random import randint

def main() -> None:
    print("Ask a yes or no question:")
    input("> ")
    print(get_answer(randint(1, 9)))
        
def get_answer(number: int) -> str:
    # Returns a fortune number based on what int number is, 1 to 9
    fortunes: dict[int, str] = {
        1: "It is certain",
        2: "It is decidedly so",
        3: "Yes",
        4: "Reply hazy try again",
        5: "Ask again later",
        6: "Concentrate and ask again",
        7: "My reply is no",
        8: "Outlook not so good",
        9: "Very doubtful"
    }
    return fortunes[number]


if __name__ == "__main__":
    main()
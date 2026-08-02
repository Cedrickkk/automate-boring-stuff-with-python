from random import randint

def main() -> None:
    messages: list[str] = [
        "It is decidedly so",
        "Yes definitely",
        "Reply hazy try again",
        "Ask again later",
        "Concentrate and ask again",
        "My reply is no",
        "Outlook not so good",
        "Very doubtful"
    ]

    input("Ask a question: ")
    print(messages[randint(0, len(messages) - 1)])

if __name__ == "__main__":
    main()
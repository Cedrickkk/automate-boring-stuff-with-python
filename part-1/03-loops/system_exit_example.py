import sys

def main() -> None:
    while True:
        print("Type 'exit' to exit.")
        response = input("> ")

        if response == "exit":
            sys.exit()

        print(f"You typed '{response}'")


if __name__ == "__main__":
    main()
def main() -> None:
    birthdays: dict[str, str] = {
        "alice": "Apr 1",
        "bob": "Dec 12",
        "carol": "Mar 4",
    }

    while True:
        name: str = input("Enter a name (blank to quit): ")
        if not name:
            break

        if name in birthdays:
            print(f"{birthdays[name]} is the birthday of {name}")
        else:
            print(f"I do not have birthdy information for {name}.")
            birthday: str = input("What is their birthday?: ")
            birthdays[name] = birthday
            print("Birthday database updated.")



if __name__ == "__main__":
    main()
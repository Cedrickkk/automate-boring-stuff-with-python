def main() -> None:
    spam: list[str] = ["cats", "dogs", "moose"]
    bacon: list[str] = ["dpgs", "moose", "cats"]
    print(spam == bacon) # False

    eggs: dict[str, str] = {
        "name": "Zophie",
        "species": "cat",
        "age": "8"
    }
    ham: dict[str, str] = {
        "species": "cat",
        "age": "8",
        "name": "Zophie"
    }
    print(eggs == ham) # True
    
    # spam['not_valid_key'] will result in error

if __name__ == "__main__":
    main()
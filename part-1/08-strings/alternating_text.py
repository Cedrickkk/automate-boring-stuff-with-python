import pyperclip

def main() -> None:
    text: str = pyperclip.paste()
    alt_text: str = ""
    make_uppercase: bool = False

    for character in text:
        # Go through each character and add it to alt_text
        if make_uppercase:
            alt_text += character.upper()
        else:
            alt_text += character.lower()

        make_uppercase = not make_uppercase

    pyperclip.copy(alt_text)
    print(alt_text)

if __name__ == "__main__":
    main()

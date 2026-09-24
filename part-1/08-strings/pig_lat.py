def main() -> None:
    message: str = input("Enter the English message to translate into pig latin: ")

    VOWELS = ("a", "e", "i", "o", "u", "y")

    pig_latin: list[str] = []

    for word in message.split():
        # separate non-letters at the start of this word
        prefix_non_letters: str = ''

        while len(word) > 0 and not word[0].isalpha():
            prefix_non_letters += word[0]
            word = word[1:]

        if len(word) == 0:
            pig_latin.append(prefix_non_letters)
            continue

        # separate the non-letters at the end of this word
        suffix_non_letters: str = ''
        while not word[-1].isalpha():
            suffix_non_letters += word[-1]
            word = word[:-1]

        # remember if the word was in uppercase or title case
        was_upper = word.isupper()
        was_title = word.istitle()

        word = word.lower()

        # separate the consonants at the start of this word
        prefix_consonants: str = ''
        while len(word) > 0 and not word[0] in VOWELS:
            prefix_consonants += word[0]
            word = word[1:]

        # add the pig latin ending to the word
        if prefix_consonants != '':
            word += prefix_consonants + 'ay'
        else:
            word += 'yay'

        # set the word back to uppercase or title case
        if was_upper:
            word = word.upper()

        if was_title:
            word = word.title()

        pig_latin.append(prefix_non_letters + word + suffix_non_letters)

    # join all the words back together
    print(' '.join(pig_latin))

if __name__ == "__main__":
    main()
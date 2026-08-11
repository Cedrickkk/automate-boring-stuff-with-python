def main() -> None:
    spam: str = "Hello, World!" 

    print(spam.isalpha()) # checks if string consists only of letters and isn't blank
    print(spam.isalnum()) # checks if string consists only of letters and numbers and isn't blank (alphanumerics)
    print(spam.isdecimal()) # checks if string consists only of numeric characters and isn't blank
    print(spam.isspace()) # checks if the string consists only of spaces, tabs, and newlines and isn't blank
    print(spam.istitle()) # checks if the string consists only of words that begin with an uppercase letter followed by only lowercase

if __name__ == "__main__":
    main()
def main() -> None:
    spam: str = "    Hello, world!     "
    print(spam.strip())
    print(spam.lstrip())
    print(spam.rstrip())

    spam: str = 'SpamSpamBaconSpamEggsSpamSpam'
    print(spam.strip("ampS"))


if __name__ == "__main__":
    main()
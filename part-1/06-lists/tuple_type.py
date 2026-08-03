def main() -> None:
    eggs: tuple[str, str] = ("hello", "world")

    for egg in eggs:
        print(egg)

if __name__ == "__main__":
    main()
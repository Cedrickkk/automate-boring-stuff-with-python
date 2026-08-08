def main() -> None:
    message: str = "It was a bright cold day in April, and the clocks were striking thirteen"
    count: dict[str, int] = {}

    for character in message:
        count.setdefault(character, 0)
        count[character] += 1

    print(count)

if __name__ == "__main__":
    main()
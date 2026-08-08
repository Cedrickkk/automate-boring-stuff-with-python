def main() -> None:
    message: str = "It was a bright cold day in April, and the clocks were striking thirteen"
    count: dict[str, int] = {}

    for character in message:
        count.setdefault(character, 0)
        count[character] += 1

    print(count)

    # another way with .get() method
    frequency: dict[str, int] = {}
    for character in message:
        frequency[character] = frequency.get(character, 0) + 1

    print(frequency)

if __name__ == "__main__":
    main()
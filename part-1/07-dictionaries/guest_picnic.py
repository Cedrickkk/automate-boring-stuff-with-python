def main() -> None:
    all_guest: dict[str, dict[str, int]] = {
        "alice": {
            "apples": 5,
            "pretzels": 12
        },
        "bob": {
            "ham_sandwich": 3,
            "apples": 2,
        },
        "carol": {
            "cups": 3,
            "apple_pies": 1,
        }
    }

    print("Number of things being brought:")
    print(f"-  Apples {total_brought(guests=all_guest, item="apples")}")
    print(f"-  Cups {total_brought(guests=all_guest, item="cups")}")
    print(f"-  Cakes {total_brought(guests=all_guest, item="cakes")}")
    print(f"-  Ham Sandwiches {total_brought(guests=all_guest, item="ham_sandwiches")}")
    print(f"-  Apple Pies {total_brought(guests=all_guest, item="apple_pies")}")


def total_brought(guests: dict[str, dict[str, int]], item: str) -> int:
    num_brought: int = 0
    for _, v in guests.items():
        num_brought = num_brought + v.get(item, 0)
    return num_brought


if __name__ == "__main__":
    main()
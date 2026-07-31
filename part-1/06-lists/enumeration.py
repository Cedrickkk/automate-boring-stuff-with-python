def main() -> None:
    """enumerate - returns two values: index and item itself"""
    supplies: list[str] = ["pens", "staplers", "flamethrowers", "binders"]

    for index, item in enumerate(supplies, start=1):
        print(f"Index {index} in supplies is {item}")

if __name__ == "__main__":
    main()
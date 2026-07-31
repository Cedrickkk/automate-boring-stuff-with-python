def main() -> None:
    """Tuple Unpacking"""
    cat: list[str] = ["fat", "gray", "loud"]
    size = cat[0]
    color = cat[1]
    disposition = cat[2]
    print(size, color, disposition)

    # with unpacking
    size, color, disposition = cat
    print(size, color, disposition)


if __name__ == "__main__":
    main()
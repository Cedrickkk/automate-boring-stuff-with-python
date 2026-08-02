def main() -> None:
    name: str = "Zophie"

    print(name[0])
    print(name[-2])
    print(name[0:4])
    print("Zo" in name)
    print("z" in name)
    print("p" not in name)

    for i in name:
        print(f"* * * {i} * * *")


if __name__ == "__main__":
    main()
def main() -> None:
    cats: list[str] = []

    while True:
        name = input(f"Enter the name of cat {len(cats) + 1} (or enter nothing to stop): ")

        if name == "":
            break

        cats.append(name)

    for cat in cats:
        print(cat)



    

if __name__ == "__main__":
    main()
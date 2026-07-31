def main() -> None:
    cats: list[str] = []

    while True:
        name = input(f"Enter the name of cat {len(cats) + 1}: ")

        if name == "":
            break

        cats += [name]

    for cat in cats:
        print(cat)



    

if __name__ == "__main__":
    main()
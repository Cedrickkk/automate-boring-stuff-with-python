def main() -> None:
    pets: list[str] = ["Zophie", "Pooka", "Fat-tail"]
    
    name = input("Enter a pet name: ")
    
    if name not in pets:
        print(f"I do not have pet named {name}")
    else:
        print(f"{name} is my pet")
        
if __name__ == "__main__":
    main()
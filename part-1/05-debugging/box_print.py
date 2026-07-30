def main() -> None:
    print("Enter symbol")
    symbol = input("> ")

    print("Enter height")
    height = int(input("> "))

    print("Enter width")
    width = int(input("> "))

    box_print(symbol, width, height)

def box_print(symbol: str, width: int, height: int) -> None:
    if len(symbol) != 1:
        raise Exception("Symbol must be a single character string.")
    if width <= 2:
        raise Exception("Width must be greater than 2.")  
    if height <= 2:
        raise Exception("Height must be greater than 2.")

    print(symbol * width)

    for _ in range(height - 2):
        print(f"{symbol + (" " * (width - 2)) + symbol}")

    print(symbol * width)

if __name__ == "__main__":
    main()
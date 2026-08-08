from typing import Any

def main() -> None:
    spam: dict[str, Any] = {"name": "Pooka", "age": 5}  

    # setting a value if key doesn't exist
    if "color" not in spam:
        spam["color"] = "black"
    print(spam)

    # setting value with .setdefault() method
    spam: dict[str, Any] = {"name": "Pooka", "age": 5}
    spam.setdefault("color", "black") # set 'colors' key to 'black's
    print(spam)

    spam.setdefault("color", "white") # does nothing
    print(spam)


    
    
    
if __name__ == "__main__":
    main()
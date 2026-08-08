from typing import Any

def main() -> None:
    spam: dict[str, Any] = {"color": "red", "age": 42}

    # iterate through the dictionary values
    for v in spam.values():
        print(v)

    # iterate through the dictionary keys
    for k in spam.keys():
        print(k)

    # check if given key exists in dictionary keys
    print("color" in spam.keys())
    print("age" not in spam.keys())

    # check if given value exists in dictionary values
    print("red" in spam.keys())

    # get item(tuple) in dictionary
    for i in spam.items():
        print(i)
        print(type(i) is tuple)

    # multiple assignment in dictionary items
    for k, v in spam.items():
        print(k, v)

    # getting a value with .get() method
    picnic_items: dict[str, int] = {"apples": 5, "cups": 2, "banana": 10}
    print(f"I am bringing {picnic_items.get("cups", 0)} cups.")
    print(f"I am bringing {picnic_items.get("eggs", 0)} eggs.")
    # print(f"I am bringing {picnic_items['eggs']} eggs.") -> will throw an error
    
    
if __name__ == "__main__":
    main()
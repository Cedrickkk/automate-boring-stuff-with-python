def main() -> None:
    """Adding new items in a list via .append() or .insert()"""

    # append()
    spam: list[str] = ["cat", "dog", "bat"]
    spam.append("moose")
    print(spam)

    # insert()
    spam.insert(1, "chicken") 
    print(spam)
    
    

if __name__ == "__main__":
    main()
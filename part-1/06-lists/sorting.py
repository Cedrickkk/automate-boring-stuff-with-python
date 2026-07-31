def main() -> None:
    spam: list[str] = ["cat", "bat", "rat", "elephant"]
    spam.sort()
    print(spam)

    nums: list[float] = [2, 5, 3.14, 1, -7]
    nums.sort() 
    print(nums)

if __name__ == "__main__":
    main()
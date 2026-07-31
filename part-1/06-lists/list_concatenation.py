def main() -> None:
    """List concatenation and replication"""
    nums: list[int] = [1, 2, 3, 4, 5]
    chars: list[str] = ["A", "B", "C", "D", "E"]
    combined_list: list[str | int] = nums + chars
    print(combined_list)
    replicated_list: list[str] = chars * 3
    print(replicated_list)

if __name__ == "__main__":
    main()
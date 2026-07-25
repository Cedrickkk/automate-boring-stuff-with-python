def main() -> None:
    say_hello_to("Cedrick")
    say_hello_to("Ericka")

def say_hello_to(name: str) -> None:
    print(f"Hello {name}")

if __name__ == "__main__":
    main()
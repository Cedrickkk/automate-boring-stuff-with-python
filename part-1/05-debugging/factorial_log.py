import logging

logging.basicConfig(filename="factorial_log.txt",level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main() -> None:
    logging.debug("Start of program")
    num = int(input("Enter a number: "))
    print(factorial(num))
    logging.debug("End of program")

def factorial(n: int) -> int:
    logging.debug(f"Start of factorial({n})")
    total: int = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug(f"i is {i}, total is {total}")
    logging.debug(f"End of factorial({n})")
    return total

if __name__ == "__main__":
    main()
import time, sys

def main() -> None:
    try:
        for i in range(1, 9):
            print("-" * (i * i))
            time.sleep(0.1)

        for i in range(7, 1, -1):
            print("-" * (i * i))
            time.sleep(0.1)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()
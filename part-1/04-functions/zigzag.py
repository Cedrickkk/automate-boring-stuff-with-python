import time, sys

def main() -> None:
    indent: int = 0
    indent_increasing: bool = True

    try:
        while True:
            print(" " * indent, end="")
            print("********")
            time.sleep(0.1) # Pause for 1/10th of a secoond

            if indent_increasing:
                # Increase the number of spaces
                indent += 1

                if indent == 20:
                    # Change direction
                    indent_increasing = False
            else:
                # Decrease the number of spaces
                indent -= 1

                if indent == 0:
                    # Change direction
                    indent_increasing = True


    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()
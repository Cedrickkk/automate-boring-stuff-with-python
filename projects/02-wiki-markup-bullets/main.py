from pyperclip import paste, copy

def main():
    text: str = paste()
    lines: list[str] = text.split("\n")

    for i in range(len(lines)):
        lines[i]  = ' * ' + lines[i]

    text = '\n'.join(lines)
    
    copy(text)    
    print(text)

if __name__ == "__main__":
    main()

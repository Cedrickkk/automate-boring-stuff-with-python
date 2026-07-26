def main() -> None:
    a()

def a() -> None:
    print("a() starts")
    b()
    d()
    print("a() returns")

def b() -> None:
    print("b() starts")
    c()
    print("b() returns")

def c() -> None:
    print("c() starts")
    print("c() returns")

def d() -> None:
    print("d() starts")
    print("d() returns")

if __name__ == "__main__":
    main()
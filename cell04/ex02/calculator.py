#!/usr/bin/env python3

def main():
    n1 = int(input("Give me the first number: "))
    n2 = int(input("Give me the second number: "))
    a = n1 + n2
    b = n1 - n2
    c = n1 // n2
    d = n1 * n2
    print(f"{n1} + {n2} = {a}")
    print(f"{n1} - {n2} = {b}")
    print(f"{n1} / {n2} = {c}")
    print(f"{n1} * {n2} = {d}")
   

if __name__ == "__main__":
    main()

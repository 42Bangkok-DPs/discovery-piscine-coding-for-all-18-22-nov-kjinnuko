#!/usr/bin/env python3

def main():
    n = int(input("Enter a number\n"))

    for i in range(0, 10):  
        print(f"{i} x {n} = {n * i}")

if __name__ == "__main__":
    main()

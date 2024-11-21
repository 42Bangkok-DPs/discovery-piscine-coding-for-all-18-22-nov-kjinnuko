#!/usr/bin/env python3

def main():
    n = input("Give me a number: ")
    
    if n.replace('.', '', 1).isdigit():
        num = float(n)
        if num.is_integer():
            print("This number is an integer.")
        else:
            print("This number is a decimal.")

if __name__ == "__main__":
    main()


#!/usr/bin/env python3

def main():

    n = float(input("Give me a number: "))
    
    if n == int(n):
        rn = int(n)  
    else:
        rn = int(n) + 1  
    
    print(f"{rn}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def main():

    n = int(input("Enter a number less than 25\n"))
    
    if n > 25:
        print("Error")
    else:
        while n <= 25:
            print(f"Inside the loop, my variable is {n}")
            n += 1

if __name__ == "__main__":
    main()
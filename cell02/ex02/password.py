#!/usr/bin/env python3

def main():
    password = "Python is awesome"
    user = input()
    if user == password:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")

if __name__ == "__main__":
    main()

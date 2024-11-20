#!/usr/bin/env python3

def main():
    user_input = input("What you gotta say? : ")  
    while True:  

        if user_input == "STOP": 
            break 
        else:
            user_input = input("I got that! Anything else? : ")

if __name__ == "__main__":
    main()

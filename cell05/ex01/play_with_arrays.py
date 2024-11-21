#!/usr/bin/env python3

def main():
    oa = [2, 8, 9, 48, 8, 22, -12, 2]

    na = [x + 2 for x in oa]
 
    print(f"Original array: {oa}")
    print(f"New array: {na}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import sys

def main():

    if len(sys.argv) != 2:
        print("none")
        return


    print(sys.argv[1].lower())

if __name__ == "__main__":
    main()

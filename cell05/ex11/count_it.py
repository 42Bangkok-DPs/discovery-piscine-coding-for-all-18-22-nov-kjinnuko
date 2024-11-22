#!/usr/bin/env python3

import sys

def main():

    if len(sys.argv) == 1:
        print("none")
        return

    parameters_count = len(sys.argv) - 1
    print(f"parameters: {parameters_count}")

    for param in sys.argv[1:]:
        print(f"{param}: {len(param)}")

if __name__ == "__main__":
    main()

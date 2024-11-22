#!/usr/bin/env python3

import sys
import re

def main():
    if len(sys.argv) != 3:
        print("none")
        return

    keyword = sys.argv[1]
    search_string = sys.argv[2]

    matches = re.findall(rf'\b{re.escape(keyword)}\b', search_string)

   
    if matches:
        print(len(matches))
    else:
        print("none")

if __name__ == "__main__":
    main()

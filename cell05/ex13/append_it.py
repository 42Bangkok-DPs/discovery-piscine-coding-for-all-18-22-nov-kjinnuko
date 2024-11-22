#!/usr/bin/env python3

import sys

def main():
 
    if len(sys.argv) == 1:
        print("none")
        return

   
    for param in sys.argv[1:]:
    
        if param.endswith("ism"):
            continue
     
        print(f"{param}ism")

if __name__ == "__main__":
    main()

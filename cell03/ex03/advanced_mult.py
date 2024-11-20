#!/usr/bin/env python3

def main():
    n = 0  
    while n <= 10:
        print(f"Table de {n}:", " ".join(str(n * i) for i in range(11)))
        n += 1 
        
if __name__ == "__main__":
    main()

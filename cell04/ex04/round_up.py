#!/usr/bin/env python3

def main():

    n = float(input("Give me a number: "))
    
    if n == int(n):
        rn = int(n)  # ถ้าเป็นจำนวนเต็มใช้ค่าตัวเลขเดิม
    else:
        rn = int(n) + 1  # ถ้าไม่ใช่จำนวนเต็มปัดขึ้น
    
    print(f"{rn}")

if __name__ == "__main__":
    main()

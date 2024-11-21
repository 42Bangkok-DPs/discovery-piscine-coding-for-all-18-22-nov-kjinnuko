import sys
from checkmate import checkmate

def main():
    # ตรวจสอบว่าได้รับอาร์กิวเมนต์ไฟล์หรือไม่
    if len(sys.argv) < 2:
        print("Error")
        return

    # อ่านไฟล์ที่ได้รับมา
    for filename in sys.argv[1:]:
        try:
            with open(filename, 'r') as file:
                board = file.read().strip()  # อ่านเนื้อหาในไฟล์
                # ตรวจสอบกระดานหมากรุก
                checkmate(board)
        except FileNotFoundError:
            print(f"Error: ไม่พบไฟล์ {filename}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

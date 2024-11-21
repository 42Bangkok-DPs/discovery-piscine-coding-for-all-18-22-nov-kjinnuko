from checkmate import checkmate  # นำเข้าฟังก์ชัน checkmate จาก checkmate.py

def main():
    board = """\
R...
.K..
..P.
....\
"""
    checkmate(board)  # เรียกฟังก์ชัน checkmate พร้อมส่งกระดานเป็นพารามิเตอร์

if __name__ == "__main__":
    main()

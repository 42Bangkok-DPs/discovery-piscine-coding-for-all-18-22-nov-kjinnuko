import sys
from checkmate import checkmate

def main():
    
    if len(sys.argv) < 2:
        print("Error")
        return


    for filename in sys.argv[1:]:
        try:
            with open(filename, 'r') as file:
                board = file.read().strip()  
                checkmate(board)
        except FileNotFoundError:
            print(f"Error: ไม่พบไฟล์ {filename}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

def checkmate(bd):
    # แปลงกระดานเป็น 2D array
    bd = bd.splitlines()
    sz = len(bd)

    # หาตำแหน่งของ King (K)
    kp = None
    for x in range(sz):
        for y in range(sz):
            if bd[x][y] == 'K':
                kp = (x, y)
                break
        if kp:
            break

    if not kp:
        print("Error: ไม่พบ King")
        return

    kx, ky = kp

    # ฟังก์ชันช่วยตรวจสอบในทิศทางต่างๆ
    def ib(x, y):
        return 0 <= x < sz and 0 <= y < sz

    # ฟังก์ชันสำหรับการตรวจสอบการโจมตีตามทิศทางต่างๆ
    def cd(dx, dy, atk):
        x, y = kx + dx, ky + dy
        while ib(x, y):
            pc = bd[x][y]
            if pc != '.':
                return pc in atk
            x += dx
            y += dy
        return False

    # ตรวจสอบการโจมตีของ Pawn (P)
    def cp():
        # Pawn โจมตีแนวทแยง (เพียงแค่ 2 ทิศทาง)
        pa = [(1, -1), (1, 1)]  # Pawn สามารถเดินทแยงไปข้างหน้าได้
        for dx, dy in pa:
            x, y = kx + dx, ky + dy
            if ib(x, y) and bd[x][y] == 'P':
                return True
        return False

    # ตรวจสอบการโจมตีของ Knight (N)
    def ck():
        # Knight โจมตีในรูปตัว L (8 ทิศทาง)
        km = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]
        for dx, dy in km:
            x, y = kx + dx, ky + dy
            if ib(x, y) and bd[x][y] == 'N':
                return True
        return False

    # ตรวจสอบการโจมตีของ Rook (R) และ Queen (Q) ในแนวตั้งและแนวนอน
    if cd(0, 1, 'RQ') or cd(0, -1, 'RQ') or \
       cd(1, 0, 'RQ') or cd(-1, 0, 'RQ'):
        print("Success")
        return

    # ตรวจสอบการโจมตีของ Bishop (B) และ Queen (Q) ในแนวทแยง
    if cd(1, 1, 'BQ') or cd(1, -1, 'BQ') or \
       cd(-1, 1, 'BQ') or cd(-1, -1, 'BQ'):
        print("Success")
        return

    # ตรวจสอบการโจมตีของ Pawn (P)
    if cp():
        print("Success")
        return

    # ตรวจสอบการโจมตีของ Knight (N)
    if ck():
        print("Success")
        return

    # หากไม่มีภัยคุกคาม
    print("Fail")

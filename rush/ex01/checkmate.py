def checkmate(bd):
    bd = bd.splitlines()
    sz = len(bd)

    kp = None
    for x in range(sz):
        for y in range(sz):
            if bd[x][y] == 'K':
                kp = (x, y)
                break
        if kp:
            break

    if not kp:
        print("Error")
        return

    kx, ky = kp

    def ib(x, y):
        return 0 <= x < sz and 0 <= y < sz

    def cd(dx, dy, atk):
        x, y = kx + dx, ky + dy
        while ib(x, y):
            pc = bd[x][y]
            if pc != '.':
                return pc in atk
            x += dx
            y += dy
        return False

    def cp():
        pa = [(1, -1), (1, 1)]
        for dx, dy in pa:
            x, y = kx + dx, ky + dy
            if ib(x, y) and bd[x][y] == 'P':
                return True
        return False

    def ck():
        km = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]
        for dx, dy in km:
            x, y = kx + dx, ky + dy
            if ib(x, y) and bd[x][y] == 'N':
                return True
        return False

    if cd(0, 1, 'RQ') or cd(0, -1, 'RQ') or cd(1, 0, 'RQ') or cd(-1, 0, 'RQ'):
        print("Success")
        return

    if cd(1, 1, 'BQ') or cd(1, -1, 'BQ') or cd(-1, 1, 'BQ') or cd(-1, -1, 'BQ'):
        print("Success")
        return

    if cp():
        print("Success")
        return

    if ck():
        print("Success")
        return

    print("Fail")

for tc in range(1, 11):
    L = int(input())
    board = [input() for _ in range(8)]

    cnt = 0

    # 가로 검사
    for r in range(8):
        row = board[r]
        for c in range(8 - L + 1):
            ok = True
            for k in range(L // 2):
                if row[c + k] != row[c + L - 1 - k]:
                    ok = False
                    break
            if ok:
                cnt += 1

    # 세로 검사
    for c in range(8):
        for r in range(8 - L + 1):
            ok = True
            for k in range(L // 2):
                if board[r + k][c] != board[r + L - 1 - k][c]:
                    ok = False
                    break
            if ok:
                cnt += 1

    print(f"#{tc} {cnt}") 
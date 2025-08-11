T = int(input())

#상하좌우 델타값
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for tc in range(1, T+1):
    N, M, = map(int, input().split())

    Hij = [list(map(int, input().split())) for _ in range(N)]
    # 각 구역의 높이 리스트

    for i in range(N):
        for j in range(M):
            s = Hij[i][j]

            for d in range(4):   # 기준점 (i, i)에서 델타값의 범위
                ni = i + di[d]
                nj = j + dj[d]

            best = 0
            if ni < 0 or ni >= N or nj < 0 or nj >= M:  #가장자리를 제외
                continue
                best = max(matrix[ni][nj])   #기준점 상하좌우 중 가장 큰 값

            count = 0       #안전구역
            if s > best:
                count += 1   #만약 기준점 크기가 best가 작다면 count가 1올라간다.
            else:
                count = 0


    print(f'#{tc} {count}')
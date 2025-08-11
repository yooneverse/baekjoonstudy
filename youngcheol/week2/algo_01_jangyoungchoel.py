T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    #N : 우주 영역의 크기
    #M : 탐색 영역의 크기
    #K : 별의 개수
    matrix = [list(map(str, input())) for _ in range(N)]

    star = 0 # M*M 영역 안의 별의 개수


    for i in range(N-M+1):     # 전체  N 영역에 놓일 수 있는 M의 크기는 N-M이다
        for j in range(N-M+1):
            s = matrix[i][j]

            for di in range(M):
                for dj in range(M):

                    if matrix[di][dj] == '0': #만약 인덱스 (di, dj)의 값이 0이라면 별의 개수는 0
                       star = 0
                    else:               # 그렇지 않다면 star의 개수 1씩 오른다
                        star += 1
            if star == K:               # 만약 star의 개수가 K랑 값이 같다면 matrix[di][dj]의 값을 생성한다
                s
            else :
                print(-1, -1)
                break


    print(f'#{tc} {s}')

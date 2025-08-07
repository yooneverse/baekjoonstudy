T = 10  # 테스트 케이스 수 고정
 
for tc in range(1, T + 1):
    input()  # 각 테스트케이스의 첫 줄은 사용하지 않으므로 무시!! input 받고 사용하지 않기
 
    N = 100  # 배열의 크기 (100x100)
 
    # 배열 입력받기
    matrix = [list(map(int, input().split())) for _ in range(N)]
 
    max_sum = 0  # 최대 합을 저장할 변수
    
    # 1. 행의 합
    for i in range(N):  # 각 행을 한 줄씩 순회
        row_sum = 0
        for j in range(N):  # 해당 행의 각 열 값을 더함
            row_sum += matrix[i][j]
        if row_sum > max_sum:
            max_sum = row_sum  # 현재까지의 최대값보다 크면 갱신
 
    # 2. 열의 합
    for j in range(N):  # 각 열을 순회
        col_sum = 0
        for i in range(N):  # 해당 열의 각 행 값을 더함
            col_sum += matrix[i][j] 
        if col_sum > max_sum:
            max_sum = col_sum
 
    # 3. 우하향 대각선 합
    # 왼쪽 위 (0,0) -> 오른쪽 아래 (99,99)
     
    diag1_sum = 0
    for i in range(N):
        diag1_sum += matrix[i][i]
    if diag1_sum > max_sum:
        max_sum = diag1_sum
 
    # 4. 우상향 대각선 합
    # 왼쪽 아래 (99,0) -> 오른쪽 위 (0,99)
    # 인덱스 공식: (i, N-1-i)
    diag2_sum = 0
    for i in range(N):
        diag2_sum += matrix[i][N - 1 - i]
    if diag2_sum > max_sum:
        max_sum = diag2_sum
 
    print(f"#{tc} {max_sum}")

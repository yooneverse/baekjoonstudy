T = int(input()) # 테스트케이스(지도) 개수(3<=T<10)

# tc=test_case 불러오기
for tc in range(1, T + 1):
    

    N, M, K = map(int, input().split())  # 문자열 -> 정수 변환

    # N*N 배열
    # box = [list(input().split()) for _ in range(N)] ** 틀림
    space = [list(input()) for _ in range(N)]
    # 입력받아서 숫자로 못 바꾸니까 리스트로만 문자열 그대로 처리 N줄 입력 받음

    # 별 자리
    # 파리 퇴치와 달리, 합이 아닌 좌표를 구해야 함, 그러나 K개를 구한다는 점에서 합이 필요
    star_idx = []
    # 우주 빈 공간은 0
    # 별은 *로 주어짐

    # 일단 없다고 가정
    row = -1
    col = -1

    # 시작점 구하기
    for i in range(N - M + 1):  # M*M 배열로 찾기
        for j in range(N - M + 1):
            total = 0

            result = []  # 정답 좌표를 담을 빈 리스트

            for r in range(i, i + M):
                for c in range(j, j + M):  # 중심점에서 M만큼
                    star = space[r][c]

                    if star == '*':   # 별은 '*' 로 주어짐
                        total += 1
                        result.append((r, c))  # 참고용으로 좌표 저장

            if total == K:
                # 합이 K인 경우 해당 시작좌표를 정답으로 기록 (1-인덱스가 필요 없으면 i, j 그대로)
                row = i
                col = j
                star_idx.append((i, j))  # 필요시 사용

    # 출력 형식
    print(f"#{tc} {row} {col}")


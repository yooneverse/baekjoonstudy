# 다른 문제지만 gravity랑 묘하게 같은 결인 느낌

T = 10  # 테스트케이스 수

# tc : test_case
for tc in range(1, T + 1):
    dump_cnt = int(input())  # 평탄화할 덤프 횟수
    heights = list(map(int, input().split()))  # 100개의 상자 높이를 리스트로 입력받음

    # 높이가 0부터 100까지 있을 수 있으므로 크기 101짜리 배열 생성
    # cnt[h]는 '높이 h를 가진 상자의 개수'를 의미함
    cnt = [0] * 101

    # 입력받은 높이들을 카운팅 배열에 반영
    for height in heights:
        cnt[height] += 1

    # 정해진 횟수만큼 평탄화 수행
    for _ in range(dump_cnt):

        # 최소 높이(left) 찾기
        # 카운팅 배열은 왼쪽에서 오른쪽으로 높이가 커지므로,
        # cnt[left] > 0인 가장 작은 left가 최소 높이
        left = 0
        while cnt[left] == 0:
            left += 1

        # 최대 높이(right) 찾기
        # 카운팅 배열은 오른쪽에서 왼쪽으로 높이가 작아지므로,
        # cnt[right] > 0인 가장 큰 right가 최대 높이
        right = 100
        while cnt[right] == 0:
            right -= 1

        # 이미 평탄화가 완료된 경우: 최대 - 최소 <= 1이면 종료
        if right - left <= 1:
            break

        # 평탄화 작업 수행
        # -> 가장 높은 곳에서 상자 하나 빼서 가장 낮은 곳 위에 놓기
        # -> 높이 차이를 줄이기 위한 전략
        cnt[left] -= 1         # 가장 낮은 위치에서 상자 1개 제거
        cnt[left + 1] += 1     # 그보다 한 칸 높은 위치에 추가

        cnt[right] -= 1        # 가장 높은 위치에서 상자 1개 제거
        cnt[right - 1] += 1    # 그보다 한 칸 낮은 위치에 추가

    # 덤프가 끝난 후, 다시 최종 최대/최소 높이를 계산
    left = 0
    while cnt[left] == 0:
        left += 1

    right = 100
    while cnt[right] == 0:
        right -= 1

    # 결과 출력: 최댓값 - 최솟값
    print(f"#{tc} {right - left}")
N, K = map(int, input().split())
A = list(map(int, input().split()))  # N개의 숫자 입력 받기

def bubble_sort(A, N, K):
    count = 0  # 전체 교환 횟수 카운트

    for last in range(N - 1, 0, -1):  # N-1부터 1까지 감소
        for i in range(0, last):      # 0부터 last-1까지 반복
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                count += 1
                if count == K:
                    print(*A)  # K번째 교환 배열 출력
                    return

    print(-1)

bubble_sort(A, N, K)

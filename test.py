def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    swaps = 0
    i = 0

    # i가 N-1 미만인 동안, 그리고 아직 K회 교환 전인 동안 반복
    while i < N-1 and swaps < K:
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
            swaps += 1
            if swaps == K:
                print(*A)
                return
            # 스왑 후에는 한 칸 뒤로 돌아가 인접 비교
            i = max(i-1, 0)
        else:
            i += 1

    # K번 교환 미달 시
    print(-1)

if __name__ == "__main__":
    solve()
def solution(n, k):
    from collections import deque
    dq = deque([x for x in range(1, n+1)])
    count = 0
    while len(dq) != 1:
        count += 1
        if count == k:
            dq.popleft()
            count %= k
        else:
            dq.rotate(-1)
    return dq.pop()


if __name__ == "__main__":
    import sys
    sys.stdin = open("./testcase/input5.txt")
    for line in sys.stdin:
        n, k = map(int, line.split())
        answer = solution(n, k)
        print(answer)
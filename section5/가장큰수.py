def solution(n, m):
    from itertools import combinations
    n = str(n)
    answer = max(list(map(lambda x: int("".join(x)), list(combinations(n, r=len(n)-m)))))
    return answer


if __name__ == "__main__":
    import sys
    sys.stdin = open("./testcase/input1.txt", "r")
    n, m = map(int, input().split())
    print(solution(n, m))

import sys
from collections import deque

def solution(n, lst):
    dq = deque()
    for i in range(n, 0, -1):
        dq.insert(lst.pop(),i)
    return " ".join(list(map(str, dq)))


if __name__ == "__main__":
    sys.stdin = open("input9.txt", "r")
    n = int(input())
    lst = list(map(int, input().split()))
    answer = solution(n, lst)
    print(answer)
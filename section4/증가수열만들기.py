import sys
from collections import deque

def solution(lst):
    dq = deque(lst)
    position = ""
    end = 0
    while(dq):
        if len(dq) == 1 :
            if dq[0] > end:
                position += "L"
                break
            break
        elif dq[0] > end and dq[-1] > end :
            if dq[0] > dq[-1]:
                end = dq.pop()
                position += "R"
            else:
                end = dq.popleft()
                position += "L"
        elif dq[0] > end or dq[-1] > end :
            if dq[0] > dq[-1]:
                end = dq.popleft()
                position += "L"
            else:
                end = dq.pop()
                position += "R"
        else:
            break
    print(len(position))
    print(position)
    return



if __name__ == "__main__" :
    sys.stdin = open("input8.txt", "r")
    n = int(input())
    lst = list(map(int, input().split()))
    solution(lst)
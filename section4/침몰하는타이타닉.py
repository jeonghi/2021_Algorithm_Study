import sys
from collections import deque

def solution(m, lst):
    lst.sort()
    count = 0
    while(lst):
        i = lst.pop(0)
        j = sorted(list(filter(lambda x: (i+x<=m), lst)), reverse = True)
        if j:
            lst.remove(j[0])
            count += 1
        else:
            count += 1
            count += len(lst)
            break
    return count

def solution2(m, lst): # 강의풀이코드
    lst.sort()
    lst = deque(lst)
    count = 0
    while(lst):
        if len(lst)==1:
            count += 1
            break
        if lst[0]+lst[-1]>m:
            lst.pop()
            count += 1
        else:
            lst.popleft()
            #lst.pop(0) # 리스트의 pop연산을 하게 되면 모든 요소 한칸씩 한칸씩 당겨지게 된다. deque를 사용하면 링크드 리스트로 되어있어서 더 효율적이다.
            lst.pop()
            count += 1
    return count


if __name__ == "__main__":
    sys.stdin = open("input7.txt", "r")
    n, m = map(int,input().split())
    lst = list(map(int, input().split()))
    print(solution2(m, lst))
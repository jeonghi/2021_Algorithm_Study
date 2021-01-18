def solution(n, m):
    from itertools import combinations
    answer = max(map(lambda x: int("".join(x)), combinations(n, r=len(n)-m)))
    return answer

def solution2(n, m):
    from collections import deque
    dq = deque(map(int,n))
    lst = list()
    while(len(dq)!=0):
        if len(lst) == 0 :
            lst.append(dq.popleft())
        elif lst[-1] < dq[0] and len(lst)+len(dq)>len(n)-m:
            lst.pop()
        else:
            if len(lst) == len(n)-m:
                dq.popleft()
            else:
                lst.append(dq.popleft())
    return "".join(map(str, lst))

def solution3(n, m):
    stk = list()
    for i in n:
        while stk and m>0 and stk[-1]<i:
            stk.pop()
            m -= 1
        stk.append(i)

    if m!= 0:
        stk = stk[:-m]
    return "".join(map(str, stk))




if __name__ == "__main__":
    import sys
    sys.stdin = open("./testcase/input1.txt", "r")
    n, m = input().split()
    m = int(m)
    print(solution3(n, m))

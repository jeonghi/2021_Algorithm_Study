import sys

def solution(m, lst):
    lst.sort(key=lambda x:x)
    for i in range(m):
        rt = len(lst)-1
        lt = 0
        while((lst[rt-1]>=lst[rt])):
            rt-=1
        while(lst[lt]>=lst[lt+1]):
            lt+=1
        lst[rt] -= 1
        lst[lt] += 1
    return (lst[-1]-lst[0])


if __name__ == "__main__":
    sys.stdin = open("input6.txt", "r")
    l = int(input())
    lst = list(map(int, input().split()))
    m = int(input())
    answer = solution(m, lst)
    print(answer)
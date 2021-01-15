import sys

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


if __name__ == "__main__":
    sys.stdin = open("input7.txt", "r")
    n, m = map(int,input().split())
    lst = list(map(int, input().split()))
    print(solution(m, lst))
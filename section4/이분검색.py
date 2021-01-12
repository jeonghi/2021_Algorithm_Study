def solution(lst, target):
    lst.sort()
    begin = 0
    end = len(lst)-1
    while(begin<=end):
        mid = (begin+end)//2
        if lst[mid] == target :
            return mid+1
        else:
            if lst[mid] < target :
                begin = mid+1
            else:
                end = mid-1

if __name__ == "__main__":
    import sys
    sys.stdin = open("input.txt", "r")
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    answer = solution(a, m)
    print(answer)
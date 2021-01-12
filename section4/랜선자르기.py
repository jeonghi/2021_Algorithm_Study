def solution1(n, lst): # O(n) 전체 탐색 이용
    answer = 0
    for i in range(1, max(lst)):
        temp = [x//i for x in lst]
        if sum(temp) >= n:
            answer = i
        else:
            return answer
    print("end")
    return answer


def solution2(n, lst): # O(log N) 이분 탐색 이용
    begin = 1
    end = max(lst)
    answer = 0
    while(begin<=end):
        mid = (begin+end)//2
        temp = [x//mid for x in lst]
        if sum(temp) >= n:
            answer = mid
            begin = mid+1
        else:
            end = mid-1
    return answer


if __name__ == "__main__":
    import sys
    sys.stdin = open("input1.txt", "r")
    k, n = map(int, input().split())
    a = list()
    for i in range(k):
        a.append(int(input()))
    answer1 = solution1(n, a)
    answer2 = solution2(n, a)
    print(answer1, answer2)
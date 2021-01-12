def is_acceptable(m, limit, lst):
    temp = lst.copy()
    count = 1
    curr = 0
    while(temp and (count <= m)):
        if curr + temp[-1] > limit:
            count += 1
            curr = 0
        else:
            curr += temp.pop()
    if count > m:
        return False
    else:
        return True

def solution(m, lst):
    begin = 1
    end = sum(lst)
    answer = 0
    while(begin<=end):
        mid = (begin+end)//2
        if is_acceptable(m, mid, lst): # acceptable
            answer = mid
            end = mid-1
        else:
            begin = mid+1
    return answer



if __name__ == "__main__":
    import sys
    sys.stdin = open("input2.txt", "r")
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    #a.reverse()
    answer = solution(m, a)
    print(answer)
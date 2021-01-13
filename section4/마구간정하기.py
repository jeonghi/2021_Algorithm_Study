def shortest_distance(lst):
    temp = max(lst)
    for i in range(len(lst)-1):
        sub = lst[i+1] - lst[i]
        if sub < temp :
            temp = sub
    return temp

def solution(c, lst):
    from itertools import combinations
    lst.sort()
    max_distance = max(map(shortest_distance, list(combinations(lst, r=c))))
    return max_distance

def is_acceptable_distance(c, distance, lst):
    count = 1
    curr = lst[0]
    for i in range(1,len(lst)):
        if lst[i]-curr >= distance:
            count += 1
            curr = lst[i]
    if count >= c:
        return True
    return False

def solution_using_binary_search(c, lst):
    lst.sort()
    lt = lst[0]
    rt = lst[-1]
    answer = 1
    while(lt<=rt):
        curr = (lt+rt)//2  # current shortest distance
        if is_acceptable_distance(c, curr, lst) is True: # 이 거리가 가능하다면 더 긴 거리도 되는지 보면 됨
            answer = curr
            lt = curr + 1
        else:
            rt = curr - 1
    return answer


if __name__ == "__main__":
    import sys
    import time
    sys.stdin = open("input3.txt", "r")
    n, c = map(int, input().split())
    lst = list()
    for i in range(n):
        lst.append(int(input()))
    prev_time = time.time()
    answer1 = solution(c, lst)
    prev_time = time.time() - prev_time
    print(prev_time)

    prev_time = time.time()
    answer2 = solution_using_binary_search(c, lst)
    prev_time = time.time() - prev_time
    print(prev_time)
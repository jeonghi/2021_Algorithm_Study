def is_acceptable_capacity(meeting_capacity, meeting):
    from itertools import combinations
    cases = list(combinations(meeting, r=meeting_capacity))
    for case in cases:
        count = 1
        for t in range(0,len(case)-1):
            if case[t][1] <= case[t+1][0]:
                count += 1
            else:
                break
        if count >= meeting_capacity:
            return True
    return False

def solution(n, meeting):
    meeting.sort(key=lambda x: (x[0],x[1]))
    lt = 1
    rt = n
    answer = 1
    while(lt<=rt):
        meeting_capacity = (lt+rt)//2
        if is_acceptable_capacity(meeting_capacity, meeting) is True:
            answer = meeting_capacity
            lt += 1
        else:
            rt -= 1
    return answer

def solution2(n, meeting): # 강의에서 풀이해준 코드
    lst.sort(key=lambda x: (x[1], x[0]))
    end_time = 0
    count = 0
    for start, end in meeting:
        if start >= end_time :
            end_time = end
            count += 1
    return count




if __name__ == "__main__":
    import sys
    sys.stdin = open("input4.txt", "r")
    n = int(input())
    lst = list()
    for i in range(n):
        lst.append(tuple(map(int, input().split())))
    answer = solution(n, lst)
    answer = solution2(n, lst)
    print("Answer is {}".format(answer))
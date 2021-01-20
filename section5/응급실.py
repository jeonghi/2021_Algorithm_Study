def solution(m, patient_lst):
    from collections import deque
    dq = deque(patient_lst)
    patient_lst.sort(reverse=False)
    count = 0
    while dq:
        if dq[0] == patient_lst[-1]:
            dq.popleft()
            patient_lst.pop()
            count += 1
            if m == 0:
                return count
            else:
                m -= 1
        else:
            dq.rotate(-1)
            if m == 0:
                m = len(dq)-1
            else:
                m -= 1




if __name__ == '__main__':
    import sys
    sys.stdin = open("./testcase/input6.txt")
    n, m = map(int, input().split())
    patient_lst = list(map(int, input().split()))
    print(solution(m, patient_lst))
def solution(curriculum, students_plans):
    from collections import deque
    answer = list()
    for students_plan in students_plans:
        dq = deque(curriculum)
        students_plan = deque(students_plan)
        while(students_plan and dq):
            if students_plan.popleft() == dq[0]:
                dq.popleft()
        answer.append("NO") if dq else answer.append("YES")
    return answer


if __name__ == "__main__":
    import sys
    sys.stdin = open("./testcase/input7.txt")
    curriculum = input().rstrip()
    n = int(input())
    students_plans = list()
    for _ in range(n):
        students_plans.append(input())
    print(solution(curriculum, students_plans))
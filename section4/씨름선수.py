import sys


def solution(applicants):
    applicants.sort(key=lambda x:x[0])
    count = 0
    for idx , applicant in enumerate(applicants) :
        if idx == len(applicants)-1:
            count += 1
            return count
        else:
            flag = True
            for i in range(idx,len(applicants)):
                if applicant[1] < applicants[i][1]:
                    flag = False
            if flag :
                count += 1

def solution2(applicants): # 문제풀이 코드
    applicants.sort(key=lambda x:x[0], reverse=True)
    largest = 0
    count = 0
    for x, y in applicants:
        if y > largest:
            largest = y
            count += 1
    return count


if __name__ == "__main__":
    sys.stdin = open("input5.txt", "r")
    n = int(input())
    applicants = list()
    for i in range(n):
        applicants.append(tuple(map(int, input().split())))

    answer1 = solution(applicants)
    answer2 = solution2(applicants)
    print(answer2)
def solution(n, answer=""):
    if n <= 1:
        answer += str(n)
        return answer[::-1]
    else:
        answer += str(n%2)
        return solution(n//2, answer)

if __name__ == "__main__":
    import sys
    sys.stdin = open("testCase/input1.txt")
    n = int(input())
    print(solution(n))
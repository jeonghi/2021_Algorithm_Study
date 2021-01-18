def solution(s):
    stk = list()
    count = 0
    stk.append(s[0])
    for x in range(1,len(s)):
        if s[x] == "(" :
            stk.append(s[x])
        else:
            if s[x-1] == "(":
                stk.pop()
                count += len(stk)
            else:
                stk.pop()
                count += 1

    return count

if __name__ == "__main__":
    import sys
    sys.stdin = open("./testcase/input2.txt", "r")
    s = input()
    print(solution(s))
def solution(s1, s2):
    from collections import Counter
    return "YES" if len(list((Counter(s1) - Counter(s2)).elements())) == 0 else "NO"


if __name__ == '__main__':
    import sys
    sys.stdin = open("./testcase/input9.txt")
    s1 = input().rstrip()
    s2 = input().rstrip()
    print(solution(s1, s2))
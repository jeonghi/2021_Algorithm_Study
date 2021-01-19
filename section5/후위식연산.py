def eval_postfix(postfix_notation):
    stk = list()
    for o in postfix_notation:
        if o in "+-*/":
            rt = stk.pop()
            lt = stk.pop()
            if o == '*':
                temp = lt * rt
            elif o == '/':
                temp = lt // rt
            elif o == '-':
                temp = lt - rt
            else:
                temp = lt + rt
            stk.append(temp)
        else:
            stk.append(int(o))

    return stk[-1]

if __name__ == "__main__":
    import sys
    sys.stdin = open("./testcase/input4.txt", "r")
    for line in sys.stdin:
        print(eval_postfix(line.rstrip()))

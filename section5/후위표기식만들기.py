prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2
}

def infix2postfix(infix_notation):
    stk = list()
    postfix_notation = ""
    for o in infix_notation:
        if o in prec:
            if not stk or stk[-1] == '(':
                stk.append(o)
            else:
                while(stk and stk[-1] is not '(' and prec[stk[-1]] >= prec[o]):
                    postfix_notation += stk.pop()
                stk.append(o)
        else:
            if o is ')':
                temp = stk.pop()
                while temp is not '(':
                    postfix_notation += temp
                    temp = stk.pop()
            elif o is '(':
                stk.append(o)
            else:
                postfix_notation += o

    while(stk):
        postfix_notation += stk.pop()
    return postfix_notation


if __name__ == "__main__":
    import sys
    sys.stdin = open("testcase/input3.txt", "r")
    sys.stdout = open("testcase/input4.txt", "w")
    for line in sys.stdin:
        print(infix2postfix(line.rstrip()))


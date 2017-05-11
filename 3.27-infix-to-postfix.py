#! /usr/bin/env python3
# infix expression to postfix ;3.27 Programming Exercises NO1

from Stack import Stack


def standard_expression(s):
    expr = s.split()
    expression = False
    stop = False
    exp_pre = None
    exp_cur = None
    para_stack = Stack()
    
    for exp in expr:
        if exp.isdigit():
            exp_cur = "num"
        elif exp in "+-*/" and len(exp) == 1:
            exp_cur = "operator"
        elif exp in "()" and len(exp) == 1:    
            exp_cur = exp
            if exp == "(":
                para_stack.push(exp)
            elif para_stack.isEmpty():
                stop = True
            else:
                para_stack.pop()
        else:
            stop = True

        if exp_cur == "num" and (exp_pre == "num" or exp_pre == ")"):
            stop = True
        elif exp_cur == "operator" and (exp_pre == "operator" or exp_pre == None or exp_pre == "("):
            stop = True
        elif exp_cur == "(" and exp_pre == ")":
            stop = True
        elif exp_cur == ")" and (exp_pre == None or exp_pre == "operator" or  exp_pre == "("):
            stop = True
        
        exp_pre = exp_cur

        if stop:
            break
    if not para_stack.isEmpty():
        stop = True

    if stop:
        return False
    else:
        return expr
            
def infix_to_postfix(expr):
    exstack = Stack()
    result_list = []

    opr_dir = {"+": 1, '-': 1, '*': 2, '/': 2, '(': 0}
    for exp in expr:
        if exp.isdigit():
            result_list.append(exp)
        elif exp == "(":
            exstack.push(exp)
        elif exp == ")":
            while exstack.peek() != "(":
                result_list.append(exstack.pop())
            exstack.pop()
        else:
            while (not exstack.isEmpty()) and opr_dir[exstack.peek()] >= opr_dir[exp]:
                result_list.append(exstack.pop())
            exstack.push(exp)

    while not exstack.isEmpty():
        result_list.append(exstack.pop())
    return " ".join(result_list)

def main():
    s = input("Please input a infix Expression:")
    expression = standard_expression(s)       
    result = "Illegal Expression, Please input again"
    if expression:
        result = infix_to_postfix(expression)
        print("Result is: ", result)
    else:
        print(result)

if __name__ == '__main__':
    main()

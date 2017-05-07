#! /usr/bin/env python3
#3.9-Conversion of POSTfix Expressions to Infix 
#计算postfix Expressions Value

from Stack import Stack

def postfixEval(postfixExpr):
    operandStak = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStak.push(int(token))
        else:
            operand2 = operandStak.pop()
            operand1 = operandStak.pop()
            result = doMath(token, operand1, operand2)
            operandStak.push(result)
    return operandStak.pop()


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2

s = input("Please input a postfix Expr:")
print("infix Expr Is:", postfixEval(s))

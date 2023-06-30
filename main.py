from stack import Stack
import operator

operations = ["+", "*", "-", "/"]
data = Stack()
expression = input("Enter an expression in RPN \n")

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}
def results(op):
    result = data.peek()
    data.pop()
    result = ops[op](data.peek(),result)
    data.pop()
    data.push(int(result))
    print(f"Results: {data.display()}")
    return f"Using RPN, the result to the expression is {result}"



for tok in range(0, len(expression)):
    if expression[tok].isnumeric():
        parsedData = int(expression[tok])
        data.push(parsedData)
    elif expression[tok] in operations:
        print(results(expression[tok]))
















def eval(str):
    expr = str.split(",")
    if len(expr) == 1: return int(str)
    stack = []

    for char in expr:
        try:
            num = int(char)
            stack.append(num)
        except:
            if char == "+":
                num = stack.pop(0) + stack.pop(0)
                
            elif char == "-":
                num = stack.pop(0) - stack.pop(0)

            elif char == "x":
                num = stack.pop(0) * stack.pop(0)

            elif char == "/":
                num = stack.pop(0) - stack.pop(0)

            stack.append(num)
    return stack[0]

print(eval("3,4,+,2,x,1,+"))

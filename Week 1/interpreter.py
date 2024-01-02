expression = input("Expression: ")
exp_parts = expression.split(' ')
num1 = float(exp_parts[0])
num2 = float(exp_parts[2])
op = exp_parts[1]
if op=='+':
    print(round(num1+num2,1))
elif op=='-':
    print(round(num1-num2,1))
elif op=='*':
    print(round(num1*num2,1))
else:
    print(round(num1/num2,1))
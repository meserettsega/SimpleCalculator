# this is a simple calculator machn
operator = input('Enter the operator(/, -, +, *):')
num1 = float(input('enter the first number:'))
num2 = float(input("enter the ssecond number:"))

if operator == '+':
    result = num1 + num2
    print(result)
elif operator == '-':
    result = num1 - num2
    print(result)
elif operator == '*':
    result =num1*num2
    print(result)
elif operator =='/':
    if num2 !=0:
        result = num1/num2
        print(result)
    else:
        print("undefined!")
else:
    print(f'your {operator} is not valid')

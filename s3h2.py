#parisa najari ghahremani thursday 14-18 class
# tabe mashin hesab sade
def calculator(num1,num2,operation):
    if operation=='+':
        print(num1+num2)
    elif operation=='-':
        print(num1-num2)

    elif operation=='*':
        print(num1*num2)
    elif operation=='/':
        print(num1/num2)

num1=float(input('please enter a number1:\n'))
num2=float(input('please enter a number2:\n'))
operation=input('please enter a operation:\n')


calculator(num1,num2,operation)

#parisa najari ghahremani thursday 14-18 class
#tabeiy ke 4 ta vorodi migire  2 taye avali moshakhasehaye hendesi
#va 2 taye badi noe shekl va khaste morde nazar manand masahat


def mohasebe(num1,num2,amaliat,shape):
    if shape=='rectangle' and amaliat=='masahat':
        print('masahat:',num1*num2)
    elif shape=='rectangle' and amaliat=='mohit':
        print('mohit:',(num1+num2)*2)
    elif shape=='squre'and amaliat=='masahat':
        print('masahat:',num1*num2)
    elif shape=='squre' and amaliat=='mohit':
        print('mohit:',num1*4)
    elif shape=='diamond' and amaliat=='masahat':
        print('masahat:',(num1*num2) /2)
    elif shape=='diamond' and amaliat=='mohit':
        print('mohit',num1*4)
    elif shape=='parallelogram' and amaliat=='masahat':
        print('masahat:',num1*num2)
    elif shape=='parallelogram' and amaliat=='mohit':
        print('mohit:',num1*4)
    else:
        print('please enter a shape in (rectangle,squre,) ')



num1=float(input('please enter a number1:\n'))
num2=float(input('please enter a number2:\n'))
shape=input('please enter a shape:\n')
amaliat=input('please enter a amaliat:\n')

mohasebe(num1,num2,amaliat,shape)

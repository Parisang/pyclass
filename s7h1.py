#parisa najari ghahremani thursday 14-18 class
#barnameiy k reshtehaye dakhele yek list ra bar asase horofe alefba
#moratab mikonad
a=['ali','negin','negar','reza','sara','hosein','mehradad','mona','X']
new=' '

tol=len(a)
for i in range(tol-1):
    for j in range(tol-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        elif a[j]<a[j+1]:
            a[j],a[j+1]=a[j],a[j+1]
        elif a.issupper()==True:
            a[j]=a[0]

        for m in a:
            new=m+new
            print(a)


# barname fibunaancci
#rahe aval

def fibonacci(n):
    if n<0:
        return 'incorect input'
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input('enter a number:\n'))
print(fibonacci(n))


#rahe dovom

def fibonacci(n):
    a=0
    b=1

        if n<0:
            return 'incorect input'
        elif n==0:
            return 0
        elif n==1:
            return 1
        else:
            for i in range(2,n+1):
                c=a+b
                a=b
                b=c
            return b

n=int(input('enter a number:\n'))
print(fibonacci(n))



#factoriel


def factoriel(num):


    if num==1:
        return 1
    elif num==0:
        return 1
    elif num<0:
        return'is not fact'
    elif num>0:
        return num*factoriel(num-1)


num=int(input('enter a number:\n'))
print(factoriel(num))

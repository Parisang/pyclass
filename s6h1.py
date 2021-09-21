#parisa najari ghahremani thursday 14-18 class
#1-barnameiy ke adad 1 ta 1000 ra migirad va agar
#bar 3 bakhshpazir bod  mojmo ra chap konad
num=1
majmo=0
while num<=1000:
    if num%3==0:
        print(num)
        num=num+1
        majmo=majmo+num
        print(majmo)






result=0
for num in range(0,1000):
    if num%3==0:

        print (num)
        result=result+num
        print (result)




#------------------------------------------------
#barnameiy ke matn migirad va karacter khas ra hazf mikonad
#rahe aval
a='salam man reza hastam'

print(a.translate({ord('a'):None}))

#rahe dovom
a='salam man reza hastam'
a=a[ : :2]
print(a)


--------------------------------------------------
# barnameiy ke adad bein 1000ta 2000 ra migirad va majmo an ra mohasebe
# mikonad
result=0
for adad in range(1000,2000):

    if adad%2!=0:
        print(adad)
        result=result+adad
        print(result)
#-----------------------------------------------------------
#barnameiy k ye ta zamni k -1 vared nakadim list be onvane
#vorodi migirad va majmo adad list ra midahad

number=list()
i=0
maj=0
tol=len(number)
while True:
    num=int(input('enter a number:\n'))
    if num!=-1:
        number.append(num)
        print(number)
        maj=maj+number[i]
        i=i+1
        print(maj)
    else:
        print('adad sahih nist')
        print('majmo ta alan:',maj)
        break


#--------------------------------------------------------

# barnameiy  k nafarat dakhele list ra be goneiy chap mikonad
#k shomare jaygahe anha niz da chap bashad


adamha=['atafe','parisa','sara','parisa','yekta']

for i,adam in enumerate(adamha):
    print('{} nafar {} kelas ast'.format(adam,i+1))







adamha=['parisa','ali','yekta','arta','anahita']
tol=len(adamha)
i=0
while i<tol:
    print('{} nafar {} kelas ast'.format(adamha[i],i))
    i=i+1
#---------------------------------------------------------

#barnameiy k namhaye dakhele list rabe sorat karakter
#chap mikonad
#rahe aval
names=['ali','parisa','yekta','sara']

for i in names:
    print('---------------------')
    for j in i:
        print(j)



#rahe dovom
names=['ali','parisa','yekta','sara']
i=0
j=0
tol=len(names)
while i<tol:
    print(names[i])
    print('------------------------------')

    i=i+1
    for j in names[i]:
        print (j)
#-------------------------------------------------
#barnameiy k miangine yek list k tavasote karbar varad mishavad

number=list()
i=0
maj=0
tol=len(number)
while True:
    num=float(input('enter a number:\n'))
    if num!=-1:
        number.append(num)
        print(number)
        maj=maj+number[i]
        i=i+1
        print(maj)

    else:
        print(number)
        tol=len(number)
        mean=(maj/tol)
        print('mean',mean)
        break







def get_list():

    while True:
        num1=int(input('enter a number:\n'))
        if num1>0:
            number.append(num1)
            print(number)
            mean=mohasebe()
           return mean

        else  :
            print('adad manfi vared nakonid ')
            break


def mohasebe():
    for i in number:
        jam=sum(i)
        mean=jam/tol
        return mean

number=list()
tol=len(number)

print(get_list())

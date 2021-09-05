
def etehad_2_moraba(a:int,b:int,darkhast):

    if darkhast=='total':
        result=a**2+(2*a*b)+b**2
        return result
    elif darkhst=='submission':
        result=a**2-(2*a*b)+b**2
        return result

def etehad_2_mokaab(a:int,b:int,darkhast):


     if darkhast=='total':

         result=a**3+(3*a**2*b)+(3*a*b**2)+b**3
         return result
     elif darkhast=='submission':
         result=a**3-(3*a**2*b)+(3*a*b**2)-b**3
         return result




def etehad_3_moraba(a,b,c,darkhast):

    if darkhast=='total':
          result=a**2 +b**2+c**2+(2*a*b)+(2*a*c)+(2*b*c)
          return result
    else:
        result=' enter only total'
        return result


def etehad_mozdavaj(a,b,darkhast):
    if darkhast=='total':
            result=a**2-b**2
            return result
    else:
        result='enter only total'
        return result




def etehad_jomle_moshtarak (a,b,x,darkhast):


    if darkhast=='total':
        result=x**2+((a+b)*x)+a*b
        return result

    elif darkhast=='submission':
        result=x**2+((a-b)*x)-a*b
        return result


def etehad_chagh_laghar(a,b,darkhast):


    if darkhast=='total':
        result=(a+b)*(a**2+(a*b)+b**2)
        return result
    elif darkhast=='submission' :
        result=(a-b)*(a**2+(a*b)+b**2)
        return result


def mohasebe_etehad(etehad):
    if etehad=='etehad_2_moraba':
        return etehad_2_moraba(a,b,darkhast)
    elif etehad=='etehad_2_mokaab':
        return etehad_2_mokaab(a,b,darkhast)
    elif etehad=='etehad_3_moraba':
        return etehad_3_moraba(a,b,c,darkhast)
    elif etehad== 'etehad_mozdavaj':
        return etehad_mozdavaj(a,b,darkhast)
    elif etehad=='etehad_jomle_moshtarak':
        return etehad_jomle_moshtarak(a,b,x,darkhast)
    elif etehad=='etehad_chagh_laghar':
        return etehad_chagh_laghar(a,b,darkhast)

c=2
x=2
a=int(input('enter a namber1:\n'))
b=int(input('enter a number2:\n'))
darkhast=input('please enter darkhst in total or submission:\n ')
etehad=input('please enter a noe etehad:\n')
print(mohasebe_etehad(etehad))

#parisa najari ghahremani thursday 14-18 class
#mohasebe tamrin bmi

def bmi():

        ghad=float(input('please inter a ghad:\n'))
        vazn=float(input('plese inea vazn:\n'))
        bmi=vazn/(ghad/100)**2
        if bmi<=18.5:
            print('dochare kambode vazn hastid')
        elif bmi>=18.5 and bmi<=24.9:
            print('shoma salem hastid')
        elif bmi>=25 and bmi<=29.9:
            print('shoma dochare ezafe vazn hastid')
        elif bmi>=30:
            print('shoma chagh hastid')
        else:
            print(' dar grohe por khatar hastid')

bmi()

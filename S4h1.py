def core(r:float,dastor):
    if dastor=='hajm':
        hajm=(4/3)*3.14*r**2
        return hajm
    elif dastor=='masahat':
        masahat=4*3.14*r**2
        return masahat





def makhrot(r:float,s:float,dastor):
    if dastor=='hajm':
        hajm=(1/3)*3.14*s*r**2
        return hajm
    elif dastor=='masahat' :
        masahat=3.14*r*s
        return masahat





def mokaab(tol,arz,h,dastor):
    if dastor=='hajm':
        hajm=tol*arz*h
        return hajm
    elif dastor=='masahat' :
        masahat=2*((tol*arz)+(h*arz)+(tol*h))
        return masahat



def mohasebe(shape):

    if shape=='core':
        r=float(input('enter a radius:\n'))

        return core(r,dastor)


    elif shape=='makhrot'  :
        r=float(input('enter a radius:\n'))
        s=float(input('enter a zel:\n'))
        
        return makhrot(r,s,dastor)

    elif shape=='mokaab' :
         tol=float(input('enter a tol:\n'))
         arz=float(input('enter a arz :\n'))
         h=float(input('enter a highe:\n'))
         return mokaab(tol,arz,h,dastor)


shape=input('enter a shape:\n')
dastor=input('enter a hajm or masahat:\n')
print(mohasebe(shape))

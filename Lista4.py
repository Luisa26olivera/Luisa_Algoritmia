a=list(range(1,21))
for i in a:
    n=int(input("digite su numero:   "))
    if n>0:
        print(a.index(n))
    else:
        if n<0:
            print ("el numero es incorrecto, tiene que ser positivo ") 
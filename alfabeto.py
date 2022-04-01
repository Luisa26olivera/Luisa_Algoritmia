contar=0
texto1=input("digite:  ")
alfabeto=("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvXxYyZz")
for i in texto1:
    if i in alfabeto:
        contar+=1
        print("se encontraron caracteres no alfabeticos ")
        break
    else:
        contar==len(contar)
        print("se encontraron que todos los caracteres son alfabeticos  ") 
        
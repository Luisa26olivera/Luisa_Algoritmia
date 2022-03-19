volar=input("Puede volar:   ")
h=input("¿Es humano?:   ")
mascara=input("¿Tiene mascara?:  ")

if volar=="si" and h== "si" and mascara=="si":
    print("Iroman")
elif volar=="si" and h=="si" and mascara=="no":
    print("captain marvel ")
elif volar=="si" and h== "no" and mascara=="si":
    print("Ronan accuser")
elif volar=="si" and h=="no" and mascara=="no":
    print("Vision")
elif volar=="no" and h=="si" and mascara=="si":
    print("Spiderman")
elif volar=="no" and h=="si" and mascara=="no":
    print("Hulk")
elif volar=="no" and h=="no" and mascara=="si":
    print("Black bolf")
elif volar=="no" and h=="no" and mascara=="no":
    print("Thanos")
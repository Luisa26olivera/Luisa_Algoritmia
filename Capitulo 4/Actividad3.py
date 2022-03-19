p1=input("introduce el  p1:   ")
p2=input("introduce el  p2:   ")

if p1==p2:
    print("empate")
elif p1=="papel" and p2== "tijera":
    print("gana p2 tijera corta papel")
elif p1=="papel"and p2=="piedra":
    print("gana p1 papel envuelve a la piedra ")
elif p1=="tijera"and p2=="papel":
    print("gana p1 tijera corta papel")
elif p1=="tijera"and p2=="piedra":
    print("gana p2 piedra daña  la tijera ")
elif p1=="piedra" and p2=="papel":
    print("gana p2 envuelve el papel ")
elif p1=="piedra" and p2=="tijera":
    print("ganap1 daña la tijera ")

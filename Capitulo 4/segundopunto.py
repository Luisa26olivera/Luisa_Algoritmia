n_1=int(input("ingrese el primer numero:  "))
n_2=int(input("ingrese el segudo numero:  "))
n_3=int(input("ingrese el tercer numemro: "))
if n_1 <= n_2 and n_1 <= n_3:
    menor=(n_1)
elif n_2 <= n_1 and n_2 <= n_3:
    menor=(n_2)
else:
    menor=(n_2)
print(f"el numero menor es {menor}")
    
a=[1,2,3,4,5,-26,-17,-48,-59,-10]
b=[]

for i in a:
    if i<=0:
        i=0
    b.append(i)
print(b)
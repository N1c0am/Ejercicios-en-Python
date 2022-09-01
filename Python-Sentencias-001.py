#IF
x=10

if (x<20):
    print(str(x) + ' es menor que 20')

if (x<1):
    print('Verdadero')

y=20
if (y<=30):
    print(str(y)+' es igual o menor que 30')

#ELSE
z=3
if (z>10):
    print(str(z)+ ' es mayor que 10')
else:
    print(str(z)+ ' NO es mayor que 10')

z=30
if (z>10):
    print(str(z)+ ' es mayor que 10')
else:
    print(str(z)+ ' NO es mayor que 10')

z=10
if (z==10):
    print(str(z)+ ' es IGUAL que 10')
else:
    print(str(z)+ ' NO es IGUAL que 10')

z=10
if (z!=10):
    print(str(z)+ ' es DISTINTO que 10')
else:
    print(str(z)+ ' NO es DISTINTO que 10')

""""""
'elif'
""""""

z=10
if (z!=10):
    print(str(z)+ ' es DISTINTO que 10')
elif (z==10):
    print(str(z)+ ' NO es DISTINTO que 10')

z=10
if (z==20):
    print(str(z)+ ' es igual que 20')
elif (z!=10):
    print(str(z)+ ' es distinto de 10')
elif (z==10):
    print(str(z)+ ' es igual a 10')
else:
    print(str(z)+ 'No cumple con ninguna condición')


















edad = int(input("Ingrese edad: "))
if edad >= 18 and edad <= 130:
    print(str(edad)+": Usted es mayor de edad")
elif edad < 18 and edad >=0:
    print(str(edad)+": Usted es menor de edad")
else:
    print(str(edad)+": Ingrese valor realista")
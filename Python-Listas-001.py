lista1 = [1, 2, "Hola", "Adios"]
print(lista1)

print(lista1[3]) #'Adios'

print(lista1[0:3:2]) #1, 'Hola'

print(lista1[-2]) #'Hola'

#AÑADIR
lista2 = ["Agregar"]
print(lista1 + lista2) #"Agregar" --> Se agrega al último

lista1.append("Agregar al final") #Se agrega en la posición final
print(lista1)

lista1.insert(2, 3) #Se agrega el valor 3 en la posición 2
print(lista1)

lista1.insert(100, 'Fuera de rango') #Se agrega al final. ya que no existe la posición 100
print(lista1)

"---------------------------------------------------"
#ELIMINAR
lista3 = ["Hello", "How", "Are", "You", ",", "My", "Friend"]
print(lista3)

lista3.pop() #Elimina el último elemento
print(lista3)

lista3.pop(4) #Elimina el elemento ubicado en la posición 4
print(lista3)

lista3.remove("My") #Elimina el elemento "My"
print(lista3)

"---------------------------------------------------"
#VERIFICAR SI UN ELEMENTO ESTÁ EN LA LISTA
lista4 = [1, "Hola", "A", "Todo", "El", "Mundo"]

"Hola" in lista4
"hola" in lista4

"Mundo" not in lista4
2 not in lista4

flag = 2 in lista4
print(flag)

"---------------------------------------------------"
#MODIFICAR
lista5 = [1, 2, 3, "Uno", "Dos", "Tres"]
print(lista5)

lista5[0] = "Cero" #Reemplaza el valor 0 al elemtno ubicado en la posición 0
print(lista5)

lista5[50] = "Cero" #No reemplaza nada, ya que no existe la posición 50
print(lista5)

#ÍNDICE
print(lista5.index(2))
print(lista5.index("Uno"))


lista6 = [1, "Hello", 2, "Bye"]
lista6

lista6[0]
lista6[3]
lista6[-1]
lista6[-4]

lista6[0] = 100
lista6

lista6.append("Welcome")
lista6

lista6.insert(5, "World")
lista6

lista6.insert(4, 1)
lista6

lista6.pop(6)
lista6

lista6.remove("Welcome")
lista6

"Hello" in lista6
"Welcome" in lista6

lista6.index("Hello")
lista6
tupla1 = (1, "Uno", 2, "Dos")
print(tupla1)

tupla1.append("3")

lista1 = ["A", 1, "a"]
print(lista1)
tupla2 = tuple(lista1)
print(tupla2)

tupla3 = ("Hello", "Hola", "Hi")
print(tupla3)
print(tupla3[1])
elemento1 = tupla3[2]
print(elemento1)

tupla4=(1.2, 3.7, "uno punto dos", "tres punto siete")
print(tupla4)
print(1.3 in tupla4)
elemento2 = "uno punto dos" in tupla4
print(elemento2)
print(3.7 not in tupla4)

tupla5 = ("Adios", "Goodbye", "Bye", 0)
print(tupla5)
tupla5.index(0)
tupla5.index("Goodbye")
tupla5.index("Good")

tupla6 = (1, 2, 1, 5, 2, 7, 5, 0, 1, 7, 1)
print(tupla6)
tupla6.count(1)
tupla6.count(9)
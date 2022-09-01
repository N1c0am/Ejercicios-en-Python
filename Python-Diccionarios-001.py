diccionario = {1:"Hello", 2:"How", 3:"Are", 4:"You"}
print(diccionario)

diccionario[1]
diccionario["Hello"]

diccionario.keys()
diccionario.get(1)

diccionario[1] = "Hola"
diccionario

diccionario[5] = "My Friend"
diccionario

del diccionario[5]
diccionario

diccionario.pop(1)
diccionario

eliminar1 = diccionario.pop(2)
eliminar1
diccionario

eliminar2 = diccionario.pop(8, "Error, no existe la llave")
eliminar2
diccionario

"Are" in diccionario.values()
3 in diccionario.keys()
diccionario.get(3, "No existe")

diccionario2 = {1:"Hola", 2:"A", 3:"Todo", 4:"El", 5:"Mundo"}
diccionario2

diccionario2[1]

diccionario2["Hola"]

diccionario2[1] = "Hello"
diccionario2

diccionario2.pop(5)
diccionario2

diccionario3 = {1:"uno", 2:"dos", 3:"tres"}
diccionario3

diccionario3[2]
diccionario3["dos"]

diccionario3[2] = "two"
diccionario3

diccionario3.pop(3)
diccionario3

diccionario3.get(1)

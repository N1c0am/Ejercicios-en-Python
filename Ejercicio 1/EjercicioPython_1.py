def Funcion(f1,f2):
    contador=0
    for elemento in f1:
        if(elemento==f2):
            contador=contador+1
    print(contador)
    print(len(arreglo1)) 
    
arreglo1=["ab","a"]
arreglo2="a"
Funcion(arreglo1,arreglo2)

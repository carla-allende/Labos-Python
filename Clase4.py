# #CICLO FOR
# clientes = ["hector", "emilia", "sofia", "pablo", 50]

# for cliente in clientes: 
         # res = 2 * 5
         # print (res)

# #Mostrar por pantalla los numero pares elevados al cuadrado de una lista: if solo elementos q cumplan una condicion

# for numero in [2, 5, 3, 10, 8, 1]:
    # if numero % 2 == 0:
        # print(numero ** 2)

# #FOR para utilizar la variable vacia, tratar de no usarlo o tratar de ponerlo neutro
# #clientes = [""]

# #FOR
# clientes = ["Pedro"]

# for cliente in clientes:
    # print (cliente)

# #imprimir por pantalla los numeros del 1 al 5
# var = 1
# while var <= 5 :
    # print(var)
    # var = var + 1
# #otra forma, un poco mas complicada la primera es mas agil
# for numero in [1, 2 , 3, 4 ,5]:
    # print(numero)
# #RANGE toma dos argumentos: variable de inicio y una var de fin. TE DEVUELVE UNA LISTA QUE COMIENZA EN INICIO E INCREMENTA EN 1 + 2 VA A GREGANDO ELEMENTOS HASTA LLEGAR A FIN -1
# ## [inicio, inicio + 1, inicio + 2 .... fin -1]
# for numero in range(1, 101):
    # print(numero)
# ~ numeros = [9, 4, 5, 8, 6 ,-2 ]
# #LABORATORIO EJERCICIOS
# ~ total = 0 
# ~ for numero in numeros:
    # ~ total = numero + total
# ~ print("Suma:",total)

# ~ #Segundo ejercicio
# ~ total = 1
# ~ for numero in numeros:
    # ~ total = total * numero
    
# ~ print ("Multiplicacion:", total)

#ejercicio 3
# ~ maximo = numeros [0]
# ~ for numero in numeros:
    # ~ if numero > maximo:
        # ~ maximo = numeros
# ~ print("maximo valor:", maximo)

#EJERCICIO MATRIZ
# ~ filas = 2
# ~ columnas = 3

# ~ filas = int(input("Ingrese la cant. de filas: ")) #2
# ~ cols = int(input ("Ingrese la cant. de columnas: ")) #3
# ~ matriz = []
# ~ for n_f in range(0, filas): #las filas [0, 1] n_f = 1
    # ~ matriz.append([])       #matriz = [[10, 1, 151]], [10]]
    # ~ for n_c in range(0, cols) : #las columnas [0, 1, 2] n_c = 0
        # ~ dato = input("Ingrese el elemento para la matriz["+ str (n_f) + "] ["+ str (n_c) +"] ")
        # ~ matriz[n_f].append(dato)

# ~ print("La matriz ingresada es: ")
# ~ print(matriz)




#LIBRERIA (Conjunto de módulos)
#MÓDULO (COnjunto de funciones y/o clases)
# Funciones
# ~ def  saludar() :
    # ~ print("bienvenidos a la clase")
    # ~ print("python para no programadores")
    # ~ print("clase n 4")
    
    
# ~ saludar()
# ~ var = 5
# ~ res = var ** 3
# ~ print(res)
# ~ saludar()
# ~ print("Clase n 4")
# ~ print(res * 2)
# ~ saludar()


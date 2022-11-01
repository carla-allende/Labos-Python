#clase3
#LISTAS Y BUCLES:(Colecciones, listas, duplas)
Clientes = ["Emilia","Jorge","Lucia"]
#INDICES       0        1       2
texto = "Hoy Vino " + Clientes [2] + ", el jueves viene " + Clientes [1]

varios = [-5, True, "Clase 3" , 326 , 3.15]
numeros_primos= [2, 3, 5, 7]
resultado = numeros_primos [1] * 10 
# Modificiar elemento
varios [2] = "Clase de Python"
print (varios)

# Agregar un elemento al final de la lista
numeros_primos.append(11)
print (numeros_primos)

varios.append("Teclado, Mouse")
print(varios)

# Agregar un elementoen la posicion especificada
Clientes.insert(1, "Rodolfo")

print(Clientes)

#Eliminar elemento
del varios [1]
print (varios)

# Longitud de una lista
print (varios [2])
print (len(Clientes))

print (varios[len(varios) -1])

# Lista vacia
alumnos = []

m1 = [[120, "Router" ,  False] , -25]
msg = "Se tildo el "+ m1 [0] [1]
print (m1[0][1]) #ubicacion dentro del elemento que corresponde  a la lista m1

#Matriz
m1 = [[120, "Router", False],
["CPU",643, 3.14],
 [True, 20 ,64] ,
  ["WSGI",2 ,-9]]

#Modificar el m1 el eelemento 6 por "Debian"
m1 [2] [2] = "Debian"
print(m1)

#Bucles
#While  mientras algo suceda hace tal cosa..
var = 1
while var <= 5:
    print("Bienvenidos a la clase")
    var = var + 1
print ("Linea principal del algoritmo")

#Otra forma
while true:
    if var < 6:
        print("Bienvendios a clase")
        var = var + 1
        else : 
            break
            
# Algoritmo que dado un numero secreto el usuario tiene que adivinarlo
numero_secreto = 20
intentos = 1 
while True:
    ingreso = int(input("Ingrese un numero"))
    if ingreso != numero_secreto:
        print("el numero ingresado es incorrecto, intente nuevamente")
        intentos = intentos + 1
        else: 
         msg = "El num es incorrecto, lo adivino en " + str (intentos) + "intentos"
         print(msg)
         break

# Acceso a una matriz
matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
fila = int(input("Ingrese el numero de fila: "))
col = int(input("Ingrese el numero de columna: "))
if (fila.....) and (col...) :
    print (...)
    else :
        print("Error en el ingreso de valores")

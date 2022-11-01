#Operaciones de comparacion
valor_uno = 10
valor_dos = 10

#Igualdad(==)
res= valor_uno == valor_dos
print(res)

#Distinto(!=)
res= valor_uno != valor_dos

#Mayor (>)
res = valor_uno > valor_dos

#Mayor o igual (>=)
res = valor_uno >= valor_dos

#Menor (<)
res = valor_uno < valor_dos
print(res)

#Menor o Igual (<=)
res= valor_uno <= valor_dos

Txt1= "Hola"
Txt2= "Hola"
res= Txt1 == Txt2
print(res)

#Operac logicas
var = 5

#Conjuncion (and) -> DEVUELVE TRUE SOLO SI AMBOS LADOS DE LA OPERACION SON TRUE, caso contrario devuelve false

res = var > 1 and var < 10 
print (res)

var_logica_1 = True
var_logica_2 = True

res = var_logica_1 and var_logica_2
print(res)

#Disyuncion (or) -> Devuelve solo FALSE si ambos lados de la operacion son false, caso contrario devuelve true
res= var_logica_1 or var_logica_2
print(res)

#Negacion (not)
res= not 5 == "Clase n2"
print (res)

#Condicionales, hace que una o mas lineas de codigo se ejecute solo si se cumple una condicion
var= 15
if var > 10:
    print("La variable mayor que 10")
    res_m= 5 * 20
    print (res_m)
    if res_m <= 20:
        print ("La variable res es menor que 21")
print("Linea principal del programa")
print(res_m)
        
#otro ejemplo
if var > 10:
    print("La var mayor que 10")
else:
    print ("La var menor que 10")

#entrada de datos (INPUT)
nombre = input("Ingrese su nombre: ")
print("Su nombre es, ", nombre)

#Comparar la entrada del usuario. 
#Crear un programa que permita ingresar dos cadenas vía la consola y luego las compare,imprimiendo un mensaje en caso que sean iguales y otro en caso que sean diferentes
password = input("Enter your password: ")
confirm = input( "Repeat your password: ")
if password==confirm:
     print("Successfully join")
else:
    print("Invalid password, or doesnt match")

#Conversiones -> puede concatenar strg no enteros
numero = int(input("ingrese un numero: "))
res= numero + 10
dia = 15
dia = str(dia)
frase = "El proximo dia "+ dia

print(txt)
print(res)
print(frase)

#Hacer un programa que determine si una
#persona es menor de edad o mayor de edad,
#teniendo la edad en una variable.
#Probar el código cambiando el valor de la
#variable “edad”.

edad


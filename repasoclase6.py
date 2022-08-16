from unicodedata import decimal
"""

decimal1 = 12.4
decimal2 = 42.5

opcion = -1

while opcion != 3: #Si opcion es diferente a 3 se ejecuta input para escoger
    opcion = int(input("Incresa una opción. 1) SUMAR 2) MAXIMO 3 SALIR"))

    if opcion == 1: #Si se ingresa 1, se suman los dos decimales
        suma = decimal1 + decimal2
        print(f"Genial, la suma es: {suma}")

    elif opcion == 2: #si se ingresa dos, se utiliza 
        maximo = decimal1
        
        if decimal1<decimal2: #Si decimal1 es menor que decimal2 se imprime el 2
            maximo = decimal2
        print(f"El máximo es: {maximo}")

    else:
        print("Saliendo...")

#Crea un programa que nos pida ingresar un numero del 1 al 20, si el numero
#no está en ese rango, lo vuelve a pedir. Una vez ingresado se vereficia en
#una lista

numero = 21
lista = [11, 13, 19, 18, 17]

while (numero < 10 or numero > 20):
    numero = int(input("Ingresa un numero entre 10 y 20: "))

#se puede simplifcar esto por
for elemento in lista:
    if(elemento==numero):
#esto
#if numero in lista:
        print("Acertaste, el número está en la lista")

#El usuario selecciona cuantos numeros desea ingresar, luego empieza a elegirlos.
#una vez terminado el ingreso se muestra la suma de los numeros

cantidad_de_numeros = int(input("Cuantos numeros quieres? "))
suma = 0

for i in range (0, cantidad_de_numeros):
    suma = suma + int(input("Ingresa uno de tus numeros: "))
    #suma += int(input("Ingresa uno de tus numeros: "))
print(f"La suma de tus numeros es {suma}")
"""
grupo = {"Miguel", "Blanca", "Mario", "Andres"}
#agregar {"Ana", "Ramón", "Marta", "Eric", "David"}
#quitar {"Pepe", "Mario", "Andrés"}

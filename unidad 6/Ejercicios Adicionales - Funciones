#Ejercicio 1
def tabla_multiplicar(numero):
    for i in range (1,10):
        print(f"i * {numero} : {i * numero}")
numero = int(input(f"Ingrese un numero: "))
tabla_multiplicar(numero)

#Ejercicio 2
def suma_pares(lista):
    suma = 0
    for numero in lista:
        if numero%2==0:
            suma += numero
    print(f"La suma de los pares es: {suma}")
lista = [1,2,3,4,5,6]
suma_pares(lista)

#Ejercicio 3
def rectangulo(longitud, anchura):
    area = longitud * anchura
    perimetro = 2 * (longitud + anchura)
    return (area, perimetro)

resultado = rectangulo(5, 3)
print(f"Area: {resultado[0]} , Perimetro:{resultado[1]}")  

#Ejercicio 4
def temperaturas(celsius):
    fahre = celsius * (9/5) + 32
    kelvin = celsius + 273.15
    return(fahre, kelvin)

temps = temperaturas(10)
print(f"Temperatura en Fahrenheit: {temps[0]} y la temperatura en Kelvin: {temps[1]}")

#Ejercicio 5
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

n = int(input("Ingrese un número entero positivo: "))
if es_primo(n):
    print(n, "es un número primo.")
else:
    print(n, "no es un número primo.")

#Ejercicio 6
def promedio(lista):
    suma = 0
    for numero in lista:
        suma += numero
    suma = suma / len(lista) 
    return(suma)

prom = promedio([10,3,5,7,3,2])
print(f"El promedio es: {prom}")

#Ejercicio 7
def validar_entrada(numero):
    return numero.isdigit()  

def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

entrada = input("Ingrese un número entero positivo: ")
if validar_entrada(entrada):
    numero = int(entrada)
    print(f"El factorial de {numero} es: {factorial(numero)}")
else:
    print("Error")

#Ejercicio 8
def es_divisible(dividendo, divisor):
    return dividendo % divisor == 0

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if es_divisible(numero, i):
            return False
    return True

n = int(input("Ingrese un número entero positivo: "))
if es_primo(n):
    print(n, "es un número primo")
else:
    print(n, "no es un número primo")

#Ejercicio 9
def convertir_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convertir_a_kelvin(celsius):
    return celsius + 273.15

def menu_conversion():
    print("\nSeleccione la unidad a la que desea convertir:")
    print("1. Fahrenheit")
    print("2. Kelvin")
    opcion = input("Opción (1 o 2): ")
    return opcion

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
opcion = menu_conversion()
if opcion == "1":
    resultado = convertir_a_fahrenheit(celsius)
    print(f"{celsius}°C equivalen a {resultado:.2f}°F")
elif opcion == "2":
    resultado = convertir_a_kelvin(celsius)
    print(f"{celsius}°C equivalen a {resultado:.2f} K")
else:
    print("Opción no válida. Intente nuevamente")

#Ejercicio 10
def validar_dimensiones(longitud, anchura):
    return longitud > 0 and anchura > 0

def calcular_area(longitud, anchura):
    return longitud * anchura

def calcular_perimetro(longitud, anchura):
    return 2 * (longitud + anchura)

try:
    longitud = float(input("Ingrese la longitud del rectángulo: "))
    anchura = float(input("Ingrese la anchura del rectángulo: "))

    if validar_dimensiones(longitud, anchura):
        area = calcular_area(longitud, anchura)
        perimetro = calcular_perimetro(longitud, anchura)
        print(f"\nÁrea del rectángulo: {area}")
        print(f"Perímetro del rectángulo: {perimetro}")
    else:
        print("Error: Las dimensiones deben ser positivas")
except ValueError:
    print("Error: Debe ingresar valores numéricos")
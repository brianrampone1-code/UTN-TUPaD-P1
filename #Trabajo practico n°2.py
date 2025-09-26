
#Actividad 1
ancho=float(input("Ingrese el valor del ancho:"))
alto=float(input("Ingrese el valor de la altura:"))

area=ancho*alto
perimetro=(ancho*2) + (alto*2)

print(f"El area es:{area}, el perimetro {perimetro}")

#actividad 2 
grados_c=float(input("Ingrese el valor de grados celsius:"))
grados_f=(grados_c*9/5) + 32

print(f"Su equivalente en grados fahrenheit: {grados_f}")

#Actividad 3

a=True
b=False

print((a and b) , (a or b ) , (not a , not b))


#Actividad 4

a=5
b=3
c=a + b
a=2
print(c)

#Actividad 5

num= int(input("Ingrese un numero:"))
cuadrado= num * num

print(f"El resultado es: {cuadrado}")
#Actividad 6

x=10
y=20

x= x + y
y= x - y
x= x - y

print(f"despues del intercambio :x ={x} y= {y}  ")


#Actividad 7

peso=float(input("Ingrese su peso en kg:"))
alto=float(input("Ingrese su altura en metros:"))

imc=peso/(alto**2)

print(f"Su masa corporal es :{imc}")

#Actividad 8 
nombre = input("Ingrese su nombre completo:")

sin_espacios= nombre.replace(" ", "")
primeras_3= nombre[:3]
alternado= "".join(c.upper() if i % 2==0 else c.lower() for i , c in enumerate(nombre) )

print("Cantidad de letras (sin espacios):",len (sin_espacios))
print("Primeras tres letras:", primeras_3)
print("Nombre con mayusculas y minusculas alternadas:" , alternado)

#Actividad 9

a=7.5
b=3.2

suma=a + b
division= round (a/b ,2)
potencia=(a**b)

print(suma, division , potencia)
#Actividad 10

precio_original=float(input("Ingrese el precio original:"))
porcentaje_de_descuento=float(input("Ingrese el porcentaje de descuento:"))
precio_final=precio_original*(1-(porcentaje_de_descuento / 100))
print(f"El precio final es : {precio_final}")


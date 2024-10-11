print(" ")
print("alexa guadalupe ramirez manzo 1205 3-W")
print(" ")
import math #fincion math
print(" ")
def area_circulo(radio): #funcion para el radio del circulo
    #Calcula el área de un círculo dado su radio.
    return math.pi * radio ** 2 #para salir
print(" ")
def volumen_cilindro(radio, altura): #funcion para el volumen del silintro
    #Calcula el volumen de un cilindro dado su radio y altura.
    area_base = area_circulo(radio)  # Utiliza la función del área del círculo
    return area_base * altura #para salir
print(" ")
# Solicitar datos al usuario
radio = float(input("Introduce el radio del círculo: ")) #sirve para introducir un valor 
altura = float(input("Introduce la altura del cilindro: "))#sirve para introducir un valor 
print(" ")
# Calcular el área del círculo
area = area_circulo(radio) #variable para calcular el area d circulo
print(f"El área del círculo es: {area:.2f}") #impresion para sacar el area 
print(" ")
# Calcular el volumen del cilindro
volumen = volumen_cilindro(radio, altura) #impresion para el volumen de silindro 
print(f"El volumen del cilindro es: {volumen:.2f}") # impresion 
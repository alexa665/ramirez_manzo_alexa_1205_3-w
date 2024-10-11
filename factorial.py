print(" ")
print("alexa guadalupe ramirez manzo 1205 3-w")
print(" ")
def factorial(n): #funcion para la factorizacion de un numero
    if n < 0:     #funcion if 
        return "El número debe ser un entero positivo." #indicasion para usar un numero positivo
    elif n == 0 or n == 1: #funcion para saver cual se deve usar
        return 1 #funcion para que se utilise el numero 1
    else: #funcion para saber si es verdadero o falso
        resultado = 1 #funcion para dar un resultado
        for i in range(2, n + 1): #funcion for para sumar
            resultado *= i # resultado 
        return resultado #impresion de resultado

num = int(input("Introduce un entero positivo: ")) #variable para introducir un un entero positivo
print(f"El factorial de {num} es: {factorial(num)}") #impresion para saber cual es el factorial del numero entero 
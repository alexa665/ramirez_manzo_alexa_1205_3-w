print(" ")
print(" alexa guadalupe ramirez manzo 1205 3-W")
print(" ")
def mayor_de_tres(num1, num2, num3): #definir funsiones
    return max(num1, num2, num3) # impresion de funciones
def main(): #ingrsar funciones 
    # ingresar tres números del usuario
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))
    print(" ")
    mayor = mayor_de_tres(num1, num2, num3)# Calcula el mayor número
    print("")
    print(f"El mayor de los tres números es: {mayor}")# Mostrar el resultado
print(" ")
if __name__ == "__main__":# Ejecutar la función principal
    main()#cerrar

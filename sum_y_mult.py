print(" ")
print("alexa guadalupe ramirez manzo 1205 3-W")
print(" ")
def sum(lista): #define funcion de lista
    # Sumar todos los números de la lista
    total = 0
    for num in lista:
        total += num
    return total
def multip(lista): #define funsion de lista 
    # Multiplicar todos los números de la lista
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado
print(" ")
def main():#define funcion main 
    numero = [1, 2, 3, 4] #valores
    print(" ")
    total_suma = sum(numero)# Calcular la suma
    total_multip = multip(numero)# Calcular la multiplicasion
    print(" ")
    print(f"La suma de {numero} es: {total_suma}") #impresion de resultados
    print(f"La multiplicación de {numero} es: {total_multip}")#impresion de resultados
# Ejecutar la función principal
if __name__ == "__main__":
    main()

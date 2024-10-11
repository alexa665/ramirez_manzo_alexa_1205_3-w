print(" ")
print("alexa guadalupe ramirez manzo 1205 3-w")
print(" ")
def es_vocal(caracter):#definir funcion
    vocales = 'aeiouAEIOU'# Definir las vocales en minúsculas y mayúsculas
    # Verificar si el carácter está en la cadena de vocales
    return caracter in vocales# Verificar si el carácter está en la cadena de vocales

def main(): #definir main
    caracter = input("Ingresa un carácter: ")# Capturar un carácter del usuario
    print(" ")
    if len(caracter) == 1:  # Asegurarse de que solo se ingrese un carácter
        resultado = es_vocal(caracter)#resultado para el caracter y vocal
        if resultado: #resultado
            print(f"{caracter} es una vocal.") #impresion de vocal
        else: #para saber si es sierto o falso
            print(f"{caracter} no es una vocal.")#impresion de vocal
    else:#para saber si es sierto o falso
        print("Por favor, ingresa solo un carácter.") #impresion para ingresar un caracter
        print(" ")
if __name__ == "__main__":# Ejecutar la función principal
    main() #cerrar

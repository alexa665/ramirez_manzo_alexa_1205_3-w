print(" ")
print("alexa guadalupe ramirez manzo 1205 3-W")
print(" ")
def es_email_valido(email): #funcion para email
    # Verificar si la dirección de email contiene '@'
    return '@' in email #para salir de la funcion 
print(" ")
def main():#define funciones
    email = input("Por favor, ingresa tu dirección de email: ") # Capturar la dirección de email
    print(" ")
    if es_email_valido(email):# Verificar si el email es válido
        print("La dirección de email es válida.") #impresion  para validar 
    else: #ejecuta si es cierto o falso
        print("La dirección de email no es válida.") #impresion para no validar 
print(" ")
if __name__ == "__main__": # Ejecutar la función principal
    main() #serrar funsion 
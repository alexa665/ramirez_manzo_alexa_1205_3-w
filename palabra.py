print(" ")
print("alexa guadalupe ramirez manzo 1205 3-W")
def longitud_ultima_palabra(texto):
    palabras = texto.split()# Divide el texto en palabras usando espacios
    print(" ")
    if palabras: # Verifica si hay palabras en el texto
        return len(palabras[-1])#Obtener la última palabra y retornar su longitud
    return 0  # Si no hay palabras, retornar 0

def main():
    texto = input("Ingresa un texto: ") # Capturar un string del usuario
    
    longitud = longitud_ultima_palabra(texto) # Calcular la longitud de la última palabra

    print(f"La longitud de la última palabra es: {longitud}") # Mostrar el resultado

if __name__ == "__main__":# Ejecutar la función principal
    main() #cerrar
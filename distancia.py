print(" ")
print("alexa guadalupe amirez manzo 1205 3-W ")
print(" ")
def distancia_dirigida(punto1, punto2):
    # Calcular la distancia dirigida en x e y
    dx = punto2[0] - punto1[0] #puntos
    dy = punto2[1] - punto1[1] #puntos
    return dx, dy #funcion return
def main():#definir main
    x1 = float(input("Ingresa la coordenada x del primer punto: "))#variables para ingressar los puntos
    y1 = float(input("Ingresa la coordenada y del primer punto: "))#variables para ingressar los puntos
    x2 = float(input("Ingresa la coordenada x del segundo punto: "))#variables para ingressar los puntos
    y2 = float(input("Ingresa la coordenada y del segundo punto: "))#variables para ingressar los puntos
    punto1 = (x1, y1) #puntos para sacar el valor
    punto2 = (x2, y2) #puntos para sacar el valor
    print(" ")
    distancia = distancia_dirigida(punto1, punto2)# Calcular la distancia dirigida
    # Mostrar el resultado
    print(f"La distancia dirigida entre los puntos {punto1} y {punto2} es: dx = {distancia[0]}, dy = {distancia[1]}")
if __name__ == "__main__":# Ejecutar la función principal
    main()

print(" ")
print("alexa guadalupe ramirez manzo 1205 3-W")
print(" ")
def calcular_total_factura(cantidad_sin_iva, porcentaje_iva): #fusion para calcular las facturas con iva y sin iva
    iva = cantidad_sin_iva * (porcentaje_iva / 100) # variable para calcular la factura sin iva
    total_factura = cantidad_sin_iva + iva #variable para calculr la factura con iva 
    return total_factura #funsion para calcular el total
print(" ")
# Solicitar al usuario la cantidad sin IVA y el porcentaje de IVA
cantidad_sin_iva = float(input("Introduce la cantidad sin IVA: ")) #para introdusir un numero
porcentaje_iva = float(input("Introduce el porcentaje de IVA: ")) #para introdusir un numero
print(" ")
# Calcular el total de la factura
total = calcular_total_factura(cantidad_sin_iva, porcentaje_iva) #variable para calcular el total
print(f"El total de la factura es: {total:.2f}") #impresion para el total de la factura 
print(" ")
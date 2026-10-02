#Pregunta 1
numeros = [10, 20, 30, 40, 50]
print(numeros[2])

#Modificar un elemento
numeros = [10, 20, 30, 40, 50]
numeros[2]=100
print(numeros)

#Agregar un elemento
numeros = [10, 20, 30, 40, 50]

numeros.append(60)

print(numeros)

#Más de un elemento
numeros = [10, 20, 30, 40, 50]
#OPC 1
numeros.append([60, 70])
#OPC 2
numeros.append(60)
numeros.append(70)

numeros = [10, 20, 30, 40, 50]
numeros.append([60, 70])
#Mostrar el elemento 60
print(numeros[5][0])

#Agregar un elemento en una posición específica
numeros = [10, 20, 30, 40]

numeros.insert(2, 25)

print(numeros)

#Para conectar otra lista
numeros = [10, 20, 30, 40]
numeros = numeros + [50]
print(numeros)

numeros = [10, 20, 30, 40]

numeros = [50, 60, 70]

print(numeros)

#extend() permite agregar a una lista los elementos de otra lista
numeros = [10, 20, 30,]
numeros.extend([40, 50, 60])
print(numeros)

numeros = [10, 20, 30,]
otros_numeros = [40, 50, 60]
numeros.extend(otros_numeros)

#Asignando directamente a una posición len()
numeros = [10, 20, 30]
numeros[len(numeros):] = [40]
print(numeros)

numeros = [10, 20, 30]
numeros[len(numeros):]
numeros[3:]
print(numeros)

# ////////////////////////////////////////
# EJERCICIO 1 - LISTA DE CALIFICACIONES

#Arreglo
calificaciones = [70, 85, 90, 65]

# Agregar 95 al final
calificaciones.append(95)

# Agregar 80 entre 85 y 90
calificaciones.insert(2, 80)

# Imprimir el arreglo completo
print("EJERCICIO 1")
print("Calificaciones:", calificaciones)


# ////////////////////////////////////////
# EJERCICIO 2 - AGREGAR VARIOS ELEMENTOS

colores = ["Azul", "Amarillo", "Rosa"]

# Agregar varios colores
colores.extend(["Verde", "Morado", "Rojo"])

# Imprimir el arreglo completo
print("EJERCICIO 2")
print("Colores:", colores)

# Imprimir únicamente Negro
colores.append("Negro")
print("Color Negro:", colores[6])

# ////////////////////////////////////////
# EJERCICIO 3 - RETO DE POSICIONES

numeros = [10, 20, 30, 40]

# Agregar 95 en la posición 2
numeros.insert(2, 95)

# Agregar 50 al final
numeros.append(50)

# Agregar 67 al final
numeros.append(67)

# Imprimir el arreglo completo
print("EJERCICIO 3")
print("Números:", numeros)

# Imprimir 95
print("Número 95:", numeros[2])

# Imprimir 67
print("Número 67:", numeros[6])

# Mostrar las posiciones
print("Posición de 95:", numeros.index(95))
print("Posición de 67:", numeros.index(67))

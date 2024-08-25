# Es un mecanismo que nos sirve para iterar, es decir,
# Que nos sirve para repetir tareas, en otras palabras 
# Pasar por un codigo varias veces

# Bucle while 
# Sintaxis
# while condicion:
#    Aqui tu codigo

# Ejemplo 
cuenta = 0
while cuenta < 5:
    print(cuenta)
    cuenta = cuenta + 1

# Imprime los numeros del 0 al 4

cuenta = 0
while cuenta < 10:
    print(cuenta)
    cuenta = cuenta + 2

# Imprime los numeros de dos en dos

# Sintaxis
#while condition:
#    Aqui tu codigo
#else:
#    Aqui tu codigo

# Ejemplo 
cuenta = 0
while cuenta < 5:
    print(cuenta)
    cuenta = cuenta + 1
else:
    print(cuenta)

# La condición de bucle anterior será falsa cuando el recuento sea 5 
# y el bucle se detenga, y la ejecución inicie la instrucción else. 
# Como resultado, se imprimira 5.

# Puedo realizar una pausa y continuar para los loops
# Sintaxis
#while condicion:
#    Aqui tu codigo
#    if otra condicion:
#        break

cuenta = 100
while cuenta < 200:
    print(cuenta)
    cuenta = cuenta + 10
    if cuenta == 130:
        break
# El bucle anterior solo imprime 100, 110, 120, 
# pero cuando llega a 130 se detiene.

# Sintaxis
#while condicion:
#    Aqui tu codigo
#    if otra condicion:
#        continue

cuenta = 1000
while cuenta < 1500:
    if cuenta == 1300:
        cuenta = cuenta + 100
        continue
    print(cuenta)
    cuenta = cuenta + 100

# El bucle anterior solo imprime 1000, 1100, 1200, 1400
# Se salta el 1300.

# Bucle for
# Sintaxis

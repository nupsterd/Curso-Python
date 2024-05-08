#  Los condicionales se utilizan para ejecutar un bloque específico de 
# Código si las condiciones dadas son verdaderas o falsas

# Sentencia if 
# Sintaxis
#   if condition:
#      esta parte del código se ejecuta en condiciones verdaderas

# Ejemplo 
num = 3
if num > 0: # Siempre debe tener una indentacion para entrar al condicional
    print("Num es un numero positivo") 

#tro ejemplo
dato = int(input("Ingrese la clave: "))
if dato == 1234:
    print("La clave es correcta")

# En el ejmplo anterior nos hace falta algo
# Que pasa cuando no es correta la clave?  
# Apare entonces el condional else
# Se cumple si if la condición es verdadera, se ejecutará el primer bloque,
# Si no, se ejecutará la condición else.

# Sintaxis
#   if condition:
#      esta parte del código se ejecuta en condiciones verdaderas
#   else:
#      esta parte del código se ejecuta en condiciones falsas

# Ejemplo 
num = -2
if num < 0: # Siempre debe tener una indentacion para entrar al condicional
    print("Num es un numero negativo")
else:
    print("Num es un numero positivo")

# Ejemplo
dato1 = int(input("Ingrese la clave: "))
if dato1 == 1234:
    print("La clave es correcta")
else:
    print("La clave no es correcta")

# Que pasa si tenemos mas condiciones ?
# Python tiene un condiconal para multiples condiciones el elif

# Sintaxis
#   if condition:
#       codigo
#   elif condition:
#       codigo
#   else:
#       codigo

# Ejemplo 
num = 0
if num > 0: # Siempre debe tener una indentacion para entrar al condicional
    print("Num es un numero positivo")
elif num < 0:
    print("Num es un numero negativo")
else:
    print("Num es cero")

# Existe la forma de hacer mas corto la sintaxis de los condicionales
# Sintaxis -- codigo if condition else codigo

# Ejemplo
num = -2
print("Num es positivo") if num > 0 else print("Num es negativo")

# Condicional anidados
# Sintaxis
# if condition:
#   codigo
#   if condition:
#   codigo

num = 10
if num > 0:
    if num % 2 == 0:
        print("Num es positivo y par")
    else:
        print("Num es positivo")
elif num == 0:
    print("Num es cero")
else:
    print("Num es negativo")

# Condicionales con operadores logicos
# Sintaxis
#   if condition and condition:
#      codigo

num = 2.6
if num > 0 and num % 2 == 0:
        print("Num es positivo y par")
elif num > 0 and num % 2 !=  0:
     print("Num es positivo")
elif num == 0:
    print("Num es cero")
else:
    print("Num es negativo")

# Sintaxis
#   if condition or condition:
#      codigo

usuario = 'Pedro'
nivel_acceso = 4
if usuario == 'admin' or nivel_acceso >= 4:
        print("Acceso concedido")
else:
    print("Acceso Denegado")
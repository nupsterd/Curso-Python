# Inicializo variables
a = 10
b = 3

# Operadores Aritmeticos
suma = a+b
resta = a-b
multiplicacion = a*b
division = a/b
potencia = a**b
modulo = a%b # entrega el residuo

# Doble backslash es floor division
floor_division = a//2  

'''
Devuelve el cociente de la division 
Si es decimal aproxima el entero hacia abajo 
Ejemplo 10/3 = 3.333 devulve 3
        10/4 = 2.5 devuelve 2 
'''

print(suma, resta, multiplicacion, division, modulo, floor_division)

# Operadores comparativos
print( a > b ) # Operador mayor
print( a < b ) # Operadormenor
print( a == b ) # Operador igual
print( a >= b ) # Operador mayor igual
print( a <= b ) # Operador menor igual
print( a != b ) # Operador no igual (diferente)

# Aqui compara el orden alfabetico por ASCII
print( "hola" > "Python") 
print( "hola" < "Python") 
print( "hola" == "hola" )
print( "hola" >= "Python") 
print( "hola" <= "Python") 
print( "hola" != "Python") 

# Operadores logicos 
print( 3 > 2 and 4 < 2 ) 
print( 3 > 2 or 4 < 2 ) 
print(not 3 > 2)
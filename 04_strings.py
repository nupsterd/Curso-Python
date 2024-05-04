# Inicializo variables con cadena de caracteres

un_string = "Hola mundo"
una_letra = "R"
una_frase = "El conocimiento es poder"

# Si quiero saber la longitud de una variable 
# Utilizo len

print(len(un_string)) # Resultado 10
print(len(una_frase)) # Resultado 24

# Si quiero un string con muchas lineas utilizo 3 comillas simples
#al inicio y 3 al final o asi mismo dobles con el mismo parametro

multi_string = '''Hola soy un aprendiz. 
Intento aprender Python 
Y por eso estoy compartiendo todo mi proceso.'''
print(multi_string)

multi_string = """Hola soy un aprendiz. 
Intento aprender Python 
Y por eso estoy compartiendo todo mi proceso."""
print(multi_string)

# Puedo concatener varios strings

nombre = "Luis"
apellido = "Figo"
espacio = " "
edad = 102
nombre_completo= nombre + espacio + apellido

print(nombre_completo)

# En Python y otros lenguajes de programación \ 
# seguido de un carácter es una secuencia de escape.
# \n: salto de linea
# \t: tabulacion es decir 4 espacios

print("Salto de \nlinea")
print("Espaciado de\ttabulacion")

# \\: Back slash
print("Para poner back slash (\\)")

# \': Single quote (')
# \": Double quote (")
print("Para poner un texto con comillas dobles \"Hola, mundo\" o simples \'Hola, mundo\'")

# Formatear strings
# para cadena de caracteres usar %s
# para enteros %d
# para flotantes %f

print ("Mi nombre es %s %s " %(nombre, apellido))
print ("Mi nombre es %s %s y mi edad es %d " %(nombre, apellido, edad))

# Formatear string con el comando format

print ("Mi nombre es {} {} " .format(nombre, apellido))
print ("Mi nombre es {} {} y mi edad es {} " .format(nombre, apellido, edad))

# Numeros y cadena de caracteres
# {:.2f} 2 digitos despues del decimal
radio = 10
pi = 3.14
area = pi * radio ** 2
formated_string = 'El area de un circulo con radio {} es {:.2f}.'.format(radio, area)
print(formated_string)

# Desempaquetar caracteres
palabra = "Python"
a, b, c, d, e, f = palabra
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Accediento a caracteres
# Python inicia el conte de caracteres desde cero
# Es decir para la palabra Python la letra
# P es la posicion 0 
# N es la posicion 5

print(palabra[0])
print(palabra[5])

# Tambien puedo contar posiciones con numeros negativos
# N es -1
# P es -6

print(palabra[-1])
print(palabra[-6])

# Tambien puedo acceder a varias posiciones 
# Realizar un slicing 

print(palabra[1:3]) # Resultado yt
print(palabra[1:]) # Resultado ython
print(palabra[0:4]) # Resultado Pyth
print(palabra[::-1]) # Palabra al reves 

palabra2 = "Python_VsCode"
print(palabra2[0:13:2]) # recorro toda la palabra e imprimo de 2 en 2
print(palabra2[0:13:3]) # recorro toda la palabra e imprimo de 3 en 3

# Funciones

print(palabra2.capitalize())
print(palabra2.upper())
print(palabra2.count("o"))
print("1".isnumeric())
print(palabra2.lower())


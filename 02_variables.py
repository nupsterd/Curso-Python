# Buenas practicas:
# Escribir en minisculas
# No comenzar con un numero
# Solo debe contener caracteres alfanumericos y giones bajos A-z, 0-9, _
# No es tan comun pero pueden empezar con un _

# Variables en Python
primer_nombre = 'Felipe'
apellido = 'Mendez'
pais = 'Colombia'
ciudad = 'Bogota'
edad = 120
skills = ['Bash', 'Git', 'Python']
informacion_completa = {
   'primer_nombre': 'Felipe',
   'Apellido': 'Mendez',
   'pais': 'Colombia',
   'ciudad': 'Bogota'
   }

# Imprimir los datos anteriores
# Concatenar de variables en print
print("Primer nombre: ", primer_nombre ) #texto y variables
print("Apellido: ", apellido)
print("Pais: ", pais )
print("Ciudad: ", ciudad)
print("Edad: ", edad )
print("Habilidades: ", skills )
print("Información completa: ", informacion_completa )
print(pais, ciudad) # solo variables


# Funciones predeterminadas
print(len('Hola Python!')) # cuenta los caracteres incluido los espacios

# Creando variables de una forma diferente
alias, fruta, animal, cosa = "Beto", "Mora", "Tortuga", "Isla"
print(alias, 'se come una', fruta, "mientras ve a su animal favorito la", animal, "y las ve caminar en una", cosa)

# Pasar argumento por consola
argumento = input('cual es tu nombre: ')
edad_arg = input('cuantos años tienes? ')
print(argumento)
print(edad_arg)

# Tener en cuenta no renombrar variables
prueba = 1 # primera forma
prueba = "hola" # segunda forma
print(prueba) # imprime el ultimo valor asignado


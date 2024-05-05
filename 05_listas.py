# Lista es una coleccion de datos ordenada y variable.
# Una lista permite valores duplicados.

# Como crear una lista
primer_lista = list()
otra_lista = []

print(len(primer_lista)) # El resultado es cero

# Lo habitual es crear la lista con []
cosas = ["Mesa", "Teclado", "Microfono", "Pantalla", "Libros", "Lapiz"]
print("Numero de cosas:", len(cosas))

# Podemos verificar de que tipo es variable
print(type(cosas))

# Podemos tener listas de diferentes elementos caracteres o numeros etc
variada = ["Mendez", 35, "Mora", 45.29, "Colombia"]
print(variada)
print(type(variada))

# Puedo tener los mismos valores
valores_repetidos = [10, 20, 30, 20, 10, 50, 40, 20, 60]
print(valores_repetidos)
print(len(valores_repetidos))
print(type(valores_repetidos))

# Como acceder a las listas
# Recordar que Python inicia el conteo posicional desde cero
# ejemplo variada = ["Mendez", 35, "Mora", 45.29, "Colombia"]
# ["Mendez", 35, "Mora", 45.29, "Colombia"]
#     0      1     2       3       4  index positivo
#    -      -4    -3      -2       -1 index negativo

print("Numero de elementos en valores repetidos:",len(valores_repetidos))
print(valores_repetidos[0]) # El resultado es 10
print(valores_repetidos[1]) # El resultado es 20
print(valores_repetidos[-4]) # El resultado es 50
print("Numero de elementos en cosas:", len(cosas))
print(cosas[0]) # El resultado es Mesa 
print(cosas[4]) # El resultado es Libros
print(cosas[-3]) # El resultado es Pantalla

# Ahora si queremos contar cuantos elementos iguales tenemos en una lista 
print(valores_repetidos.count(20)) # El resultado es 3

# Desempacar los items de una lista 
variada = ["Mendez", 35, "Mora", 45.29, "Colombia"]
apellido, edad, fruta, promedio, pais = variada
print(edad) # La respuesta es 35

# Aqui un ejemplo de como puedo tomar 
# Varios datos continuos de una lista en una sola variable
paises = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = paises
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

# Pruebas con funciones
# Agregar un elemento al final de la lista
variada.append("Caminar")
print(variada)

# Agregar elemento en la posicion que queramos
variada.insert(1, "Amarillo")
print(variada)

# Eliminar el elemento final de una lista por defecto y guardarlo
pop1 = variada.pop()
print(variada)
print(pop1)

# Eliminar el elemento con la posicion deseada y guardarlo
pop2 = variada.pop(2)
print(variada)
print(pop2)

# Eliminar por indice
print(paises)
del paises[0]
print(paises)

# Eliminar indicando el o los valores a eliminar 
print(paises)
paises.remove("Estonia")
print(paises)


# Slicing de listas
frutas = ['banano', 'naranja', 'mango', 'limon']
todas_frutas = frutas[0:4] # Todas las frutas
print(todas_frutas)
todas_frutas = frutas[0:] 
print(todas_frutas)
naranja_y_mango = frutas[1:3] 
print(naranja_y_mango)
naranja_mango_limon = frutas[1:]
print(naranja_mango_limon)
banano_y_mango = frutas[::2] 
print(banano_y_mango)
naranja_y_limon = frutas[1::2]
print(naranja_y_limon)


# Otras funciones
print(frutas)
frutas.sort() # Organiza en orden alfabetico
print(frutas)
frutas.reverse() # Organiza de la z a la a
print(frutas)
# Una tupla es una coleccion de diferentes tipos de datos 
# Que estan ordenados y no cambian es decir inmutables
# Despues de crear una tupla no se pueden cambiar los valores
# No se pueden usar funciones como agregar insertar eliminar 

# Como crea una tupla
tupla_vacia = ()
otra_tupla = tuple()

# Lo habitual es crear una tupla con ()
tupla1 = ("valor 1", "valor 2", "valor 3 ", "valor 4", "valor 1" )
frutas = ('banano', 'naranja', 'mango', 'limon')

# Imprimir los valores de las tuplas
print(tupla1)
print(frutas)

# Acceder a posiciones de las tuplas
print(tupla1[1])
print(frutas[3])

# Conocer la longitud de una tupla
print(len(tupla1))

# Funciones
print(tupla1.count("valor 1"))
print(frutas.index("mango"))

# Puedo sumar tuplas
tupla_larga = tupla1 + frutas
print(tupla_larga)
print(tupla_larga[::2])

# Si quiero modificar una tupla debemos convertirla (no es normal)
# Pero la hacemos lista, agregamos valores y nuevamente pasarla a tupla 
tupla1 = list(tupla1)
print(type(tupla1))
tupla1.insert(0 , "nuevo valor")
print(tupla1)
tupla1 = tuple(tupla1)
print(type(tupla1))
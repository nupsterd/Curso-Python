# un diccionario es una coleccion de datos no ordenados
# Con la caracteristica que son mutables 
# Emparejados con clave y valor 

# Creo un diccionario vacio
diccionario_0 = dict()
diccionario_1 = {}

print(type(diccionario_0))
print(type(diccionario_1))

# Creo un diccionario inicial 
# Sintaxiz {clave: valor, clave valor,...}
diccionario_2 = {"Nombre": "Felipe", "Apellido": "Mett", "Edad": 32, 1:"Python"}
print(diccionario_2)

diccionario_3 = {
    "Nombre": "Felipe", 
    "Apellido": "Mett", 
    "Edad": 32, 
    "lenguajes": {"Python", "Bash", "Matlab"},
    1: 1.77,
    }
print(diccionario_3)

# Puedo saber el tamaño
print(len(diccionario_2))
print(len(diccionario_3))

# Accediendo al diccionario
print(diccionario_3["Nombre"])
print(diccionario_3["Apellido"])
print(diccionario_3["Edad"])
print(diccionario_3[1])

# Agregar nuevos valores al diccionario
diccionario_3["Año"] = 2024
diccionario_3["Calle"] = "Avenida pensilvania"
print(diccionario_3)

# Modificar valores de un diccionario
diccionario_3["Nombre"] = "Pedro"
print(diccionario_3)

# Eliminar datos de diccionario
del diccionario_3["Calle"] # Eliminar una clave y valor indicado
print(diccionario_3)

diccionario_3.pop("Nombre") # Eliminar una clave y valor indicado
print(diccionario_3)

diccionario_3.popitem() # Elimino el ultimo item del diccionario
print(diccionario_3)

# Verificar claves en un diccionario
print("Apellido" in diccionario_3)

# Funciones diccionarios
print(diccionario_3.items()) # Listado de cada uno de los items
print(diccionario_3.keys()) # Acceso a las claves
print(diccionario_3.values()) # Acceso a los valores

# La función dict.fromkeys() en Python crea un nuevo diccionario 
# a partir de una secuencia de claves y asigna un valor inicial 
# común a todas esas claves.
claves = ['clave1', 'clave2', 'clave3'] # Claves que quiero en el diccionario
mi_diccionario = dict.fromkeys(claves, 0)# Crear un diccionario donde todas las claves tienen el valor 0
print(mi_diccionario)


# Un conjunto es una coleccion de datos.
# Datos distintos no ordenados y no indexados

# Creo un conjunto vacio
mi_conjunto = set()
mi_conjunto1 = {}

print(type(mi_conjunto))
print(type(mi_conjunto1))

# Creo un conjunto inicial con datos
mi_conjunto2 = {'item1', 'item2', 'item3', 'item4'} 
print(type(mi_conjunto2))

# El conjunto y el diccionario comparten{}
# Pero tener en cuenta la forma en que se crean para este caso
# Lo anterior es la forma correcta para set

# Creando otro set probado el metodo len()
frutas = {'banano', 'naranja', 'mango', 'limon'}
print(len(frutas))

# Comprobacion que existe los elementos 
print("Tengo a item3 en el conjunto?", "item3" in mi_conjunto2)
print("mora" in frutas) # Comprobacion de elementos 

# Agregando valores al conjunto 
mi_conjunto2 = {'item1', 'item2', 'item3', 'item4'} 
mi_conjunto2.add("item100")
print(mi_conjunto2) # El valor agregado no tiene posicion fija es desordenado

frutas.add("mora")
print(frutas) # El conjunto es de estructura no ordenados

frutas.add("mora")
print(frutas) # Un conjunto no admite valores repetidos por eso solo tenemos una mora

mi_conjunto2.update(["item200", "item300"]) # Otra forma de agregar datos
print(mi_conjunto2)

# Podemos eliminar valores
mi_conjunto2.remove("item200")
print(mi_conjunto2)

mi_conjunto2.pop() # Elimina un valor aleatorio
print(mi_conjunto2)

valor_eliminado = mi_conjunto2.pop() #Para almacenar el valor eliminado
print(mi_conjunto2)
print(valor_eliminado)

# Puedo borrar todos los elementos del conjunto
mi_conjunto2.clear()
print(len(mi_conjunto2))

mi_conjunto2 = {'item1', 'item2', 'item3', 'item4'} 
del mi_conjunto2 # Aqui eliminamos todo los elementos y la variable 

# Convertir de lista a conjuntos
lista1 =  ['item1', 'item2', 'item3', 'item4']
print(type(lista1))
mi_conjunto2 = set(lista1)
print(type(mi_conjunto2))

# Operaciones con conjunto 
mi_conjunto2 = {'item1', 'item2', 'item4'} 
otro_conjunto = {"Python", "Matlab", " Bash"}
nuevo_set = mi_conjunto2.union(otro_conjunto)
print(nuevo_set)
print(nuevo_set.union(["Java"]))

mi_conjunto2 = {'item1', 'item2', 'item4'} 
otro_conjunto = {"Python", "Matlab", " Bash", "item1"}
nuevo_set2 = mi_conjunto2.intersection(otro_conjunto)
print(nuevo_set2)

mi_conjunto2 = {'item1', 'item2', 'item4'} 
otro_conjunto = {"Python", "Matlab", " Bash"}
print(mi_conjunto2.difference(otro_conjunto))
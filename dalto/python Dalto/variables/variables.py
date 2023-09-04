#VARIABLES: espacios que se almacenan en un espacio de la memoria
#CONCATENAR: unir cadenas

nombre = "mica"
bienvenida = "hola " + nombre + " como estas?"
print(bienvenida)

nombre = "mica"
bienvenida = f"hola {nombre} como estas?" #"Fstring" para poder concatenar. convierte a texto cualquier tipo de dato
print(bienvenida)

#del para borrar variables

#operadores de pertenencia (in / not in)
print("mica" in bienvenida) #true
print("mica" not in bienvenida) #false


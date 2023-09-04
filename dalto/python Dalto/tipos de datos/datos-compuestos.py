#datos que adentro tienen datos

#listas
lista = ["mica reartes","soy mica","23 años",True,1.67] #array/arreglo las posiciones(INDICE) van desde 0
print(lista[0]) #Entre corchetes idicar el indice

#tuplas, usa parentesis en vez de corchetes. se diferencia en que sus elementos no se pueden modificar
tupla = ("mica reartes","soy mica","23 años",True,1.67)

lista[3] = "maquinola" #esto es valido

tupla[3] = "maquinola" #esto no es valido

#creando un conjunto (set) - se usan llaves y los elementos estan desordenados. se puede redifinir o recontruir el conjunto pero no se pueden modificar los elementos
#no se puede acceder al elemento por indice, solo se puede hacer con un BUCLE
#no repite elementos, no puede haber datos duplicados

conjunto = {"mica reartes","soy mica","23 años",True,1.67}
print(conjunto)

#creando un diccionario (dict)
diccionario = {
    'nombre' : "mica reartes", #no olvidar las comas
    'quien soy' : "soy mica",
    'edad' : "23 años",
    'esta_emocionado' : True,
    'altura' : 1.67,
    'dato duplicado' : "soy mica"
}
print(diccionario['nombre'])
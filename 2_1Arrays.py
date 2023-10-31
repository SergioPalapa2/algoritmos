#Selection sort
#Seleccion ordenada
#Los arreglos y listas ordenadas son estructuras de datos basicas.
#El algoritmo de busqueda binaria(binary search) solo funciona en listas ordenadas.

#Ejemplo:
#Almacenar una lista TODO en un espacio en memoria
#Usar un array o una lista ¿?

###Array
#En un arreglo se sabe la posicion de cada item, llamado indice(index)
#Lectura=0(1)
#Escritura=0(n)
#Borrado=O(n)


###Linked list
#Una lista enlazada nos ofrece la posibilidad de conocer la direccion o ubicacion en memoria de cada elemento
#Cada elemento almacena la siguiente direccion
#Se optimiza el uso de memoria (inserts)
#Son buenas cuando se leeran los items uno por uno
#Lectura=0(n)
#Escritura=0(1)
#Borrado=O(1)

#Ejemplos
arreglo=[0]
arreglo=[1,2,3,4,5,6,7,8,9]
print("El elemento arreglo contiene",arreglo," y en python es del tipo: ",type(arreglo))


#Existen dos tipos de acceso a los datos
# -Acceso aleatorio
# -Acceso secuencial

##SELECTION SORT
#Ordenamiento por seleccion.
#Caso de uso: Ordenar de mayor a menor numero de reproduccion por grupo musical

#Ejercicio:
##########################################################
def findSmallest(arr):
    smallest=arr[0] #Valor menor antes de la busqueda
    smallest_index=0#Indice del menor valor encontrado
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index

arreglo=[9,6,5,8,7,1,79,3,7]
print("Busqueda del indice con el menor valor en ", arreglo)
print(findSmallest(arreglo))

#Ahora es posible usar la funcion para escribir el algoritmo de ordenamiento por seleccion
def selectionSort(arr):
    newArr=[]
    for i in range(len(arr)):
        smallest=findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort(arreglo))
##########################################################




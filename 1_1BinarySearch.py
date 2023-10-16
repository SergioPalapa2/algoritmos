#BINARY SEARCH
# En una busqueda binaria se tiene como entrada una lista ordenada.
# Si en la lista existe el elemento que se esta buscando, se devuelve su posicion.
#De lo contrario se devuelve un elemento nulo (NULL)

#Para cada lista de n elementos, en el peor de los casos tomara log2 n pasos devolver el resultado.

#Nota: La busqueda binaria solo funciona cuando la lista esta ordenada

#Ejemplo
def binary_search(list, item):
    low=0
    high=len(list)-1

    while low <= high:
        mid=(low+high)//2
        guess=list[mid]

        if guess == item:
            return mid
        if guess > item:
            high=mid+1
        else:
            low=mid+1
    return None


lista=["1","3","5","7","9"]
print(binary_search(lista,"7"))




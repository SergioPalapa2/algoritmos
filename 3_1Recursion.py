#RECURSION
#Ocurre recursión cuando una funcion se llama a si misma
#La recursion se utiliza para hacer un codigo mas claro; no necesariamente mas optimo.
#En algunos casos es mejor usar loops

#La recurasividad puede derivar en loop infinitos si no se usa correctamente.
#Caso recursivo: El momento en que se llama a la recursion
#Caso base: Cuando no se llama a si misma nuevamente en la ejecucion

#Ejemplo:
#Conteo en descendente desde un numero i
def countdown(i):
    print(i)
    if i<=1:#caso base
        return
    else:#caso recursivo
        countdown(i-1)

countdown(3)

#THE STACK
#Apilado de elementos en donde se eascribe al inicio y se lee deasde el inicio(LIFO)
#Las funciones recursivas usan llamado de pila

#Ejemplo
def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)
    
print("Factorial de 5 es",fact(5))
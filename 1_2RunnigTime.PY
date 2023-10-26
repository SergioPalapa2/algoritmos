import matplotlib.pyplot as plt



#RUNNING TIME
#El tiempo que un algoritmo tarda en ejecutarse.
#Definicion: Tiempo logaritmico

#Big O notation
#Esta notacion nos indica que tan rapido es un algoritmo.

#-Busqueda simple: Tomara n operaciones -> O(n)
#-Busqueda binaria: Tomara log2 n -> O(log n)

#Nota: No se mide en segundos, se compara numeros de operaciones (como crece el algoritmo)

#Big O siempre establece el peor de los casos
#Existen 5 tiempos de ejecucion Big 0 que son las mas comunes:
print("Tiempos de ejecucion Big O mas usados")
print("- O(log n)       ->Tiempo logaritmico(binary search)")
print("- O(n)           ->Tiempo lineal (simple search)")
print("- O(n * log n)   ->Busqueda rapida(quicksort)")
print("- O(n^2)         ->Busqueda lenta (selection sort)")
print("- O(n!)          ->(traveling salesperson)")

# #Graficas ejemplpo
# xi = [0,1,2,3,4,5,6]
# yi = [0,1,4,9,16,25,36]
# plt.plot(xi,yi)
# plt.show()



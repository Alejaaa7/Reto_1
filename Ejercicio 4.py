#-----------------------------------------------------------------------
# 4. Escribir una función que reciba una lista de números enteros y 
# retorne la mayor suma entre dos elementos consecutivos.
#-----------------------------------------------------------------------

#Se crea una función que primero cree la variable de la suma entre los 
#dos primeros números de la lista, y luego vaya recorriendo la lista y 
#sume cada número con el que le sigue, para comparar cada resultado con 
#la variable creada inicialmente. 
def largest_sum(list_of_ints):

    max_sum = list_of_ints[0] + list_of_ints[1] #se crea la primera variable
    for i in range(1, len(list_of_ints) - 1):
        new_sum = list_of_ints[i] + list_of_ints[i + 1] #se hace cada suma
        if new_sum > max_sum:
            max_sum = new_sum #si es mayor, se remplaza

    return max_sum

#Se presenta el programa.    
print("Bienvenid@, este es un programa en el que podrás encontrar la mayor suma " \
"entre dos números consecutivos de una lista de números que usted proporcione.")

#Se piden los números de una vez separados por comas
list_of_ints = list(map(int, input("Por favor, ingrese los números" \
"separados por comas: ").split(',')))

while len(list_of_ints) < 2:
    print("Ingresa más números. Por favor")
    list_of_ints = list(map(int, input().split(',')))

result = largest_sum(list_of_ints)
print("La mayor suma es: ", result)
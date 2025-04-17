#-----------------------------------------------------------------------
# 5. Escribir una función que reciba una lista de string y retorne 
# únicamente aquellos elementos que tengan los mismos carácteres. e.g. 
# entrada: ["amor", "roma", "perro"], salida ["amor", "roma"].
#-----------------------------------------------------------------------

#Se crea la función que nos retorne los anagramas
def same_characters(list_of_str):
    groups = {} #se crea un diccionario para agrupar las palabras 

    for i in list_of_str:
        cleaned_word = i.strip().lower()
        order = ''.join(sorted(cleaned_word)) #se ordenan las letras de
                                              #la palabra para crear una
                                              #pista única 

        if order in groups:
            groups[order].append(cleaned_word) #si ya existe esa pista, 
                                               #se agrega la palabra al 
                                               #grupo
        else:
            groups[order] = [cleaned_word] #si no existe, se crea una 
                                           #nueva lista con esa palabra
    
    result = [] #esta lista es para guardar los resultados finales

    for j in groups.values():
        if len(j) > 1: #solo se toman los grupos con más de una palabra 
                       #porque esos son los anagramas entre sí
            result.extend(j) #se agregan las palabras del grupo al 
                             #resultado final
    
    return result #finalmente, se devuelve la lista final

#Se presenta el programa.    
print("Bienvenid@, este es un programa en el que podrás encontrar los anagramas " \
"de una lista de palabras que tú proporciones.")

#Se pide la lista de palabras
list_of_str = input("Ingresa tu lista de palabras separadas por comas: ").split(',')
new_list = same_characters(list_of_str) #se prepara la respuesta
print("La lista resultante es: ", new_list)

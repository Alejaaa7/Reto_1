#-----------------------------------------------------------------------
# 2. Realice una función que permita validar si una palabra es un 
# palíndromo. Condición: No se vale hacer slicing para invertir la 
# palabra y verificar que sea igual a la original.
#-----------------------------------------------------------------------

def is_palindrome(word):
    word = word.lower() #por si tiene mayúsculas
    for i in range(len(word) // 2): #para revisar la mitad
        if word[i] != word[-(i+1)]: #para comparar los extremos
            return False
    return True


word = str(input("Por favor, ingrese la palabra a verificar: "))

if is_palindrome(word):
    print("¡Esta palabra es un palíndromo!")
else:
    print("Error. Esta palabra no es un palíndromo.")
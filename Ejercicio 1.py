#-----------------------------------------------------------------------
# 1. Crear una función que realice operaciones básicas (suma, resta, 
# multiplicación y división) entre dos números, según la selección del 
# usuario, la forma de entrada de la función será los dos operandos y el
# caracter usado para la operación. entrada:(1,2,"+"), salida (3).
#-----------------------------------------------------------------------

#Primero, creé una función que pida y arregle los datos para no tener que
#volver a escribir las mismas líneas para cada que el usuario se equivoque:
def get_input():
    #Se reciben los valores a usar.
    num1, num2, operation = input("Por favor, ingresa a continuación el primer y " \
"segundo número a operar y la operación a realizar, separados por comas: " \
"").split(',')
    #Se convierten los números recibidos y la operación, para evitar errores:
    num1 = int(num1.strip()) if num1.strip().isdigit() else float(num1.strip())
    num2 = int(num2.strip()) if num2.strip().isdigit() else float(num2.strip())
    #_ se usa x.strip() para evitar errores con los espacios adicionales por
    #  si el usuario los añade.
    #_ se usa .isdigit() para revisar si el número ingresado solo es positivo
    #  y sin decimales, o no; y se usa con un if ternario para que sea entero
    #  o float.
    operation = operation.strip() #para evitar que se convierta a número
    return num1, num2, operation

#Ahora sí se crea una función que opere los números según la indicación 
#del usuario, y los descarte si la operación no es posible o si la 
#entrada está mal. 
def basic_operation(num1, num2, operation):
    while operation not in ["+", "-", "*", "/", "%"]:
        #se revisa que se haya elegido bien la operación
        print("Entrada inválida, por favor intenta nuevamente.")
        num1, num2, operation = get_input() #se llama la función creada
    if operation == "+":        #aquí los if para ver cuál operación es
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        while num2 == 0: #para asegurarse de que sea posible
            print("No es posible dividir entre 0. Ingrese el segundo número de" \
            "nuevo, por favor.") 
            num2 = float(input(" ")) #para dar otra oportunidad
        return num1 / num2
    elif operation == "%":
        return num1 % num2

#Se presenta el programa.    
print("Bienvenid@, este es un programa en el que podrás realizar la operación" \
"básica que desees entre dos números.")

#Se piden los datos.
num1, num2, operation = get_input()

#Se llama la función y se le muestra el resultado al usuario :) y fin.
result = basic_operation(num1, num2, operation)
print("El resultado es: ", result)


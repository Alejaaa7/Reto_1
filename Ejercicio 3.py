#-----------------------------------------------------------------------
# 3. Escribir una función que reciba una lista de números y devuelva 
# solo aquellos que son primos. La función debe recibir una lista de 
# enteros y retornar solo aquellos que sean primos.
#-----------------------------------------------------------------------
import random

primes = []

def prime_number(num_list):
    for i in num_list:
        if i < 2: #no será primo si es menor que 2
            continue
        for j in range (2, i):
            if i % j == 0:
                break #si es divisible por algún número tampoco lo será
        else:
            primes.append(i)
    return primes

num_list = list(map(int, input("Ingrese los números a verificar separados por" \
" comas: ").split(',')))
prime_number(num_list)
print("Estos son los números primos de tu lista: ", primes)



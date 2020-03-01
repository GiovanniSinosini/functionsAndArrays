"""
Crie uma função contaPrimos() que receba dois valores inteiros
como argumentos e retorne o número de números primos entre estes
dois números, inclusive. P. Ex. contaPrimos(3,10) deverá retornar
o valor 3 (3, 5, 7). A função deverá ser testada sendo que os dois
valores são introduzidos pelo utilizador. 
"""


def num_prime(n):

    for x in range (2,n):
        if n % x == 0:
            return False
    return True

def contaPrimos(min, max):
    resultado = []
    for x in range (min, max+1):
        if num_prime(x) == True:
            resultado.append(x)
    return resultado

def main():

    while True:

        min = input("Enter the minimum value: ")
        max = input("Enter the maximum value: ")

        if min.isnumeric() and max.isnumeric():
            min = int(min)
            max = int (max)
            break
        else:
            print ("Input ERROR. Try again.")

    print ("The prime numbers are: ", contaPrimos(min, max))
    













main()




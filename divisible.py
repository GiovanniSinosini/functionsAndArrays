"""
7) Crie uma função que receba dois valores inteiros como argumentos
e retorne um valor booleano indicando se os números são divisíveis. 
"""


def disible(n1, n2):

    if n1 % n2 == 0:
        return True 
    else:
        return False

def main():

    cont = "yes"

    while cont == "yes":
        cont = input("Do you want check? (yes/no) ")

        if cont == "yes":
            while True:
                n1 = input("Enter de first number: ")
                n2 = input("Enter second number: ")

                if n1.isnumeric() and n2.isnumeric():
                    n1 = int(n1)
                    n2 = int (n2)
                    break
                else:
                    print ("Input ERROR. Try again.")
            print ("%d is divisible by %d ? " %(n1, n2), disible(n1,n2))

        else:
            print ("Program successfully completed.")


main()
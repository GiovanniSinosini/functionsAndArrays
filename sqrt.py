"""
3) Crie uma função que receba dois valores float como argumentos e
retorne o valor da raiz quadrada da soma dos quadrados.

"""


def sum_srt(n1,n2):
    return ((n1**2 + n2**2)**0.5)



def main():

    while True:
        n1 = input("Enter first value: ")
        n2 = input("Enter second value: ")

        if n1.isnumeric() and n2.isnumeric():
            n1 = float(n1)
            n2 = float(n2)
            break
        else:
            print ("Input ERROR. Try again")

    print ("The result is: {:.2f}" .format(sum_srt(n1,n2)))


main()
"""
4) Crie uma função que receba um número inteiro como argumento e
retorne o maior valor primo inferior a esse argumento. Se o
argumento for negativo, a função deverá retornar o valor zero. 
"""

def ePrimo(n):
    for x in range(2,n):
        if n % x == 0:
            return False
    return True


def maiorPrimoInferior(n):
    n -=1        
    while n >= 1 or n < 0:

        if n < 0:
            return 0

        elif ePrimo(n) == True:
            return n
        else:  
            n -= 1
     
    
def main():
    while True:
        n = input("Enter value: ")

        if n.isnumeric():
            n = int(n)
            break
        else:
            print ("Input Error. Try again.")

    if maiorPrimoInferior(n) == 0:
        print ("Negative value entered - return ", maiorPrimoInferior(n))
    else:    
        print ("The highest prime number is ", maiorPrimoInferior(n))


main()
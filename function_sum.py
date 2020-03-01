"""
1) Crie uma função que receba 2 valores inteiros como argumentos e
retorne a sua soma. Se o valor da soma for negativo a função deverá
retornar o valor 0. 
"""




def soma (a, b):
    
    if a + b > 0:
        return a + b
    else:
        return 0


def main():
    
    while True:

        print ("Sum with function")
        num1 = input("Enter value 1: ")
        num2 = input("Enter value 2: ")
        
        if num1.isnumeric() and num2.isnumeric():
            num1 = int(num1)
            num2 = int(num2)
            break
        else:
            print("Error. Enter numeric values. Try again.")

    print ("The sum is %d. " %(soma(num1, num2)))


main()


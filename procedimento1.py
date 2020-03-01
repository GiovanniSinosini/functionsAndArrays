"""
14 - Crie um procedimento que receba 3 variáveis inteiras como
argumento e altere o valor das variáveis, colocando-as no máximo
dos 3 valores.
"""

def change(n1, n2, n3):
    bigger = 0

    if n1 > n2  and n1 > n3:
        bigger = n1
    elif n2 > n3:
        bigger = n2
    else:
        bigger = n3
    
    n1 = bigger
    n2 = bigger
    n3 = bigger

    
    print ("\nThe values of the variables are: \nn1 = %d \nn2 = %d \nn3 = %d\n" %(n1,n2,n3))

def main():

    start = "yes"
    while start == "yes":
        start = input("Do want start ? (yes/no) ")
        
        if start == "yes":
            while True:
                n1 = input("Enter the first number: ")
                n2 = input("Enter the second number: ")
                n3 = input("Enter the third number: ")

                if n1.isnumeric() and n2.isnumeric() and n3.isnumeric():
                    n1 = int(n1)
                    n2 = int(n2)
                    n3 = int (n3)
                    break
                else:
                    print ("Input ERROR. Try again.")
            change(n1,n2,n3)         

        else:
            print ("Program sucessfully completed.")







main()
"""
15) Crie um procedimento que receba um valor inteiro como
argumento e o altere para o seu simétrico (negativo passa a positivo
e vice-versa).
"""

def is_number(num): 
#Tests to see if arg is number.
    
    try:
        float(num) #Try to convert the input.
        return True #If successful, returns true.
        
    except:
        pass #Silently ignores any exception.
     
    #If this point was reached, the input is not a number and the function will return False.
    return False


def symmetrical(n):

    n = n*-1

    print ("Your symmetrical is: ", n)


def main():

    start = "yes"
    while start == "yes":
        start = input("Do you want start? ")
        if start == "yes":
            while True:
                n1 = input("Enter number: ")

                if is_number(n1):
                    n1 = int(n1)
                    break
                else:
                    print ("Input ERROR. Try again.")
            symmetrical(n1)
        
        else:
            print ("Program sucessfully completed.")






main()
"""
12) Crie uma função que receba um número inteiro n e retorne o nésimo número primo.
"""


def num_prime(n):

    for x in range (2,n):
        if n % x == 0:
            return False
    return True

def pos_Primos(n):   # returns the number x element of the prime number sequence
    resultado = []
    x = 1

    while len(resultado) < n:
        if num_prime(x) == True:
            resultado.append(x)
            x += 1
        else:
            x +=1
    return resultado[-1]   # return the last element
   

def main():
    start = "yes"
    while start == "yes":
        n = input("Do you want start? (yes/no) ")
        if start == "yes":
            while True:
               n = input("Enter the number: ")

               if n.isnumeric():
                   n = int (n)
                   break
               else:
                print ("Input ERROR. Try again.")
            print ("The prime number is: ", pos_Primos(n))    
        else:
                print ("Program sucessfully completed.")

    













main()




"""
8) Crie uma função que receba um número inteiro como argumento e
retorne o número da série de Fibonacci correspondente. 
"""

def fibo(n):
     
     if n <= 1:
         return n
     else:
         return fibo(n-1) + fibo(n-2)


def main():

    continued = "yes"

    while continued == "yes":
        continued = input("Want to view the fibonacci series? ")

        if continued == "yes":
            n = input("What element do you want to see? ")

            while True:
                if n.isnumeric(): 
                    n = int(n)
                    if n > 0:
                        break
                    else:
                        print ("Input ERROR. Try again.")
                else:
                    print ("Input ERROR. Try again.")

            print ("The element is: %d" %(fibo(n)))            
    
        else:
            print ("Program sucessfully completed.")








main()


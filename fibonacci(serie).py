"""
8) Crie uma função que receba um número inteiro como argumento e
retorne o número da série de Fibonacci correspondente. 
"""

def fibo(n):
    res = []
    t1 = 0
    t2 = 1
    
    res.append(t1)
    res.append(t2)

    cont = 3
    while cont <= n:
        t3 = t1 + t2
        res.append(t3)
        t1 = t2
        t2 = t3
        cont +=1
    
    return res

def main():

    continued = "yes"

    while continued == "yes":
        continued = input("Want to view the fibonacci series? ")

        if continued == "yes":
            n = input("How many terms do you want to show ? ")

            while True:
                if n.isnumeric(): 
                    n = int(n)
                    if n > 0:
                        break
                    else:
                        print ("Input ERROR. Try again.")
                else:
                    print ("Input ERROR. Try again.")

            print (fibo(n))            
    
        else: 
            print ("Program sucessfully completed.")








main()


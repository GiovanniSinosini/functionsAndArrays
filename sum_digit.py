"""
9) Crie uma função que receba um número inteiro e retorne a soma
dos seus algarismos. 
"""

def sum_digit(n):


    sum_dig = 0
    
    while n >= 1:
        res = n % 10
        sum_dig += res
        n = n // 10    # **** will take the last digit

    return sum_dig
    

def main():

    start = "yes"
    while start == "yes":
        start = input("Do you want to add the digits? (yes/no) ")

        if start == "yes":

            while True:
                n = input("Enter number: ")
                if n.isnumeric():
                    n = int(n)
                    break
                else:
                    print ("Input ERROR. Try again.")
                        
            print ("The sum of the digits is ", sum_digit(n))



            
        else:
            print ("Program sucessfully completed.")




main()
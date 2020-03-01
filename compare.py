"""
10) Crie uma função que receba 3 valores inteiros (a, b, c) e
retorne um valor booleano true se a > b > c e false em caso
contrário. 
"""

def compare(a,b,c):

    if a > b > c:
        return True
    else:
        return False


def main():

    start = "yes"
    while start == "yes":
        start = input("Do you wanna compare? (yes/no) ")
        if start == "yes":
            
            while True:
                a = input("Enter the value of A: ")
                b = input("Enter the value of B: ")
                c = input("Enter the value of C: ")

                if a.isnumeric() and b.isnumeric() and c.isnumeric():
                    a = int(a)
                    b = int (b)
                    c = int(c)
                    break
                else:
                    print ("Input ERROR. Try again.")

            print(compare(a,b,c))
          

        else:
            print("Program sucessfully completed.")


main()

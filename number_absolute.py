"""
2) Crie uma função que receba 3 valores float como argumento e
retorne o maior valor absoluto.
"""


def number_absolute(a,b,c):
    
    if abs(a) > abs(b) and abs(a) > abs(c):
        return a
    elif abs(b) > abs(c):
        return b
    else:
        return c

    
def main():

    while True:
        a = input("Enter first float number: ")
        b = input("Enter second float number: ")
        c = input ("Enter third float numver: ")
        
        if a.isnumeric() and b.isnumeric() and c.isnumeric():
            a = float(a)
            b = float(b)
            c = float(c)
            break
        else:
            print ("Error. Enter numeric values. Try again.")

    print (number_absolute(a,b,c), "is the highest absolute number")
   

main()


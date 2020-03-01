"""
6) Crie uma função que receba 2 notas (F1 e F2) de um aluno e
retorne um booleano indicando se o aluno passou. Para passar, a
soma das notas deve ser igual ou superior a 19 e ambas devem ser
superiores a 7.
"""
def eNumero(num):
    try:
        float(num)
        return True
    except:
        pass

    return False


def std_values(f1, f2):

    if f1 + f2 >= 19 and f1 > 7 and f2 > 7:
        return True
    else:
        return False

def main():
    c = "sim"
    while c == "sim":
        c = input("Do you want to insert student grade ?")
        
        if c == "sim":

            while True:
                f1 = input("Enter the first value: ")
                f2 = input("Enter the second value: ")

                if eNumero(f1) and eNumero(f2):
                    f1 = float(f1)
                    f2 = float(f2)
                    break
                else:
                    print ("Input ERROR. Try again.")

            if std_values(f1,f2) == True:
                print ("Approved student")
            else:
                print ("Failed student")
        else:
            print ("Programa finalizado com sucesso.")
            break









main()
"""
13) Crie uma função que receba três inteiros como argumentos (year,
mês, dia) e verifique se se trata de uma data válida. O year deverá
estar entre 1900 e o presente year. Deverá retornar um valor
booleano.
"""

from datetime import datetime

def date_val(year, month, day):

    now = datetime.now()

    if year >= 1900 and year <= now.year and month > 0 and month < 12 and day > 0 and day < 31:
        return True
    else:
        return False


def main():

    start = "yes"
    while start == "yes":
        start = input("Do you want check date? ")
        if start == "yes":
            while True:
                year = input("Enter year: ") 
                month = input ("Enter month: ")
                day = input ("Enter day: ")
                if year.isnumeric() and month.isnumeric() and day.isnumeric():
                    year = int(year)
                    month = int (month)
                    day = int (day)
                    break
                else:
                    print ("Input ERROR. Try again.")
            print ("Date entered is: ", date_val(year, month, day))
        else:
            print ("Program sucessfully completed.")







main()


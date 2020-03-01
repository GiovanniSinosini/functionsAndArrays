"""
Contar cada caractere da string
"""


import test2_functions as f

def main():

    start = "yes"
    while start == "yes":
        start = input("Deseja iniciar o programa ? (yes/no) ")
        if start == "yes":

            vCaracterGuard = []  # vetor para guardar os caracteres já analisados
            contar_ocor = 0  # variável para contar o número de ocorrências dos caracteres
            resultado = ""   # variável que irá apresentar o resultado


            vCaracterGuard.clear()    # limpar vetor para análises seguidas

            string = input("Digite a string que deseja analisar: ")

            for x in range (len(string)):  # for para percorrer a string
                
                if not f.eRepetido(string[x], vCaracterGuard) and string[x].isalpha():  
                # irá verificar se já foi verificado           e  apenas caracteres (elimina espaços)
                    
                    contar_ocor = f.contaOccorencias(string[x], string)    # contar os caracteres da string
                    vCaracterGuard.append(string[x])  # guardar o caracter já analisado, para não repetir

                    resultado +=str(string[x]) + ":" + str(contar_ocor)+ "x; "  # guardar o resulta em forma de string 

           
            print ("Os caracteres digitados foram:\n",resultado)



        else:
            print ("Programa finalizado com sucesso.")

    









main()
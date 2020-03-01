"""
Trocar os elementos do vetor por = o vetor com o minimo impar trocado pelo maximo par e maxPar pelo min impar
"""

import test2_functions as f
import random as r


def gerar_vetor2_no_repeat(inicio, fim, tamanho):

    vetor = []
    for x in range (0, tamanho):    # função para criar um vetor aleatório com elementos não repetidos
        while True:
            valor = r.randint(inicio, fim)
            if valor not in vetor:
                break
        vetor.append(valor)  
    return vetor



def main():
    start = "yes"
    while start == "yes":
        start = input("Deseja executar o programa? ")
        if start == "yes":
            vetor1 = gerar_vetor2_no_repeat(0,200,5)

            minimoImpar = 9999999999999
            maxPar = -999999999999999
        
            for x in range (0,len(vetor1)):   #condicional para encontrar o minImpar e MaxPAr
        
                if vetor1[x] < minimoImpar and vetor1[x] % 2 != 0:   #minimo IMPAR
                    minimoImpar = vetor1[x]
                    posMinimoImpar =  x
      
                if vetor1[x] > maxPar and vetor1[x] % 2 == 0:   # maximo PAR
                    maxPar = vetor1[x]
                    posMaxPar = x
    

            print ("Vetor original = ", vetor1)
            print ("O mínimo impar é: ", minimoImpar, "e está na posição ", posMinimoImpar)
            print ("O máximo par é: ", maxPar, " e está na posição ", posMaxPar)

            temp = vetor1[posMinimoImpar]      #variável para guardar mínimo impar  
            vetor1[posMinimoImpar] = vetor1[posMaxPar]   #maxPar foi para o Mínimo Impar
            vetor1[posMaxPar] = temp  #MinimoImpar vai para MaxPar

            print ("Vetor com os elementos: ", vetor1)

        else:
            print ("Programa finalizado com sucesso.")
        






    


main()
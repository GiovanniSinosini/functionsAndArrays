
"""
Funções para op teste
"""

import random as r

def gerar_vetor(tamanho, inicio, fim, aleatório):

    vetor = []
 
    
    if aleatório == "yes":
        for x in range (0, tamanho):
            vetor.append(r.randint(inicio, fim))
        return vetor
    
    else:     
        for x in range (1, tamanho+1):
            while True:
                valor = input("Digite o valor %d de %d : " %(x, tamanho))
                if valor.isnumeric():
                    valor = int(valor)
                    break
                else:
                    print("Digite números.")
            
            vetor.append(valor)
        return vetor          
        

def number(n):
    if n.isnumeric():
        return int(n)

    else:
        return False


def contaOccorencias(valor,vetor) :   # conta quantos vezes o elemento aparece no vetor

    count = 0
    for x in vetor:
        if x == valor: # x = elemento que tem no vetor  - valor = valor a pesquisar
            count += 1
    return count


def eRepetido(valor, vetor):
    
    for n in vetor:   #  se N elemento do vetor 
        if n == valor:     # for igual ao valor, retorne:
            return True
    return False


def inverse_string(string):
    out = ""
    for c in range (len(string)-1, -1, -1):
        out += string[c]       # vai gravando dentro da variável
    return out







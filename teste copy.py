import random as r
import test2_functions as f

def contaOccorencias(valor,vetor) :   # conta quantos vezes o elemento aparece no vetor
    count = 0
    for x in vetor:
        if valor == x :
            count += 1
    return count

def eRepetido(valor, vetor):
    for n in vetor:   #  se N elemento do vetor 
        if n == valor:     # for igual ao valor, retorne:
            return True
    return False


def main1():


    
    res_Mais_Comum =[]
    res_Segu_Mais_Comum =[]
    vezes_q_Aparece = []
    
    start = "yes"
    while start == "yes":
        start = input("Deseja iniciar o programa ? (yes/no) ")
        vetor1 = f.gerar_vetor(200, 1, 20, "yes")
        maisComum = 0
        maisComum2 = 0
        res_Mais_Comum.clear()
        res_Segu_Mais_Comum.clear()
        vezes_q_Aparece .clear()
        if start == "yes": 
            for x in range (len(vetor1)):
                vezesQueAparece = contaOccorencias(vetor1[x], vetor1)
                vezes_q_Aparece .append(vezesQueAparece)
                
                
                if vezesQueAparece >= maisComum:  # primeira condicional entra aqui se for mais comum = maior Vezesaparece
                    maisComum = vezesQueAparece
                else:
                    if vezesQueAparece > maisComum2 :  # segunda condicional (segunda mais comum)
                        maisComum2 = vezesQueAparece
                
            for x in range (len(vezes_q_Aparece )): # comparar os dois vetores e correlacionar o vetor da contagem repetida com o vetor gerado, pois os dois possuiem o mesmo índice
                if maisComum == vezes_q_Aparece [x] and vetor1[x] not in res_Mais_Comum: 
                        res_Mais_Comum.append(vetor1[x])
                elif maisComum2 == vezes_q_Aparece [x] and vetor1[x] not in res_Segu_Mais_Comum:
                        res_Segu_Mais_Comum.append(vetor1[x])


            print("Vetor de ocorrências: ",vezes_q_Aparece )
            print("Vetor criado", vetor1)  
            print ("====="*30)
            print ("O(s) valor(es) mais comun(uns) é(são): ", res_Mais_Comum, "e aparece(m) ", maisComum, "vezes")
            print("O(s) segundo(s) valor(es) mais comum(uns) é(são): ", res_Segu_Mais_Comum, "e aparece(m) ", maisComum2, "vezes")    
            
        else:
            print ("Programa finalizado com sucesso.")


    

main1()
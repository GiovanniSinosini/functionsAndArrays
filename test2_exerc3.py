"""
criar um vetor aleatório e apresentar o segundo mais comum.
"""

import test2_functions as f

  
def main():

    res_Mais_Comum =[]
    res_Segu_Mais_Comum =[]
    vezes_q_Aparece = []

    start = "yes"
    while start == "yes":
        start = input("Deseja executar o programa ? (yes/no) ")
        vetor1 = f.gerar_vetor(200, 1, 10, "yes")  # criar vetor aleatório com função
        maisComum = 0 # variáveis dentro do ciclo para possibilitar consultas seguidas
        maisComum2 = 0
            
        res_Mais_Comum.clear()    # comando para limpar vetores para várias consultas seguidas
        res_Segu_Mais_Comum.clear()
        vezes_q_Aparece .clear()
        
        if start == "yes":
            
            for x in range (len(vetor1)):   # ciclo para criar um vetor com a contagem de cada elemento
                vezesQUEapareceVARI = f.contaOccorencias(vetor1[x], vetor1)
                vezes_q_Aparece.append(vezesQUEapareceVARI) 
            
                if vezesQUEapareceVARI >= maisComum:  # primeira condicional para descobrir o que mais repete
                    maisComum = vezesQUEapareceVARI
                
                elif vezesQUEapareceVARI > maisComum2: # segundo condicional para descobrir o segundo que mais repete
                    maisComum2 = vezesQUEapareceVARI

            for x in range (len(vetor1)):  # comparar os dois vetores e correlacionar o vetor da contagem repetida com o vetor gerado, pois os dois possuem o mesmo índice
                if maisComum == vezes_q_Aparece[x] and vetor1[x] not in res_Mais_Comum:
                    res_Mais_Comum.append(vetor1[x])
                elif maisComum2 == vezes_q_Aparece[x] and vetor1[x] not in res_Segu_Mais_Comum:
                    res_Segu_Mais_Comum.append(vetor1[x])
                     
            print ("Resultado da pesquisa de numeros repetidos por elemento: ", vezes_q_Aparece)
            print ("Vetor criado aleatoriamente: ", vetor1)
            print ("="*60)
            print ("O(s) valor(es) mais comun(uns) é(são): ", res_Mais_Comum, "e aparece(m) ", maisComum, "vezes")
            print("O(s) segundo(s) valor(es) mais comum(uns) é(são): ", res_Segu_Mais_Comum, "e aparece(m) ", maisComum2, "vezes")    
            
        else:
            print ("Programa finalizado com sucesso.")


main()
import test2_functions as f


def main():

    start = "yes"
    while start == "yes":
        start = input("Deseja iniciar o programa? (yes/no) ")
        
        vetor1 = []
        vResultado_repeticao = []
        vModa = []
        maisComum = 0


        if start == "yes":
            vetor1 = f.gerar_vetor(100, 1, 20, "yes")

            for x in range (len(vetor1)):           # for para criar vetor de ocorrências - analisa cada elemento do vetor
                vezesQUEapareceVAR = f.contaOccorencias(vetor1[x], vetor1)
                vResultado_repeticao.append(vezesQUEapareceVAR)

                if vezesQUEapareceVAR >= maisComum:   # condicional para descobrir o mais comum
                    maisComum = vezesQUEapareceVAR
            
            for x in range (len(vetor1)): # for para correlacionar os vetores de ocorrência e o vetor1 e adicionar no vModa
 
                if maisComum == vResultado_repeticao[x] and vetor1[x] not in vModa:
                    vModa.append(vetor1[x])


            print ("Vetor criado aleatoriamente ", vetor1)
            print ("A moda desse vetor é(são): ", vModa)



                








        

        else:
            print ("Programa finalizado com sucesso.")














main()
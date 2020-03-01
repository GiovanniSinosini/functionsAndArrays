"""
Gerar 2 vetores aleatórios, depois criar um terceiro vetor com elementos não repetidos dos 2 vetores anterioes
"""

import test2_functions as f

def main():

    start = "yes"

    while start == "yes":
        start = input("Deseja iniciar o programa? (yes/no): ")

        if start =="yes":
            while True:
                tamanho = input("Digite o tamanho do vetor que deseja: ")
                inicio = input("Digite o valor MÍNIMO de um elemento:")
                fim = input("Digite o valor MÁXIMO de um elemento:")
                aleatório = input("Deseja criar o vetor automaticamente? (yes/no) ")

                if tamanho.isnumeric() and inicio.isnumeric() and fim.isnumeric():
                    tamanho = int(tamanho)
                    inicio = int(inicio)
                    fim = int(fim)
                    break   
                else:
                    print ("Input ERROR. Trya again.")
            vetor1 = f.gerar_vetor(tamanho,inicio,fim,aleatório)
            vetor2 = f.gerar_vetor(tamanho,inicio,fim,aleatório)
            novo_vetor = []
            

            for x in range (len(vetor1)):
                if not f.eRepetido(vetor1[x],novo_vetor):
                    novo_vetor.append(vetor1[x])
            for x in range (len(vetor2)):
                if not f.eRepetido(vetor2[x], novo_vetor):
                    novo_vetor.append(vetor2[x])

            print (sorted(vetor1))
            print (sorted(vetor2))
            print ("Elementos não repetidos dos vetores anteriores", sorted(novo_vetor))
            




        else:
            print("Program sucessfully completed.")
            








main()
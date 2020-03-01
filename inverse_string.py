import test2_functions as f
def main():

    start = "yes"
    while start == "yes":
        
        resultado = ""
        start = input("Deseja iniciar o programa? (yes/no) ")
        
        if start == "yes":
            string = input("Digite a string que deseja imprimir inversamente: ")

            resultado = f.inverse_string(string)
            

            print (resultado)


        else:
            print("Programa finalizado com sucesso.")










main()
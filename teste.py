import random as r

def main():


    vetor1 = [1,1,1,1,1]
    vetor2 = []
    res_vetor1=[]
    count = 0

    res_vetor1.append(vetor1)

    
    while count < 100:

        if vetor1 not in res_vetor1:
            res_vetor1.append(vetor1)
            count += 1

    print(res_vetor1)

 

main()
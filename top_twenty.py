def main():

    v = []

    for x in range (1, 21):
        while True:
            n = int(input("Enter position number %d: " %(x)))
            if (n >= 1 and n <= 10): 
                break
            else: 
                print ("Enter a number from 1 to 10. Try again.")
        v.append (n)
    
    print (v)

    print ("")
    loc = int(input("Enter the number you want to find: "))
    print ("")

    for c in range (0, 20):
        if v[c] == loc:
            print("This number was entered at postion:  %d" %(c))
        else:
            
    

















main()
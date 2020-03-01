def main():
    highest = 0
    v = []
    for x in range (0, 10):
        v.append (int(input(f'Enter {x+1} number: ')))
        if v [x] > highest:
            highest = v [x]
            position = x 
    
    print (v)
 
    print ("The largest valuer is %d inserted at position %d ." %(highest, position) )

    
    













main()
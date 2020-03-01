

def main():

    string = "Giovanni Carvalho Sinosini"
    a = "i"
    b = "a"
    out = ""

    print (string)

    #string = string.replace("i", "a")

    for x in range (len(string)):
        if string[x] == a:
            out += b
        else:
            out += string[x]

    print (out)


    for x in range (len(string)):
        c = "io"
        d = "uu"
        out2 = ""
        if string[x:x + len(c)] == c:
            out2 += c
        else:
            out2 += string[x]

    print (out2)      






main()
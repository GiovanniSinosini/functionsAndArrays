def main():

    v = []

    totalPares = 100
    n = 0
    while totalPares > 0:
        if n % 2 == 0:
            v.append(n)
            totalPares -= 1
        n += 1

    print(v)


main()

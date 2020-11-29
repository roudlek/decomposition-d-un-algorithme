print("entrer un nombre entier positif :")
nbr = int(input())

Q = nbr // 10
R = nbr % 10
print("le chiffre des unites est:", R)

if Q >= 0 :
    nbr = Q
    Q = nbr // 10
    R = nbr % 10
    print("le chiffre des dizaines est:", R)

    if Q >= 0 :
        nbr = Q
        Q = nbr // 10
        R = nbr % 10
        print("le chiffre des centaines est:", R)

        if Q >= 0 :
            nbr = Q
            Q = nbr // 10
            R = nbr % 10
            print("le chiffre des milliers est:", R)
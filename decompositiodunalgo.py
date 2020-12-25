while True:      # tanque ca est vrai :
    print("veuillez entrer un nombre entier positif entre [1;9999] :")
    nbr = int(input())                  # int pour entrer un nombre entier positif

    if nbr > 0 and nbr <10 :
        Q = nbr // 10
        R = nbr % 10
        print("le chiffre des unites est:", R)
        print("Fin de programme")
        break

    elif nbr > 9 and nbr <100 :
        Q = nbr // 10
        R = nbr % 10
        print("le chiffre des unites est:", R)
        nbr = Q
        Q = nbr // 10
        R = nbr % 10
        print("le chiffre des dizaines est:", R)
        print("Fin de programme")
        break

    elif nbr > 99 and nbr <1000 :
        Q = nbr // 10
        R = nbr % 10
        print("le chiffre des unites est:", R)
        nbr = Q
        Q = nbr // 10
        R = nbr % 10
        print("le chiffre des dizaines est:", R)
        nbr = Q
        Q = nbr // 10
        R = nbr % 10
        print("le chiffre des centaines est:", R)
        print("Fin de programme")
        break

    elif nbr > 999 and nbr <10000 :
        Q = nbr // 10
        R = nbr % 10
        print("le chiffre des unites est:", R)
        nbr = Q
        Q = nbr // 10
        R = nbr % 10
        print("le chiffre des dizaines est:", R)
        nbr = Q
        Q = nbr // 10
        R = nbr % 10
        print("le chiffre des centaines est:", R)
        nbr = Q
        Q = nbr // 10
        R = nbr % 10
        print("le chiffre des milliers est:", R)
        print("Fin de programme")
        break

    else:
        continue

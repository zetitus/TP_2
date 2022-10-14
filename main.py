
import random
restart = True


nb_essais = 1

Choix_1 = int(input("Choisi la borne minimale du jeux "))
Choix_2 = int(input("Choisi la borne maximale du jeux "))
nombre = random.randint(Choix_1, Choix_2)



while restart:


    user_that_guess = int(input("Ecriver un nombre entre la borne minimale et maximale"))
    if user_that_guess > nombre:
        print("Le chiffre est plus bas")
        nb_essais +=1

    elif user_that_guess < nombre:
        print("Le chiffre est plus gros")
        nb_essais +=1


    elif user_that_guess == nombre:
        print("Bravo vous l'avez trouvé ")
        print("Vous avez réussi en : " , nb_essais ,"essais" )


        finish = int(input("Voules vous recommencer? apuyez 1 pour OUI et 2 pour NON "))

        if finish == 1:
            nombre = random.randint(Choix_1, Choix_2)

        elif finish == 2:
            restart = False




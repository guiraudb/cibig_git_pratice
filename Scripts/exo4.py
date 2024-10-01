# 1. initialiser la liste
odds_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

# 2. récuperer la longueur de la liste odds

#3. declare la nouvelle liste vide events

#4. parcourir la liste odds avec arret à la fin de la liste

### recuperer la valeur de l'element de la list odds et le mettre dans une variable impair_value

### ajouter +1 à la valeur de la variable impair_value

### ajouter la valeur impair_value dans la nouvelle liste events

#5. afficher la liste events
#APPLICATION

#Présenter ou initialiser la list existante
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

#récupérer la longueur de la liste odds
# Déclarer ou Assigner
indice = 0
# 2 Récuperer la taille de notre liste avec la fonction len(list) et on stock la valeur retournee dans la variable lenght_animal_list
#3- parcourir la liste avec while et la variable indice
length_odds = len(odds)
while indice < length_odds :
    print(f"Mon indice est : {indice}")
    print(f"Mon element lu est : {odds[indice]}\n")

    # à la fin de chaque boucle, on ajoute 1 à indice
    indice = indice + 1

    print("fin de la boucle")



    # ON PEUT EGALEMENT UTILISER FOR !/usr/bin/env python3

    # Créer la variable animal_list de type liste
    # et assigner  la liste avec 4 valeurs
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

    ## observer les indices et les elements de la liste
    # print(list(enumerate(odds_list)))

    # parcourir les elements de la liste en utilisant la boucle for
    ### en recuperant les indices et les elements avec enumerate
    for indice, odds in enumerate(odds):
        print(f"indice : {indice}, element : {odds}")

    # Utiliser la boucle "for"
    # Créer une variable animal_list et assigner la liste avec 4 valeurs
    odds_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    # observer les indices et les éléments de la liste
    # print(list(enumérate(animal_list)))
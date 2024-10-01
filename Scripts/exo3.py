#Objectif de ce script est d'afficher le contenu de la liste en utilisant le préfixze While
from operator import length_hint, lshift

#Given the following list: animal_list = ['cow', 'mouse', 'yeast', 'bacteria']
#Nous voulons parcourir la liste avec une condition

#On va créer la liste et assigner des valeurs à cette liste

#Définir "animal_list"
animal_list = ['cow', 'mouse', 'yeast', 'bacteria']
# 1- Créer une variable indice qui va être assignée à 0
indice = 0
# 2 Récuperer la taille de notre liste avec la fonction len(list) et on stock la valeur retournee dans la variable lenght_animal_list
#3- parcourir la liste avec while et la variable indice
length_animal_list = len(animal_list)
while indice < length_animal_list :
    print(f"Mon indice est : {indice}")
    print(f"Mon element lu est : {animal_list[indice]}\n")

#à la fin de chaque boucle, on ajoute 1 à indice
    indice = indice + 1

print("fin de la boucle)

#ON PEUT EGALEMENT UTILISER FOR !/usr/bin/env python3

# Créer la variable animal_list de type liste
# et assigner  la liste avec 4 valeurs
animal_list = ['cow', 'mouse', 'yeast', 'bacteria', "snake"]

## observer les indices et les elements de la liste
#print(list(enumerate(animal_list)))

# parcourir les elements de la liste en utilisant la boucle for
### en recuperant les indices et les elements avec enumerate
for indice, animal in enumerate(animal_list):
    print(f"indice : {indice}, element : {animal}")

#Utiliser la boucle "for"
#Créer une variable animal_list et assigner la liste avec 4 valeurs
animal_list = ['cow', 'mouse', 'yeast', 'bacteria']
# observer les indices et les éléments de la liste
#print(list(enumérate(animal_list)))








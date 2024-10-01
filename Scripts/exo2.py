# On récupère les 3 notes de l'utilisateur pour faire la moyenne
grade1 = input("Enter first grade: ")
grade2 = input("Enter second grade: ")
grade3 = input("Enter third grade: ")
#type de variable (la variable est de type str donc nous devons la convertir en float qui prend en compte les valeurs décimales et entierères)
print(type(grade1))
#calculer la somme des 3 notes
somme = float(grade1) + float(grade2) + float(grade3)

#Diviser par 3 pour avoir la moyenne
moyenne = somme/3
#Afficher la moyenne
print(f"ceci est la moyenne {moyenne:.2f}")
#
#Emettre des conditions:Je marque "very good" si la moyenne est supérieure ou égale à 16
#Je marque "good" si la moyenne est supérieure ou égale à 14
#Je marque "faired good" si la moyenne est supérieure ou égale à 12
#Je marque "passable" si la moyenne est supérieure ou égale à 10
# je marque "failed" si la moyenne est inférieure à 10
# Je marque nothing pour le reste

#if moyenne >= 16:
    grade = "very good"
#elif moyenne >= 14:
    grade = "good"
#elif moyenne >= 12:
    grade = "faired good"
#elif moyenne >= 10:
    grade = "passable"
#elif moyenne < 10:
    grade = "failed"
#else:
    grade = "nothing"
#print (grade)
# Si la moyenne est inférieur à 10 indique 'failed'
#if moyenne < 10:
# print("failed")
# Si la moyenne est supérieure ou égale 10 et inférieure à 12 indique 'passable'
#elif moyenne >= 10 and moyenne < 12:
#   print("passable")
# Si la moyenne est supérieure ou égale 12 et inférieure à 14 indique 'fairy good'
#   print("fairy good")
#elif moyenne >= 12 and moyenne < 14:
# Si la moyenne est supérieure ou égale 14 et inférieure à 16 indique 'good'
#print("fairy good")
#elif moyenne >= 14 and moyenne < 16:
#    print("good")
# Si la moyenne est supérieure ou égale 16 et inférieure à 20 indique 'very good'
#elif moyenne >= 16 and moyenne <= 20:
    print("very good")
#else :
#   grade = "retry"

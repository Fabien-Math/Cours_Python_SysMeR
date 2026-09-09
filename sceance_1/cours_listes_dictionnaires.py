# Creation d'une liste
nombres = [10, 20, 30, 40, 50, 60]
# nombres = [10, 20, 30, "eheh"]
print("Liste :", nombres)
input()









# Acceder aux elements
print("Premier element :", nombres[0])
print("Deuxieme element :", nombres[1])
print("Dernier element :", nombres[-1])
print("Trois premiers elements :", nombres[:3])
print("Trois derniers elements :", nombres[3:])
print("Deux elements entre l'indice 1 et 2 :", nombres[1:3])
input()









# Modifier un element
print("Avant modification :", nombres)
nombres[1] = 99
print("Apres modification :", nombres)
input()









# Ajouter un element
print("Avant ajout :", nombres)
nombres.append(50)
print("Apres ajout :", nombres)
input()









# Taille de la liste
print("Nombre d'elements :", len(nombres))
input()









# Parcourir la liste
print("Parcours de la liste :")
for nombre in nombres:
    print(nombre)
input()









# Parcourir avec les indices
print("Indices et valeurs :")
for i in range(len(nombres)):
    print("Indice", i, ":", nombres[i])
input()









# Supprimer un element
print("Avant suppression :", nombres)
nombres.remove(30)
print("Apres suppression :", nombres)
input()










# QUESTION
nombres_bis = nombres
print("Avant modification de nombres:", nombres)
print("Avant modification de nombres_bis:", nombres_bis)

nombres_bis[1] = 17

print("\nApres modification de nombres_bis:", nombres_bis)
input()
print("Apres modification de nombres:", nombres)


























































print("La liste nombres a change, pourquoi ?")
exit()


































# Creation d'un dictionnaire
personne = {
    "nom": "alice",
    "age": 20,
    "ville": "paris"
}

print("\nDictionnaire :", personne)
input()









# Acceder aux valeurs
print("Nom :", personne["nom"])
print("Age :", personne["age"])
print("Ville :", personne["ville"])
input()









# Modifier une valeur
print("Avant modification :", personne)

personne["age"] = 21

print("Apres modification :", personne)
input()









# Ajouter une nouvelle valeur
print("Avant ajout :", personne)

personne["metier"] = "developpeur"

print("Apres ajout :", personne)
input()









# Taille du dictionnaire
print("Nombre d'elements :", len(personne))
input()









# Verifier si une cle existe
print("nom" in personne)
print("email" in personne)
input()









# Obtenir une valeur avec get()
print("Nom :", personne.get("nom"))
print("Email :", personne.get("email"))
input()









# Parcourir les cles
print("Cles du dictionnaire :")

for cle in personne:
    print(cle)

input()









# Parcourir les valeurs
print("Valeurs du dictionnaire :")

for valeur in personne.values():
    print(valeur)

input()









# Parcourir les cles et les valeurs
print("Cles et valeurs :")

for cle, valeur in personne.items():
    print(cle, ":", valeur)

input()









# Supprimer un element
print("Avant suppression :", personne)

del personne["ville"]

print("Apres suppression :", personne)
input()









# Supprimer avec pop()
personne["ville"] = "paris"

print("Avant pop() :", personne)

age = personne.pop("age")

print("Age supprime :", age)
print("Apres pop() :", personne)
input()









# Vider le dictionnaire
personne.clear()

print("Dictionnaire apres clear() :", personne)
input()







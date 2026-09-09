import random


produits = ["ordinateur", "souris", "clavier", "casque"]
prix = [800, 30, 50, 70]
panier = []


def afficher_produits():
    for i in range(len(produits)):
        print(produits[i], ":", prix[i], "euros")


def ajouter_au_panier():
    produit = input("Quel produit veux-tu acheter ? ")

    if produit in produits:
        panier.append(produit)
        print(produit, "ajoute au panier")
    else:
        print("Produit inconnu")


def calculer_total():
    total = 0

    for produit in panier:
        index = produits.index(produit)
        total += prix[index]

    return total


def appliquer_reduction(total):
    reduction = random.randint(0, 20)
    total_final = total - (total * reduction / 100)

    print("Reduction :", reduction, "%")
    print("Total apres reduction :", total_final, "euros")


print("========== MAGASIN ==========")

while True:
    print("\nProduits disponibles :")
    afficher_produits()

    choix = input("\nProduit a acheter ou 'stop' : ")

    if choix == "stop":
        break

    if choix in produits:
        panier.append(choix)
        print("Produit ajoute au panier")
    else:
        print("Produit inconnu")


print("\n========== RESUME ==========")

print("Nombre de produits :", len(panier))

print("\nPanier :")

for produit in panier:
    print("-", produit)

total = calculer_total()

print("\nTotal :", total, "euros")

appliquer_reduction(total)

print("\nMerci pour votre achat !")

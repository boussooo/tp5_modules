class Produit:
    def __init__(self, nom, prix, description):
        self.nom = nom
        self.prix = prix
        self.description = description


    def afficher_infos(self):
        print("Nom :", self.nom)
        print("Prix :", self.prix)
        print("Description :", self.description)


    def modifier_prix(self, nouveau_prix):
        self.prix = nouveau_prix

    def mettre_a_jour_description(self, nouvelle_description):
        self.description = nouvelle_description
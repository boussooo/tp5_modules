class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    def se_deplacer(self):
        print(f"{self.nom} se déplace.")

class Chien(Animal):
    def aboyer(self):
        print(f"{self.nom} aboie.")

rex = Chien("Rex", 5)
rex.se_deplacer()
rex.aboyer()


class Employe:
    def __init__(self, nom):
        self.nom = nom
    def travailler(self):
        print(f"{self.nom} travaille.")

class Instructeur:
    def __init__(self, nom):
        self.nom = nom
    def enseigner(self):
        print(f"{self.nom} enseigne.")

class Formateur(Employe, Instructeur):
    def __init__(self, nom):
        Employe.__init__(self, nom)
        Instructeur.__init__(self, nom)

samba = Formateur("Samba")
samba.travailler()
samba.enseigner()

from Produit import Produit

p1 = Produit("Ordinateur", 500000, "PC portable gaming")

print("=== AVANT MODIFICATION ===")
p1.afficher_infos()

p1.modifier_prix(450000)
p1.mettre_a_jour_description("PC portable gaming performant et léger")

print("\n=== APRÈS MODIFICATION ===")
p1.afficher_infos()
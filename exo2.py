# Demandez à l'utilisateur d'entrer le niveau de charge actuel de la batterie
niveau_charge = int(input("Veuillez entrer le niveau de charge actuel de votre batterie:"))
# Vérifiez si le niveau de charge est valide
condition = (0 <= niveau_charge <= 100 )
if condition:
    niveau_charge_arrondi = round(niveau_charge, -1) 
    nombre_barre_pleine = int(niveau_charge // 10)
    nombre_total_barre = 10
    barre_pleine = "❚"
    graphique = ""
else: 
    niveau_charge = int(input("Veuillez entrer un niveau de charge valide:"))

for i in range(nombre_total_barre):
    if i < nombre_barre_pleine:
        graphique += "❚"
    else:
        graphique += " "
print([graphique])

# Arrondir le pourcentage à la dizaine la plus proche

# Calculer le nombre de barres

# Afficher la représentation graphique de la charge de la batterie

# Exemple d'utilisation :
# Si l'utilisateur entre 76, la sortie sera :
# [❚❚❚❚❚❚❚❚     ]
# 76%
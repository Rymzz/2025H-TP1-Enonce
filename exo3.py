import math

a = int(input("Entrez a, non nul: "))
b = int(input("Entrez b: "))
c = int(input("Entrez c: "))

delta = (b**2 - 4*(a*c))
#Définitions des cas possibles
naPasDeSolution = delta < 0
aUneSeuleSolution = delta == 0
aDeuxSolutions = delta > 0

naPasDeSolution = delta < 0
if naPasDeSolution:
    print("Aucune racine")


else:
     aUneSeuleSolution = delta == 0
     if aUneSeuleSolution:
        x1 = float(-b/(2*a))
        print("Une seule racine", )
        print(x1)
        
     else: aDeuxSolutions = delta > 0
     if aDeuxSolutions:
             x1 = float((-b-(delta)**0.5)/(2*a))
             x2 = float((-b+(delta)**0.5)/(2*a))
             print("Deux racines")
             print(x1, x2)
             

# Exemple d'utilisation:
# Pour a = 1, b = -3, c = 2
# delta = 1
# Deux racines
# x1 = 1.0, x2 = 2.0

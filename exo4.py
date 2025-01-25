secondes = int(input("Entrez un nombre de secondes : "))

# Ne pas modifier.
annees = semaines = jours = heures = minutes = 0

# TODO: Assigner à la variable "annees" le nombre d'années
nb_annees = secondes // (24*60*60*365)
reste = secondes % (24*60*60*365)
# TODO: Assigner à la variable "semaines" le nombre de semaines restantes
nb_semaines = reste // (7*24*60*60)
reste %= (7*24*60*60)
# TODO: Assigner à la variable "jours" le nombre de jours restants
nb_jours = reste // (60*60*24)
reste %= (60*60*24)
# TODO: Assigner à la variable "heures" le nombre d'heures restantes
nb_heures = reste // (60*60)
reste %= (60*60)
# TODO: Assigner à la variable "minutes" le nombre de minutes restantes
nb_minutes = reste // (60)
reste %= (60)
# TODO: Assigner à la variable "secondes" le nombre de secondes restantes
nb_secondes = reste

condition1 = nb_annees > 0
condition2 = nb_semaines > 0
condition3 = nb_jours > 0
condition4 = nb_heures > 0
condition5 = nb_minutes > 0
condition6 = nb_secondes > 0

texte = "Dans " + str(secondes) + " secondes, il y a "
if condition1:
    texte += str(nb_annees) + " années,"
if condition2:
    texte += str(nb_semaines) + " semaines,"
if condition3:
    texte += str(nb_jours) + " jours,"
if condition4:
    texte += str(nb_heures) + " heures,"
if condition5:
    texte += str(nb_minutes) + " minutes et"
if condition6:
    texte += str(nb_secondes) + " secondes."

print(texte)

# TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes

# Exemple: print(annees, semaines, jours, heures, minutes, secondes)

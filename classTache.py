# --- Implémenttion de la classe Tache ---
import os

class Tache:
    def __init__(self, nom="", taille=0, strategie="", temps=0):
        self.nom = nom
        self.taille = taille
        self.temps = temps
        self.strategie = strategie

    # Méthode pour remplir les informations de la tache
    def remplir(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("Remplir les informations de la Tache\n")
        self.nom = input("Nom de la tache: ")
        self.taille = int(input("Taille en octet: "))
        self.temps = int(input("Durée d'execution (en secondes): "))
        strat = input("Strategie utilisée [1:premier, 2:petit, 3:grand]: ")
        if strat == "1":
            self.strategie = "premier"
        elif strat == "2":
            self.strategie = "petit"
        elif strat == "3":
            self.strategie = "grand"
        else:
            print("Stratégie inconnue, utilisation de 'premier' par défaut.")
            self.strategie = "premier"
        print(f"\n** Tache créée avec succès **\nNom: {self.nom} \nTaille: {self.taille} \nDurée: {self.temps} \nStrategie: {self.strategie}")
        input("\nAppuyez sur Entrée pour continuer...")

    def __str__(self):
        return f"Nom: {self.nom} Taille: {self.taille} Durée: {self.temps} Strategie: {self.strategie}"
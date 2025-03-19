# --- Implémenttion de la classe Block ---
class Block:
    def __init__(self, adresse=0, taille=0, libre=True, tache=None):
        self.adresse = adresse
        self.taille = taille
        self.libre = libre
        self.tache = tache

    def __str__(self):
        return f"Adresse: {self.adresse} Taille: {self.taille} Libre: {self.libre} Tâche: {self.tache}"
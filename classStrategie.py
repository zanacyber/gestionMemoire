# --- Implémenttion de la classe des Algorithmes de placement utilisés ---
class Strategie:
    def __init__(self, memoire):
        self.memoire = memoire

    # Premier emplacement suffisant
    def premier_emplacement_suffisant(self, taille):
        for block in self.memoire:
            if block.libre and block.taille >= taille:
                return block
        return None

    # Plus petit emplacement suffisant
    def plus_petit_emplacement_suffisant(self, taille):
        meilleur_block = None
        for block in self.memoire:
            if block.libre and block.taille >= taille:
                if meilleur_block is None or block.taille < meilleur_block.taille:
                    meilleur_block = block
        return meilleur_block

    # Plus grand emplacement suffisant
    def plus_grand_emplacement_suffisant(self, taille):
        meilleur_block = None
        for block in self.memoire:
            if block.libre and block.taille >= taille:
                if meilleur_block is None or block.taille > meilleur_block.taille:
                    meilleur_block = block
        return meilleur_block
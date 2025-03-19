# pip install rich
# sujet 5
# group 17
# 10 + 98 + 29 + 32 + 56 = 225 lignes de code

from classTache import Tache
from classGestion import GestionMemoire
import os

# --- Fonction du menu ---
def afficher_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print("\n--- Menu de Gestion de Mémoire ---")
    print("1. Ajouter une tache")
    print("2. Consulter l'état de la mémoire")
    print("3. Libérer une tache")
    print("0. Quitter")

def ajouter_tache(gestion_memoire):
    nouvelle_tache = Tache()
    nouvelle_tache.remplir()
    resultat = gestion_memoire.allouer(nouvelle_tache)
    print(resultat)

def liberer_tache(gestion_memoire):
    nom_tache = input("Entrez le nom de la tâche à libérer: ")
    resultat = gestion_memoire.liberer(nom_tache)
    print(resultat)

# --- Fonction principale ---
def main():
    taille_totale = 4096
    gestion_memoire = GestionMemoire(taille_totale)

    try:
        while True:
            afficher_menu()
            choix = input("Faites un choix [0-3]: ")
            if choix == "1":
                ajouter_tache(gestion_memoire)
            elif choix == "2":
                gestion_memoire.afficherMemoire()
            elif choix == "3":
                liberer_tache(gestion_memoire)
            elif choix == "0":
                print("Au revoir!")
                break
            else:
                print("Choix invalide, veuillez réessayer.")
    except KeyboardInterrupt:
        print("\nInterruption du programme.")
    finally:
        gestion_memoire.stopper()

if __name__ == "__main__":
    main()
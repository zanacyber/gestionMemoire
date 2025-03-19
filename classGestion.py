# --- Classe Gestion Memoire ---
import random
import os
import time
import threading
from rich.table import Table
from rich.console import Console
from classStrategie import Strategie
from classBlock import Block


class GestionMemoire:
    def __init__(self, tailleMemoire):
        self.tailleMemoire = tailleMemoire
        self.memoire = []
        self.creerBlock()
        self.algo = Strategie(self.memoire)

        self.verrou = threading.Lock() # Création d'un verrou pour gérer l'accès à des ressources partagées
        self.stop = False # Controler l'arret du thread
        # Création d'un thread qui exécute la méthode 'decremente_temps_background' en arrière-plan
        self.compteur = threading.Thread(target=self.decrementeTemps, daemon=True)
        self.compteur.start() # Démarrage du thread

    def creerBlock(self):
        adresse = 0
        tailleRestante = self.tailleMemoire
        while(tailleRestante > 0):
            tailleBlock = random.randint(100, 500)
            if(tailleBlock <= tailleRestante):
                self.memoire.append(Block(adresse, tailleBlock, True, None))
                adresse += tailleBlock
                tailleRestante -= tailleBlock
            else:
                self.memoire.append(Block(adresse, tailleRestante, True, None))
                tailleRestante = 0

    def afficherMemoire(self):
        os.system("cls" if os.name == "nt" else "clear")
        table = Table(title="État de la mémoire", show_header=True, header_style="bold magenta")
        table.add_column("Adresse", justify="center")
        table.add_column("Taille", justify="center")
        table.add_column("Statut", justify="center")
        table.add_column("Tâche", justify="center")

        for bloc in self.memoire:
            tach = bloc.tache if bloc.tache else "None"
            statut = "[green]Libre[/green]" if bloc.libre else "[red]Occupé[/red]"
            table.add_row(str(bloc.adresse), str(bloc.taille), statut, str(tach))
        Console().print(table)
        
        actualiser = input("\n[Entrée] = Actualiser la table des taches, [0] = Voir menu\nChoix: ")
        if actualiser == "":
            self.afficherMemoire()

    def liberer(self, nom_tache):
        liber = False

        for bloc in self.memoire:
            if bloc.tache and bloc.tache.nom == nom_tache:
                bloc.libre = True
                bloc.tache = None
                print(f"\nLa tâche '{nom_tache}' a été libérée avec succès.")
                liber = True
        if not liber:
            print(f"\nErreur: La tâche '{nom_tache}' n'a pas été trouvée dans la mémoire.")
        return liber

    def allouer(self, tache):
        with self.verrou:
            if tache.strategie == "premier":
                bloc = self.algo.premier_emplacement_suffisant(tache.taille)
            elif tache.strategie == "petit":
                bloc = self.algo.plus_petit_emplacement_suffisant(tache.taille)
            elif tache.strategie == "grand":
                bloc = self.algo.plus_grand_emplacement_suffisant(tache.taille)
            else:
                return "\nStratégie non reconnue"

            if bloc is None:
                return "\nPas de place disponible"
            else:
                bloc.libre = False
                bloc.tache = tache
                return "\nTâche en cours d'exécution"

    def decrementeTemps(self):
        while not self.stop:
            time.sleep(1)
            with self.verrou:
                for bloc in self.memoire:
                    if not bloc.libre and bloc.tache:
                        bloc.tache.temps -= 1
                        if bloc.tache.temps <= 0:
                            self.liberer(bloc.tache.nom)

    def stopper(self):
        self.stop = True
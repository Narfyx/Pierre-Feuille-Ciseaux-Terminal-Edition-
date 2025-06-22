import time, random
from InquirerPy import inquirer
"""Pierre-Feuille-Ciseaux
🧱 Structure (orientée objet) :
    Une classe Player (nom, points de vie, méthode d’attaque)

    Une classe Game qui gère le déroulé du duel (boucle de jeu)

⚔️ Règles :
    Chaque joueur commence avec 5 points de vie.

    Chacun choisi entre pierre, feuille ou ciseaux

    Si égalité : pas de dégâts.

    Le premier à tomber à 0 PV perd.

🔧 Ce que tu travailles :
    Classes, attributs, méthodes

    Constructeurs __init__

    Encapsulation soft

    Logique de boucle de jeu

    L'affichage propre en ligne de commande

🚫 Et toujours : pas d’IA, pas de triche.
    C’est toi et Python, version dojo. 🥋

"""
# Une classe Player (nom, points de vie, méthode d’attaque)
class Player():
    def __init__(self, name) -> None:
        self.name = name
        self.pv = 5
        self.attack_method = ["Pierre", "Feuille", "Ciseaux"]

# Une classe Game qui gère le déroulé du duel (boucle de jeu, tour par tour)
class Game():
    def __init__(self) -> None:
        self.boucle = 10

        

def menu(player):
    
    choice = inquirer.select(
    message = f"choisissez entre : {player.attack_method}",
    choices = player.attack_method
    ).execute()

    index = player.attack_method.index(choice)
    
    return index


def start():
    print("""This is Pierre-Feuille-Ciseaux
    Rules:
        - Chaque joueur commence avec 5 points de vie.

        - Chacun choisi entre pierre, feuille ou ciseaux

        - Si égalité : pas de dégâts.

        - Le premier à tomber à 0 PV perd.
        
    =====================================================
    
    Le Match commence dans 5 secondes.
          """)
    time.sleep(5)
    
    playerHumain = Player(name='toto')
    playerBot = Player(name='bot')
    
    Lancement = Game()
    
    while Lancement.boucle > 0:
        
        print(f"Match restant {Lancement.boucle} : {playerHumain.name} vs {playerBot.name}")
        Lancement.boucle = Lancement.boucle - 1
        
        user_choice = menu(playerHumain)
        bot_choice = index = playerBot.attack_method.index(random.choice(playerBot.attack_method))


        
        if user_choice == 0 and bot_choice == 1:
            playerHumain.pv = playerHumain.pv - 1
        elif user_choice == 1 and bot_choice == 0:
            playerBot.pv = playerBot.pv - 1
        elif user_choice == 0 and bot_choice == 2:
            playerBot.pv = playerBot.pv - 1
        elif user_choice == 2 and bot_choice == 0:
            playerHumain.pv = playerHumain.pv - 1
        elif user_choice == 2 and bot_choice == 1:
            playerBot.pv = playerBot.pv - 1
        elif user_choice == 1 and bot_choice == 2:
            playerHumain.pv = playerHumain.pv - 1
        
        print(f"""
        ========================================
              Votre choix : {playerHumain.attack_method[user_choice]}, PV: {playerHumain.pv}
              Choix du bot : {playerBot.attack_method[bot_choice]}, PV: {playerBot.pv}
        ========================================
              """)        
        
        if playerHumain.pv <= 0 or playerBot.pv <= 0:
            if playerHumain.pv <= 0:
                print("Vous avez perdu")
            else:
                print("Vous avez gagné")
            exit()

if __name__ == "__main__":
    start()

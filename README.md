# 🥋 Pierre-Feuille-Ciseaux (Terminal Edition)

Un petit projet Python réalisé en une soirée, pour me remettre dans le bain après une pause d’un an sans pratiquer.

---

## 🎯 Objectif

Reprendre la main sur Python en codant un jeu simple mais structuré, en orienté objet, **sans aucune aide d’intelligence artificielle**. Le but : reprendre, me forcer à réfléchir par moi-même, et remettre les mains dans le cambouis avec un sujet ludique.

---

## ⚙️ Technologies

- Python 3.x
- [InquirerPy](https://github.com/kazhala/InquirerPy) pour une interface terminal agréable

---

## 🧠 Ce que j’ai travaillé

- Conception en **orienté objet**
- Création de classes (`Player`, `Game`)
- Boucle de jeu, logique conditionnelle
- Utilisation de `random` pour simuler un adversaire IA
- Utilisation de `time.sleep()` pour rendre le tout plus vivant
- Menu interactif dans le terminal

---

## 🕹️ Règles du jeu

- Chaque joueur (toi et le bot) commence avec 5 points de vie.
- À chaque tour, chacun choisit entre **Pierre**, **Feuille** ou **Ciseaux**.
- Les règles classiques s’appliquent :
  - Pierre bat Ciseaux
  - Ciseaux bat Feuille
  - Feuille bat Pierre
- Le perdant du duel perd 1 point de vie.
- Le premier à tomber à 0 PV perd la partie.

---

## 📦 Lancer le jeu

1. Installer les dépendances :
   ```bash
   pip install InquirerPy
   ```
2. Lancer le script :
   ```bash
   python pfc.py
   ```
  

---
title: "De l'éditeur de texte à l'éditeur de code"
description: "Un programme est un texte : la différence entre un traitement de texte, un éditeur de texte et un éditeur de code, ce qu'un éditeur de code ajoute (couleurs, complétion, terminal dans la même fenêtre) et les quatre zones de sa fenêtre."
tags:
  - bit
  - editor
  - computer
difficulty: beginner
duration: 8
requires: "0.6.0"
---

Un programme est un texte, et il existe des outils faits pour écrire ce texte-là. Vous saurez pourquoi un traitement de texte ne convient pas, ce qu'un éditeur de code ajoute à un éditeur de texte, et à quoi servent les quatre zones de sa fenêtre. C'est l'outil que vous installerez au lab suivant.

**Prérequis** : avoir écrit et lancé un premier script, comme `fiche.sh` dans le lab [Votre premier script, sur votre machine](https://byte-layers.com/fr/labs/first-script-lab).

# De l'éditeur de texte à l'éditeur de code

Pour écrire `fiche.sh`, vous avez ouvert l'éditeur de texte de votre système, tapé six lignes, enregistré, puis lancé le script dans le terminal. Ça marche, mais rien ne vous a aidé : ni pour taper, ni pour trouver une faute. Ce contenu présente l'outil que les développeurs utilisent à la place.

## Un traitement de texte n'est pas un éditeur de texte

Word ou LibreOffice Writer sont des **traitements de texte** : ils mettent en forme un document (gras, polices, marges) et enregistrent par défaut, à côté de vos mots, tout ce qu'il faut pour cette mise en forme. Un script enregistré ainsi n'est plus un texte que `bash` sait lire. Un traitement de texte remplace aussi les guillemets droits `"` par des guillemets typographiques, `« »` en français, que `bash` ne prend pas pour des guillemets.

Un **éditeur de texte** enregistre les caractères que vous tapez, rien de plus : c'est ce qu'on appelle du **texte brut**. Chaque système en a un : le Bloc-notes sous Windows, TextEdit sous macOS.

| Outil | Ce qu'il enregistre | Pour un programme |
|---|---|---|
| **Traitement de texte** (Word, Writer) | vos mots et leur mise en forme | ne convient pas |
| **Éditeur de texte** (Bloc-notes, TextEdit) | les caractères tapés, sans mise en forme | convient, sans aide |
| **Éditeur de code** | les caractères tapés, sans mise en forme | convient, et vous aide à écrire |

> ⚠️ **Si vous utilisez TextEdit**, il se comporte par défaut comme un traitement de texte : texte enrichi, guillemets typographiques, corrections automatiques. Le lab sur votre machine donne les réglages à faire, dans **TextEdit > Réglages**.

## Avec l'éditeur de texte du système : deux fenêtres, aucune aide

Reprenons `fiche.sh`, avec un guillemet oublié à la ligne 4. Dans le Bloc-notes, rien ne le montre.

```scene
lesson: assets/editor.scene.json
step: bloc-notes
```

Pour le lancer, il faut **changer de fenêtre**. `bash` exécute d'abord la ligne 3, qui affiche le nom de la machine, puis s'arrête. Son message, en anglais, dit qu'il a atteint la fin du fichier (*EOF*, *end of file*) en cherchant un guillemet de fin, et il cite la **ligne 5**, alors que la faute est à la ligne 4 : `bash` associe les guillemets dans l'ordre, celui du début de la ligne 5 ferme celui de la ligne 4, et le dernier reste seul. Selon la version de `bash`, une seconde ligne d'erreur peut citer la fin du fichier. Il ne reste qu'à relire chaque ligne, caractère par caractère.

## Avec un éditeur de code : une fenêtre, des couleurs

Un **éditeur de code** est un éditeur de texte fait pour les programmes. Il enregistre toujours du texte brut, mais il reconnaît le langage du fichier, ici celui de `bash`, à son nom et à sa première ligne, et il vous aide à l'écrire.

```scene
lesson: assets/editor.scene.json
step: editeur-de-code
```

Le terminal est **dans la même fenêtre**, et les **numéros de ligne** mènent tout droit à la ligne citée par `bash`. On ajoute le guillemet, on enregistre, on relance, sans changer de fenêtre.

Les **couleurs** distinguent les commandes, les textes entre guillemets et les commentaires : on parle de **coloration syntaxique**. Dans un vrai éditeur de code, le guillemet oublié se voit aussi à elles : les lignes qui suivent la ligne 4 changent de couleur, et `df -h ~` prend celle d'un texte entre guillemets. Le schéma, qui colore chaque ligne à part, ne le montre pas.

L'éditeur de code ajoute aussi ce que le schéma ne montre pas. Le tableau en donne l'essentiel.

| Ce qu'il ajoute | Ce que ça change |
|---|---|
| **Coloration syntaxique** | chaque sorte de mot a sa couleur ; une faute de frappe se voit |
| **Complétion** | il propose la fin d'un mot ou d'une commande pendant que vous tapez |
| **Numéros de ligne et erreurs soulignées** | pour beaucoup de langages, il souligne certaines fautes avant même qu'on lance le programme |
| **Terminal intégré** | un vrai terminal, dans la même fenêtre, ouvert sur le dossier où vous travaillez |

## Les quatre zones de la fenêtre

Un éditeur de code peut ouvrir un **dossier** entier, et pas seulement un fichier : tous les fichiers d'un programme sont sous la main. Dans VS Code, l'éditeur de code de ce parcours, la fenêtre se partage en quatre zones ; les autres éditeurs en ont de semblables.

| Zone | Où | À quoi elle sert |
|---|---|---|
| **Barre d'activité** | une colonne d'icônes, tout à gauche | choisir ce qu'affiche le panneau d'à côté : les fichiers, la recherche, d'autres outils |
| **Explorateur** | le panneau de gauche | voir les fichiers et sous-dossiers du dossier ouvert, rangés les uns dans les autres ; un clic en ouvre un |
| **Zone d'édition** | au centre | écrire dans le fichier ouvert, un onglet par fichier |
| **Terminal intégré** | en bas, quand on l'ouvre | lancer des commandes dans le dossier ouvert |

L'explorateur fait le même travail que l'explorateur de fichiers du système, limité au dossier ouvert. Le terminal intégré est un vrai terminal : sous macOS et Linux, il lance le même shell que le terminal du système ; sous Windows, on y choisit Git Bash, comme le montrera le lab.

## VS Code, l'éditeur de ce parcours

Il existe beaucoup d'éditeurs de code. Ce parcours utilise **Visual Studio Code**, qu'on abrège en **VS Code** : il est gratuit, il fonctionne sous Windows, macOS et Linux, et il est très répandu dans les entreprises. Vous l'installerez au lab suivant, pour corriger `fiche.sh` et lancer votre premier programme.

> 📖 [Visual Studio Code, documentation (en anglais)](https://code.visualstudio.com/docs) · [L'interface de VS Code (en anglais)](https://code.visualstudio.com/docs/getstarted/userinterface) · [Guide d'utilisation de TextEdit (Apple)](https://support.apple.com/fr-fr/guide/textedit/welcome/mac)

## Récap

- Un programme s'écrit en **texte brut** : un traitement de texte ajoute une mise en forme qui le rend illisible pour la machine.
- Un **éditeur de texte** enregistre ce que vous tapez, sans mise en forme ; un **éditeur de code** fait de même et vous aide : couleurs, numéros de ligne, complétion, terminal intégré, et pour beaucoup de langages des erreurs soulignées.
- La fenêtre de VS Code a quatre zones : la barre d'activité, l'explorateur du dossier ouvert, la zone d'édition et le terminal intégré.
- **VS Code** est l'éditeur de code de ce parcours.

Reste une question : ce texte, bien écrit et sans faute, la machine ne le comprend pas tel quel. Qui le lui traduit ? C'est l'objet du contenu [Compilé ou interprété](https://byte-layers.com/fr/bits/compiled-or-interpreted).

Trois questions pour vérifier ce que vous avez retenu.

```quiz
title: "De l'éditeur de texte à l'éditeur de code"
tracksProgress: false
showNotice: false
questions:
  - prompt: "Pourquoi ne pas écrire un script dans un traitement de texte comme Word ?"
    answers:
      - "Parce qu'il enregistre aussi la mise en forme, et remplace souvent les guillemets droits par des guillemets typographiques"
      - "Parce qu'il est trop lent pour un fichier de quelques lignes"
      - "Parce qu'un script doit obligatoirement s'écrire dans le terminal"
    correct: 1
    explanation: "Un programme est du texte brut. Un traitement de texte ajoute la mise en forme au fichier, et ses guillemets typographiques ne sont pas ceux que bash attend."
  - prompt: "Qu'ajoute un éditeur de code à un éditeur de texte ?"
    answers:
      - "Il transforme le script en programme que le processeur exécute directement"
      - "Il aide à écrire : couleurs selon le langage, numéros de ligne, complétion, terminal dans la même fenêtre"
      - "Il enregistre le fichier avec sa mise en forme"
    correct: 2
    explanation: "Il enregistre le même texte brut qu'un éditeur de texte. Ce qu'il ajoute, c'est de l'aide pour écrire et lancer le programme."
  - prompt: "Dans la fenêtre d'un éditeur de code, à quoi sert l'explorateur ?"
    answers:
      - "À naviguer sur le web sans quitter l'éditeur"
      - "À lancer des commandes dans le dossier du projet"
      - "À voir les fichiers du dossier ouvert et à en ouvrir un d'un clic"
    correct: 3
    explanation: "L'explorateur montre les fichiers et sous-dossiers du dossier ouvert. Les commandes se lancent dans le terminal intégré."
```

```ack
J'ai compris
```

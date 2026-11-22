---
title: "De l'éditeur de texte à l'éditeur de code"
description: "Un programme est un texte : la différence entre un traitement de texte, un éditeur de texte et un éditeur de code, et les outils essentiels d'un IDE (explorateur, zone d'édition, terminal intégré, support du langage)."
tags:
  - bit
  - editor
  - computer
difficulty: beginner
duration: 10
requires: "0.8.0"
---

Un programme est un texte, et il existe des outils faits pour écrire ce texte-là. Vous saurez pourquoi un traitement de texte ne convient pas, ce qu'un éditeur de code ajoute à un éditeur de texte, et quels sont les outils essentiels d'un IDE.

**Prérequis** : savoir ce qu'est un script, un petit programme écrit dans un fichier texte, et qu'on le lance dans un terminal.

# De l'éditeur de texte à l'éditeur de code

Un script peut s'écrire dans n'importe quel outil qui enregistre du texte. Mais tous ne conviennent pas, et certains aident bien plus que d'autres : pour taper, pour trouver une faute, pour lancer le programme. Ce contenu présente l'outil que les développeurs utilisent.

## Trois outils, trois usages

Un script et un document ne s'écrivent pas avec le même outil. Voici trois outils, et le fichier que chacun enregistre.

```scene
lesson: assets/ide.scene.json
step: traitement
```

Un **éditeur de texte** enregistre les caractères tapés, rien de plus : du **texte brut**. Certains s'ouvrent dans le terminal (`nano`, `vi`), d'autres dans une fenêtre (le Bloc-notes sous Windows, gedit sous Linux). C'est assez pour un petit script.

Un **traitement de texte** (Word, LibreOffice Writer) fait des **documents** : le texte, sa mise en forme, les commentaires, la mise en page pour l'impression. Un script n'y passe pas bien : les guillemets droits `"` deviennent des guillemets typographiques `« »`, que `bash` ne reconnaît pas.

Un **éditeur de code** enregistre le même texte brut qu'un éditeur de texte, et ajoute des **outils pour programmer** : les erreurs soulignées, un terminal intégré pour lancer le script, l'exécution pas à pas. Il en existe en fenêtre (VS Code) et dans le terminal (Neovim, avec des extensions).

| Outil | Exemples | Ce qu'il enregistre | Pour un script |
|---|---|---|---|
| **Éditeur de texte** | nano, vi, Bloc-notes, gedit | du texte brut | convient, sans aide |
| **Traitement de texte** | Word, Writer | un document mis en forme | ne convient pas |
| **Éditeur de code** | VS Code, Neovim | du texte brut | convient, et aide à écrire, lancer, déboguer |

> 💡 **Remarque.** Certains traitements de texte savent aussi enregistrer du texte brut, avec les bons réglages : c'est le cas de TextEdit sous macOS.

## Avec l'éditeur de texte du système : deux fenêtres, aucune aide

Imaginons un petit script, `fiche.sh`, qui affiche la fiche de la machine : son nom, l'utilisateur, la date et la place libre sur le disque. À la ligne 4, un guillemet a été oublié. Dans le Bloc-notes, rien ne le montre.

```scene
lesson: assets/editor.scene.json
step: bloc-notes
```

Pour le lancer, il faut **changer de fenêtre** et passer au terminal. On lance le script, `bash` l'exécute, puis s'arrête en plein milieu. Son message, en anglais, dit qu'il est arrivé à la fin du fichier (*EOF*, *end of file*) sans trouver de guillemet de fin. Il cite la **ligne 5**, alors que la faute est à la ligne 4 : `bash` a pris le premier guillemet de la ligne 5 pour celui qui manquait. Il ne reste qu'à relire chaque ligne, caractère par caractère.

## Avec un éditeur de code : une fenêtre, des couleurs

Un **éditeur de code** est un éditeur de texte fait pour les programmes. Il enregistre toujours du texte brut, mais il reconnaît le langage du fichier, ici celui de `bash`, à son nom et à sa première ligne, et il vous aide à l'écrire.

```scene
lesson: assets/editor.scene.json
step: editeur-de-code
```

Le terminal est **dans la même fenêtre**, et les **numéros de ligne** mènent tout droit à la ligne citée par `bash`. On ajoute le guillemet, on enregistre, on relance, sans changer de fenêtre.

Les **couleurs** distinguent les commandes, les textes entre guillemets et les commentaires : on parle de **coloration syntaxique**. Dans un vrai éditeur de code, le guillemet oublié se voit aussi à elles : les lignes qui suivent la ligne 4 changent de couleur. Le schéma, qui colore chaque ligne à part, ne le montre pas.

## Les outils essentiels d'un IDE

Un éditeur de code réunit dans une fenêtre tout ce qu'il faut pour écrire, lancer et corriger un programme. Quand il en fait beaucoup, on parle d'**IDE** (*integrated development environment*, environnement de développement intégré). Voici ses outils essentiels.

```scene
lesson: assets/ide.scene.json
step: outils
```

| Outil | À quoi il sert |
|---|---|
| **Explorateur** | voir les fichiers et sous-dossiers du **dossier ouvert** ; un clic en ouvre un |
| **Zone d'édition** | écrire dans le fichier ouvert, avec les numéros de ligne ; un onglet par fichier |
| **Terminal intégré** | un vrai terminal, dans la même fenêtre, ouvert sur le dossier ; sous Windows, on y choisit Git Bash |
| **Support du langage** | coloration, complétion, erreurs soulignées avant de lancer (*linting*), lancement ou compilation, débogage, modèles de code |

Le **support du langage** ne se voit pas comme une zone : il travaille dans la zone d'édition et le terminal. Dans VS Code, chaque langage (bash, Java, Python…) s'ajoute par une **extension**.

## VS Code, l'éditeur de ce parcours

Il existe beaucoup d'éditeurs de code. Ce parcours utilise **Visual Studio Code**, qu'on abrège en **VS Code** : il est gratuit, il fonctionne sous Windows, macOS et Linux, et il est très répandu dans les entreprises. Les labs du parcours expliquent comment l'installer.

> 📖 [Visual Studio Code, documentation (en anglais)](https://code.visualstudio.com/docs) · [L'interface de VS Code (en anglais)](https://code.visualstudio.com/docs/getstarted/userinterface) · [Guide d'utilisation de TextEdit (Apple)](https://support.apple.com/fr-fr/guide/textedit/welcome/mac)

## Récap

- Un programme s'écrit en **texte brut** : un traitement de texte ajoute une mise en forme qui le rend illisible pour la machine.
- Un **éditeur de texte** enregistre ce que vous tapez, sans mise en forme ; un **éditeur de code** fait de même et vous aide à écrire et à lancer le programme.
- Les outils essentiels d'un **IDE** : l'explorateur du dossier ouvert, la zone d'édition, le terminal intégré et le support du langage (coloration, complétion, erreurs soulignées, lancement, débogage).
- **VS Code** est l'éditeur de code de ce parcours.

Reste une question : ce texte, bien écrit et sans faute, la machine ne le comprend pas tel quel. Qui le lui traduit ? C'est l'objet du contenu [Compilé ou interprété](https://byte-layers.com/fr/bits/compiled-or-interpreted).

## Trois questions pour vérifier ce que vous avez retenu

```quiz
title: "De l'éditeur de texte à l'éditeur de code"
tracksProgress: false
showNotice: false
place: stage
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
      - "Il aide à écrire et à lancer : couleurs selon le langage, numéros de ligne, complétion, terminal dans la même fenêtre"
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

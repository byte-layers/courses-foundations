---
title: "Votre poste de développeur : VS Code et un premier programme"
description: "Lab débutant : installer VS Code, y ouvrir son dossier de travail, corriger une faute dans fiche.sh avec l'aide de l'éditeur, puis installer Node.js et lancer un premier programme en JavaScript ; variante Java avec le JDK, javac et java."
tags:
  - lab
  - editor
  - programming
difficulty: beginner
duration: 45
introTitle: "Présentation"
requires: "0.4.0"
options:
  allowManualProgress: true
  autoCompleteOnNext: unverifiable
---

Votre poste devient un poste de développeur. Vous installez **VS Code**, l'éditeur de code de ce parcours, vous y ouvrez le dossier du lab précédent et vous corrigez une faute dans `fiche.sh` en vous aidant des couleurs. Puis vous installez **Node.js**, un runtime, et vous écrivez et lancez votre premier programme en JavaScript, sans quitter l'éditeur.

## Pour qui ?

Ce lab s'adresse à quelqu'un qui n'a **jamais programmé**. Il suppose trois contenus :

- le lab [Votre premier script, sur votre machine](https://byte-layers.com/fr/labs/first-script-lab) : vous avez un dossier `~/byte-layers/foundations` qui contient `fiche.sh` ;
- le bit [De l'éditeur de texte à l'éditeur de code](https://byte-layers.com/fr/bits/code-editor) : les quatre zones de la fenêtre d'un éditeur de code ;
- le bit [Compilé ou interprété](https://byte-layers.com/fr/bits/compiled-or-interpreted) : ce qu'est un runtime, un compilateur, le bytecode Java.

## Comment ça se passe

Quatre étapes pour tout le monde, environ 45 minutes, puis une cinquième, à part, **si votre parcours passe par Java** : installer le JDK, compiler avec `javac` et lancer avec `java`.

C'est le premier lab qui **installe des logiciels** : VS Code, Node.js, et le JDK pour la variante Java. Sur un ordinateur d'entreprise ou d'école, l'installation peut demander des droits d'administrateur : demandez-les avant de commencer.

Vos fichiers vivent toujours dans `~/byte-layers/foundations`. Ce lab y ajoute `bonjour.js`, et pour la variante Java `Bonjour.java` et `Bonjour.class`, et ne supprime rien.

**Sous Windows**, les commandes se tapent dans **Git Bash**, installé au lab précédent ; la première étape vous montre comment l'ouvrir dans VS Code. Tapez ou collez chaque commande vous-même : le bouton ▶ ne fonctionne que dans l'extension, pas encore disponible sous Windows.

> 💡 **Remarque.** Les boutons de vérification fonctionnent quand ce contenu est ouvert dans VS Code avec l'extension byte_layers, disponible pour macOS et Linux : la page [Comment ça marche](https://byte-layers.com/fr/comment-ca-marche) explique comment l'installer. Sinon, comparez votre résultat à celui affiché sous chaque commande.

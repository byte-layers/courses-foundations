---
title: "Votre premier script, sur votre machine"
description: "Lab débutant : ouvrir le vrai terminal de son ordinateur, interroger la machine avec quatre commandes, écrire le script fiche.sh avec l'éditeur de texte du système, le lancer et ranger son résultat dans un fichier."
tags:
  - lab
  - shell
  - computer
difficulty: beginner
duration: 35
introTitle: "Présentation"
requires: "0.4.0"
options:
  allowManualProgress: true
  autoCompleteOnNext: unverifiable
---

Jusqu'ici, les commandes se tapaient dans un terminal simulé, dans la page. Ce lab passe sur **votre ordinateur** : vous ouvrez son vrai terminal, vous lui demandez qui il est, puis vous écrivez un petit script, `fiche.sh`, qui range dans un fichier le nom de la machine, l'utilisateur, la date et l'espace disque.

## Pour qui ?

Ce lab s'adresse à quelqu'un qui n'a **jamais programmé**. Il suppose que vous avez lu [L'ordinateur en couches, du matériel au premier script](https://byte-layers.com/fr/bits/computer-layers) : vous savez ce que sont le noyau, un terminal, un shell, et à quoi ressemble un script. Il ne suppose rien d'autre : chaque commande est expliquée à sa première apparition.

## Comment ça se passe

Quatre étapes, environ 35 minutes en tout. Le résultat diffère chez chacun : c'est la fiche de **votre** machine. Le script ne déplace et ne supprime rien.

Vos fichiers vivent dans `~/byte-layers/foundations`, le signe `~` désignant votre dossier personnel. Ce lab ne les supprime pas : le lab suivant reprend `fiche.sh`.

**Sous Windows**, les commandes se tapent dans **Git Bash**, un terminal que la première étape vous fait installer. Sous macOS et Linux, le terminal est déjà là.

> 💡 **Remarque.** Les boutons de vérification fonctionnent quand ce contenu est ouvert dans VS Code, l'éditeur que vous installerez au lab suivant. Sur le site, comparez votre résultat à celui affiché sous chaque commande : il doit avoir la même forme, avec les valeurs de votre machine.

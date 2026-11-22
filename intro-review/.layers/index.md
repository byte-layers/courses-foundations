---
title: "Quiz de fin d'introduction : du matériel aux conteneurs"
description: "Quinze questions sur les sept étapes de l'introduction à l'informatique : les couches de l'ordinateur, les commandes, le script, l'éditeur de code, compilé ou interprété, les architectures d'un programme, machines virtuelles et conteneurs."
tags:
  - bit
  - quiz
  - computer
  - review
difficulty: beginner
duration: 10
requires: "0.5.0"
---

Ce quiz reprend les sept étapes de l'introduction, du matériel aux conteneurs. Chaque section porte sur une étape et renvoie au contenu qui l'explique : une question qui résiste, relisez ce contenu et revenez. Les questions comptent pour votre progression : une section est validée quand toutes ses réponses sont justes.

**Prérequis** : avoir suivi les contenus de l'introduction, dans l'ordre : [L'ordinateur en couches](https://byte-layers.com/fr/bits/computer-layers) (étapes 1 à 3), [De l'éditeur de texte à l'éditeur de code](https://byte-layers.com/fr/bits/code-editor), [Compilé ou interprété](https://byte-layers.com/fr/bits/compiled-or-interpreted), [Les architectures d'un programme](https://byte-layers.com/fr/bits/program-architectures) et [Machines virtuelles et conteneurs](https://byte-layers.com/fr/bits/virtual-machines-and-containers).

# Quiz de fin d'introduction : du matériel aux conteneurs

## Étape 1 : les couches de l'ordinateur, le terminal et le shell

Deux questions sur la pile de couches et sur les deux programmes qu'on ouvre pour taper des commandes. Contenu : [L'ordinateur en couches](https://byte-layers.com/fr/bits/computer-layers), ses quatre premières sections.

```quiz
title: "Les couches, le terminal et le shell"
tracksProgress: true
showNotice: false
questions:
  - prompt: "Quelle couche de l'ordinateur est la seule à parler au matériel ?"
    answers:
      - "Le shell"
      - "Le noyau"
      - "L'interface graphique"
    correct: 2
    explanation: "Le noyau partage le processeur, la mémoire et le disque entre les programmes. Les autres couches lui demandent tout par des appels système."
  - prompt: "Vous tapez `ls` dans un terminal, puis Entrée. Quel programme comprend cette ligne et la fait exécuter ?"
    answers:
      - "Le shell"
      - "Le terminal"
      - "L'explorateur de fichiers"
    correct: 1
    explanation: "Le terminal est la fenêtre : il affiche et transmet ce que vous tapez, sans le comprendre. Le shell lit la ligne et fait ce qu'elle demande, en passant par le noyau."
```

## Étape 2 : changer de dossier, copier, déplacer, supprimer

Deux questions sur les commandes qui manipulent des dossiers et des fichiers, celles que vous avez tapées pour ranger un dossier. Contenu : [L'ordinateur en couches](https://byte-layers.com/fr/bits/computer-layers), sections sur les premières commandes et sur le rangement.

```quiz
title: "Les commandes de fichiers"
tracksProgress: true
showNotice: false
questions:
  - prompt: "Le shell travaille dans `/home/alice/projets`. Le fichier `notes.txt` est rangé dans `/home/alice`. Quelle commande l'affiche ?"
    answers:
      - "`cat notes.txt`"
      - "`cd notes.txt`"
      - "`cat ../notes.txt`"
    correct: 3
    explanation: "`..` désigne le dossier au-dessus du dossier courant, ici `/home/alice`. `cat notes.txt` chercherait le fichier dans `projets`, et `cd` change de dossier, il n'affiche pas de fichier."
  - prompt: "Après `cp facture.pdf sauvegarde/`, où se trouve `facture.pdf` ?"
    answers:
      - "Seulement dans `sauvegarde`"
      - "Dans le dossier courant et dans `sauvegarde`"
      - "Nulle part : `cp` l'a supprimé"
    correct: 2
    explanation: "`cp` copie : le fichier est maintenant à deux endroits. C'est `mv` qui déplace, l'original quitte alors le dossier courant."
```

## Étape 3 : le premier script

Trois questions sur le script, des commandes rangées dans un fichier, et sur la façon de le lancer. Contenu : [L'ordinateur en couches](https://byte-layers.com/fr/bits/computer-layers), sections sur le script, et le lab sur votre machine si vous l'avez fait.

```quiz
title: "Le script"
tracksProgress: true
showNotice: false
questions:
  - prompt: "Qu'est-ce qu'un script ?"
    answers:
      - "Un fichier de code machine que le processeur exécute directement"
      - "Un fichier texte que le terminal affiche sans l'exécuter"
      - "Un fichier texte de commandes, que le shell exécute dans l'ordre"
    correct: 3
    explanation: "Un script range dans un fichier les commandes qu'on taperait, une par ligne. Le shell les exécute comme si vous les tapiez."
  - prompt: "On lance un script avec `./hello.sh`. À quoi sert sa première ligne, `#!/bin/bash` ?"
    answers:
      - "Elle indique quel programme doit lire le fichier : ici `bash`"
      - "Elle affiche le nom du shell au lancement"
      - "Elle rend le fichier exécutable"
    correct: 1
    explanation: "Lancé avec `./`, le script est lu par le programme que nomme sa première ligne. Les autres lignes qui commencent par `#` sont des commentaires ; c'est `chmod +x` qui rend le fichier exécutable."
  - prompt: "Le script `ranger.sh` doit pouvoir se relancer sans message d'erreur quand les dossiers qu'il crée existent déjà. Quelle ligne écrire ?"
    answers:
      - "`mkdir photos`"
      - "`mkdir -p photos`"
      - "`mkdir -r photos`"
    correct: 2
    explanation: "Avec l'option `-p`, `mkdir` ne dit rien si le dossier existe déjà. Sans elle, la deuxième fois, il affiche une erreur."
```

## Étape 4 : l'éditeur de code

Deux questions sur l'outil avec lequel on écrit un programme. Contenu : [De l'éditeur de texte à l'éditeur de code](https://byte-layers.com/fr/bits/code-editor).

```quiz
title: "L'éditeur de code"
tracksProgress: true
showNotice: false
questions:
  - prompt: "Votre script, écrit dans Word, affiche des erreurs, et ses guillemets sont devenus `« »`. Pourquoi ?"
    answers:
      - "Parce qu'un script doit être écrit en anglais"
      - "Parce que Word enregistre par défaut une mise en forme et des guillemets typographiques"
      - "Parce que Word n'enregistre pas les fichiers en `.sh`"
    correct: 2
    explanation: "Un programme s'écrit en texte brut. Un traitement de texte enregistre par défaut la mise en forme, et ses guillemets typographiques ne sont pas des guillemets pour `bash`."
  - prompt: "Le même `fiche.sh` est ouvert dans le Bloc-notes et dans VS Code. Que voit-on de plus dans VS Code ?"
    answers:
      - "Des couleurs, des numéros de ligne et un terminal dans la même fenêtre"
      - "Une mise en forme : gras, polices, marges"
      - "Il traduit le programme en code machine"
    correct: 1
    explanation: "Les deux enregistrent du texte brut ; l'éditeur de code vous aide en plus à écrire et à trouver vos fautes. Il ne traduit rien en code machine : c'est le travail d'un compilateur."
```

## Étape 5 : compilé ou interprété

Deux questions sur le trajet du code source jusqu'au processeur. Contenu : [Compilé ou interprété](https://byte-layers.com/fr/bits/compiled-or-interpreted).

```quiz
title: "Compilé ou interprété"
tracksProgress: true
showNotice: false
questions:
  - prompt: "Vous modifiez le code source d'un programme en C, déjà compilé. Que faut-il faire avant de le relancer ?"
    answers:
      - "Rien : la modification se voit au lancement suivant"
      - "Installer le runtime du C"
      - "Le recompiler, pour produire un nouveau binaire"
    correct: 3
    explanation: "Le binaire a été traduit avant la modification. Il faut recompiler. Un script interprété, lui, est relu à chaque lancement."
  - prompt: "On vous donne `bonjour.js` à lancer sur votre machine. De quoi avez-vous besoin, et comment l'appelle-t-on ?"
    answers:
      - "De Node.js, le runtime : le programme qui lit et exécute `bonjour.js`"
      - "D'un compilateur, qui en fait un binaire"
      - "De rien : le processeur lit le JavaScript"
    correct: 1
    explanation: "Hors du navigateur, un script JavaScript ne tourne pas sans Node.js, un programme Java pas sans la JVM, un script shell pas sans `bash` : ce sont leurs runtimes."
```

## Étape 6 : où vivent les programmes

Deux questions sur les architectures d'un programme et l'appli Prêts de la bibliothèque. Contenu : [Les architectures d'un programme](https://byte-layers.com/fr/bits/program-architectures).

```quiz
title: "Les architectures d'un programme"
tracksProgress: true
showNotice: false
questions:
  - prompt: "Dans l'architecture client léger, ou trois tiers, que faut-il installer sur chaque poste pour se servir de l'appli Prêts ?"
    answers:
      - "L'appli Prêts et la base de données"
      - "Rien de plus que le navigateur, déjà présent"
      - "Un serveur web"
    correct: 2
    explanation: "Le navigateur affiche les pages ; l'appli tourne sur le serveur web et les données restent dans la base. Une mise à jour se fait une fois, sur le serveur."
  - prompt: "Le paiement par carte de l'appli Prêts est assuré par un prestataire. Comment l'appli s'en sert-elle ?"
    answers:
      - "Elle lui envoie des demandes par son API"
      - "Elle intègre le code du prestataire dans l'appli Prêts"
      - "Elle demande au noyau de son serveur"
    correct: 1
    explanation: "Un service externe se sert à distance, par son API. Rien à écrire ni à héberger, mais on dépend de lui : prestataire en panne, plus de paiement par carte."
```

## Étape 7 : machines virtuelles et conteneurs

Deux questions sur les façons de faire tourner plusieurs « machines » sur une seule. Contenu : [Machines virtuelles et conteneurs](https://byte-layers.com/fr/bits/virtual-machines-and-containers).

```quiz
title: "Machines virtuelles et conteneurs"
tracksProgress: true
showNotice: false
questions:
  - prompt: "Sur un serveur tournent deux machines virtuelles et trois conteneurs. Combien de noyaux tournent sur cette machine ?"
    answers:
      - "Six : un par machine virtuelle, un par conteneur, et celui de l'hôte"
      - "Un seul, partagé par tous"
      - "Trois : celui de l'hôte, et un par machine virtuelle"
    correct: 3
    explanation: "Une machine virtuelle est un ordinateur simulé, noyau compris. Un conteneur n'a pas de noyau à lui : il isole un programme et ses fichiers sur le noyau de la machine qui l'accueille. Ici : le noyau de l'hôte, et un par machine virtuelle."
  - prompt: "L'appli Prêts tourne sur le poste du développeur dans un conteneur, avec son Node.js 22. Pourquoi le même conteneur marchera-t-il sur le serveur ?"
    answers:
      - "Parce qu'il emporte son propre Node.js 22"
      - "Parce que le conteneur installe Node.js 22 sur le serveur"
      - "Parce qu'un conteneur n'a besoin d'aucun noyau"
    correct: 1
    explanation: "Le conteneur emporte l'appli et son runtime. Il a besoin du noyau de l'hôte, mais pas du Node.js installé sur l'hôte."
```

## Récap

Les sept étapes, en une ligne chacune :

1. Un ordinateur est une pile de couches, et seul le **noyau** parle au matériel ; le **terminal** affiche, le **shell** comprend.
2. Des **commandes** se déplacent dans les dossiers et manipulent les fichiers : `cd`, `ls`, `mkdir`, `cp`, `mv`, `rm`.
3. Un **script** range ces commandes dans un fichier que le shell rejoue.
4. Un programme s'écrit en **texte brut**, de préférence dans un **éditeur de code**.
5. Le code source est **compilé** en binaire, **interprété**, ou compilé en bytecode pour la JVM ; le **runtime** est ce qu'il faut installer pour le lancer.
6. Un programme peut se répartir entre le poste et des **serveurs**, et se servir de services externes par leur **API**.
7. Une **machine virtuelle** simule un ordinateur entier ; un **conteneur** isole un programme sur le noyau de l'hôte.

> 📖 [Système d'exploitation (Wikipédia)](https://fr.wikipedia.org/wiki/Syst%C3%A8me_d%27exploitation) · [Manuel de Bash (en anglais)](https://www.gnu.org/software/bash/manual/bash.html)

## Et après l'introduction

Vous savez maintenant ce qu'est un ordinateur, comment lui parler, comment s'écrit et s'exécute un programme, où il tourne. La suite n'est plus de l'introduction : chaque outil s'installe au moment où il règle un problème, et sert aussitôt. Le premier est **Git**, qui garde chaque version de vos fichiers et permet de revenir à une version qui marchait : [Pourquoi versionner son travail](https://byte-layers.com/fr/bits/why-version-control) (sous Windows, il est déjà installé avec Git Bash) ; **Docker** vient avec le contenu [Pourquoi les conteneurs](https://byte-layers.com/fr/bits/containers-why).

```ack
J'ai terminé l'introduction
```

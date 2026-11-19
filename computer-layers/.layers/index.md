---
title: "L'ordinateur en couches, du matériel au premier script"
description: "Ce qui se passe sous vos fenêtres : le matériel, le noyau, le shell, l'interface graphique, puis le terminal, les premières commandes et un premier script."
tags:
  - bit
  - computer
  - os
  - terminal
difficulty: beginner
duration: 15
requires: "0.5.0"
---

Un ordinateur est fait de couches posées les unes sur les autres, et chacune ne parle qu'à ses voisines. Vous saurez ce que fait chaque couche, pourquoi un serveur se passe d'interface graphique, ce que sont un terminal et un shell, à quoi ressemblent les premières commandes et ce qu'est un script. Ce contenu est écrit pour quelqu'un qui n'a jamais ouvert de terminal : chaque section a son schéma animé, que le bouton ▶ Jouer ouvre en grand.

**Prérequis** : aucun.

# L'ordinateur en couches, du matériel au premier script

Vous utilisez un ordinateur tous les jours, à la souris : vous ouvrez des fenêtres, vous double-cliquez sur des dossiers. Ce contenu soulève le capot, couche par couche, puis montre une autre façon de s'en servir, en tapant du texte.

## Les cinq couches d'un ordinateur

Ce que vous voyez à l'écran, ce sont des **applications** dans des fenêtres : le navigateur, un éditeur de texte, un jeu. Sous elles, quatre couches travaillent sans se montrer. Le tableau les présente de bas en haut.

| Couche | Ce qu'elle fait |
|---|---|
| **Matériel** | ce que vous pouvez toucher : le processeur (CPU) qui calcule, la mémoire vive (RAM), le disque qui garde vos fichiers, la carte réseau |
| **Noyau** (en anglais *kernel*) | le chef d'orchestre : il partage le processeur, la mémoire et le disque entre les programmes, et il est le seul à parler au matériel |
| **Shell et services** | le shell est un programme qui lit des commandes et les fait exécuter ; les services sont des programmes qui tournent en fond, sans fenêtre |
| **Interface graphique** | elle dessine les fenêtres, suit la souris et gère le bureau |
| **Applications** | les programmes que vous utilisez, posés sur toutes les autres couches |

Un programme ne touche jamais le matériel lui-même. Quand il a besoin du disque, de l'écran ou du réseau, il le demande au noyau : cette demande s'appelle un **appel système** (*system call*). Les couches entre le matériel et vos applications forment le **système d'exploitation** (*operating system*, OS) : Windows, macOS et Linux en sont trois.

Le schéma montre un clic de souris : il descend la pile jusqu'au matériel, puis la réponse remonte jusqu'à l'écran.

```scene
lesson: assets/os.scene.json
step: couches
```

## Ouvrir un dossier à la souris : un appel au noyau

Vous double-cliquez sur le dossier **Documents** dans l'**explorateur de fichiers**, le programme qui montre vos dossiers sous forme d'icônes. L'explorateur ne lit pas le disque lui-même : il fait un appel système au noyau, le noyau lit le disque, et la liste des fichiers remonte jusqu'à l'explorateur, qui la dessine en icônes.

Un geste aussi simple déclenche donc plusieurs demandes au noyau : ouvrir le dossier, lister son contenu, lire la taille et la date de chaque fichier. Le schéma suit ce double-clic, de la souris jusqu'au disque et retour.

```scene
lesson: assets/os.scene.json
step: explorateur
```

## Un serveur fonctionne sans interface graphique

Un **serveur** est un ordinateur qui rend un service à d'autres : il héberge un site web, garde une base de données, distribue des fichiers. Il tourne le plus souvent dans un centre de données (*data center*), au milieu de centaines d'autres machines, et personne ne regarde son écran.

On lui retire donc l'interface graphique et les applications de bureau. Il reste le matériel, le noyau, et le shell avec ses services. Ce choix a trois raisons :

- la mémoire et le disque servent au travail du serveur, pas à dessiner des fenêtres ;
- moins de logiciels installés, c'est moins de logiciels à mettre à jour et à protéger ;
- tout ce qui se tape au clavier peut s'écrire dans un fichier et se rejouer, sans personne devant l'écran.

Pour travailler sur un serveur, on s'y connecte depuis sa propre machine, à travers le réseau, avec **`ssh`** : un programme qui ouvre une session en texte sur une machine distante. Le schéma montre la pile du serveur, réduite à trois couches, et une commande envoyée par `ssh`.

```scene
lesson: assets/os.scene.json
step: sans-gui
```

## Le terminal et le shell remplacent l'explorateur

Sans explorateur, on voit le contenu d'un dossier en tapant une commande. Deux programmes se partagent ce travail, et on les confond souvent :

- le **terminal** est la fenêtre de texte : il affiche ce qu'on lui envoie et transmet ce que vous tapez, sans rien y comprendre ;
- le **shell** lit la ligne que vous avez tapée, la comprend et fait ce qu'elle demande, en passant par le noyau. Sous Linux, le shell le plus courant s'appelle `bash` ; macOS utilise `zsh`.

Cette façon de se servir d'un ordinateur, en tapant des commandes, s'appelle la **ligne de commande** (*command-line interface*, CLI). Le shell n'est pas propre aux serveurs : il est déjà sur votre ordinateur, caché sous l'interface graphique. L'application « Terminal » de macOS ou de Linux, ou PowerShell sous Windows, vous y donne accès.

Le schéma rejoue l'ouverture du dossier Documents, cette fois avec la commande `ls Documents` : le chemin jusqu'au noyau et au disque est le même que pour le double-clic, et la réponse arrive en texte au lieu d'icônes.

```scene
lesson: assets/os.scene.json
step: terminal
```

## Vos premières commandes : pwd, ls, cd, mkdir, cat

Une commande s'écrit sur une ligne et se valide avec la touche Entrée. Elle commence par un **nom**, le programme à lancer ; viennent ensuite, si besoin, des **options**, qui changent son comportement et commencent par un tiret, et des **arguments**, ce sur quoi elle agit. Dans `ls -l Documents`, `ls` est le nom, `-l` une option qui demande une liste détaillée, et `Documents` l'argument.

Le shell travaille toujours dans un dossier, le **dossier courant**, comme une fenêtre d'explorateur ouverte sur un dossier. Au départ, c'est votre dossier personnel, que le shell abrège en `~` et que `pwd` affiche en entier, par exemple `/home/alice`. Voici les cinq commandes du schéma.

| Commande | Ce qu'elle fait |
|---|---|
| `pwd` | affiche le dossier courant (*print working directory*) |
| `ls` | liste le contenu du dossier courant (*list*) |
| `mkdir projets` | crée un dossier nommé `projets` (*make directory*) |
| `cd projets` | change de dossier courant (*change directory*) |
| `cat ../notes.txt` | affiche le contenu d'un fichier texte ; `..` désigne le dossier au-dessus |

`cd` et `pwd` font partie du shell lui-même. `ls`, `mkdir` et `cat` sont de petits programmes rangés dans le dossier `/usr/bin` : le shell les lance, et ce sont eux qui parlent au noyau. Le schéma tape les cinq commandes l'une après l'autre.

```scene
lesson: assets/os.scene.json
step: commandes
```

Si vous voulez essayer, ouvrez un terminal comme indiqué dans la section précédente. La première commande affiche le dossier dans lequel le shell travaille.

```exec
pwd
```

La seconde liste ce que contient ce dossier. Sous Windows, PowerShell connaît aussi `pwd` et `ls`, avec un affichage différent.

```exec
ls
```

## Un script : des commandes rangées dans un fichier

Taper les mêmes commandes chaque jour devient vite pénible. Un **script** les range dans un fichier texte, une par ligne, et le shell les exécute dans l'ordre, de haut en bas, comme si vous les tapiez. Voici un script de six lignes, nommé `hello.sh`.

```bash
#!/bin/bash
# mon premier programme
echo "Bonjour $USER !"
date
mkdir -p ~/byte-layers/demo
ls ~/byte-layers
```

Chaque ligne a un rôle précis.

| Ligne | Rôle |
|---|---|
| `#!/bin/bash` | indique quel programme doit lire le fichier : ici `bash` |
| `# mon premier programme` | un commentaire : le shell ignore toute ligne qui commence par `#`, elle sert au lecteur |
| `echo "Bonjour $USER !"` | `echo` affiche un texte ; `$USER` est une **variable**, remplacée par votre nom d'utilisateur |
| `date` | affiche la date et l'heure, comme si vous tapiez la commande |
| `mkdir -p ~/byte-layers/demo` | crée le dossier `demo` dans `byte-layers` ; l'option `-p` crée aussi `byte-layers` s'il n'existe pas encore |
| `ls ~/byte-layers` | liste le dossier `byte-layers`, pour voir que `demo` est apparu |

Pour lancer le fichier, on le rend d'abord **exécutable**, une fois pour toutes, avec `chmod +x hello.sh` : `chmod` (*change mode*) change les droits d'un fichier, et `+x` lui ajoute le droit d'être exécuté. On le lance ensuite avec `./hello.sh`, où `./` veut dire « dans le dossier courant ». Le schéma suit le shell qui lit le script ligne à ligne et lance chaque commande.

```scene
lesson: assets/os.scene.json
step: script
```

Ces six lignes sont déjà un programme. Écrire et lancer votre propre script sera l'objet d'un contenu pratique, à venir.

> 📖 [Ligne de commande pour débutants (Ubuntu, en anglais)](https://ubuntu.com/tutorials/command-line-for-beginners) · [Guide d'utilisation de Terminal sur Mac](https://support.apple.com/fr-fr/guide/terminal/welcome/mac) · [Manuel de Bash (en anglais)](https://www.gnu.org/software/bash/manual/bash.html)

## Récap

- Un ordinateur est une pile de couches : matériel, noyau, shell et services, interface graphique, applications.
- Seul le noyau touche au matériel ; les programmes lui demandent tout par des appels système.
- Un serveur se passe d'interface graphique : on s'y connecte avec `ssh` et on travaille dans le shell.
- Le terminal affiche, le shell comprend. L'explorateur et le terminal font le même travail, l'un à la souris, l'autre en texte.
- Une commande, c'est un nom, des options et des arguments ; un script, ce sont des commandes rangées dans un fichier.

Le schéma reprend la pile entière, avec ses deux chemins : le clic de souris et le script lancé dans le terminal.

```scene
lesson: assets/os.scene.json
step: recap
```

Trois questions pour vérifier ce que vous avez retenu.

```quiz
title: "L'ordinateur en couches"
tracksProgress: false
showNotice: false
questions:
  - prompt: "Un programme veut lire un fichier sur le disque. Comment fait-il ?"
    answers:
      - "Il lit le disque directement, sans passer par personne"
      - "Il demande au noyau, par un appel système, et le noyau lit le disque"
      - "Il demande à l'interface graphique, qui lit le disque à sa place"
    correct: 2
    explanation: "Seul le noyau parle au matériel. Un programme, même l'explorateur de fichiers, lui demande ce dont il a besoin par un appel système."
  - prompt: "Quelle phrase décrit le mieux la différence entre le terminal et le shell ?"
    answers:
      - "Le terminal affiche le texte et transmet ce qu'on tape ; le shell comprend la commande et la fait exécuter"
      - "Le terminal et le shell sont deux noms pour le même programme"
      - "Le shell affiche le texte ; le terminal comprend les commandes"
    correct: 1
    explanation: "Le terminal est la fenêtre de texte, il ne comprend rien à ce qu'il transmet. Le shell, par exemple bash, lit la ligne et lance le bon programme."
  - prompt: "Pourquoi retire-t-on l'interface graphique d'un serveur ?"
    answers:
      - "Parce qu'un serveur n'a pas de noyau"
      - "Parce que personne ne regarde son écran : sa mémoire sert à son travail, et il y a moins de logiciels à mettre à jour"
      - "Parce que le shell ne fonctionne pas quand une interface graphique est installée"
    correct: 2
    explanation: "Un serveur tourne dans un centre de données, sans personne devant. On le pilote à distance avec ssh, dans le shell, qui existe aussi sur un ordinateur de bureau."
```

```ack
J'ai compris
```

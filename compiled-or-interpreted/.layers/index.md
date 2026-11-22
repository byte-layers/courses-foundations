---
title: "Compilé ou interprété : du code source au programme qui tourne"
description: "Le processeur ne lit pas le texte d'un programme : le code source, le code machine, les trois trajets entre les deux (interprété, compilé, bytecode et machine virtuelle Java) et ce qu'est un runtime."
tags:
  - bit
  - programming
  - computer
difficulty: beginner
duration: 12
requires: "0.6.0"
---

Un programme commence par un texte, que quelqu'un écrit ; le processeur, lui, n'exécute que des nombres. Vous saurez ce que sont le code source et le code machine, les trois chemins qui mènent de l'un à l'autre (un interpréteur, un compilateur, ou les deux avec Java), ce qu'il faut refaire quand on modifie un programme, et ce qu'est un runtime, le programme qu'il faut installer pour en faire tourner un autre.

**Prérequis** : [L'ordinateur en couches, du matériel au premier script](https://byte-layers.com/fr/bits/computer-layers), pour le noyau, le shell et le script `hello.sh`.

# Compilé ou interprété : du code source au programme qui tourne

Dans le contenu sur les couches, vous avez vu le shell exécuter `hello.sh`, un petit fichier de texte, ligne après ligne. Ce contenu regarde comment un texte devient quelque chose que la machine exécute.

## Le code source et le code machine

Le texte d'un programme, écrit par une personne, s'appelle le **code source**. Il est écrit dans un **langage de programmation**, avec ses mots et ses règles : le langage de `bash` pour `hello.sh`, et d'autres que vous croiserez, comme C (un langage ancien, encore très utilisé pour les systèmes d'exploitation), Java ou JavaScript. Le code source se lit avec n'importe quel éditeur de texte : ce sont des mots, des signes, des retours à la ligne.

Le processeur ne lit pas ce texte. Il exécute des **instructions**, des ordres très simples (additionner deux nombres, ranger un nombre en mémoire, passer à une autre instruction), écrits sous forme de nombres : c'est le **code machine**. Chaque famille de processeurs a le sien : les processeurs Intel et AMD de la plupart des PC n'ont pas les mêmes instructions que les puces des Mac récents. Un programme en code machine dépend aussi du système d'exploitation, puisqu'il passe par son noyau.

| | Code source | Code machine |
|---|---|---|
| Qui l'écrit | une personne | un programme, à partir du code source |
| À quoi il ressemble | du texte : `echo "Bonjour"` | des nombres, illisibles pour nous |
| Qui le lit | une personne, un éditeur, un autre programme | le processeur |
| Où il marche | partout où un programme sait le lire | sur une famille de processeurs et un système d'exploitation |

Entre les deux, il faut donc toujours un programme qui fasse le passage. Il y a trois façons de s'y prendre. Les schémas qui suivent ne gardent que deux couches de la pile, le matériel et le noyau : les programmes qui tournent sont posés sur le noyau, les fichiers restent au sol, sur le disque.

## Interprété : un programme lit le script ligne à ligne

Le script `hello.sh` ne devient jamais du code machine. Quand vous tapez `./hello.sh`, sa première ligne, `#!/bin/bash`, dit au système de confier le fichier au programme **`bash`**, qui, lui, est déjà en code machine. `bash` lit une ligne, fait ce qu'elle demande en passant par le noyau, puis lit la suivante.

```scene
lesson: assets/compile.scene.json
step: interprete
```

Un programme qui lit du code source et fait ce qu'il dit, au fur et à mesure, s'appelle un **interpréteur**. Le fichier reste un texte du début à la fin. Conséquence : dans un script simple comme celui-ci, si la ligne 3 contient une faute, `bash` ne s'en aperçoit en général qu'en y arrivant, quand les deux premières ont déjà été exécutées.

## Compilé : un compilateur traduit tout, une fois

En langage C, on procède autrement. Un programme, le **compilateur**, lit tout le code source `bonjour.c` et écrit un nouveau fichier, le **binaire** : les mêmes instructions, traduites en code machine. Cette traduction s'appelle compiler. Le schéma ne montre pas la commande qui lance le compilateur C : vous n'en aurez pas besoin dans ce parcours.

```scene
lesson: assets/compile.scene.json
step: compile
```

On lance ensuite le binaire comme n'importe quel programme, ici avec `./bonjour` : le noyau le charge en mémoire et le processeur exécute ses instructions, **sans programme pour le lire**. Le code source et le compilateur ne servent plus pour le faire tourner : on peut donner le binaire à quelqu'un d'autre, à condition qu'il ait le même type de processeur et le même système. Un binaire compilé pour Windows ne se lance pas sur un Mac.

## Modifier le code source : ce qu'il faut refaire

La différence se voit le jour où l'on change une ligne. Remplaçons « Bonjour » par « Salut » dans les deux codes sources, puis relançons chaque programme.

```scene
lesson: assets/compile.scene.json
step: modifier
```

Le script dit « Salut » dès qu'on le relance, puisque `bash` relit le fichier à chaque fois. Le binaire, lui, dit encore « Bonjour » : c'est une traduction faite **avant** le changement. Il faut **recompiler** pour fabriquer un nouveau binaire. En échange de cette étape, le compilateur relit tout le code source et signale certaines fautes avant même que le programme ne démarre.

## Java : compilé, puis lu par une machine virtuelle

Java prend un chemin entre les deux. Le compilateur Java, `javac`, lit `Bonjour.java`, mais n'écrit pas du code machine : il écrit `Bonjour.class`, du **bytecode**, des instructions pour une machine qui n'existe pas en vrai. La commande `java Bonjour` lance alors la **machine virtuelle Java** (*Java Virtual Machine*, JVM), un programme qui lit ce bytecode et le fait exécuter par le processeur.

```scene
lesson: assets/compile.scene.json
step: bytecode
```

L'intérêt : le même `Bonjour.class` tourne sur Windows, macOS et Linux, chacun avec sa propre JVM. On compile une fois, et le résultat voyage. Pour écrire du Java, on installe le **JDK** (*Java Development Kit*), qui contient `javac` et la JVM.

> 💡 **Remarque.** L'expression « machine virtuelle » sert aussi pour autre chose : un ordinateur complet simulé par un programme, que vous rencontrerez plus loin dans ce parcours. Ici, c'est seulement le programme qui lit le bytecode Java.

## Le runtime : ce qu'il faut avoir installé

Pour lancer un programme interprété ou en bytecode, le programme qui le lit doit être installé sur la machine. Ce programme s'appelle le **runtime** du langage, l'environnement d'exécution.

```scene
lesson: assets/compile.scene.json
step: runtime
```

| Programme | Trajet | Runtime à installer |
|---|---|---|
| `hello.sh` | interprété | `bash` : déjà là sous Linux et macOS ; sous Windows, il arrive avec le terminal qu'installe le lab sur votre machine |
| `Bonjour.class` | compilé en bytecode | la JVM, installée avec le JDK |
| `bonjour.js` | interprété | Node.js |
| `bonjour` (binaire) | compilé en code machine | aucun : rien de plus que le système pour lequel il a été compilé |

## JavaScript et Node.js

Le **JavaScript** est le langage des pages web : votre navigateur contient son propre interpréteur, qui fait réagir les boutons et les menus. **Node.js** est un autre runtime pour ce langage, qui l'exécute hors du navigateur, comme n'importe quel programme de votre machine.

Le lab qui suit ce contenu vous fait installer un runtime et lancer votre premier programme : Node.js pour tout le monde, ou le JDK si votre parcours passe par Java.

> 📖 [Qu'est-ce que JavaScript ? (MDN)](https://developer.mozilla.org/fr/docs/Learn_web_development/Core/Scripting/What_is_JavaScript) · [Introduction à Node.js (en anglais)](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs) · [Compiler et lancer un premier programme Java (Oracle, en anglais)](https://dev.java/learn/getting-started/)

## Récap

- Le **code source** est un texte écrit par une personne ; le processeur n'exécute que du **code machine**.
- **Interprété** : un programme, l'interpréteur, lit le code source ligne à ligne et le fait exécuter ; une modification se voit au lancement suivant.
- **Compilé** : le compilateur traduit tout le code source en un **binaire** ; le noyau le charge et le processeur l'exécute sans programme pour le lire, mais il faut recompiler après chaque modification, et le binaire ne marche que pour un processeur et un système.
- **Bytecode** : Java compile vers un code intermédiaire, que la **machine virtuelle Java** lit sur chaque système.
- Le **runtime**, c'est le programme qu'il faut installer pour en exécuter un autre : `bash`, la JVM, Node.js.

Jusqu'ici, chaque programme tourne en entier sur votre machine. Ceux que vous utilisez tous les jours, un site web ou une application de banque, se répartissent souvent entre votre machine et d'autres : c'est l'objet du contenu [Les architectures d'un programme](https://byte-layers.com/fr/bits/program-architectures).

Trois questions pour vérifier ce que vous avez retenu.

```quiz
title: "Compilé ou interprété"
tracksProgress: false
showNotice: false
questions:
  - prompt: "Vous modifiez une ligne d'un script `bash`, puis vous le relancez. Que se passe-t-il ?"
    answers:
      - "Le script exécute la nouvelle ligne : bash relit le fichier à chaque lancement"
      - "Rien ne change tant que vous n'avez pas recompilé le script"
      - "Le script refuse de démarrer, parce que le binaire n'est plus à jour"
    correct: 1
    explanation: "Un script n'est jamais traduit en binaire : l'interpréteur, ici bash, le relit à chaque lancement. La modification se voit tout de suite."
  - prompt: "Vous avez compilé `bonjour.c` en un binaire `bonjour`, puis modifié `bonjour.c`. Que dit `./bonjour` ?"
    answers:
      - "La nouvelle version, puisque le code source a changé"
      - "L'ancienne version : le binaire a été fabriqué avant la modification, il faut recompiler"
      - "Une erreur, parce que le code source et le binaire ne correspondent plus"
    correct: 2
    explanation: "Le binaire est une traduction faite au moment de la compilation. Il ne sait rien des changements faits ensuite dans le code source : il faut recompiler pour en fabriquer un nouveau."
  - prompt: "Qu'est-ce qu'un runtime ?"
    answers:
      - "Un programme qu'on a compilé pour un processeur précis"
      - "Le binaire produit par un compilateur"
      - "Le programme qu'il faut avoir installé pour en exécuter un autre, comme Node.js pour du JavaScript"
    correct: 3
    explanation: "Un programme interprété ou en bytecode a besoin du programme qui le lit : bash pour un script, la JVM pour Java, Node.js pour du JavaScript. C'est son runtime."
```

```ack
J'ai compris
```

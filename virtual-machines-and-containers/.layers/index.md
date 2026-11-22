---
title: "Machines virtuelles et conteneurs : plusieurs machines sur une seule"
description: "Pourquoi faire tourner plusieurs « machines » sur un seul ordinateur : la machine virtuelle, un ordinateur entier simulé avec son propre noyau, le conteneur, isolé sur le noyau de l'hôte, et la même boîte du poste au serveur."
tags:
  - bit
  - virtualization
  - containers
  - computer
difficulty: beginner
duration: 12
requires: "0.8.0"
---

Un serveur fait tourner beaucoup de programmes, et le poste du développeur aussi. Vous saurez pourquoi on veut les isoler les uns des autres, ce qu'est une machine virtuelle, ce qu'est un conteneur, ce qui les distingue, et comment un conteneur fait tourner un programme à l'identique sur un poste et sur un serveur. Rien à installer, aucune commande à taper.

**Prérequis** : [L'ordinateur en couches](https://byte-layers.com/fr/bits/computer-layers), pour le matériel et le noyau ; [Compilé ou interprété](https://byte-layers.com/fr/bits/compiled-or-interpreted), pour le runtime ; [Les architectures d'un programme](https://byte-layers.com/fr/bits/program-architectures), pour l'appli Prêts de la bibliothèque.

# Machines virtuelles et conteneurs : plusieurs machines sur une seule

Les schémas reprennent la pile de couches : une machine, c'est son **matériel** et son **noyau**, et les programmes qui tournent sont posés sur le noyau.

## Un programme qui marche sur le poste, et pas sur le serveur

L'appli Prêts de la bibliothèque est écrite en JavaScript : son runtime est Node.js. Le développeur la fait tourner sur son poste, l'ordinateur sur lequel il travaille, puis l'installe sur le serveur de la bibliothèque.

```scene
lesson: assets/vm-containers.scene.json
step: probleme
```

Sur le poste, Node.js 22 ; sur le serveur, Node.js 18, installé il y a longtemps pour un autre programme. L'appli attend la version 22 : sur le serveur, elle tombe en panne. On ne peut pas simplement changer la version du serveur, puisque l'autre programme a besoin de la 18. Il faudrait, sur une même machine, des **environnements séparés**, chacun avec ses versions.

## Une machine virtuelle : un ordinateur entier, simulé

Première solution : simuler des ordinateurs. Un logiciel, l'**hyperviseur**, fabrique sur une seule machine réelle plusieurs **machines virtuelles** (*virtual machines*, VM), chacune avec son matériel virtuel : processeur, mémoire, disque.

```scene
lesson: assets/vm-containers.scene.json
step: machines-virtuelles
```

Chaque machine virtuelle a **son propre noyau** et son propre système d'exploitation : c'est un ordinateur complet, en logiciel. On peut y installer ce qu'on veut, Node.js 18 dans l'une, Node.js 22 dans l'autre, et même faire tourner Linux dans une fenêtre d'un Mac. La machine réelle, qui accueille les autres, s'appelle l'**hôte**. Le prix : chaque machine virtuelle réserve de la mémoire et du disque pour tout un système, et démarre comme un ordinateur.

L'hyperviseur existe sous deux formes, et la scène les dessine de la même façon :

| Hyperviseur | Où il vit | Exemples |
|---|---|---|
| **type 1** | intégré au système de la machine, sur les serveurs | KVM (dans Linux), Hyper-V, VMware ESXi |
| **type 2** | un logiciel installé sur un système existant, sur un poste | VirtualBox, VMware Workstation |

> 💡 **Remarque.** La « machine virtuelle Java » du bit sur la compilation n'a que le nom en commun : c'est un programme qui lit du bytecode, pas un ordinateur simulé.

## Un conteneur : isolé, sur le noyau de l'hôte

Seconde solution, plus légère : isoler les programmes sans simuler d'ordinateur. Un **conteneur** fait tourner un programme à part du reste de la machine, avec ses propres fichiers, mais **sans noyau à lui** : il utilise le noyau de l'hôte.

```scene
lesson: assets/vm-containers.scene.json
step: conteneurs
```

Les conteneurs sont créés, démarrés et isolés par un **moteur de conteneurs** (Docker, Podman), un programme installé sur la machine, comme l'hyperviseur pour les machines virtuelles. Mais le moteur ne simule rien : les programmes des conteneurs s'adressent **directement au noyau de l'hôte**. Pas de matériel simulé, pas de système entier à démarrer : un conteneur démarre comme un programme, et une machine en fait tourner bien plus que de machines virtuelles. En échange, l'isolation est moins forte, puisque tous les conteneurs partagent le **même noyau**, et un conteneur fait pour Linux a besoin d'un noyau Linux.

> 💡 **Remarque.** Sur Mac ou sous Windows, il n'y a pas de noyau Linux. Le moteur de conteneurs y fait donc tourner une petite machine virtuelle Linux, qui accueille les conteneurs : machines virtuelles et conteneurs se combinent déjà sur votre poste.

## Machine virtuelle ou conteneur

Les deux isolent des programmes sur une même machine ; ils ne le font pas au même niveau. Posons les deux piles côte à côte, sur le même serveur.

```scene
lesson: assets/vm-plan.scene.json
step: piles
```

Chaque machine virtuelle porte **un système entier** ; un conteneur, seulement **son appli et ses bibliothèques**. Le tableau détaille la différence.

| | Machine virtuelle | Conteneur |
|---|---|---|
| Ce qui est simulé ou isolé | un ordinateur entier : matériel simulé, noyau, système | un programme et ses fichiers |
| Le noyau | le sien, dans chaque machine virtuelle | celui de l'hôte, partagé |
| Le poids | celui d'un système entier | celui du programme et de ce qu'il emporte |
| Le démarrage | comme un ordinateur | comme un programme |
| L'isolation | forte : chaque machine virtuelle a son noyau ; seuls l'hyperviseur et le matériel sont partagés | moins forte : le noyau est partagé |
| On s'en sert pour | faire tourner un autre système, séparer des clients sur un même serveur | livrer une appli avec ce dont elle a besoin |

Les deux se combinent souvent : beaucoup de serveurs loués sur Internet sont des machines virtuelles, sur lesquelles tournent des conteneurs.

## Du poste au serveur : la même boîte

Revenons à l'appli Prêts. Mise dans un conteneur, elle **emporte** avec elle ce dont elle a besoin, son Node.js 22 compris.

```scene
lesson: assets/vm-containers.scene.json
step: dev-prod
```

Le serveur a lui aussi un moteur de conteneurs, et une copie du même conteneur y tourne, quel que soit le Node.js installé sur le serveur : l'appli n'en dépend plus. Sur le poste et en production, c'est-à-dire sur le serveur des vrais utilisateurs, **la même appli avec les mêmes versions** : beaucoup moins de surprises. Le moteur de conteneurs le plus connu s'appelle **Docker** ; le contenu [Pourquoi les conteneurs](https://byte-layers.com/fr/bits/containers-why) le présente, avec les images et les registres qui permettent de partager ces boîtes, et ce qu'un conteneur ne règle pas.

> 📖 [Machine virtuelle (Wikipédia)](https://fr.wikipedia.org/wiki/Machine_virtuelle) · [Qu'est-ce qu'un conteneur ? (Docker, en anglais)](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)

## Trois questions pour vérifier ce que vous avez retenu

```quiz
title: "Machines virtuelles et conteneurs"
tracksProgress: false
showNotice: false
place: stage
questions:
  - prompt: "Qu'est-ce qui distingue une machine virtuelle d'un conteneur ?"
    answers:
      - "La machine virtuelle a son propre noyau ; le conteneur utilise celui de l'hôte"
      - "Le conteneur a son propre noyau ; la machine virtuelle utilise celui de l'hôte"
      - "Aucune différence : ce sont deux noms pour la même chose"
    correct: 1
    explanation: "Une machine virtuelle est un ordinateur entier simulé, noyau compris. Un conteneur isole un programme mais partage le noyau de la machine qui l'accueille."
  - prompt: "Pourquoi un conteneur démarre-t-il plus vite qu'une machine virtuelle ?"
    answers:
      - "Parce qu'il a plus de mémoire qu'une machine virtuelle"
      - "Parce qu'il n'a ni matériel simulé ni système entier à démarrer : c'est un programme isolé"
      - "Parce qu'il tourne sur un autre ordinateur"
    correct: 2
    explanation: "Une machine virtuelle démarre comme un ordinateur, système compris. Un conteneur démarre comme un programme, sur le noyau déjà en marche de l'hôte."
  - prompt: "L'appli Prêts tourne dans un conteneur avec son Node.js 22. Le serveur a Node.js 18. Que se passe-t-il quand on y lance le même conteneur ?"
    answers:
      - "L'appli tombe en panne, comme sans conteneur"
      - "Le serveur remplace son Node.js 18 par le 22"
      - "L'appli marche : elle utilise le Node.js 22 emporté dans son conteneur"
    correct: 3
    explanation: "Le conteneur emporte ce dont l'appli a besoin. Elle ne dépend plus de ce qui est installé sur le serveur."
```

## Récap

- Plusieurs programmes sur une même machine ont parfois besoin de versions différentes : il faut des **environnements séparés**.
- Une **machine virtuelle** est un ordinateur entier simulé par un **hyperviseur**, avec son propre noyau : isolation forte, poids d'un système entier.
- Un **conteneur** isole un programme et ses fichiers en partageant le **noyau de l'hôte** : plus léger, démarre comme un programme.
- Un conteneur emporte ce dont l'appli a besoin : la même boîte tourne sur le poste et sur le serveur. **Docker** est l'outil le plus connu.

C'est la dernière étape de l'introduction. Le [quiz de fin d'introduction](https://byte-layers.com/fr/bits/intro-review) reprend les sept étapes, du matériel aux conteneurs.

```ack
J'ai compris
```

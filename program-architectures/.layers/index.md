---
title: "Les architectures d'un programme, du poste seul au n tiers"
description: "Où vivent les trois rôles d'une application (afficher, décider, stocker) : un poste, plusieurs postes, le deux tiers avec un client lourd, le trois tiers avec un client léger, le n tiers, les services externes, et pour aller plus loin les services et micro-services."
tags:
  - bit
  - architecture
  - computer
difficulty: beginner
duration: 12
requires: "0.8.0"
---

Un même programme peut être découpé et réparti de plusieurs façons entre les machines : c'est son **architecture**. Vous saurez reconnaître les formes les plus courantes (un poste, le deux tiers, le trois tiers, le n tiers), ce que chacune résout et ce qu'elle coûte. Le fil rouge est un seul programme, la gestion des prêts d'une bibliothèque ; chaque section a son schéma animé, que le bouton ▶ Jouer ouvre en grand.

**Prérequis** : [L'ordinateur en couches, du matériel au premier script](https://byte-layers.com/fr/bits/computer-layers), pour savoir ce que sont un programme, un disque et un serveur.

# Les architectures d'un programme, du poste seul au n tiers

Une bibliothèque prête des livres. Au comptoir, la bibliothécaire enregistre chaque prêt : qui emprunte quel livre, et jusqu'à quand. Elle se sert pour cela d'un programme, l'**appli Prêts**. Ce contenu suit ce programme à mesure que la bibliothèque grandit, et regarde où il s'installe.

Quelle que soit sa forme, l'appli Prêts tient toujours trois **rôles**. Les schémas les affichent sous chaque élément, comme des pastilles :

| Rôle | Ce qu'il fait dans l'appli Prêts |
|---|---|
| **afficher** | montrer les écrans et les formulaires, recevoir les clics et la saisie : c'est l'interface |
| **décider** | appliquer les règles de la bibliothèque : cinq livres au plus par lecteur, trois semaines de prêt, une amende par jour de retard. On parle de **règles métier** |
| **stocker** | garder les données : les livres, les lecteurs, les prêts, même ordinateur éteint |

Chaque architecture qui suit répond à une seule question : sur quelle machine vit chacun de ces trois rôles ?

## Un programme sur un poste

Un **poste**, c'est l'ordinateur sur lequel travaille un employé, ici celui du comptoir. Le programme dont on parle est une **application** : un programme avec une interface graphique, fait pour un utilisateur final, ici la bibliothécaire. Pas une commande qu'on tape dans un terminal.

La forme la plus simple installe l'appli Prêts sur ce poste, et tout y vit : l'appli affiche et décide, et elle range ses données dans un fichier, sur le disque du poste.

```scene
lesson: assets/architectures.scene.json
step: poste-seul
```

Une application se présente sous deux formes, et les deux noms reviendront dans la suite :

| Forme | Comment on la lance | Nom |
|---|---|---|
| un programme installé sur le poste | elle s'ouvre dans sa propre fenêtre | **client lourd** |
| une application web | elle s'ouvre dans le navigateur | **client léger** |

Le navigateur est lui-même un client lourd, déjà installé sur tous les postes : il sert à ouvrir les clients légers.

## Un programme sur plusieurs postes : comment gérer les données

Tout va bien tant qu'il n'y a qu'un comptoir. Quand la bibliothèque en ouvre un deuxième, on installe l'appli sur un deuxième poste, et ce poste a ses propres données.

```scene
lesson: assets/architectures.scene.json
step: plusieurs-postes
```

Un prêt enregistré au poste 1 n'existe pas pour le poste 2, qui répond « aucun prêt » pour un livre déjà sorti. Le problème est le **partage des données** : chaque poste a sa copie, et les copies ne se parlent pas. Les deux sections suivantes montrent les deux façons classiques de le résoudre.

## Deux tiers, avec un client lourd

Pour partager les données, on les sort des postes. Elles vont dans une **base de données** (BDD), un programme spécialisé qui range les données et répond aux demandes de lecture et d'écriture. Elle tourne sur un **serveur**, que tous les postes joignent à travers le réseau de la bibliothèque.

Sur chaque poste reste l'appli installée, le client lourd. Elle fait l'essentiel du travail elle-même : les écrans, les règles, les calculs. Elle ne demande au serveur que les données. Un programme qui demande, un programme qui répond : c'est la communication **client-serveur**. Il y a ici deux niveaux, les postes puis le serveur de données : on parle d'architecture **deux tiers** (*tiers* vient de l'anglais *tier*, « niveau »).

```scene
lesson: assets/architectures.scene.json
step: client-lourd
```

Un prêt saisi au poste 1 se lit au poste 3. Le prix : quand une nouvelle version de l'appli sort, il faut **mettre à jour chaque poste**. Avec quarante postes, c'est un chantier, et il suffit d'un poste oublié pour que deux versions de l'appli écrivent dans la même base.

> 💡 **Remarque.** Historiquement, c'étaient les clients lourds qui parlaient directement à la base de données. Aujourd'hui, selon la base utilisée, une application web peut parfois le faire aussi.

## Trois tiers, avec un client léger

Le **navigateur** (Firefox, Chrome, Edge, Safari) est déjà installé sur tous les postes. Dans cette forme, il est le seul programme dont les postes ont besoin : il affiche les pages de l'appli Prêts, c'est le client léger.

On reste en client-serveur, mais avec une machine de plus au milieu : un **serveur web**. C'est lui qui fait tourner l'appli Prêts, applique les règles et fait les traitements ; on l'appelle aussi le **backend**. Le navigateur ne parle pas à la base : il demande au serveur web, qui demande à la base.

| Rôle | Où il vit | Nom du niveau |
|---|---|---|
| afficher | le navigateur, sur chaque poste | tiers **présentation** |
| décider | l'appli Prêts, sur le serveur web | tiers **métier** |
| stocker | la base de données, sur son serveur | tiers **données** |

Trois niveaux : l'architecture **trois tiers**.

```scene
lesson: assets/architectures.scene.json
step: client-leger
```

La mise à jour change tout : le technicien installe la nouvelle version **une seule fois**, sur le serveur web, et les trois postes l'ont dès leur prochaine page.

## Le n tiers : on compte les machines

Le « n » de **n tiers** compte les **machines**, les serveurs par lesquels passe une demande, pas les programmes ni les couches de code. Dans la très grande majorité des cas, il reste **une seule base de données**, même si elle est parfois répartie sur plusieurs machines : on parle alors d'un **cluster** de base de données.

```scene
lesson: assets/architectures.scene.json
step: n-tiers
```

Deux exemples courants :

| Tiers | Les machines, dans l'ordre |
|---|---|
| **4 tiers** | le navigateur ; un serveur web en façade, qui envoie les fichiers fixes et passe le reste (on l'appelle souvent *reverse proxy*) ; le serveur d'application, qui applique les règles ; le serveur de base de données |
| **5 tiers** | les mêmes, plus un serveur pour une tâche à part : l'envoi des mails, une file d'attente de messages, ou un serveur d'intégration qui relie l'appli à d'autres logiciels |

Chaque machine de plus a une tâche précise, et on peut lui donner plus de puissance sans toucher aux autres. En contrepartie, il y a plus de machines à surveiller.

> 📖 [La relation client-serveur (MDN)](https://developer.mozilla.org/fr/docs/Learn_web_development/Extensions/Server-side/First_steps/Client-Server_overview) · [Comment fonctionne le Web (MDN)](https://developer.mozilla.org/fr/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works)

## Des programmes qui ne sont pas à vous : les services externes

La bibliothèque veut accepter la carte bancaire, et ne plus retaper le titre de chaque nouveau livre. Elle n'écrit aucun de ces deux programmes : ils **existent déjà, chez d'autres**.

```scene
lesson: assets/architectures.scene.json
step: externes
```

Un programme tenu par une autre organisation, dont on se sert à distance, est un **service externe**. Pour lui parler, l'appli Prêts passe par son **API** : le guichet qu'un programme ouvre aux autres programmes, avec la liste des demandes qu'il accepte. Vous n'avez rien à écrire ni à héberger. En contrepartie, vous dépendez de lui : prestataire en panne, plus de paiement par carte.

> 💡 **Remarque.** La plupart de ces échanges passent aujourd'hui par le web. Comment, ce sera l'objet du module sur le réseau.

## Pour aller plus loin : services et micro-services

Les grandes applications vont plus loin que le n tiers : elles se découpent en **services**. Pensez à un restaurant qui passe du cuisinier seul à une **brigade** : chacun son poste, et ils se passent les assiettes.

```scene
lesson: assets/architectures.scene.json
step: services
```

Chaque service a une seule tâche et, souvent, **ses propres données** : Recherche a son catalogue, Paiement ses amendes. Les services se parlent par leurs API, comme avec un service externe, et l'application mélange services internes et externes. On parle d'architecture **orientée services** (*SOA*), ou de **micro-services** quand ils sont nombreux et petits. On peut modifier ou remplacer un service sans toucher aux autres ; en échange, il faut des outils et une organisation pour déployer et surveiller tous ces programmes.

## Quatre questions pour vérifier ce que vous avez retenu

```quiz
title: "Les architectures d'un programme"
tracksProgress: false
showNotice: false
place: stage
questions:
  - prompt: "La bibliothèque a installé son appli de prêts sur deux postes, chacun avec ses propres données. Quel problème rencontre-t-elle ?"
    answers:
      - "Un prêt enregistré sur un poste n'est pas visible depuis l'autre"
      - "Les deux postes ne peuvent pas afficher les mêmes écrans"
      - "L'appli ne peut pas appliquer les règles de prêt sans serveur"
    correct: 1
    explanation: "Chaque poste range ses données sur son propre disque. Les deux copies ne se parlent pas : c'est le problème du partage des données, que la base de données sur un serveur résout."
  - prompt: "Une nouvelle version de l'appli sort. Dans quelle architecture suffit-il de l'installer à un seul endroit ?"
    answers:
      - "Le client lourd, parce que la base de données est sur un serveur"
      - "Le client léger, parce que l'appli tourne sur le serveur web et que les postes n'ont qu'un navigateur"
      - "Un programme sur un poste, parce que tout est sur la même machine"
    correct: 2
    explanation: "Avec un client lourd, l'appli est installée sur chaque poste : il faut la mettre à jour partout. Avec un client léger, elle vit sur le serveur web, et chaque poste reçoit la nouvelle version à sa prochaine page."
  - prompt: "Dans une architecture trois tiers, où vit le rôle « décider », celui des règles métier ?"
    answers:
      - "Dans le navigateur de chaque poste"
      - "Dans la base de données"
      - "Sur le serveur web, dans l'appli"
    correct: 3
    explanation: "Le navigateur affiche (tiers présentation), le serveur web décide (tiers métier) et la base de données stocke (tiers données)."
  - prompt: "Une demande passe par le navigateur, un serveur web en façade, un serveur d'application et un serveur de base de données. Combien de tiers ?"
    answers:
      - "Quatre : on compte les machines par lesquelles passe la demande"
      - "Trois : présentation, métier, données"
      - "Un seul, puisqu'il n'y a qu'une base de données"
    correct: 1
    explanation: "Le « n » du n tiers compte les machines, pas les rôles ni les programmes : ici quatre, avec une seule base."
```

## Récap

- Une application tient trois rôles : afficher, décider, stocker. Son architecture dit où vit chacun.
- **Un poste** : les trois rôles sur la même machine. Sur plusieurs postes, les données ne se partagent pas.
- **Deux tiers**, avec un **client lourd** : l'appli installée sur chaque poste, en client-serveur avec la base ; les données sont partagées, mais chaque mise à jour se fait poste par poste.
- **Trois tiers**, avec un **client léger** : afficher dans le navigateur, décider sur le serveur web (le backend), stocker dans la base ; rien à installer sur les postes.
- **n tiers** : n compte les machines par lesquelles passe une demande ; la base reste en général une seule.
- **Service externe** : un programme tenu par quelqu'un d'autre, dont on se sert à travers son **API**.
- **Pour aller plus loin** : des services, chacun sa tâche et ses données (architecture orientée services, micro-services).

Le schéma pose la bibliothèque sous ses formes, côte à côte, avec une zone pour aller plus loin. Reste une question : comment ces programmes se parlent-ils, d'une machine à l'autre ? Ce sera l'objet d'un module sur le réseau, à venir.

```scene
lesson: assets/architectures.scene.json
step: recap
```

```ack
J'ai compris
```

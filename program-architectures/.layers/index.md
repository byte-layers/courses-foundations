---
title: "Les architectures d'un programme, du poste seul au n tiers"
description: "Où vivent les trois rôles d'un programme (afficher, décider, stocker) : un poste seul, le client lourd, le client léger en trois tiers, puis plusieurs programmes qui collaborent."
tags:
  - bit
  - architecture
  - computer
difficulty: beginner
duration: 12
requires: "0.5.0"
---

Un même programme peut être découpé et réparti de plusieurs façons entre les machines : c'est son **architecture**. Vous saurez reconnaître les quatre formes les plus courantes (un poste seul, le client lourd, le client léger, plusieurs programmes qui collaborent), ce que chacune résout et ce qu'elle coûte. Le fil rouge est un seul programme, la gestion des prêts d'une bibliothèque ; chaque section a son schéma animé, que le bouton ▶ Jouer ouvre en grand.

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

## Un programme sur un poste : les données ne se partagent pas

Un **poste**, c'est l'ordinateur sur lequel travaille un employé, ici celui du comptoir. La forme la plus simple installe l'appli Prêts sur ce poste, et tout y vit : l'appli affiche et décide, et elle range ses données dans un fichier, sur le disque du poste.

Tout va bien tant qu'il n'y a qu'un comptoir. Quand la bibliothèque en ouvre un deuxième, on installe l'appli sur un deuxième poste, et ce poste a ses propres données. Le schéma montre la conséquence : un prêt enregistré au poste 1 n'existe pas pour le poste 2, qui répond « aucun prêt » pour un livre déjà sorti.

```scene
lesson: assets/architectures.scene.json
step: poste-seul
```

Le problème est le **partage des données** : chaque poste a sa copie, et les copies ne se parlent pas.

## Le client lourd, ou deux tiers : une base partagée, une mise à jour par poste

Pour partager les données, on les sort des postes. Elles vont dans une **base de données** (BDD), un programme spécialisé qui range les données et répond aux demandes de lecture et d'écriture. Elle tourne sur un **serveur**, que tous les postes joignent à travers le réseau de la bibliothèque. Le rôle « stocker » quitte les postes ; « afficher » et « décider » y restent, dans l'appli installée sur chaque poste.

Cette appli installée, qui fait l'essentiel du travail et ne demande au serveur que les données, s'appelle un **client lourd**. Le mot **client** désigne le programme qui demande un service à un serveur. L'ensemble forme une architecture **deux tiers** : *tiers* vient de l'anglais *tier*, « niveau », et il y a ici deux niveaux, les postes puis le serveur de données.

Le schéma montre ce que cela change : un prêt saisi au poste 1 se lit au poste 3. Il montre aussi le prix à payer : quand une nouvelle version de l'appli sort, un technicien doit l'installer sur chaque poste, un par un.

```scene
lesson: assets/architectures.scene.json
step: client-lourd
```

Avec trois postes, la mise à jour reste faisable. Avec quarante, répartis dans plusieurs bibliothèques, elle devient un chantier, et il suffit d'un poste oublié pour que deux versions de l'appli écrivent dans la même base.

## Le client léger, ou trois tiers : rien à installer sur les postes

Le **navigateur** (Firefox, Chrome, Edge, Safari) est déjà installé sur tous les postes. Dans cette forme, il est le seul programme dont les postes ont besoin : il affiche les pages de l'appli Prêts, et rien d'autre. C'est le **client léger**. L'appli elle-même tourne sur un **serveur web**, une machine qui fabrique les pages et applique les règles ; la base de données reste sur son serveur.

Chacun des trois rôles a désormais sa place :

| Rôle | Où il vit | Nom du niveau |
|---|---|---|
| afficher | le navigateur, sur chaque poste | tiers **présentation** |
| décider | l'appli Prêts, sur le serveur web | tiers **métier** |
| stocker | la base de données, sur son serveur | tiers **données** |

Trois niveaux, c'est l'architecture **trois tiers**. Client léger et trois tiers décrivent la même installation, vue de deux côtés : le premier nom regarde le poste, qui n'a presque rien à faire ; le second regarde l'ensemble, rangé en trois niveaux.

Le schéma suit un prêt du navigateur jusqu'à la base, puis montre une mise à jour : le technicien installe la nouvelle version une seule fois, sur le serveur web, et les trois postes l'ont dès leur prochaine page.

```scene
lesson: assets/architectures.scene.json
step: client-leger
```

## Plusieurs programmes qui collaborent : le n tiers

La bibliothèque grandit encore. Elle veut une recherche dans le catalogue, un mail automatique aux lecteurs en retard, l'encaissement des amendes. On pourrait tout ajouter dans l'appli Prêts, mais elle deviendrait énorme : la moindre modification de la recherche obligerait à remettre en route tout le programme, prêts compris.

Pensez à un restaurant. Au début, un cuisinier seul fait tout : les entrées, les plats, les desserts, la vaisselle. Quand la salle se remplit, on passe à une **brigade** : chacun son poste, et ils se passent les assiettes. Le restaurant sert plus de monde, et on peut remplacer le pâtissier sans fermer la cuisine.

Les programmes font de même. Chaque tâche devient un programme à part, parfois sur sa propre machine : **Recherche** trouve les livres du catalogue, **Paiement** encaisse les amendes, **Mails de retard** tourne seul chaque nuit et écrit aux lecteurs concernés. L'appli Prêts ne fait plus tout : elle demande aux autres. Le rôle « décider » est désormais réparti entre plusieurs programmes. Comme le nombre de niveaux n'est plus fixé, on parle d'architecture **n tiers**.

Le schéma montre trois de ces collaborations : une recherche, le paiement d'une amende, puis l'envoi des mails de retard pendant la nuit, sans personne devant l'écran.

```scene
lesson: assets/architectures.scene.json
step: n-tiers
```

Chaque programme a une seule tâche : on peut le modifier, le remplacer ou lui donner une machine plus puissante sans toucher aux autres. En contrepartie, il y a plus de machines à surveiller et plus d'échanges entre programmes.

> 📖 [La relation client-serveur (MDN)](https://developer.mozilla.org/fr/docs/Learn_web_development/Extensions/Server-side/First_steps/Client-Server_overview) · [Comment fonctionne le Web (MDN)](https://developer.mozilla.org/fr/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works)

## Des programmes qui ne sont pas à vous : les services externes

La bibliothèque veut accepter la carte bancaire, et ne plus retaper le titre de chaque nouveau livre. Elle n'écrit aucun de ces deux programmes : ils **existent déjà, chez d'autres**.

```scene
lesson: assets/architectures.scene.json
step: externes
```

Un programme tenu par une autre organisation, dont on se sert à distance, est un **service externe**. Pour lui parler, l'appli Prêts passe par son **API** : le guichet qu'un programme ouvre aux autres programmes, avec la liste des demandes qu'il accepte. Vous n'avez rien à écrire ni à héberger. En contrepartie, vous dépendez de lui : prestataire en panne, plus de paiement par carte.

> 💡 **Remarque.** La plupart de ces échanges passent aujourd'hui par le web. Comment, ce sera l'objet du module sur le réseau.

## Récap

- Tout programme tient trois rôles : afficher, décider, stocker. Son architecture dit où vit chacun.
- **Un poste** : les trois rôles sur la même machine ; simple, mais les données ne se partagent pas.
- **Client lourd** (deux tiers) : l'appli installée sur chaque poste, la base de données sur un serveur ; les données sont partagées, mais chaque mise à jour se fait poste par poste.
- **Client léger** (trois tiers) : afficher dans le navigateur, décider sur le serveur web, stocker dans la base ; rien à installer sur les postes.
- **n tiers** : plusieurs programmes qui collaborent, chacun sa tâche, comme une brigade en cuisine.
- **Service externe** : un programme tenu par quelqu'un d'autre, dont on se sert à travers son **API**.

Le schéma pose la bibliothèque sous ses quatre formes, côte à côte. Reste une question : comment ces programmes se parlent-ils, d'une machine à l'autre ? Ce sera l'objet d'un module sur le réseau, à venir.

```scene
lesson: assets/architectures.scene.json
step: recap
```

Trois questions pour vérifier ce que vous avez retenu.

```quiz
title: "Les architectures d'un programme"
tracksProgress: false
showNotice: false
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
```

```ack
J'ai compris
```

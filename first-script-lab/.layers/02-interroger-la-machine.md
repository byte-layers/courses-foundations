---
title: "02 - Interroger la machine avec quatre commandes"
description: "hostname, whoami, date et df : ce que chaque commande demande, et quelle couche répond"
---

Avant de ranger des commandes dans un script, on les essaie une par une. Les quatre commandes de cette étape ne modifient rien : chacune est un petit programme qui pose une question à la machine et écrit la réponse, que le terminal affiche. Pour obtenir l'information, chaque programme passe par le **noyau**, la couche qui connaît le matériel, avec un appel système, comme dans le bit sur les couches.

## 02.1 - Le nom de la machine avec hostname

Un ordinateur a un nom, qui le désigne sur un réseau. `hostname` l'affiche.

```exec "Afficher le nom de la machine"
hostname
```

Le terminal répond par un nom, différent sur chaque machine. Sur un Mac, par exemple :

```text
MacBook-Pro-de-Alice.local
```

Sous Windows, le nom ressemble plutôt à `DESKTOP-AB12CD`.

## 02.2 - Votre nom d'utilisateur avec whoami

Plusieurs personnes peuvent avoir un compte sur la même machine. `whoami` (*who am I*, « qui suis-je ») affiche le compte avec lequel vous êtes connecté.

```exec "Afficher l'utilisateur connecté"
whoami
```

La réponse est votre nom de compte, souvent votre prénom :

```text
alice
```

## 02.3 - La date et l'heure avec date

`date` affiche la date et l'heure de l'horloge de la machine. Selon votre système et sa langue, le format change : en français ou en anglais, avec ou sans le fuseau horaire.

```exec "Afficher la date"
date
```

Sur un Mac réglé en français, la réponse ressemble à ceci :

```text
dim. 22 nov. 2026 10:14:03 CET
```

## 02.4 - L'espace disque avec df

`df` (*disk free*) affiche l'espace du disque. L'option `-h` (*human*) écrit les tailles en unités lisibles, `G` ou `Gi` pour des gigaoctets, et `~` demande le disque qui contient votre dossier personnel.

```exec "Afficher l'espace disque"
df -h ~
```

La réponse tient en deux lignes, ici sur un Mac :

```text
Filesystem      Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s5   926Gi   352Gi   519Gi    41%    5.9M  5.4G    0%   /System/Volumes/Data
```

La première ligne nomme les colonnes, la seconde décrit votre disque. Les colonnes qui comptent ici sont la taille totale (`Size`), l'espace occupé (`Used`) et l'espace libre (`Avail`) ; les autres varient d'un système à l'autre. Sous Linux réglé en français, les mêmes colonnes s'appellent `Taille`, `Utilisé` et `Dispo`.

## 02.5 - Ce que chaque commande demande

Les quatre réponses viennent du système, pas du terminal. Le tableau dit où chaque programme va chercher la sienne.

| Commande | Ce qu'elle demande | D'où vient la réponse |
|---|---|---|
| `hostname` | le nom de la machine | le noyau, qui garde ce nom |
| `whoami` | le compte connecté | le noyau donne le numéro du compte qui lance le programme ; `whoami` cherche le nom qui va avec |
| `date` | la date et l'heure | le noyau lit l'horloge du matériel ; `date` met l'heure en forme, dans la langue du système |
| `df -h ~` | l'espace du disque | le noyau, qui gère le disque |

Taper ces quatre commandes chaque fois qu'on veut la fiche de sa machine serait fastidieux. L'étape suivante les range dans un fichier.

> 📖 [Manuel de Bash (en anglais)](https://www.gnu.org/software/bash/manual/bash.html)

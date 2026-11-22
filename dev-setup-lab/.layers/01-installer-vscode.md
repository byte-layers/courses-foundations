---
title: "01 - Installer VS Code et y ouvrir votre dossier"
description: "Installer VS Code selon son système, ouvrir ~/byte-layers/foundations, retrouver les quatre zones de la fenêtre et ouvrir le terminal intégré"
---

VS Code est gratuit et s'installe comme n'importe quelle application. Une fois installé, on l'ouvre de préférence sur un **dossier** : celui de votre travail.

## 01.1 - Installer VS Code selon votre système

La page [code.visualstudio.com](https://code.visualstudio.com/download) propose le bon fichier pour chaque système. Le tableau dit quoi faire de ce fichier.

| Système | Le fichier à télécharger | L'installation |
|---|---|---|
| macOS | **macOS**, un fichier `.dmg` | ouvrez le `.dmg`, glissez **Visual Studio Code** dans le dossier **Applications**, puis éjectez le disque |
| Windows | **Windows**, l'installeur *User Installer* | lancez-le et gardez les options proposées par défaut ; à la fin, il lance VS Code |
| Linux | `.deb` pour Debian et Ubuntu, `.rpm` pour Fedora | ouvrez le fichier pour l'installer ; le système demande votre mot de passe. Voir aussi la [page Linux](https://code.visualstudio.com/docs/setup/linux) |

Lancez ensuite VS Code, comme une autre application : depuis le Launchpad ou Cmd+Espace sous macOS, le menu Démarrer sous Windows, le menu des applications sous Linux. Au premier lancement sous macOS, le système prévient que l'application vient d'Internet : choisissez **Ouvrir**.

VS Code s'affiche en anglais, avec une page d'accueil (*Welcome*) qui propose de choisir un thème : vous pouvez la fermer. Si votre système est en français, VS Code propose, en bas à droite, d'installer le module de langue française (*language pack*) ; vous pouvez accepter, il redémarre en français. Ce lab donne le nom anglais de chaque menu, suivi du nom français entre parenthèses.

## 01.2 - Ouvrir le dossier ~/byte-layers/foundations

Pour travailler sur `fiche.sh`, ouvrez tout le dossier qui le contient. Dans le menu **File (Fichier)**, choisissez **Open Folder… (Ouvrir le dossier…)**. Dans la fenêtre qui s'ouvre, allez dans le dossier en tapant son chemin, comme pour enregistrer `fiche.sh` au lab précédent :

| Système | Aller dans le dossier |
|---|---|
| macOS | Cmd+Maj+G, tapez `~/byte-layers/foundations`, Entrée, puis **Ouvrir** |
| Windows | cliquez dans la barre d'adresse, tapez `%USERPROFILE%\byte-layers\foundations`, Entrée, puis **Sélectionner un dossier** |
| Linux | Ctrl+L, tapez `~/byte-layers/foundations`, Entrée, puis **Ouvrir** |

VS Code demande alors si vous faites confiance aux auteurs des fichiers de ce dossier. Ce sont les vôtres : répondez **Yes, I trust the authors (Oui, je fais confiance aux auteurs)**. Sans cette confiance, VS Code désactive certaines fonctions dans ce dossier.

## 01.3 - Retrouver les quatre zones de la fenêtre

La fenêtre a les quatre zones vues dans le bit sur l'éditeur de code. Le tableau dit où les trouver chez vous.

| Zone | Ce que vous y voyez |
|---|---|
| **Barre d'activité**, tout à gauche | une colonne d'icônes ; la première, deux feuilles, affiche l'explorateur |
| **Explorateur** | `FOUNDATIONS`, le nom du dossier ouvert, avec `fiche.sh` et `fiche.txt` |
| **Zone d'édition**, au centre | vide pour l'instant, ou la page d'accueil |
| **Terminal intégré**, en bas | caché pour l'instant ; la section suivante l'ouvre |

À droite, un panneau de discussion (*Chat*) peut aussi s'ouvrir, et proposer de se connecter : fermez-le, il ne sert pas dans ce parcours.

Double-cliquez sur `fiche.sh` dans l'explorateur : il s'ouvre dans la zone d'édition, dans un onglet, **en couleurs**. VS Code a reconnu un script `bash` à son nom et à sa première ligne.

## 01.4 - Ouvrir le terminal intégré

Dans le menu **Terminal**, choisissez **New Terminal (Nouveau terminal)**. Un terminal s'ouvre en bas de la fenêtre, déjà placé dans le dossier ouvert.

Sous macOS et Linux, c'est le même shell que dans le terminal du système. **Sous Windows**, VS Code ouvre PowerShell par défaut : cliquez sur la petite flèche à droite du **+**, en haut du terminal, choisissez **Select Default Profile (Sélectionner le profil par défaut)**, puis **Git Bash**. Dans le terminal PowerShell, tapez `exit` pour le fermer, puis ouvrez-en un nouveau : c'est Git Bash.

Vérifiez où vous êtes, avec la commande du lab précédent :

```exec "Afficher le dossier courant"
pwd
```

Le terminal intégré répond par le chemin du dossier ouvert dans VS Code, ici sur un Mac :

```text
/Users/alice/byte-layers/foundations
```

Sous Linux, le chemin commence par `/home/`, et sous Git Bash par `/c/Users/`.

```verify
if [ ! -f ~/byte-layers/foundations/fiche.sh ]; then
  echo "Il n'y a pas de fiche.sh dans ~/byte-layers/foundations. Faites d'abord le lab « Votre premier script, sur votre machine »."
  exit 1
fi
echo "Le dossier du lab contient fiche.sh : vous pouvez travailler dessus."
```

## 01.5 - Installer l'extension byte_layers, sous macOS et Linux

VS Code installé, les boutons de vérification de ce lab peuvent fonctionner. Ils passent par l'**extension** byte_layers, un module qu'on ajoute à VS Code : la page [Comment ça marche](https://byte-layers.com/fr/comment-ca-marche) dit comment l'installer et rouvrir ce lab dedans. Elle n'existe pas encore pour Windows : sous Windows, continuez sur le site et comparez vos sorties à celles du lab. Cette section est facultative.

> 📖 [Installer VS Code (en anglais)](https://code.visualstudio.com/docs/setup/setup-overview) · [L'interface de VS Code (en anglais)](https://code.visualstudio.com/docs/getstarted/userinterface) · [Le terminal intégré (en anglais)](https://code.visualstudio.com/docs/terminal/basics)

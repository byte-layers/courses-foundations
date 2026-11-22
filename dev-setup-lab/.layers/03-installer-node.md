---
title: "03 - Installer Node.js, le runtime de JavaScript"
description: "Installer la version LTS de Node.js selon son système et vérifier sa version dans le terminal intégré"
---

Un programme en JavaScript est un texte, comme `fiche.sh`. Pour l'exécuter hors d'un navigateur, il faut son **runtime**, le programme qui le lit : **Node.js**. C'est ce que dit le bit « Compilé ou interprété », et c'est ce que vous installez maintenant.

## 03.1 - Installer la version LTS

Sur la page [nodejs.org](https://nodejs.org/fr/download), prenez la version marquée **LTS** (*Long Term Support*), la première proposée : elle reçoit des corrections pendant des années, c'est celle qu'on choisit pour apprendre et pour travailler.

La page commence par des commandes à copier : ignorez-les, elles supposent des outils que vous n'avez pas. Descendez jusqu'à la partie **Ou obtenez un Node.js® préconstruit**, choisissez votre système, puis téléchargez l'installeur.

| Système | L'installation |
|---|---|
| macOS | l'installeur `.pkg` ; ouvrez-le et suivez les étapes |
| Windows | l'installeur `.msi` ; lancez-le et gardez les options proposées par défaut |
| Linux | la partie Linux de la même page, qui donne les commandes à taper dans le terminal ; le logiciel fourni par votre version de Linux est souvent trop ancien |

Quittez VS Code, pour qu'il voie le programme installé : Cmd+Q sous macOS, menu **File > Exit (Fichier > Quitter)** ailleurs. Sous Windows surtout, un terminal ouvert avant l'installation ne connaît pas le nouveau programme. Relancez VS Code ; s'il ne rouvre pas le dossier `foundations`, choisissez **File > Open Recent (Fichier > Ouvrir les éléments récents)**. Rouvrez le terminal intégré, menu **Terminal**, **New Terminal (Nouveau terminal)**.

## 03.2 - Vérifier la version de Node.js

La commande `node`, installée avec Node.js, lance le runtime. Avec l'option `--version`, elle affiche seulement son numéro de version :

```exec "Afficher la version de Node.js"
node --version
```

Le terminal répond par un numéro qui commence par `v`. Celui-ci vient de la machine où le lab a été vérifié ; le vôtre sera sans doute plus récent :

```text
v22.18.0
```

Si le terminal répond `command not found`, l'installation n'est pas terminée, ou le terminal a été ouvert avant elle : quittez VS Code, relancez-le, et relancez la commande.

```verify
if ! command -v node >/dev/null 2>&1; then
  echo "La commande node est introuvable. Installez Node.js, puis quittez et relancez VS Code."
  exit 1
fi
echo "Node.js est installé : $(node --version)."
```

> 📖 [Télécharger Node.js](https://nodejs.org/fr/download) · [Introduction à Node.js (en anglais)](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs)

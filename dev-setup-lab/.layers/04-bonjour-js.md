---
title: "04 - Écrire et lancer bonjour.js, votre premier programme"
description: "Créer un fichier JavaScript depuis l'explorateur, l'exécuter avec node, le modifier et constater qu'il n'y a rien à refaire"
---

Votre premier programme tient en une ligne : il affiche un message. Vous l'écrivez dans VS Code, vous le faites lire par Node.js dans le terminal intégré, puis vous le modifiez.

## 04.1 - Créer bonjour.js depuis l'explorateur

Dans l'explorateur, survolez `FOUNDATIONS` : des icônes apparaissent à droite du nom. Cliquez sur la première, **New File… (Nouveau fichier…)**, tapez le nom `bonjour.js`, puis Entrée. Le fichier vide s'ouvre dans la zone d'édition. La fin du nom, `.js`, qu'on appelle l'extension du fichier, dit à VS Code et aux lecteurs que c'est du JavaScript.

Tapez cette ligne, puis enregistrez avec Cmd+S ou Ctrl+S. En tapant `console.`, une liste de suggestions s'ouvre : continuez à taper, ou appuyez sur Échap. Les guillemets et les parenthèses se ferment d'eux-mêmes, comme dans `fiche.sh` :

```javascript
console.log("Bonjour depuis Node.js !");
```

Prenez-la comme une recette : `console.log(…)` affiche ce qu'on met entre les parenthèses, ici un texte entre guillemets, et le `;` termine l'instruction. Le parcours de JavaScript expliquera chaque morceau.

## 04.2 - Lancer le programme avec node

Dans le terminal intégré, `node` suivi du nom du fichier demande à Node.js de lire ce fichier et d'exécuter ses instructions, comme `bash fiche.sh` pour un script :

```exec "Lancer bonjour.js"
node bonjour.js
```

Le terminal affiche le message :

```text
Bonjour depuis Node.js !
```

```verify
F=~/byte-layers/foundations/bonjour.js
if [ ! -f "$F" ]; then
  echo "Il n'y a pas de bonjour.js dans ~/byte-layers/foundations. Créez-le depuis l'explorateur de VS Code, puis enregistrez."
  exit 1
fi
if ! command -v node >/dev/null 2>&1; then
  echo "La commande node est introuvable. Installez Node.js, puis quittez et relancez VS Code."
  exit 1
fi
OUT=$(cd ~/byte-layers/foundations && node bonjour.js 2>&1)
if [ $? -ne 0 ]; then
  echo "node bonjour.js échoue : $OUT"
  exit 1
fi
if [ -z "$OUT" ]; then
  echo "node bonjour.js n'affiche rien. Vérifiez la ligne console.log(\"…\"); et enregistrez."
  exit 1
fi
echo "Votre programme affiche : $OUT"
```

```hint
Si `node` répond `SyntaxError`, comparez votre ligne au modèle : les guillemets droits, les deux parenthèses, et rien d'autre sur la ligne. Si rien ne s'affiche, le fichier n'est peut-être pas enregistré : un rond plein sur l'onglet le signale.
```

## 04.3 - Modifier le texte et relancer

Remplacez `Bonjour` par `Salut` dans `bonjour.js`, enregistrez, puis relancez le programme :

```exec "Relancer bonjour.js"
node bonjour.js
```

Le nouveau texte s'affiche tout de suite :

```text
Salut depuis Node.js !
```

Il n'y a rien eu à refaire entre la modification et le lancement : Node.js relit le fichier à chaque fois, comme `bash` relit `fiche.sh`. C'est le trajet **interprété** du bit « Compilé ou interprété », et Node.js en est le **runtime**.

> 📖 [Exécuter un programme avec Node.js (en anglais)](https://nodejs.org/en/learn/command-line/run-nodejs-scripts-from-the-command-line) · [console.log, sur MDN](https://developer.mozilla.org/fr/docs/Web/API/console/log_static)

## Récap

- **VS Code** s'ouvre sur un dossier : l'explorateur montre ses fichiers, l'éditeur les affiche en couleurs, le **terminal intégré** lance les commandes dans ce dossier.
- Les couleurs et les numéros de ligne aident à trouver une faute ; la **fermeture automatique** évite d'en faire certaines.
- **Node.js** est le runtime de JavaScript : `node bonjour.js` lit le fichier et exécute ses instructions, et une modification se voit au lancement suivant.

Votre programme tourne en entier sur votre machine. Ceux que vous utilisez tous les jours, un site web ou une application de banque, se répartissent souvent entre plusieurs machines : c'est l'objet du contenu [Les architectures d'un programme](https://byte-layers.com/fr/bits/program-architectures).

Si votre parcours passe par Java, l'étape suivante est pour vous.

## Questions

```quiz
title: "Votre poste de développeur"
tracksProgress: false
showNotice: false
questions:
  - prompt: "Pourquoi ouvrir le dossier foundations dans VS Code, plutôt que le seul fichier fiche.sh ?"
    answers:
      - "Parce que VS Code refuse d'ouvrir un fichier seul"
      - "Pour avoir tous les fichiers du dossier dans l'explorateur, et un terminal intégré placé dans ce dossier"
      - "Pour que le fichier soit enregistré en texte brut"
    correct: 2
    explanation: "Ouvert sur un dossier, VS Code montre tous ses fichiers dans l'explorateur, et le terminal intégré démarre dans ce dossier."
  - prompt: "Après une modification de bonjour.js, que faut-il faire avant de relancer `node bonjour.js` ?"
    answers:
      - "Recompiler le programme"
      - "Réinstaller Node.js"
      - "Seulement enregistrer le fichier : Node.js le relit à chaque lancement"
    correct: 3
    explanation: "Node.js interprète le fichier : il le relit à chaque lancement. Il suffit d'enregistrer la modification."
  - prompt: "Dans ce lab, quel est le rôle de Node.js ?"
    answers:
      - "C'est le runtime : le programme qui lit bonjour.js et le fait exécuter"
      - "C'est l'éditeur dans lequel on écrit bonjour.js"
      - "C'est le compilateur qui traduit bonjour.js en binaire"
    correct: 1
    explanation: "Node.js est le runtime de JavaScript hors du navigateur. VS Code est l'éditeur, et on ne lance soi-même aucune compilation."
```

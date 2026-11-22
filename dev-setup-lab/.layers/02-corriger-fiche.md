---
title: "02 - Corriger une faute dans fiche.sh avec l'aide de l'éditeur"
description: "Ajouter une ligne à fiche.sh, y glisser une faute exprès, la voir aux couleurs, la lire dans le terminal intégré et la corriger"
---

Au lab précédent, une faute dans `fiche.sh` ne se voyait qu'au lancement. Cette fois, vous en glissez une exprès, pour voir ce que l'éditeur de code montre avant même de lancer le script.

## 02.1 - Ajouter une ligne, et la casser exprès

On veut que la fiche affiche aussi le dossier courant, que donne `pwd`. Dans l'onglet `fiche.sh`, placez le curseur à la fin de la ligne 5, `echo "Date : $(date)"`, appuyez sur Entrée, puis tapez :

```bash
echo "Dossier : $(pwd)"
```

La nouvelle ligne est la ligne 6, et `df -h ~` passe en ligne 7. Dès la première lettre, un rond plein remplace la croix sur l'onglet : le fichier est modifié, et pas encore enregistré.

En tapant le premier guillemet, vous avez sans doute vu VS Code écrire **lui-même** le guillemet de fin, et la parenthèse fermante après `(`. C'est la **fermeture automatique** : l'éditeur ferme ce que vous ouvrez, pour éviter justement la faute de ce lab. Si vous tapez quand même le caractère de fin, VS Code passe par-dessus au lieu d'en ajouter un.

Pour voir ce qui se passe sans cette aide, placez le curseur tout au bout de la ligne 6, puis appuyez une fois sur la touche d'effacement (Retour arrière, ⌫) : le dernier guillemet disparaît. Regardez la ligne 7 : `df -h ~` a pris la couleur des textes entre guillemets. Pour l'éditeur, le texte ouvert à la ligne 6 n'est jamais fermé, et il continue jusqu'au bout du fichier.

Enregistrez le fichier avec Cmd+S sous macOS, Ctrl+S ailleurs : le rond plein redevient une croix.

## 02.2 - Lire l'erreur dans le terminal intégré

Lancez le script dans le terminal intégré, sans changer de fenêtre :

```exec "Lancer fiche.sh"
bash fiche.sh
```

`bash` exécute les lignes qu'il comprend, puis s'arrête :

```text
Machine : MacBook-Pro-de-Alice.local
Utilisateur : alice
Date : dim. 22 nov. 2026 10:14:03 CET
fiche.sh: line 6: unexpected EOF while looking for matching `"'
fiche.sh: line 8: syntax error: unexpected end of file
```

Les trois premières lignes viennent des commandes que `bash` a lancées avant de buter : il lit et exécute le script au fur et à mesure. Le message, en anglais, dit qu'il a atteint la fin du fichier (*EOF*, *end of file*) en cherchant le guillemet qui ferme celui de la ligne 6 (*looking for matching*). Selon la version de `bash`, une seconde ligne d'erreur parle de la fin du fichier. L'espace disque ne s'affiche pas : pour `bash` aussi, `df -h ~` fait partie du texte resté ouvert. Les numéros de ligne s'affichent à gauche de l'éditeur : on va directement à la ligne 6.

## 02.3 - Corriger et relancer

Remettez le guillemet à la fin de la ligne 6, enregistrez, puis relancez :

```exec "Relancer fiche.sh"
bash fiche.sh
```

La fiche est complète, avec une ligne de plus avant l'espace disque :

```text
Machine : MacBook-Pro-de-Alice.local
Utilisateur : alice
Date : dim. 22 nov. 2026 10:16:28 CET
Dossier : /Users/alice/byte-layers/foundations
Filesystem      Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s5   926Gi   352Gi   519Gi    41%    5.9M  5.4G    0%   /System/Volumes/Data
```

Les couleurs pour voir la faute, le numéro de ligne pour la trouver, le terminal dans la même fenêtre pour relancer : c'est ce qui manquait au lab précédent.

```verify
F=~/byte-layers/foundations/fiche.sh
if ! grep -q 'Dossier' "$F"; then
  echo "fiche.sh n'a pas encore la ligne du dossier. Ajoutez echo \"Dossier : \$(pwd)\" après la ligne 5, puis enregistrez."
  exit 1
fi
if ! bash -n "$F" 2>/dev/null; then
  echo "bash refuse encore de lire fiche.sh. Remettez le guillemet de fin sur la ligne 6, puis enregistrez."
  exit 1
fi
if ! (cd ~/byte-layers/foundations && bash fiche.sh 2>&1) | grep -q '^Dossier : /'; then
  echo "fiche.sh n'affiche pas le dossier courant. Vérifiez la ligne : echo \"Dossier : \$(pwd)\", avec des guillemets droits doubles."
  exit 1
fi
echo "fiche.sh affiche le dossier courant, et bash sait le lire."
```

```hint
Si la vérification échoue alors que la ligne vous semble juste, regardez l'onglet `fiche.sh` : un rond plein à la place de la croix veut dire que le fichier n'est pas enregistré. Si la ligne 6 finit par deux guillemets, l'éditeur en a ajouté un : effacez-en un.
```

> 📖 [Modifier du code dans VS Code (en anglais)](https://code.visualstudio.com/docs/editing/codebasics)

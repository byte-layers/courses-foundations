---
title: "04 - Lancer fiche.sh et ranger la fiche dans un fichier"
description: "Faire lire le script par bash, puis envoyer ce qu'il affiche dans fiche.txt avec une redirection"
---

Le script est écrit. Il reste à le faire lire par `bash`, puis à garder son résultat dans un fichier plutôt qu'à l'écran.

## 04.1 - Lancer le script avec bash

La commande `bash fiche.sh` demande à `bash` de lire le fichier et d'exécuter ses lignes, l'une après l'autre. Tapez-la depuis `~/byte-layers/foundations` :

```exec "Lancer fiche.sh"
bash fiche.sh
```

Le terminal affiche la fiche de votre machine, avec vos propres valeurs :

```text
Machine : MacBook-Pro-de-Alice.local
Utilisateur : alice
Date : dim. 22 nov. 2026 10:14:03 CET
Filesystem      Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s5   926Gi   352Gi   519Gi    41%    5.9M  5.4G    0%   /System/Volumes/Data
```

Vos quatre commandes ont tourné d'un coup, dans l'ordre du fichier.

> 💡 **Remarque.** Le bit sur les couches lançait `hello.sh` avec `./hello.sh`, après `chmod +x`. `bash fiche.sh` donne le même résultat sans changer les droits du fichier : on désigne soi-même le programme qui doit le lire.

```hint
Si `bash` répond `No such file or directory`, vous n'êtes pas dans le bon dossier : tapez `cd ~/byte-layers/foundations`, puis relancez. Si la sortie se termine par `df: ~: No such file or directory`, ou cite `$'\r'`, le fichier a des fins de ligne Windows : lancez `dos2unix fiche.sh`. Si une ligne affiche une erreur qui cite un numéro de ligne, ouvrez à nouveau `fiche.sh` dans l'éditeur et comparez cette ligne, et celle d'avant, au modèle : un guillemet ou une parenthèse manque souvent.
```

## 04.2 - Ranger la fiche dans fiche.txt

Pour garder la fiche, on envoie ce que le script affiche dans un fichier, au lieu de l'écran. C'est une **redirection**, avec le signe `>` :

```exec "Ranger la fiche dans fiche.txt"
bash fiche.sh > fiche.txt
```

Cette fois, le terminal n'affiche rien : tout est parti dans `fiche.txt`, que la commande a créé.

> 🔍 **Comprendre la commande** `bash fiche.sh > fiche.txt`
>
> | Morceau | Rôle |
> |---|---|
> | `bash fiche.sh` | lance le script, comme à la section précédente |
> | `>` | une **redirection** : envoie ce que la commande affiche dans un fichier, au lieu du terminal |
> | `fiche.txt` | le fichier qui reçoit la fiche ; `>` le crée s'il n'existe pas, et **remplace** son contenu s'il existe |

`cat`, vu dans le bit sur les couches, affiche le contenu d'un fichier. Lisez la fiche :

```exec "Lire fiche.txt"
cat fiche.txt
```

Vous retrouvez la fiche que le script affichait tout à l'heure :

```text
Machine : MacBook-Pro-de-Alice.local
Utilisateur : alice
Date : dim. 22 nov. 2026 10:14:03 CET
Filesystem      Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s5   926Gi   352Gi   519Gi    41%    5.9M  5.4G    0%   /System/Volumes/Data
```

Attendez quelques secondes, relancez `bash fiche.sh > fiche.txt`, puis `cat fiche.txt` : la date a changé, parce que le script redemande tout à chaque lancement, et `>` a remplacé l'ancienne fiche.

```verify
F=~/byte-layers/foundations/fiche.txt
if [ ! -f "$F" ]; then
  echo "Il n'y a pas encore de fiche.txt. Depuis ~/byte-layers/foundations, lancez bash fiche.sh > fiche.txt."
  exit 1
fi
for label in "Machine :" "Utilisateur :" "Date :"; do
  if ! grep -q "^$label" "$F"; then
    echo "fiche.txt ne contient pas la ligne « $label ». Relancez bash fiche.sh > fiche.txt."
    exit 1
  fi
done
if [ "$(wc -l < "$F")" -lt 5 ]; then
  echo "fiche.txt n'a pas les lignes de l'espace disque. Vérifiez la dernière ligne de fiche.sh, df -h ~, puis lancez dos2unix fiche.sh si vous êtes sous Windows."
  exit 1
fi
echo "fiche.txt contient la fiche de votre machine."
```

> 📖 [Les redirections, dans le manuel de Bash (en anglais)](https://www.gnu.org/software/bash/manual/html_node/Redirections.html)

## 04.3 - Ce qui a manqué pour écrire

Le script marche, mais repensez à la façon dont vous l'avez écrit. Le Bloc-notes et TextEdit affichent tout en noir, sans distinguer une commande d'un texte entre guillemets. Une faute de frappe ne se voyait qu'au lancement, dans une autre fenêtre, avec un message qui ne pointe pas toujours la bonne ligne. Pour un script de six lignes, ça passe ; pour un programme de cent lignes, beaucoup moins.

## Récap

- Le **terminal** de votre système est Terminal sous macOS et Linux, **Git Bash** sous Windows ; vos fichiers vivent dans `~/byte-layers/foundations`.
- `hostname`, `whoami`, `date` et `df -h ~` posent une question à la machine, et c'est le **noyau** qui répond.
- Un script s'écrit dans un **éditeur de texte**, en texte brut, avec des guillemets droits ; `$(commande)` met la réponse d'une commande dans un texte.
- `bash fiche.sh` fait lire le script par `bash` ; `>` envoie ce qu'il affiche dans un fichier, en remplaçant son contenu.

Écrire un programme sans aide, c'est possible, mais lent. Il existe des éditeurs faits pour ça : c'est l'objet du contenu [De l'éditeur de texte à l'éditeur de code](https://byte-layers.com/fr/bits/code-editor).

## Questions

```quiz
title: "Votre premier script, sur votre machine"
tracksProgress: false
showNotice: false
questions:
  - prompt: "Dans fiche.sh, que devient `$(whoami)` quand bash lit la ligne `echo \"Utilisateur : $(whoami)\"` ?"
    answers:
      - "Il reste écrit tel quel : `Utilisateur : $(whoami)`"
      - "Il est remplacé par la réponse de la commande `whoami`, votre nom d'utilisateur"
      - "Il provoque une erreur, parce qu'une commande ne peut pas être entre guillemets"
    correct: 2
    explanation: "C'est une substitution : le shell lance la commande entre `$(` et `)` d'abord, puis met sa réponse à la place."
  - prompt: "Vous lancez `bash fiche.sh > fiche.txt`. Pourquoi le terminal n'affiche-t-il rien ?"
    answers:
      - "Parce que le script a échoué"
      - "Parce que `>` envoie ce que le script affiche dans fiche.txt, au lieu du terminal"
      - "Parce que bash attend qu'on appuie une seconde fois sur Entrée"
    correct: 2
    explanation: "La redirection `>` envoie la sortie de la commande dans un fichier. On la lit ensuite avec `cat fiche.txt`."
  - prompt: "Pourquoi ne pas écrire fiche.sh dans Word ?"
    answers:
      - "Parce que Word enregistre aussi la mise en forme, que bash ne sait pas lire"
      - "Parce que Word ne sait pas enregistrer de fichier de six lignes"
      - "Parce qu'un script doit obligatoirement s'écrire dans le terminal"
    correct: 1
    explanation: "Un script est du texte brut. Un traitement de texte ajoute au fichier de quoi le mettre en forme, et remplace souvent les guillemets droits."
```

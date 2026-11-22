---
title: "03 - Écrire fiche.sh avec l'éditeur de texte du système"
description: "Ouvrir l'éditeur de texte de son système, y écrire les six lignes du script et l'enregistrer en texte brut dans le dossier du lab"
---

Un script est un fichier de texte qui contient des commandes. Pour l'écrire, il faut un **éditeur de texte** : un programme qui enregistre les caractères que vous tapez, sans mise en forme. C'est ce qu'on appelle du **texte brut**. Chaque système a son éditeur de texte. Word ou LibreOffice Writer ne conviennent pas : par défaut, ils enregistrent avec le texte de quoi le mettre en forme, que le shell ne sait pas lire.

## 03.1 - Ouvrir l'éditeur de texte et le régler

On peut tout éditer **depuis le terminal**, sans le quitter : l'éditeur occupe alors la fenêtre du terminal et se pilote au clavier. On parle d'interface en mode texte, ou **TUI** (*text user interface*). On peut aussi éditer **en mode graphique**, ou **GUI** (*graphical user interface*) : l'éditeur ouvre sa propre fenêtre, et la souris sert aussi. Dans les deux cas, il existe de simples éditeurs de texte et des **IDE** (*environnement de développement intégré*), des éditeurs qui ajoutent de quoi écrire, lancer et vérifier du code.

| | Éditeur de texte | IDE |
|---|---|---|
| **Dans le terminal (TUI)** | `nano` | `vim` ou Neovim, enrichis d'extensions |
| **En mode graphique (GUI)** | TextEdit, Bloc-notes, Éditeur de texte | VS Code, IntelliJ IDEA |

Pour ce premier script, on prend l'**éditeur de texte graphique** de votre système : il est déjà installé et s'utilise comme n'importe quelle application. Les IDE viendront plus tard, avec le contenu [L'éditeur de code](https://byte-layers.com/fr/bits/code-editor).

Le tableau suivant dit quel éditeur ouvrir, et le réglage à faire avant de taper.

| Système | L'éditeur | Le réglage |
|---|---|---|
| macOS | **TextEdit** (Cmd+Espace, « TextEdit ») | une fois pour toutes, voir ci-dessous |
| Windows | **Bloc-notes** (menu Démarrer, « Bloc-notes ») | aucun |
| Linux | **Éditeur de texte** sous GNOME (Ubuntu, Fedora), **KWrite** sous KDE | aucun |

**Sous macOS**, TextEdit corrige ce que vous tapez comme un traitement de texte : il met des majuscules, corrige des mots qu'il ne connaît pas (`df` peut devenir `de`) et remplace les guillemets droits `"` par des guillemets typographiques, que `bash` ne reconnaît pas. Avant d'écrire, ouvrez le menu **TextEdit > Réglages**, onglet **Nouveau document** :

- dans **Format**, choisissez **Texte** ;
- dans **Options**, décochez **Corriger l'orthographe automatiquement**, **Guillemets intelligents** et **Tirets intelligents**.

Fermez les réglages. TextEdit affiche une fenêtre pour choisir un fichier : cliquez sur **Nouveau document**. Dans les autres systèmes, l'éditeur s'ouvre directement sur une page vide.

## 03.2 - Taper les six lignes du script

Tapez ces six lignes dans l'éditeur, ou copiez-les depuis cette page et collez-les, en gardant les guillemets droits `"` et les parenthèses :

```bash
#!/bin/bash
# fiche.sh : la fiche de ma machine
echo "Machine : $(hostname)"
echo "Utilisateur : $(whoami)"
echo "Date : $(date)"
df -h ~
```

Chaque ligne a son rôle. Les deux premières viennent du bit sur les couches ; les autres reprennent les commandes de l'étape précédente.

| Ligne | Ce qu'elle fait |
|---|---|
| `#!/bin/bash` | dit au système que ce fichier se lit avec `bash`, quand on le lance comme `./hello.sh` dans le bit sur les couches |
| `# fiche.sh : …` | un **commentaire** : une ligne qui commence par `#` est ignorée par `bash`, elle sert au lecteur |
| `echo "Machine : $(hostname)"` | affiche le texte entre guillemets, où `$(hostname)` est remplacé par la réponse de `hostname` |
| `echo "Utilisateur : $(whoami)"` | de même, avec le nom de l'utilisateur |
| `echo "Date : $(date)"` | de même, avec la date |
| `df -h ~` | affiche l'espace disque, comme à l'étape précédente |

> 🔍 **Comprendre la commande** `echo "Machine : $(hostname)"`
>
> | Morceau | Rôle |
> |---|---|
> | `echo` | affiche ce qui le suit |
> | `"…"` | les guillemets gardent ensemble le texte à afficher, espaces compris |
> | `Machine : ` | du texte, affiché tel quel |
> | `$(hostname)` | une **substitution** : le shell lance `hostname` d'abord, et met sa réponse à la place |

## 03.3 - Enregistrer le fichier dans le dossier du lab

Enregistrez avec Cmd+S sous macOS, Ctrl+S ailleurs. Dans la fenêtre d'enregistrement, tapez le nom **`fiche.sh`**, exactement, puis allez dans le dossier du lab. Le plus sûr est de taper son chemin :

| Système | Aller dans le dossier du lab |
|---|---|
| macOS | Cmd+Maj+G, tapez `~/byte-layers/foundations`, puis Entrée |
| Windows | cliquez dans la barre d'adresse, en haut, tapez `%USERPROFILE%\byte-layers\foundations`, puis Entrée |
| Linux | Ctrl+L, tapez `~/byte-layers/foundations`, puis Entrée |

**Sous Windows**, réglez aussi le bas de la fenêtre : le type **Tous les fichiers**, sinon le Bloc-notes ajoute `.txt` au nom, et l'encodage **UTF-8**, pas « UTF-8 avec BOM ». L'**encodage** est la façon d'écrire chaque caractère en nombres dans le fichier ; avec BOM, le Bloc-notes ajoute au début des caractères invisibles qui gênent `bash`.

> ⚠️ **Si TextEdit demande s'il faut utiliser l'extension `.txt`**, choisissez de garder `.sh`.

De retour dans le terminal, `ls` liste les fichiers du dossier courant. C'est le seul contrôle fiable : l'explorateur de Windows cache souvent la fin des noms.

```exec "Lister les fichiers du dossier"
ls
```

La réponse liste un seul fichier, au nom exact :

```text
fiche.sh
```

Si vous lisez `fiche.sh.txt` ou `fiche.sh.rtf`, renommez-le avec `mv`, suivi du nom lu puis de `fiche.sh`, par exemple `mv fiche.sh.txt fiche.sh`. Si la liste est vide, le fichier a été enregistré ailleurs : enregistrez-le à nouveau, dans `byte-layers/foundations`.

**Sous Windows seulement**, une dernière correction. Le Bloc-notes termine chaque ligne par deux caractères invisibles, là où `bash` n'en attend qu'un. La commande `dos2unix`, installée avec Git Bash, convertit le fichier :

```exec "Sous Windows : convertir les fins de ligne"
dos2unix fiche.sh
```

Elle répond par une ligne qui dit qu'elle a converti le fichier :

```text
dos2unix: converting file fiche.sh to Unix format...
```

```verify
F=~/byte-layers/foundations/fiche.sh
if [ ! -f "$F" ]; then
  echo "Il n'y a pas de fichier fiche.sh dans ~/byte-layers/foundations. Lancez ls : si vous lisez fiche.sh.txt ou fiche.sh.rtf, renommez-le avec mv."
  exit 1
fi
if head -c 6 "$F" | grep -q 'rtf'; then
  echo "fiche.sh est enregistré en texte enrichi. Dans TextEdit, choisissez Format > Convertir au format texte, puis enregistrez à nouveau."
  exit 1
fi
if [ "$(head -c 3 "$F" | od -An -tx1 | tr -d ' ')" = "efbbbf" ]; then
  echo "fiche.sh commence par des caractères invisibles (UTF-8 avec BOM). Enregistrez-le à nouveau avec l'encodage UTF-8."
  exit 1
fi
if grep -qF -e '“' -e '”' -e '«' -e '»' "$F"; then
  echo "fiche.sh contient des guillemets typographiques (“ ” ou « »). Remplacez-les par des guillemets droits \", et désactivez les guillemets intelligents de l'éditeur."
  exit 1
fi
if grep -q "$(printf '\r')" "$F"; then
  echo "fiche.sh a des fins de ligne Windows. Dans Git Bash, lancez dos2unix fiche.sh depuis ~/byte-layers/foundations."
  exit 1
fi
for piece in '$(hostname)' '$(whoami)' '$(date)' 'df -h'; do
  if ! grep -qF "$piece" "$F"; then
    echo "fiche.sh ne contient pas $piece. Comparez votre fichier aux six lignes du modèle."
    exit 1
  fi
done
if [ "$(grep -c '^echo ' "$F")" -lt 3 ]; then
  echo "fiche.sh devrait avoir trois lignes qui commencent par echo, en minuscules. Comparez-le au modèle."
  exit 1
fi
if ! bash -n "$F" 2>/dev/null; then
  echo "bash refuse de lire fiche.sh : un guillemet ou une parenthèse manque. Comparez chaque ligne au modèle."
  exit 1
fi
echo "fiche.sh contient les quatre commandes, et bash sait le lire."
```

> 📖 [Les réglages de TextEdit (Apple)](https://support.apple.com/fr-fr/guide/textedit/txted1063/mac) · [La substitution de commande, dans le manuel de Bash (en anglais)](https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html)

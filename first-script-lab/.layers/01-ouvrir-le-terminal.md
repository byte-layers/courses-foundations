---
title: "01 - Ouvrir le terminal de votre ordinateur"
description: "Trouver le terminal de son système, ou installer Git Bash sous Windows, puis créer le dossier du lab"
---

Le terminal est un programme comme un autre : il suffit de le trouver dans votre système. Une fois ouvert, vous y créez le dossier où vivront vos fichiers.

## 01.1 - Trouver le terminal de votre système

Chaque système a le sien. Le tableau dit où le trouver.

| Système | Le terminal | Comment l'ouvrir |
|---|---|---|
| macOS | **Terminal** | Cmd+Espace, tapez « Terminal », puis Entrée |
| Linux | **Terminal** (selon la distribution : Console, Konsole) | Ctrl+Alt+T, ou cherchez « Terminal » dans le menu des applications |
| Windows | **Git Bash**, à installer | voir ci-dessous |

Sous Windows, le terminal fourni, PowerShell, ne lit pas les scripts `bash` comme celui que vous allez écrire, et plusieurs commandes y répondent autrement. Installez **Git for Windows**, qui apporte **Git Bash**, un terminal qui comprend les mêmes commandes que Linux et macOS :

1. Sur [la page officielle](https://git-scm.com/install/windows), téléchargez l'installeur proposé (*Git for Windows Setup*, en version x64 pour la plupart des PC).
2. Lancez-le. Windows demande s'il faut autoriser l'application à modifier l'appareil : répondez **Oui**.
3. L'installeur est en anglais et compte une quinzaine d'écrans : gardez les options proposées et cliquez sur **Next** jusqu'à **Install**, puis **Finish**.
4. Ouvrez Git Bash depuis le menu Démarrer, en cherchant « Git Bash ».

Git for Windows installe aussi Git, un outil que vous rencontrerez plus tard.

Une fenêtre s'ouvre, avec une ligne qui se termine par `$` ou `%` et un curseur qui clignote : c'est l'**invite**. Le shell attend votre commande. Sous Git Bash, l'invite tient sur deux lignes, la première avec votre nom et `MINGW64`, la seconde avec `$`.

> 💡 **Remarque.** Sous macOS, le terminal lance `zsh`, un shell cousin de `bash`. Les commandes de ce lab s'y tapent de la même façon, et le script sera lu par `bash`, qui est aussi installé.

## 01.2 - Taper ou coller une commande

Vous pouvez taper chaque commande, ou la copier depuis cette page et la coller dans le terminal. Le raccourci pour coller dépend du terminal :

| Terminal | Coller |
|---|---|
| Terminal de macOS | Cmd+V |
| Terminal de Linux | Ctrl+Maj+V |
| Git Bash | Maj+Inser |

> ⚠️ **Si vous tapez à la main sur un clavier français**, le signe `~` ne s'obtient pas directement : Option+N puis Espace sur Mac, AltGr+é puis Espace sous Windows et Linux.

## 01.3 - Savoir où vous êtes avec pwd

Première commande, déjà vue dans le bit sur les couches : `pwd` affiche le dossier dans lequel le shell travaille. Tapez-la, puis Entrée.

```exec "Afficher le dossier courant"
pwd
```

Le terminal répond par le **chemin** de votre dossier personnel, celui que `~` désigne : la suite des dossiers à ouvrir pour y arriver, depuis le tout premier, `/`. Sur un Mac, pour le compte `alice` :

```text
/Users/alice
```

Sous Linux, le chemin commence par `/home/`, et sous Git Bash par `/c/Users/`.

## 01.4 - Créer le dossier du lab

Vos fichiers vont dans `~/byte-layers/foundations`. Ce dossier n'existe pas encore : `mkdir` le crée.

```exec "Créer le dossier du lab"
mkdir -p ~/byte-layers/foundations
```

L'option `-p` crée aussi `byte-layers` s'il manque, et ne dit rien si le dossier existe déjà. Si tout s'est bien passé, le terminal n'affiche rien et rend l'invite.

Entrez maintenant dans ce dossier avec `cd`, puis vérifiez avec `pwd` :

```exec "Entrer dans le dossier du lab"
cd ~/byte-layers/foundations
pwd
```

`pwd` montre que vous êtes bien dans le dossier du lab :

```text
/Users/alice/byte-layers/foundations
```

À partir d'ici, toutes les commandes du lab se tapent depuis ce dossier. Si vous fermez le terminal, rouvrez-le et retapez `cd ~/byte-layers/foundations`.

```verify
if [ ! -d ~/byte-layers/foundations ]; then
  echo "Le dossier ~/byte-layers/foundations n'existe pas. Lancez mkdir -p ~/byte-layers/foundations."
  exit 1
fi
echo "Le dossier ~/byte-layers/foundations existe."
```

> 📖 [Guide d'utilisation de Terminal sur Mac (Apple)](https://support.apple.com/fr-fr/guide/terminal/welcome/mac) · [Installer Git for Windows](https://git-scm.com/install/windows) · [Ligne de commande pour débutants (Ubuntu, en anglais)](https://ubuntu.com/tutorials/command-line-for-beginners)

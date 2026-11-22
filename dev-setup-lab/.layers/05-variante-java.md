---
title: "05 - Variante Java : compiler avec javac, lancer avec java"
description: "Pour les parcours qui passent par Java : installer le JDK, écrire Bonjour.java, le compiler en bytecode, le lancer avec la JVM, et constater qu'une modification demande de recompiler"
---

**Cette étape est pour vous si votre parcours passe par Java.** Sinon, le lab est terminé.

Java ne suit pas le trajet de Node.js : le code source est d'abord **compilé** en bytecode par `javac`, puis la **machine virtuelle Java** (JVM) lit ce bytecode. C'est le troisième trajet du bit « Compilé ou interprété », et vous allez le voir dans l'explorateur de VS Code.

## 05.1 - Installer le JDK

Le **JDK** (*Java Development Kit*) contient le compilateur `javac` et la JVM, lancée par la commande `java`. Une distribution gratuite et répandue est **Temurin**, sur [adoptium.net](https://adoptium.net/fr/temurin/releases). La page affiche des filtres : choisissez votre système, son architecture (`aarch64` pour un Mac récent, `x64` pour la plupart des PC), le type **JDK**, la dernière version **LTS**, puis téléchargez l'installeur.

| Système | L'installation |
|---|---|
| macOS | l'installeur `.pkg` ; ouvrez-le et suivez les étapes |
| Windows | l'installeur `.msi` ; gardez les options proposées par défaut, qui ajoutent `java` et `javac` aux commandes connues du terminal |
| Linux | les commandes de la page [Installation d'Adoptium (en anglais)](https://adoptium.net/installation/linux), à taper dans le terminal |

Comme pour Node.js, quittez VS Code, relancez-le, puis rouvrez le terminal intégré. Vérifiez la version du compilateur :

```exec "Afficher la version de javac"
javac -version
```

Le terminal répond par un numéro de version, peut-être plus récent :

```text
javac 25.0.2
```

Si un message dit `Unable to locate a Java Runtime`, ou si une fenêtre propose d'installer Java, le JDK n'est pas encore installé.

```verify
if ! javac -version >/dev/null 2>&1 || ! java -version >/dev/null 2>&1; then
  echo "javac ou java ne répond pas. Installez le JDK, puis quittez et relancez VS Code."
  exit 1
fi
echo "Le JDK est installé : $(javac -version 2>&1)."
```

## 05.2 - Écrire Bonjour.java

Depuis l'explorateur, créez un fichier nommé **`Bonjour.java`**, avec une majuscule : en Java, le nom du fichier doit être celui de la classe qu'il contient, à la majuscule près. Tapez ces cinq lignes, puis enregistrez. Attention aux accolades `{ }` : quand vous tapez `{` puis Entrée, VS Code écrit lui-même l'accolade fermante, plus bas ; ne la retapez pas. Une notification peut aussi proposer des extensions pour Java : ignorez-la pour ce lab.

```java
public class Bonjour {
    public static void main(String[] args) {
        System.out.println("Bonjour depuis Java !");
    }
}
```

Prenez-les comme une recette : en Java, tout programme est rangé dans une **classe**, ici `Bonjour`, et commence à `main`. La seule ligne qui agit est la troisième : `System.out.println(…)` affiche le texte entre parenthèses. Le parcours de Java expliquera le reste.

## 05.3 - Compiler avec javac

Avant de lancer le programme, on le compile. `javac` lit `Bonjour.java` et écrit le bytecode dans un nouveau fichier :

```exec "Compiler Bonjour.java"
javac Bonjour.java
```

Si tout va bien, le terminal n'affiche rien. Regardez l'explorateur : un fichier **`Bonjour.class`** est apparu à côté de `Bonjour.java`. C'est le bytecode ; il ne se lit pas comme un texte, et VS Code refuse de l'afficher : inutile de l'ouvrir.

Si `javac` trouve une faute, il refuse de compiler et dit où elle est, avant que rien ne s'exécute. Par exemple, sans le `;` de la ligne 3 :

```text
Bonjour.java:3: error: ';' expected
        System.out.println("Bonjour depuis Java !")
                                                   ^
1 error
```

## 05.4 - Lancer avec java

La commande `java` démarre la JVM, qui lit le bytecode. On lui donne le nom de la classe, **sans** extension :

```exec "Lancer le programme Java"
java Bonjour
```

La JVM exécute le bytecode, et le message s'affiche :

```text
Bonjour depuis Java !
```

## 05.5 - Modifier, et recompiler

Remplacez `Bonjour depuis` par `Salut depuis` dans `Bonjour.java`, enregistrez, puis relancez **sans recompiler** :

```exec "Relancer sans recompiler"
java Bonjour
```

Le message n'a pas changé :

```text
Bonjour depuis Java !
```

La JVM lit `Bonjour.class`, fabriqué avant votre modification. Recompilez, puis relancez :

```exec "Recompiler, puis relancer"
javac Bonjour.java && java Bonjour
```

Cette fois, le nouveau texte s'affiche :

```text
Salut depuis Java !
```

> 🔍 **Comprendre la commande** `javac Bonjour.java && java Bonjour`
>
> | Morceau | Rôle |
> |---|---|
> | `javac Bonjour.java` | compile le code source en bytecode, dans `Bonjour.class` |
> | `&&` | lance la commande suivante **seulement si** la première a réussi |
> | `java Bonjour` | lance la JVM sur le nouveau bytecode |

C'est la différence avec `bonjour.js` : un programme compilé ne change qu'après une nouvelle compilation.

> 💡 **Remarque.** Vous croiserez peut-être `java Bonjour.java`, qui compile et lance d'un coup, sans écrire de `.class`. C'est pratique pour un essai, mais ça cache l'étape que ce lab veut montrer.

```verify
D=~/byte-layers/foundations
if [ ! -f "$D/Bonjour.java" ]; then
  echo "Il n'y a pas de Bonjour.java dans ~/byte-layers/foundations. Créez-le, avec un B majuscule."
  exit 1
fi
if [ ! -f "$D/Bonjour.class" ]; then
  echo "Il n'y a pas encore de Bonjour.class. Lancez javac Bonjour.java."
  exit 1
fi
if [ "$D/Bonjour.java" -nt "$D/Bonjour.class" ]; then
  echo "Bonjour.java a été modifié après la dernière compilation. Lancez javac Bonjour.java."
  exit 1
fi
OUT=$(java -cp "$D" Bonjour 2>&1)
if [ $? -ne 0 ]; then
  echo "java Bonjour échoue : $OUT"
  exit 1
fi
echo "Votre programme Java, compilé après sa dernière modification, affiche : $OUT"
```

```hint
Si `java Bonjour` répond `Could not find or load main class`, vérifiez que vous êtes dans `~/byte-layers/foundations`, que `Bonjour.class` existe, et que vous n'avez pas tapé `java Bonjour.class` : le nom de la classe se donne sans extension. Si `javac` répond `class Bonjour is public, should be declared in a file named Bonjour.java`, le nom du fichier ne correspond pas : dans l'explorateur, clic droit sur le fichier, **Rename (Renommer)**, et un B majuscule. Si `javac` répond `class, interface, enum, or record expected`, une accolade fermante est en trop : comparez au modèle.
```

> 📖 [Compiler et lancer un premier programme Java (Oracle, en anglais)](https://dev.java/learn/getting-started/) · [Temurin, chez Adoptium](https://adoptium.net/fr/temurin/releases)

## Récap de la variante Java

- Le **JDK** apporte `javac`, le compilateur, et `java`, qui lance la JVM.
- `javac Bonjour.java` compile le code source en **bytecode**, `Bonjour.class` ; une faute est signalée avant toute exécution.
- `java Bonjour` lance la JVM sur ce bytecode ; après une modification, il faut **recompiler**.

"""Scène du bit 5 « Compilé ou interprété » (courses-foundations/compiled-or-interpreted).

Dessin repris du bit 1 (computer-layers, étape « Script »), retour de Boris du 22/11 : « la couche système de base et
des composants à côté, le terminal… le compilateur en ferait partie ». Une règle par sorte :
- le système de base = deux blocs au fond : le Noyau (r, ✱, comme le bit 1) et, à côté, le Processeur (n) ;
- devant, ce qu'on utilise : le Terminal (i, >_) où l'on tape, à côté du Shell bash (g, $) qui lance les programmes ;
- les programmes que le shell lance sont des blocs « programme » sur une rangée entre le shell et le noyau, comme
  ls, mkdir et date au bit 1 : les compilateurs (v), les runtimes (JVM, Node.js) verts comme bash ;
- les fichiers sont des blocs fichier à côté de qui les lit : source à gauche (y), ce qui est écrit à droite
  (binaire n, bytecode b).
Grille d'écran G(sx, sy) : trois rangées, terminal et shell 8, programmes -1, noyau et processeur -10.
Couleurs (légende) : y code source, v compilateur, n code machine (binaire, processeur), g runtime (programme qui en lit un autre :
bash, JVM, Node.js), b bytecode. Les paquets prennent la couleur de ce qu'ils portent.
"""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools" / "scenes"))
from paths import outputs
from scene_kit import G, L, scene, send, wait, write, hud

Y_SH, Y_PROG, Y_K = 8, -1, -10


def out(t):
    return {"do": "output", "text": t}


def typ(t):
    return {"do": "type", "text": t}


PROMPT = {"do": "prompt"}

ents = [
    {"id": "cpu", "kind": "node", "at": G(6, Y_K), "tone": "n", "title": "Processeur", "sub": "0101 1100 0011", "icon": "01",
     "detail": "Le **processeur** n'exécute qu'une sorte d'instructions : le **code machine**, des nombres propres à sa famille de processeurs."},
    {"id": "kbox", "kind": "node", "at": G(0, Y_K), "tone": "r", "title": "Noyau", "sub": "charge les programmes", "icon": "✱",
     "detail": "Le **noyau** charge les programmes en mémoire et leur partage le processeur. Tout programme passe par lui, quel que soit son langage."},
    {"id": "term", "kind": "node", "at": G(-6, Y_SH), "tone": "i", "title": "Terminal", "icon": ">_",
     "detail": "Le **terminal** affiche le texte et transmet ce que vous tapez au shell, comme au bit « L'ordinateur et ses couches »."},
    {"id": "bash", "kind": "node", "at": G(0, Y_SH), "tone": "g", "title": "Shell", "sub": "bash", "icon": "$",
     "detail": "`bash` lance les programmes qu'on lui demande. Il sait aussi lire un script : c'est un **interpréteur**, un programme déjà en code machine qui fait ce que dit chaque ligne."},
    {"id": "sh", "kind": "file", "at": G(5, Y_SH), "tone": "y", "title": "hello.sh",
     "detail": "Un **script** : du texte, écrit par une personne. Il reste un texte du début à la fin ; c'est `bash` qui le lit."},
    {"id": "cc", "kind": "program", "at": G(-4, Y_PROG), "tone": "v", "title": "compilateur C",
     "detail": "Le **compilateur** est un programme comme `ls` ou `date`, lancé par le shell. Il lit tout le code source et écrit un nouveau fichier, le **binaire**, en code machine. Il travaille avant l'exécution, pas pendant."},
    {"id": "csrc", "kind": "file", "at": G(-10, Y_PROG), "tone": "y", "title": "bonjour.c",
     "detail": "Le **code source** du programme, en langage C : un texte, comme un script. Le processeur ne sait pas le lire."},
    {"id": "bin", "kind": "file", "at": G(4, Y_PROG), "tone": "n", "title": "bonjour", "label": "binaire",
     "detail": "Le **binaire** : les instructions du programme en code machine. Le noyau le charge en mémoire et le processeur l'exécute. Il ne marche que pour une famille de processeurs et un système d'exploitation."},
    {"id": "javac", "kind": "program", "at": G(-5, Y_PROG), "tone": "v", "title": "javac", "label": "compilateur Java",
     "detail": "Le compilateur Java (`javac`) traduit le code source, mais pas en code machine : en **bytecode**."},
    {"id": "jsrc", "kind": "file", "at": G(-11, Y_PROG), "tone": "y", "title": "Bonjour.java",
     "detail": "Le code source en **Java** : encore un texte."},
    {"id": "cls", "kind": "file", "at": G(6, Y_SH), "tone": "b", "title": "Bonjour.class", "label": "bytecode",
     "detail": "Le **bytecode** : des instructions pour la machine virtuelle Java, pas pour le processeur. Le même fichier sert sur Windows, macOS et Linux."},
    {"id": "jvm", "kind": "node", "at": G(5, Y_PROG), "tone": "g", "title": "JVM", "sub": "machine virtuelle Java",
     "detail": "La **machine virtuelle Java** (JVM) est un programme en code machine qui lit le bytecode et le fait exécuter. Elle s'installe avec Java, une par système."},
    {"id": "node", "kind": "node", "at": G(2.5, Y_PROG), "tone": "g", "title": "Node.js",
     "detail": "**Node.js** lit et exécute du JavaScript hors du navigateur. Il s'installe à part."},
    {"id": "you", "kind": "actor", "at": G(11, 15), "label": "vous"},
    {"id": "js", "kind": "file", "at": G(2.5, Y_SH), "tone": "y", "title": "bonjour.js",
     "detail": "Un programme en **JavaScript** : un texte, lu par Node.js."},
]

TERM = {"kind": "terminal", "title": "alice@pc — bash", "prompt": "alice@pc", "cwd": "~"}
BASE = ["cpu", "kbox", "term", "bash"]
steps = []

# ---------- 1. interprété
steps.append({
    "id": "interprete", "label": "Interprété", "title": "Un script est lu ligne à ligne",
    "body": ["`bash` est un programme : il lit `hello.sh` une ligne après l'autre et fait ce qu'elle demande. Le fichier reste un texte."],
    "hud": [{"label": "trajet", "value": "interprété"}],
    "labels": "left",
    "show": BASE + ["sh"],
    "links": [L("term", "bash"), L("sh", "bash", dashed=True), L("bash", "kbox"), L("kbox", "cpu")],
    "widgets": [{"kind": "editor", "title": "hello.sh", "lang": "bash",
                 "lines": ["#!/bin/bash", "echo \"Bonjour $USER !\"", "date"]}, TERM],
    "script": [
        wait(600), typ("./hello.sh"),
        send(["term", "bash"], label="./hello.sh",
             explain=["Vous tapez `./hello.sh` : le terminal passe la ligne au **shell**, comme au bit 1."]),
        {"do": "line", "n": 1},
        send(["sh", "bash"], kind="read", tone="y", label="ligne 1",
             explain=["La ligne 1, `#!/bin/bash`, dit que c'est `bash` qui lit le fichier."]),
        {"do": "line", "n": 2},
        send(["sh", "bash"], kind="read", tone="y", label="ligne 2",
             explain=["`bash` lit la ligne 2 et la comprend : afficher un texte."]),
        send(["bash", "kbox", "cpu"], label="écrire",
             explain=["Il demande au **noyau** d'écrire ce texte à l'écran.",
                      "Le processeur exécute `bash`, pas le fichier : le fichier n'est qu'un texte."]),
        out("Bonjour alice !"), wait(300), {"do": "line", "n": 3},
        send(["sh", "bash"], kind="read", tone="y", label="ligne 3",
             explain=["Puis `bash` lit la ligne 3, après avoir exécuté la 2."]),
        send(["bash", "kbox", "cpu"], label="date",
             explain=["Il demande l'heure au noyau.",
                      "Du début à la fin, un **interpréteur** a lu le texte pour le processeur."]),
        out("dim. 22 nov. 2026 10:14:03"), {"do": "line", "n": 0}, PROMPT, wait(2200),
    ],
})

# ---------- 2. compilé
steps.append({
    "id": "compile", "label": "Compilé", "title": "Un compilateur traduit tout, une fois",
    "body": ["Le compilateur est un programme que le shell lance, comme `ls`. Il lit tout `bonjour.c` et écrit un nouveau fichier, le binaire, en code machine. Le noyau le charge et le processeur l'exécute, sans programme pour le lire."],
    "hud": [{"label": "trajet", "value": "compilé"}],
    "labels": "left",
    "show": BASE + ["csrc", "cc", {"id": "bin", "dim": True, "label": "pas encore écrit"}],
    "links": [L("term", "bash"), L("bash", "cc"), L("csrc", "cc"), L("kbox", "cpu")],
    "widgets": [TERM],
    "script": [
        wait(600), typ("cc bonjour.c -o bonjour"),
        send(["term", "bash", "cc"], label="cc",
             explain=["Vous tapez la commande du **compilateur** : le terminal la passe au shell.",
                      "Le shell lance le compilateur, un programme comme `ls` ou `date`."]),
        send(["csrc", "cc"], kind="read", tone="y", label="tout le fichier",
             explain=["Le compilateur lit tout `bonjour.c`, d'un bout à l'autre, avant que rien ne s'exécute."]),
        scene(say="Il écrit un nouveau fichier, le **binaire** : les mêmes instructions, en code machine.",
              set=[{"id": "bin", "dim": False, "label": "binaire"}], link=[L("cc", "bin")], ms=900),
        PROMPT, wait(500),
        scene(say="Pour lancer le programme, plus besoin du code source ni du compilateur.",
              set=[{"id": "csrc", "dim": True}, {"id": "cc", "dim": True}],
              unlink=[L("cc", "bin"), L("bash", "cc")], link=[L("bash", "bin"), L("bin", "kbox")]),
        typ("./bonjour"),
        send(["term", "bash", "bin"], label="./bonjour",
             explain=["Vous tapez `./bonjour` : le terminal passe la ligne au shell.",
                      "Le shell lance le **binaire**, comme il lance `ls` ou le compilateur."]),
        send(["bin", "kbox", "cpu"], tone="n", label="code machine",
             explain=["Le **noyau** le charge en mémoire : il est déjà en code machine…",
                      "… le **processeur** exécute ses instructions : aucun programme ne le lit à sa place."]),
        out("Bonjour !"), PROMPT, wait(2400),
    ],
})

# ---------- 3a. modifier un script : on relance, c'est tout
steps.append({
    "id": "modifier-script", "label": "Modifier un script", "title": "Modifier un script : on relance, c'est tout",
    "body": ["Vous changez une ligne de `hello.sh`, puis vous le relancez. `bash` relit le fichier : la modification se voit tout de suite."],
    "hud": [{"label": "à refaire", "value": "rien"}],
    "labels": "left",
    "show": BASE + [{"id": "sh", "note": "dit Bonjour"}, {"id": "you", "at": G(11, 15)}],
    "links": [L("you", "sh"), L("term", "bash"), L("sh", "bash", dashed=True), L("bash", "kbox"), L("kbox", "cpu")],
    "widgets": [TERM],
    "script": [
        wait(700),
        send(["you", "sh"], tone="y", label="Bonjour → Salut",
             explain=["Vous ouvrez `hello.sh` dans un éditeur et remplacez « Bonjour » par « Salut »."]),
        scene(say="Vous enregistrez : le fichier dit maintenant « Salut ».", set=[{"id": "sh", "note": "dit Salut"}]),
        typ("./hello.sh"),
        send(["term", "bash"], label="./hello.sh",
             explain=["Vous relancez le script, sans rien faire d'autre."]),
        send(["sh", "bash"], kind="read", tone="y", label="ligne 2",
             explain=["`bash` relit le fichier : il trouve la nouvelle ligne."]),
        send(["bash", "kbox", "cpu"], label="écrire",
             explain=["Il demande au noyau d'écrire le texte…", "… et le processeur exécute `bash`, comme avant."]),
        out("Salut alice !"), PROMPT,
        scene(say="Modifier, relancer : rien d'autre à refaire.", hud=[hud("à refaire", "rien", "g")]),
        wait(2400),
    ],
})

# ---------- 3b. modifier un programme compilé : il faut recompiler
steps.append({
    "id": "modifier-compile", "label": "Modifier du C", "title": "Modifier un programme compilé : recompiler",
    "body": ["Même changement dans `bonjour.c`. Le binaire, lui, a été écrit avant : tant qu'on ne recompile pas, il dit encore « Bonjour »."],
    "hud": [{"label": "binaire", "value": "à jour", "tone": "g"}],
    "labels": "left",
    "show": BASE + [{"id": "csrc", "note": "dit Bonjour"}, "cc", {"id": "bin", "label": None, "note": "dit Bonjour"},
                    {"id": "you", "at": G(-15, 6)}],
    "links": [L("you", "csrc"), L("term", "bash"), L("csrc", "cc"), L("cc", "bin", dashed=True),
              L("bash", "bin"), L("bin", "kbox"), L("kbox", "cpu")],
    "widgets": [TERM],
    "script": [
        wait(700),
        send(["you", "csrc"], tone="y", label="Bonjour → Salut",
             explain=["Vous faites le même changement dans `bonjour.c`."]),
        scene(say="Le code source dit « Salut »… mais le binaire a été écrit **avant** : il est périmé.",
              set=[{"id": "csrc", "note": "dit Salut"}], hud=[hud("binaire", "périmé", "r")]),
        typ("./bonjour"),
        send(["term", "bash", "bin"], label="./bonjour",
             explain=["Vous relancez le programme : le shell lance le binaire.", "C'est toujours l'ancien."]),
        send(["bin", "kbox", "cpu"], tone="n",
             explain=["Le noyau le charge…", "… et le processeur exécute l'ancienne version."]),
        out("Bonjour !"), PROMPT, wait(500),
        scene(say="Il faut **recompiler** : relancer le compilateur.", link=[L("bash", "cc")]),
        typ("cc bonjour.c -o bonjour"),
        send(["term", "bash", "cc"], label="recompiler",
             explain=["Vous relancez la commande du compilateur…", "… que le shell lance, comme la première fois."]),
        send(["csrc", "cc", "bin"], kind="read", tone="y",
             explain=["Le compilateur relit tout `bonjour.c`…", "… et écrit un nouveau binaire à la place de l'ancien."]),
        scene(say="Le binaire est à jour.", set=[{"id": "bin", "note": "dit Salut"}], hud=[hud("binaire", "à jour", "g")]),
        PROMPT, typ("./bonjour"),
        send(["term", "bash", "bin"], label="./bonjour",
             explain=["Vous relancez le programme.", "Le shell lance le nouveau binaire."]),
        send(["bin", "kbox", "cpu"], tone="n",
             explain=["Le noyau le charge…", "… et le processeur exécute la nouvelle version."]),
        out("Salut !"), PROMPT, wait(2400),
    ],
})

# ---------- 4. bytecode
steps.append({
    "id": "bytecode", "label": "Java", "title": "Java : compilé, puis lu par une machine virtuelle",
    "body": ["Le compilateur Java écrit du bytecode ; la machine virtuelle Java le lit et le fait exécuter."],
    "hud": [{"label": "trajet", "value": "bytecode"}],
    "labels": "left",
    "show": BASE + ["jsrc", "javac", "jvm", {"id": "cls", "dim": True, "label": "pas encore écrit"}],
    "links": [L("term", "bash"), L("bash", "javac"), L("jsrc", "javac"), L("kbox", "cpu")],
    "widgets": [TERM],
    "script": [
        wait(600), typ("javac Bonjour.java"),
        send(["term", "bash", "javac"], label="javac",
             explain=["Vous tapez `javac Bonjour.java` : le terminal passe la ligne au shell.",
                      "Le shell lance le compilateur Java, `javac`."]),
        send(["jsrc", "javac"], kind="read", tone="y", label="tout le fichier",
             explain=["`javac` lit tout `Bonjour.java`."]),
        scene(say="Il écrit `Bonjour.class` : du **bytecode**, pas du code machine.",
              set=[{"id": "cls", "dim": False, "label": "bytecode"}], link=[L("javac", "cls")], ms=900),
        PROMPT, wait(400),
        scene(say="Pour lancer le programme, on passe par la **machine virtuelle Java**.",
              set=[{"id": "jsrc", "dim": True}, {"id": "javac", "dim": True}],
              unlink=[L("bash", "javac"), L("javac", "cls")],
              link=[L("bash", "jvm"), L("cls", "jvm", dashed=True), L("jvm", "kbox")]),
        typ("java Bonjour"),
        send(["term", "bash", "jvm"], label="java Bonjour",
             explain=["`java Bonjour` : le shell lance la JVM.", "La JVM démarre : c'est elle qui va lire le bytecode."]),
        send(["cls", "jvm"], kind="read", tone="b", label="bytecode",
             explain=["Elle lit `Bonjour.class`."]),
        send(["jvm", "kbox", "cpu"], label="exécuter",
             explain=["Elle passe par le noyau, comme tout programme.",
                      "Le processeur exécute la JVM, qui fait ce que dit le bytecode."]),
        out("Bonjour !"), PROMPT, wait(2400),
    ],
})

# ---------- 5. runtime (récap) : les runtimes sur la rangée des programmes, leurs fichiers devant eux
steps.append({
    "id": "runtime", "label": "Runtime", "title": "Le runtime : ce qu'il faut avoir installé",
    "body": ["Un script a besoin de son interpréteur, le bytecode de sa machine virtuelle, le JavaScript de Node.js : c'est leur runtime. Le binaire n'a besoin que du système."],
    "hud": [{"label": "runtime", "value": "—"}],
    "show": ["cpu", "kbox",
             {"id": "bash", "at": G(-9, Y_PROG)}, {"id": "jvm", "at": G(-3, Y_PROG), "sub": None},
             {"id": "node", "at": G(3, Y_PROG)},
             {"id": "sh", "at": G(-9, Y_SH)}, {"id": "cls", "at": G(-3, Y_SH), "label": None},
             {"id": "js", "at": G(3, Y_SH)},
             {"id": "bin", "at": G(9, Y_PROG), "label": "aucun runtime"}],
    "links": [L("sh", "bash", dashed=True), L("cls", "jvm", dashed=True), L("js", "node", dashed=True),
              L("bash", "kbox"), L("jvm", "kbox"), L("node", "kbox"), L("bin", "kbox"), L("kbox", "cpu")],
    "script": [
        wait(700),
        scene(hud=[hud("runtime", "bash")]),
        send(["sh", "bash", "kbox"], kind="read", tone="y",
             explain=["Un script a besoin de son interpréteur, `bash` : c'est son **runtime**.", "`bash` fait travailler le noyau."]),
        scene(hud=[hud("runtime", "JVM")]),
        send(["cls", "jvm", "kbox"], kind="read", tone="b",
             explain=["Le bytecode a besoin de la JVM.", "La JVM fait travailler le noyau."]),
        scene(hud=[hud("runtime", "Node.js")]),
        send(["js", "node", "kbox"], kind="read", tone="y",
             explain=["Un programme JavaScript a besoin de **Node.js**.", "Node.js fait travailler le noyau."]),
        scene(hud=[hud("runtime", "aucun")]),
        send(["bin", "kbox", "cpu"], tone="n",
             explain=["Le binaire n'a besoin d'aucun runtime : le noyau le charge…", "… et le processeur l'exécute."]),
        wait(2200),
    ],
})

# ordre du bit (Boris, 22/11) : « Modifier » vient après Java
ORDER = ["interprete", "compile", "bytecode", "modifier-script", "modifier-compile", "runtime"]
steps.sort(key=lambda st: ORDER.index(st["id"]))

lesson = {
    "format": "bl-scenes/0.3", "id": "compiled-or-interpreted",
    "title": "Compilé ou interprété : du code source au programme qui tourne",
    "lang": "fr", "kit": "feuillete",
    "legend": [{"tone": "y", "label": "source"}, {"tone": "v", "label": "compilateur"}, {"tone": "n", "label": "code machine"},
               {"tone": "g", "label": "runtime"}, {"tone": "b", "label": "bytecode"}],
    "entities": ents, "steps": steps,
}
write(lesson, *outputs(HERE, "compile.scene.json", "compiled-compile"))

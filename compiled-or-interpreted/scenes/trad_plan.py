"""Scène 2D (kit plan) du bit 5 « Compilé ou interprété » : quatre fichiers, quatre chemins jusqu'au processeur.

Retour de Boris (22/11) : dire tout de suite qu'il y a du code source interprété et du code source compilé, avec ses
exemples (script.sh interprété par bash, script.py par un moteur à installer, Java compilé puis interprété, C compilé en
code machine), et la phrase à retenir : le processeur ne lit que le code machine, la seule question est qui traduit, et quand.

Dessin : une rangée par fichier, de gauche à droite ; deux colonnes de traducteurs, « avant l'exécution » (compilateurs)
et « pendant l'exécution » (interpréteurs) ; le processeur à droite, commun à tous. Le binaire C saute la colonne
« pendant » : rien ne le lit, le processeur l'exécute.
Kit plan : x vers la droite, y vers le bas, en unités de 28 px ; un enfant (in) est relatif au centre du parent.
Couleurs : y code source, g traduit avant (compilateur), v traduit pendant (interpréteur), b code machine et bytecode.
"""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools" / "scenes"))
from paths import outputs
from scene_kit import L, scene, send, wait, write


def ent(id, kind, at, size=None, tone=None, parent=None, **kw):
    d = {"id": id, "kind": kind, "at": list(at)}
    if tone: d["tone"] = tone
    if size: d["size"] = list(size) + [1]
    if parent: d["in"] = parent
    d.update({k: v for k, v in kw.items() if v is not None})
    return d


X_SRC, X_AV, X_MID, X_PE, X_CPU = -17, -8.5, -0.5, 7.5, 16.5
ROWS = {"sh": -6.3, "py": -2.1, "java": 2.1, "c": 6.3}
COL_H = 19.6
Y_COL = 0.2
FILE = (6.0, 2.0)
TOOL = (5.4, 2.4)

ents = [
    ent("avant", "layer", (X_AV, Y_COL), (7.0, COL_H), "g", title="avant l'exécution"),
    ent("pendant", "layer", (X_PE, Y_COL), (7.0, COL_H), "v", title="pendant l'exécution"),
    ent("cpu", "node", (X_CPU, 3.0), (5.0, 12.4), "n", title="processeur", sub="0101 1100 0011",
        detail="Le **processeur** n'exécute que du **code machine** : des instructions très simples écrites sous forme de nombres. Tout programme finit par lui parvenir sous cette forme."),
    # les quatre codes sources
    ent("s-sh", "file", (X_SRC, ROWS["sh"]), FILE, "y", title="hello.sh"),
    ent("s-py", "file", (X_SRC, ROWS["py"]), FILE, "y", title="hello.py"),
    ent("s-java", "file", (X_SRC, ROWS["java"]), FILE, "y", title="Bonjour.java"),
    ent("s-c", "file", (X_SRC, ROWS["c"]), FILE, "y", title="bonjour.c"),
    # pendant l'exécution : les interpréteurs (positions relatives à la colonne)
    ent("bash", "node", (0, ROWS["sh"] - Y_COL), TOOL, "v", parent="pendant", title="bash", sub="déjà installé",
        detail="`bash` est l'**interpréteur** des scripts shell. Il est déjà là sous Linux et macOS."),
    ent("python", "node", (0, ROWS["py"] - Y_COL), TOOL, "v", parent="pendant", title="python", sub="à installer",
        detail="L'**interpréteur** Python : un programme à installer, comme Node.js pour du JavaScript ou PHP pour du PHP."),
    ent("jvm", "node", (0, ROWS["java"] - Y_COL), TOOL, "v", parent="pendant", title="JVM", sub="à installer",
        detail="La **machine virtuelle Java** lit le bytecode et le fait exécuter par le processeur. Elle s'installe avec le JDK."),
    # avant l'exécution : les compilateurs
    ent("javac", "node", (0, ROWS["java"] - Y_COL), TOOL, "g", parent="avant", title="javac", sub="compilateur Java",
        detail="`javac` traduit `Bonjour.java` en **bytecode**, une langue intermédiaire, une fois, avant de lancer le programme."),
    ent("cc", "node", (0, ROWS["c"] - Y_COL), TOOL, "g", parent="avant", title="compilateur C",
        detail="Le **compilateur** traduit tout `bonjour.c` en code machine, une fois pour toutes, avant de lancer le programme."),
    # ce que produisent les compilateurs
    ent("class", "file", (X_MID, ROWS["java"]), FILE, "b", title="Bonjour.class",
        detail="Du **bytecode** : des instructions pour la machine virtuelle Java, pas pour le processeur."),
    ent("bin", "file", (X_MID, ROWS["c"]), FILE, "b", title="bonjour (binaire)",
        detail="Le **binaire** : le programme traduit en code machine, pour un type de processeur et un système."),
]

traduction = {
    "id": "traduction", "label": "Quatre chemins", "title": "Qui traduit, et quand",
    "body": ["Le processeur ne lit que du code machine. Pour chaque code source, un traducteur : pendant l'exécution, ou avant."],
    "show": ["pendant", "cpu", "s-sh", "s-py", "s-java", "s-c"],
    "links": [],
    "script": [
        wait(1000),
        scene(say="Un script shell : bash, déjà installé, le lit et le traduit pendant l'exécution, ligne à ligne.",
              show=["bash"], link=[L("s-sh", "bash"), L("bash", "cpu")]),
        send(["s-sh", "bash", "cpu"], label="ligne à ligne"),
        wait(600),
        scene(say="Un script Python, JavaScript ou PHP : même chose, mais l'interpréteur du langage est à installer.",
              show=["python"], link=[L("s-py", "python"), L("python", "cpu")]),
        send(["s-py", "python", "cpu"], label="ligne à ligne"),
        wait(600),
        scene(say="Java ajoute une étape **avant l'exécution** : la compilation.", show=["avant"]),
        wait(500),
        scene(say="javac traduit d'abord vers une langue intermédiaire, le bytecode…",
              show=["javac", "class"], link=[L("s-java", "javac"), L("javac", "class")]),
        send(["s-java", "javac", "class"], label="une fois"),
        scene(say="…que la machine virtuelle Java traduit ensuite pendant l'exécution.",
              show=["jvm"], link=[L("class", "jvm"), L("jvm", "cpu")]),
        send(["class", "jvm", "cpu"], label="à chaque lancement"),
        wait(600),
        scene(say="Le C : le compilateur traduit tout, une fois pour toutes, en un fichier de code machine.",
              show=["cc", "bin"], link=[L("s-c", "cc"), L("cc", "bin")]),
        send(["s-c", "cc", "bin"], label="une fois"),
        scene(say="Ce binaire va droit au processeur : plus rien ne le lit ni ne le traduit.",
              link=[L("bin", "cpu")]),
        send(["bin", "cpu"], tone="b", label="directement"),
        scene(say="Interprété ne veut pas dire « pas traduit » : il y a toujours un traducteur, la question est quand.",
              set=[{"id": "cpu", "label": "rien que lui"}]),
        wait(2800),
    ],
}

lesson = {
    "format": "bl-scenes/0.3", "id": "compiled-or-interpreted-plan",
    "title": "Compilé ou interprété (2D)", "lang": "fr", "kit": "plan",
    "legend": [{"tone": "y", "label": "code source"}, {"tone": "g", "label": "traduit avant"},
               {"tone": "v", "label": "traduit pendant"}, {"tone": "b", "label": "fichier traduit"}],
    "entities": ents, "steps": [traduction],
}
write(lesson, *outputs(HERE, "traduction.scene.json", "compiled-traduction"))

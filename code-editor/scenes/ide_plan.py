"""Scènes 2D (kit plan) du bit 4 « De l'éditeur de texte à l'éditeur de code » (courses-foundations/code-editor).

Retour de Boris (22/11) : « Un traitement de texte n'est pas un éditeur de texte » et « les outils essentiels d'un IDE »
en animation 2D. Le kit est choisi par leçon : ces deux étapes vivent dans assets/ide.scene.json, à côté de
editor.scene.json (Feuilleté, les deux fenêtres et l'éditeur de code).

Kit plan : x vers la droite, y vers le bas, en unités de 28 px ; un enfant (in) est relatif au centre du parent.
Couleurs : v outil d'écriture, y texte brut (ce que bash sait lire), r mise en forme (ce qu'il ne sait pas lire),
g aide de l'éditeur et support du langage, b terminal (le ton i du kit plan est illisible : texte sombre sur fond sombre), g support du langage.
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


# ── Étape 1 : trois outils, trois usages ─────────────────────────────────────────────────────────────────────
# Retour de Boris (22/11) : montrer les usages, pas une même ligne tapée partout.
#   bonjour.sh dans un éditeur de texte (terminal : nano, vi ; fenêtre : Bloc-notes, gedit) : que le texte ;
#   mon-document.docx dans un traitement de texte : texte, mise en forme, commentaires, impression ; un script n'y passe pas bien ;
#   bonjour.sh dans un éditeur de code / IDE (fenêtre ou terminal) : erreurs soulignées, terminal intégré, pas à pas.
# Trois colonnes de même dessin : l'outil en haut, le fichier en dessous ; le verdict s'affiche sur l'outil.
XS = {"te": -11.5, "wp": 0, "ce": 11.5}
Y_TOOL, Y_FILE = -6.2, 2.4
FS = (9.4, 9.0)
ROWS = [-1.6, 0.0, 1.6, 3.2]
IW = (7.8, 1.2)
ents = [
    ent("te", "node", (XS["te"], Y_TOOL), (8.6, 2.2), "v", title="éditeur de texte", sub="nano, vi · Bloc-notes, gedit",
        detail="Un **éditeur de texte** enregistre les caractères tapés, rien de plus : du **texte brut**. Certains s'ouvrent dans le terminal (`nano`, `vi`), d'autres dans une fenêtre (Bloc-notes, gedit)."),
    ent("wp", "node", (XS["wp"], Y_TOOL), (8.6, 2.2), "v", title="traitement de texte", sub="Word, Writer",
        detail="Un **traitement de texte** fait partie d'une suite bureautique : il sert à écrire des documents mis en forme."),
    ent("ce", "node", (XS["ce"], Y_TOOL), (8.6, 2.2), "v", title="éditeur de code, IDE", sub="VS Code · Neovim",
        detail="Un **éditeur de code** (ou **IDE**) enregistre le même texte brut qu'un éditeur de texte, et ajoute des outils pour programmer. Il en existe en fenêtre (VS Code) et dans le terminal (Neovim avec des extensions)."),
    # éditeur de texte : le script, rien d'autre
    ent("f-te", "layer", (XS["te"], Y_FILE), FS, "y", title="bonjour.sh"),
    ent("f-te-1", "file", (0, ROWS[0]), IW, "y", parent="f-te", title='echo "Bonjour"'),
    # traitement de texte : un document
    ent("f-wp", "layer", (XS["wp"], Y_FILE), FS, "r", title="mon-document.docx"),
    ent("f-wp-1", "file", (0, ROWS[0]), IW, "y", parent="f-wp", title="le texte"),
    ent("f-wp-2", "program", (0, ROWS[1]), IW, "r", parent="f-wp", title="mise en forme"),
    ent("f-wp-3", "program", (0, ROWS[2]), IW, "r", parent="f-wp", title="commentaires, notes"),
    ent("f-wp-4", "program", (0, ROWS[3]), IW, "r", parent="f-wp", title="mise en page, impression"),
    # éditeur de code : le même script, et des outils pour programmer
    ent("f-ce", "layer", (XS["ce"], Y_FILE), FS, "y", title="bonjour.sh"),
    ent("f-ce-1", "file", (0, ROWS[0]), IW, "y", parent="f-ce", title='echo "Bonjour"'),
    ent("f-ce-2", "program", (0, ROWS[1]), IW, "g", parent="f-ce", title="erreurs soulignées",
        detail="On parle de **linting** : l'éditeur relit le script et souligne les fautes avant qu'on le lance."),
    ent("f-ce-3", "program", (0, ROWS[2]), IW, "g", parent="f-ce", title="terminal intégré : lancer",
        detail="Le script se lance dans un **terminal intégré**, ou d'un clic, sans changer de fenêtre."),
    ent("f-ce-4", "program", (0, ROWS[3]), IW, "g", parent="f-ce", title="pas à pas",
        detail="Le **débogueur** exécute le script ligne par ligne, pour suivre ce qu'il fait."),
]

traitement = {
    "id": "traitement", "label": "Trois outils", "title": "Trois outils, trois usages",
    "body": ["Un script et un document ne s'écrivent pas avec le même outil. Chaque colonne montre un outil et le fichier qu'il enregistre."],
    "show": ["te", "wp", "ce"],
    "links": [],
    "script": [
        wait(900),
        scene(say="Un éditeur de texte, dans le terminal ou dans une fenêtre : il enregistre le script, rien d'autre.",
              show=["f-te", "f-te-1"], link=[L("te", "f-te")]),
        wait(1200),
        scene(say="Du texte brut : c'est assez pour un petit script.", set=[{"id": "te", "label": "que le texte"}]),
        wait(1600),
        scene(say="Un traitement de texte fait des documents : le texte, sa mise en forme, les commentaires, l'impression.",
              show=["f-wp", "f-wp-1", "f-wp-2", "f-wp-3", "f-wp-4"], link=[L("wp", "f-wp")]),
        wait(1600),
        scene(say="Un script n'y passe pas bien : il change les guillemets et ajoute sa mise en forme.",
              set=[{"id": "wp", "label": "pas pour un script"}]),
        wait(1800),
        scene(say="Un éditeur de code enregistre le même script, en texte brut…",
              show=["f-ce", "f-ce-1"], link=[L("ce", "f-ce")]),
        wait(1200),
        scene(say="…et ajoute des outils : erreurs soulignées, terminal intégré pour le lancer, exécution pas à pas.",
              show=["f-ce-2", "f-ce-3", "f-ce-4"], set=[{"id": "ce", "label": "écrire, lancer, déboguer"}]),
        wait(2800),
    ],
}

# ── Étape 2 : les outils essentiels d'un IDE ──────────────────────────────────────────────────────────────────
# La fenêtre (layer) porte l'explorateur à gauche, la zone d'édition au centre, le terminal en bas.
# Le support du langage est à droite, hors de la fenêtre : il ne se voit pas, il aide la zone d'édition et le terminal.
ents += [
    ent("win", "layer", (0, 0), (21, 15), "n", title="éditeur de code", sub="un dossier ouvert"),
    ent("explorer", "layer", (-7, 1.2), (5.4, 11.4), "v", parent="win", title="explorateur",
        detail="L'**explorateur** montre les fichiers et sous-dossiers du dossier ouvert ; un clic en ouvre un."),
    ent("f-fiche", "file", (0, -2.2), (4.2, 1.1), "y", parent="explorer", title="fiche.sh"),
    ent("f-notes", "file", (0, -0.6), (4.2, 1.1), "y", parent="explorer", title="notes.md"),
    ent("edit", "node", (2.7, -1.6), (13.2, 5.8), "v", parent="win", title="zone d'édition", sub="un onglet par fichier",
        detail="La **zone d'édition** : le fichier ouvert, avec les numéros de ligne. Un onglet par fichier ouvert."),
    ent("term", "node", (2.7, 4.6), (13.2, 3.0), "b", parent="win", title="terminal intégré",
        detail="Le **terminal intégré** : un vrai terminal, ouvert sur le dossier, dans la même fenêtre."),
    ent("lang", "layer", (16.5, 0), (9.0, 15), "g", title="support du langage", sub="une extension par langage",
        detail="Le **support du langage** reconnaît le langage du fichier (bash, Java, Python…). Dans VS Code, il s'ajoute par une **extension**."),
    ent("l-color", "program", (0, -3.6), (7.4, 1.1), "g", parent="lang", title="coloration"),
    ent("l-comp", "program", (0, -2.0), (7.4, 1.1), "g", parent="lang", title="complétion"),
    ent("l-lint", "program", (0, -0.4), (7.4, 1.1), "g", parent="lang", title="erreurs soulignées",
        detail="On parle aussi de **linting** : l'outil relit le code et souligne les fautes avant qu'on lance le programme."),
    ent("l-run", "program", (0, 1.2), (7.4, 1.1), "g", parent="lang", title="lancer, compiler"),
    ent("l-dbg", "program", (0, 2.8), (7.4, 1.1), "g", parent="lang", title="déboguer"),
    ent("l-tpl", "program", (0, 4.4), (7.4, 1.1), "g", parent="lang", title="modèles de code"),
]
LANG_TOOLS = ["l-color", "l-comp", "l-lint", "l-run", "l-dbg", "l-tpl"]

outils = {
    "id": "outils", "label": "Outils d'un IDE", "title": "Les outils essentiels d'un IDE",
    "body": ["L'explorateur montre les fichiers du dossier ouvert. La même fenêtre réunit aussi la zone d'édition et le terminal ; le support du langage les aide."],
    "show": ["win", "explorer", "f-fiche", "f-notes"],
    "links": [],
    "script": [
        wait(1400),
        scene(show=["edit"], link=[L("f-fiche", "edit")]),
        send(["f-fiche", "edit"], label="ouvrir"),
        scene(say="Un clic ouvre le fichier dans la zone d'édition, un onglet par fichier.",
              set=[{"id": "edit", "label": "fiche.sh"}]),
        wait(1400),
        scene(say="Le terminal intégré lance les commandes dans le même dossier, sans changer de fenêtre.",
              show=[{"id": "term", "label": "bash fiche.sh"}]),
        wait(1700),
        scene(say="Le support du langage reconnaît le langage du fichier, ici celui de bash.",
              show=["lang"] + LANG_TOOLS, link=[L("lang", "edit"), L("lang", "term")]),
        wait(1600),
        send(["lang", "edit"], tone="r", label="ligne 4"),
        scene(say="Il colore, complète, et souligne une faute avant même qu'on lance le script.",
              set=[{"id": "edit", "label": "guillemet oublié, ligne 4"}]),
        wait(1700),
        send(["lang", "term"], label="lancer"),
        scene(say="Il sait aussi lancer, compiler ou déboguer le programme.",
              set=[{"id": "term", "label": "lancer, déboguer"}]),
        wait(2600),
    ],
}

lesson = {
    "format": "bl-scenes/0.3", "id": "code-editor-plan",
    "title": "De l'éditeur de texte à l'éditeur de code (2D)", "lang": "fr", "kit": "plan",
    "legend": [{"tone": "y", "label": "texte brut"}, {"tone": "r", "label": "mise en forme"}, {"tone": "g", "label": "outils de l'IDE"}],
    "entities": ents, "steps": [traitement, outils],
}
write(lesson, *outputs(HERE, "ide.scene.json", "code-editor-ide"))

"""Scène du bit 4 « De l'éditeur de texte à l'éditeur de code » (courses-foundations/code-editor).

Dessin : une fenêtre = un bloc `node` ; l'éditeur de code = une zone qui réunit ses fenêtres (in: ide).
Le fichier fiche.sh (y, source) est sur le disque, en arrière ; vous (acteur) devant.
Couleurs : v éditeur, i terminal, y fichier source.
"""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools" / "scenes"))
from paths import outputs
from scene_kit import G, L, scene, send, wait, write, hud

FICHE_BAD = [
    "#!/bin/bash",
    "# fiche.sh : la fiche de ma machine",
    "echo \"Machine : $(hostname)\"",
    "echo \"Utilisateur : $(whoami)",
    "echo \"Date : $(date)\"",
    "df -h ~",
]
ERR = ["Machine : pc-alice",
       "fiche.sh: line 5: unexpected EOF while looking for",
       "  matching `\"'"]

ents = [
    {"id": "you", "kind": "actor", "at": G(5, 12), "label": "vous"},
    {"id": "notepad", "kind": "node", "at": G(-4.5, 2), "tone": "v", "title": "éditeur de texte",
     "sub": "Bloc-notes, vi…",
     "detail": "Un **éditeur de texte** enregistre les caractères que vous tapez, sans mise en forme. Celui du système suffit pour écrire un script, mais il ne vous aide en rien."},
    {"id": "term", "kind": "node", "at": G(4.5, 2), "tone": "i", "title": "terminal", "icon": ">_",
     "detail": "Le **terminal**, dans sa propre fenêtre : c'est là que vous lancez le script."},
    {"id": "fiche", "kind": "file", "at": G(0, -8), "tone": "y", "title": "fiche.sh", "icon": "sh",
     "detail": "Le script, rangé sur le disque. L'éditeur l'écrit, `bash` le lit : les deux travaillent sur **le même fichier**."},
    {"id": "ide", "kind": "zone", "at": G(0, 2), "size": [7, 6], "label": "éditeur de code"},
    {"id": "code", "kind": "node", "in": "ide", "at": G(-2.2, -0.4), "tone": "v", "title": "zone d'édition",
     "sub": "couleurs · n° de ligne",
     "detail": "La **zone d'édition** : le fichier ouvert, en couleurs, avec les numéros de ligne. Un onglet par fichier ouvert."},
    {"id": "iterm", "kind": "node", "in": "ide", "at": G(2.2, 0.6), "tone": "i", "title": "terminal intégré", "icon": ">_",
     "detail": "Le **terminal intégré** : un vrai terminal, ouvert sur le dossier, dans la même fenêtre que la zone d'édition."},
]

TERM = {"kind": "terminal", "title": "alice@pc-alice — bash", "prompt": "alice@pc-alice", "cwd": "~/byte-layers/foundations"}

steps = [
    {
        "id": "bloc-notes", "label": "Bloc-notes", "title": "Deux fenêtres, aucune aide",
        "body": ["Imaginons un script, `fiche.sh`, écrit dans l'éditeur de texte du système : pour le lancer, on passe dans le terminal."],
        "labels": "left",
        "show": ["you", "notepad", "term", "fiche"],
        "links": [L("you", "notepad", dashed=True), L("you", "term", dashed=True), L("notepad", "fiche"), L("term", "fiche", dashed=True)],
        "widgets": [{"kind": "editor", "title": "fiche.sh — Bloc-notes", "lang": "text", "lines": FICHE_BAD}, TERM],
        "script": [
            wait(700),
            send(["you", "notepad", "fiche"], label="enregistrer",
                 explain=["Vous tapez le script dans l'**éditeur de texte** : tout a la même couleur, rien ne ressort.",
                          "Vous l'enregistrez : l'éditeur écrit `fiche.sh` sur le disque."]),
            scene(say="Pour le lancer, vous changez de fenêtre : le terminal.",
                  set=[{"id": "you", "at": G(6, 10)}], ms=900),
            {"do": "type", "text": "bash fiche.sh"},
            send(["you", "term", "fiche"], kind="read", label="bash fiche.sh",
                 explain=["Vous tapez `bash fiche.sh` dans le terminal.",
                          "`bash` exécute le script, puis s'arrête en plein milieu : un guillemet n'est pas fermé."]),
            {"do": "output", "text": ERR[0]},
            {"do": "output", "text": ERR[1]},
            {"do": "output", "text": ERR[2]},
            {"do": "prompt"},
            scene(say="Le message parle de la ligne 5 ; la faute est à la ligne 4, et rien ne la signale dans l'éditeur.",
                  set=[{"id": "you", "at": G(5, 12)}], ms=900),
            wait(2200),
        ],
    },
    {
        "id": "editeur-de-code", "label": "Éditeur de code", "title": "Une fenêtre, le numéro de ligne",
        "body": ["Dans un éditeur de code, le même fichier s'affiche en couleurs, et le terminal est dans la même fenêtre."],
        "labels": "left",
        "show": ["you", "ide", "code", "iterm", "fiche"],
        "links": [L("you", "code", dashed=True), L("you", "iterm", dashed=True), L("code", "fiche"), L("iterm", "fiche", dashed=True)],
        # widget ide (Boris, 22/11) : une seule fenêtre, explorateur, zone d'édition et terminal intégré
        "widgets": [{"kind": "ide", "title": "foundations — éditeur de code", "files": ["fiche.sh", "notes.md"],
                     "lang": "bash", "lines": FICHE_BAD, "prompt": TERM["prompt"], "cwd": TERM["cwd"]}],
        "script": [
            wait(900),
            {"do": "type", "text": "bash fiche.sh"},
            send(["you", "iterm", "fiche"], kind="read", label="bash fiche.sh",
                 explain=["Sans quitter la fenêtre, vous lancez le script dans le **terminal intégré**.",
                          "`bash` lit le même fichier, et bute au même endroit."]),
            {"do": "output", "text": ERR[0]},
            {"do": "output", "text": ERR[1]},
            {"do": "output", "text": ERR[2]},
            {"do": "prompt"},
            {"do": "line", "n": 5},
            scene(say="Les numéros de ligne mènent tout droit à la ligne 5 citée par bash.",
                  set=[{"id": "code", "label": "ligne 5"}]),
            wait(1200),
            {"do": "line", "n": 4},
            scene(say="Juste au-dessus, la ligne 4 : son guillemet de fin manque.",
                  set=[{"id": "code", "label": "guillemet oublié, ligne 4"}]),
            wait(2400),
        ],
    },
]

lesson = {
    "format": "bl-scenes/0.3", "id": "code-editor",
    "title": "De l'éditeur de texte à l'éditeur de code", "lang": "fr", "kit": "feuillete",
    "entities": ents, "steps": steps,
}
write(lesson, *outputs(HERE, "editor.scene.json", "code-editor"))

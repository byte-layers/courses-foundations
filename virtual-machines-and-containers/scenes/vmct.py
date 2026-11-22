"""Scène du bit 7 « Machines virtuelles et conteneurs » (courses-foundations/virtual-machines-and-containers).

Dessin (storyboards/07-virtual-machines-and-containers.md) :
- une machine = Matériel (n) + Noyau (r), deux plaques ;
- une machine virtuelle = Matériel simulé (n) + Noyau (r) en petit, posés sur l'hyperviseur (g) ;
- un conteneur = plaque bleue (b) qui porte l'appli (v) et son runtime (g), posée sur le moteur de conteneurs (g, Docker,
  Podman), lui-même un programme sur le noyau de l'hôte (retour de Boris du 22/11 : montrer le moteur, comme l'hyperviseur) ;
- l'hyperviseur dit qu'il existe en deux sortes : intégré au système (type 1) ou logiciel installé (type 2, VirtualBox) ;
- une étiquette par sorte.
"""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools" / "scenes"))
from paths import outputs
from scene_kit import G, L, scene, send, wait, write, hud

PLATE = [5.6, 5.6, 0.55]
SMALL = [4.2, 4.2, 0.55]
H = 0.55


def at(sx, sy, z):
    x, y = G(sx, sy)
    return [x, y, z]


def rel(sx, sy, z=H):
    x, y = G(sx, sy)
    return [x, y, z]


ents = []


def machine(prefix, sx, sy, size, title_hw, title_k, label=True):
    ents.append({"id": f"{prefix}hw", "kind": "layer", "at": at(sx, sy, 0), "size": size, "tone": "n",
                 **({"title": title_hw} if title_hw else {}),
                 "detail": "Le **matériel** de la machine : processeur, mémoire, disque."})
    ents.append({"id": f"{prefix}k", "kind": "layer", "at": at(sx, sy, 0.95), "size": size, "tone": "r",
                 **({"title": title_k} if title_k else {}),
                 "detail": "Le **noyau** de la machine : il partage le matériel entre les programmes qui tournent."})


# --- étape 1 et 4 : poste (gauche) et serveur (droite)
machine("p", -5.5, -1, SMALL, "poste", None)
machine("s", 5.5, -1, SMALL, "serveur", None)
ents += [
    {"id": "papp", "kind": "program", "in": "pk", "at": rel(-0.9, 0), "tone": "v", "title": "appli Prêts",
     "detail": "L'**appli Prêts** de la bibliothèque, écrite en JavaScript : elle a besoin de Node.js pour tourner."},
    {"id": "pnode", "kind": "program", "in": "pk", "at": rel(0.9, 0), "tone": "g", "title": "Node.js 22",
     "detail": "Le **runtime** installé sur le poste : Node.js en version 22."},
    {"id": "sapp", "kind": "program", "in": "sk", "at": rel(-0.9, 0), "tone": "v",
     "detail": "La même appli, installée sur le serveur."},
    {"id": "snode", "kind": "program", "in": "sk", "at": rel(-1.6, 1.4), "size": [1.1, 1.1, 0.6], "tone": "g", "title": "Node.js 18",
     "detail": "Le serveur a un autre Node.js, en version 18 : l'appli n'y trouve pas ce qu'elle attend."},
]

# --- étapes 2 et 3 : un grand serveur au centre
ents += [
    {"id": "hhw", "kind": "layer", "at": at(0, -1, 0), "size": PLATE, "tone": "n", "title": "Matériel",
     "detail": "Le **matériel** du serveur, le seul vrai : processeur, mémoire, disque."},
    {"id": "hk", "kind": "layer", "at": at(0, -1, 0.95), "size": PLATE, "tone": "r", "title": "Noyau de l'hôte",
     "detail": "Le **noyau** du serveur, qu'on appelle l'**hôte** : la machine réelle qui accueille les autres."},
    {"id": "hyp", "kind": "layer", "in": "hk", "at": rel(0, 0), "size": [5.0, 5.0, 0.4], "tone": "g", "title": "hyperviseur",
     "sub": "intégré ou installé",
     "detail": "L'**hyperviseur** simule des ordinateurs complets et leur partage le vrai matériel. Il est soit **intégré au système** de la machine (*type 1* : KVM dans Linux, Hyper-V, VMware ESXi), soit un **logiciel installé** sur un système existant (*type 2* : VirtualBox, VMware Workstation)."},
    {"id": "eng", "kind": "layer", "in": "hk", "at": rel(0, 0), "size": [4.8, 4.8, 0.3], "tone": "g", "title": "moteur de conteneurs",
     "sub": "Docker, Podman",
     "detail": "Le **moteur de conteneurs** (Docker, Podman) est un programme installé sur la machine : il crée, démarre et isole les conteneurs. Les programmes dans les conteneurs, eux, s'adressent **directement au noyau de l'hôte** : le moteur ne simule rien."},
]
for i, sx in enumerate([-2.4, 2.4]):
    LASTI = 1
    first = i == LASTI
    ents += [
        {"id": f"vm{i}hw", "kind": "layer", "in": "hyp", "at": rel(sx, 0.6, 0.4), "size": [1.9, 1.9, 0.4], "tone": "n",
         **({"title": "matériel simulé"} if first else {}),
         "detail": "Une **machine virtuelle** commence par un matériel simulé : processeur, mémoire et disque, imités par l'hyperviseur."},
        {"id": f"vm{i}k", "kind": "layer", "in": f"vm{i}hw", "at": rel(0, 0, 0.4), "size": [1.9, 1.9, 0.4], "tone": "r",
         **({"title": "noyau de la VM"} if first else {}),
         "detail": "Chaque machine virtuelle a **son propre noyau**, et souvent son propre système d'exploitation : c'est un ordinateur complet, en logiciel."},
        {"id": f"vm{i}app", "kind": "program", "in": f"vm{i}k", "at": rel(0, 0, 0.4), "size": [1.1, 1.1, 0.7], "tone": "g",
         "title": ["Node.js 18", "Node.js 22"][i],
         "detail": "Dans chaque machine virtuelle, sa version de Node.js : l'une a la 18, l'autre la 22, sans se gêner."},
    ]
for i, sx in enumerate([-2.9, 0, 2.9]):
    LASTI = 2
    first = i == LASTI
    ents += [
        {"id": f"c{i}", "kind": "layer", "in": "eng", "at": rel(sx, 0.8, 0.3), "size": [1.2, 1.2, 0.35], "tone": "b",
         **({"title": "conteneur"} if first else {}),
         "detail": "Un **conteneur** isole un programme et ses fichiers du reste de la machine, mais **sans noyau à lui** : il utilise celui de l'hôte."},
        {"id": f"c{i}app", "kind": "program", "in": f"c{i}", "at": rel(0, 0, 0.35), "size": [0.8, 0.8, 0.6], "tone": "g",
         **({"title": ["Node.js 18", "Node.js 22", None][i]} if i != 2 else {}),
         "detail": "Le programme qui tourne dans le conteneur, avec sa version de Node.js."},
    ]

# --- étape 4 : la boîte qui voyage (posée sur le noyau du poste, hors `in` pour pouvoir glisser)
TOPK = 0.95 + 0.55
ents += [
    {"id": "peng", "kind": "layer", "in": "pk", "at": rel(0, 0.4), "size": [3.6, 2.4, 0.3], "tone": "g",
     "detail": "Le moteur de conteneurs, installé sur le poste."},
    {"id": "seng", "kind": "layer", "in": "sk", "at": rel(0.9, -1.0), "size": [3.4, 2.4, 0.3], "tone": "g",
     "detail": "Le moteur de conteneurs, installé sur le serveur."},
    {"id": "box", "kind": "layer", "in": "peng", "at": rel(0, 0, 0.3), "size": [3.0, 1.8, 0.35], "tone": "b", "title": "conteneur",
     "detail": "Le **conteneur** emporte l'appli **et son runtime**, Node.js 22 : ce dont elle a besoin voyage avec elle."},
    {"id": "bapp", "kind": "program", "in": "box", "at": rel(-0.75, 0, 0.35), "size": [1.1, 1.1, 0.6], "tone": "v", "title": "appli Prêts",
     "detail": "L'appli Prêts, dans son conteneur."},
    {"id": "bnode", "kind": "program", "in": "box", "at": rel(0.75, 0, 0.35), "size": [1.1, 1.1, 0.6], "tone": "g", "title": "Node.js 22",
     "detail": "Son Node.js 22, dans le même conteneur."},
    {"id": "box2", "kind": "layer", "in": "seng", "at": rel(0, 0, 0.3), "size": [3.0, 1.8, 0.35], "tone": "b",
     "detail": "Une **copie** du même conteneur, sur le serveur : la même appli, avec le même Node.js 22."},
    {"id": "b2app", "kind": "program", "in": "box2", "at": rel(-0.75, 0, 0.35), "size": [1.1, 1.1, 0.6], "tone": "v",
     "detail": "L'appli Prêts, dans la copie du conteneur."},
    {"id": "b2node", "kind": "program", "in": "box2", "at": rel(0.75, 0, 0.35), "size": [1.1, 1.1, 0.6], "tone": "g",
     "detail": "Le Node.js 22 emporté dans le conteneur."},
]

LEGEND = [{"tone": "n", "label": "matériel"}, {"tone": "r", "label": "noyau"},
          {"tone": "v", "label": "appli"}, {"tone": "g", "label": "programme ou outil"}, {"tone": "b", "label": "conteneur"}]

steps = [
    {
        "id": "probleme", "label": "Le problème", "title": "Sur le poste, ça marche ; sur le serveur, non",
        "body": ["L'appli Prêts tourne sur le poste du développeur. Installée sur le serveur, elle n'y trouve pas la bonne version de Node.js."],
        "labels": "left",
        "hud": [{"label": "poste", "value": "l'appli marche"}],
        "show": ["phw", "pk", "papp", "pnode", "shw", "sk", "snode"],
        "script": [
            wait(800),
            scene(say="Sur le poste, l'appli Prêts tourne avec Node.js 22.", set=[{"id": "papp", "label": "marche"}]),
            wait(800),
            scene(say="On l'installe sur le serveur, qui a Node.js 18.", show=["sapp"], ms=900),
            wait(700),
            scene(say="Elle attend une autre version : sur le serveur, elle est en panne.",
                  set=[{"id": "sapp", "label": "en panne"}],
                  hud=[{"label": "serveur", "value": "en panne"}]),
            wait(2200),
        ],
    },
    {
        "id": "machines-virtuelles", "label": "Machines virtuelles", "title": "Des ordinateurs entiers, simulés",
        "body": ["Sur un seul serveur, un hyperviseur simule plusieurs ordinateurs. Chacun a son matériel simulé et son propre noyau."],
        "labels": "left",
        "hud": [{"label": "noyaux", "value": "1"}],
        "show": ["hhw", "hk"],
        "script": [
            wait(700),
            scene(say="Un programme, l'hyperviseur, simule des ordinateurs.", show=["hyp"], ms=900),
            wait(500),
            scene(say="Chaque machine virtuelle a son matériel simulé et son propre noyau.",
                  show=["vm0hw", "vm0k", "vm0app"], hud=[{"label": "noyaux", "value": "2"}], ms=1000),
            wait(600),
            scene(say="Une seconde machine, isolée de la première : trois noyaux tournent.",
                  show=["vm1hw", "vm1k", "vm1app"], hud=[{"label": "noyaux", "value": "3"}], ms=1000),
            wait(2200),
        ],
    },
    {
        "id": "conteneurs", "label": "Conteneurs", "title": "Isolés, sur le noyau de l'hôte",
        "body": ["Un conteneur isole un programme sans simuler d'ordinateur : il se pose directement sur le noyau de la machine."],
        "labels": "left",
        "hud": [{"label": "noyaux", "value": "1"}],
        "show": ["hhw", "hk"],
        "script": [
            wait(700),
            scene(say="Un programme, le moteur de conteneurs, est installé sur la machine.", show=["eng"], ms=900),
            wait(500),
            scene(say="Il crée un conteneur : pas de matériel simulé, pas de noyau à lui.", show=["c0", "c0app"], ms=900),
            wait(600),
            scene(say="Trois conteneurs, isolés les uns des autres : leurs programmes utilisent tous le noyau de l'hôte.",
                  show=["c1", "c1app", "c2", "c2app"], hud=[{"label": "noyaux", "value": "1, partagé"}], ms=1000),
            wait(2200),
        ],
    },
    {
        "id": "dev-prod", "label": "Du poste au serveur", "title": "La même boîte, partout",
        "body": ["L'appli tourne dans un conteneur qui contient aussi son Node.js. Une copie du même conteneur part sur le serveur."],
        "labels": "left",
        "hud": [{"label": "poste", "value": "l'appli marche"}],
        "show": ["phw", "pk", "shw", "sk", "peng", "box", "bapp", "bnode"],
        "script": [
            wait(800),
            scene(say="Sur le poste, l'appli tourne dans un conteneur, avec son Node.js 22.", set=[{"id": "bapp", "label": "marche"}]),
            wait(700),
            scene(say="Le serveur a lui aussi un moteur de conteneurs : une copie de la même boîte y part.", show=["seng", "box2", "b2app", "b2node"], ms=1200),
            wait(500),
            scene(say="Elle y emporte son Node.js : rien à installer sur le serveur, l'appli marche.",
                  set=[{"id": "box2", "label": "marche"}],
                  hud=[{"label": "serveur", "value": "l'appli marche"}]),
            wait(2400),
        ],
    },
]

lesson = {
    "format": "bl-scenes/0.3", "id": "virtual-machines-and-containers",
    "title": "Machines virtuelles et conteneurs", "lang": "fr", "kit": "feuillete",
    "legend": LEGEND, "entities": ents, "steps": steps,
}
write(lesson, *outputs(HERE, "vm-containers.scene.json", "vm"))

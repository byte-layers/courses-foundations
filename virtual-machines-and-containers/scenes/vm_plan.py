"""Scène 2D (kit plan) du bit 7, section « Machine virtuelle ou conteneur » : les deux piles côte à côte.

Retour de Boris (22/11) : un schéma en couches comme le classique « Containers vs. VMs »
(lake/bronze/local/2026-11-22-vm-vs-containers-stack), redessiné, pas recopié.

Dessin : deux piles qui partent du même socle (serveur, système hôte). À gauche, l'hyperviseur, puis chaque machine
virtuelle (layer) porte son système invité, ses bibliothèques et son appli. À droite, le moteur de conteneurs, puis
chaque conteneur (layer) ne porte que ses bibliothèques et son appli : la pile est plus basse, c'est le message.
Une étiquette par sorte : seul le premier exemplaire porte un titre de carte.
Kit plan : x vers la droite, y vers le bas, unités de 28 px ; un enfant (in) est relatif au centre du parent.
Couleurs : n matériel, b système et noyau, v hyperviseur ou moteur, g bibliothèques, y appli.
"""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools" / "scenes"))
from paths import outputs
from scene_kit import scene, wait, write


def ent(id, kind, at, size=None, tone=None, parent=None, **kw):
    d = {"id": id, "kind": kind, "at": list(at)}
    if tone: d["tone"] = tone
    if size: d["size"] = list(size) + [1]
    if parent: d["in"] = parent
    d.update({k: v for k, v in kw.items() if v is not None})
    return d


XV, XC = -9.5, 9.5           # centres des deux piles
W = 16.0                        # largeur d'une pile
BAR = 1.7                       # hauteur d'une couche
Y_SRV, Y_OS, Y_MID = 9.0, 7.0, 5.0   # serveur, système hôte, hyperviseur / moteur

# machines virtuelles : trois colonnes, chacune système invité + bibliothèques + appli
VM_W, VM_H = 5.0, 9.0
Y_VM = Y_MID - BAR / 2 - 0.35 - VM_H / 2
VM_X = [XV - 5.4, XV, XV + 5.4]
# conteneurs : quatre colonnes, chacun bibliothèques + appli
CT_W, CT_H = 3.6, 5.8
Y_CT = Y_MID - BAR / 2 - 0.35 - CT_H / 2
CT_X = [XC - 6.0, XC - 2.0, XC + 2.0, XC + 6.0]

ents = [
    ent("v-srv", "node", (XV, Y_SRV), (W, BAR), "n", title="serveur",
        detail="Le **matériel** : processeur, mémoire, disque."),
    ent("v-os", "node", (XV, Y_OS), (W, BAR), "b", title="système hôte", sub="et son noyau",
        detail="Le **système d'exploitation** installé sur la machine, avec son **noyau**."),
    ent("hyp", "node", (XV, Y_MID), (W, BAR), "v", title="hyperviseur",
        detail="L'**hyperviseur** simule des ordinateurs entiers. Ici installé sur le système (type 2, comme VirtualBox) ; "
               "sur un serveur, il est souvent intégré au système (type 1)."),
    ent("c-srv", "node", (XC, Y_SRV), (W, BAR), "n", title="serveur"),
    ent("c-os", "node", (XC, Y_OS), (W, BAR), "b", title="système hôte", sub="et son noyau"),
    ent("eng", "node", (XC, Y_MID), (W, BAR), "v", title="moteur de conteneurs", sub="Docker, Podman",
        detail="Le **moteur de conteneurs** crée et isole les conteneurs. Il ne simule rien : les programmes parlent au noyau de l'hôte."),
]
for i, x in enumerate(VM_X):
    first = i == 0
    ents += [
        ent(f"vm{i}", "layer", (x, Y_VM), (VM_W, VM_H), "b", title="machine virtuelle" if first else None,
            detail="Sur le schéma, trois **machines virtuelles** : chacune est un ordinateur entier, simulé." if first else None),
        ent(f"vm{i}-os", "node", (0, 2.6), (VM_W - 0.6, 2.6), "b", parent=f"vm{i}",
            title="système invité" if first else None, sub="son noyau" if first else None,
            detail="Chaque machine virtuelle démarre **son propre système**, avec son noyau." if first else None),
        ent(f"vm{i}-lib", "node", (0, 0.3), (VM_W - 0.6, BAR), "g", parent=f"vm{i}",
            title="bibliothèques" if first else None),
        ent(f"vm{i}-app", "node", (0, -1.7), (VM_W - 0.6, BAR), "y", parent=f"vm{i}",
            title="appli" if first else None),
    ]
for i, x in enumerate(CT_X):
    first = i == 0
    ents += [
        ent(f"ct{i}", "layer", (x, Y_CT), (CT_W, CT_H), "y", title="conteneur" if first else None,
            detail="Sur le schéma, quatre **conteneurs** : chacun emporte son appli et ses bibliothèques, rien de plus." if first else None),
        ent(f"ct{i}-lib", "node", (0, 1.5), (CT_W - 0.6, BAR), "g", parent=f"ct{i}"),
        ent(f"ct{i}-app", "node", (0, -0.5), (CT_W - 0.6, BAR), "y", parent=f"ct{i}"),
    ]

vm_all = [e for i in range(3) for e in (f"vm{i}", f"vm{i}-os")]
vm_top = [e for i in range(3) for e in (f"vm{i}-lib", f"vm{i}-app")]
ct_all = [e for i in range(4) for e in (f"ct{i}", f"ct{i}-lib", f"ct{i}-app")]

piles = {
    "id": "piles", "label": "Les deux piles", "title": "Machine virtuelle ou conteneur",
    "body": ["Même point de départ : un serveur, son système et son noyau. Deux façons d'y isoler des programmes."],
    "show": ["v-srv", "v-os", "c-srv", "c-os"],
    "links": [],
    "hud": [{"label": "VM", "value": "—"}, {"label": "conteneurs", "value": "—"}],
    "script": [
        wait(1000),
        scene(say="À gauche, un **hyperviseur** se pose sur le système.", show=["hyp"]),
        wait(700),
        scene(say="Chaque machine virtuelle démarre **un système entier**, avec son propre noyau…",
              show=vm_all, hud=[{"label": "VM", "value": "3 systèmes"}]),
        wait(700),
        scene(say="…puis seulement les bibliothèques et l'appli.", show=vm_top),
        wait(900),
        scene(say="À droite, un **moteur de conteneurs**, qui ne simule rien.", show=["eng"]),
        wait(700),
        scene(say="Chaque conteneur n'emporte que **son appli et ses bibliothèques**.",
              show=ct_all, hud=[{"label": "conteneurs", "value": "0 système"}]),
        wait(700),
        scene(say="Tous s'adressent au **noyau de l'hôte**, partagé : la pile est plus légère, l'isolation moins forte.",
              set=[{"id": "c-os", "label": "noyau partagé"}]),
        wait(3000),
    ],
}

lesson = {
    "format": "bl-scenes/0.3", "id": "vm-containers-plan",
    "title": "Machine virtuelle ou conteneur (2D)", "lang": "fr", "kit": "plan",
    "legend": [{"tone": "n", "label": "matériel"}, {"tone": "b", "label": "système"},
               {"tone": "v", "label": "hyperviseur, moteur"}, {"tone": "g", "label": "bibliothèques"},
               {"tone": "y", "label": "appli"}],
    "entities": ents, "steps": [piles],
}
write(lesson, *outputs(HERE, "vm-plan.scene.json", "vm-plan"))

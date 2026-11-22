"""Scènes du bit « Les architectures d'un programme » (courses-foundations/program-architectures), format 0.3.

Retour de Boris (22/11) :
- commencer simple : un poste seul, puis plusieurs postes (le constat : les données ne se partagent pas) ;
- deux tiers avec client lourd, trois tiers avec client léger, tous deux en client-serveur ;
- le n tiers compte les machines (4 tiers : navigateur → serveur web → serveur d'application → BDD ; 5 tiers : + un
  serveur de mails), pas les programmes ; une seule base ;
- les programmes qui collaborent (Recherche, Paiement, Mails, chacun avec ses données) passent dans « Aller plus
  loin : services et micro-services », après les services externes ;
- le récap ajoute une zone « aller plus loin ».
Part de archi_base.json (la leçon 0.2 publiée, écrite à la main) : les blocs repris gardent leurs textes.
Kit Feuilleté, coordonnées brutes [x, y] (la diagonale de l'écran va de [-x, +y] devant à gauche vers [+x, -y]).
"""
import copy
import json
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools" / "scenes"))
from paths import outputs
from scene_kit import L, scene, send, wait, write, hud

BASE = json.load(open(HERE / "archi_base.json", encoding="utf-8"))
STEPS = {s["id"]: s for s in BASE["steps"]}


def ent(step, id, **changes):
    """Bloc repris d'une étape publiée, avec des changements (None efface le champ)."""
    e = copy.deepcopy(next(x for x in STEPS[step]["show"] if x["id"] == id))
    for k, v in changes.items():
        if v is None:
            e.pop(k, None)
        else:
            e[k] = v
    return e


def pulse(at):
    return {"do": "pulse", "at": at}


def shift(e, dx, dy):
    e["at"] = [round(e["at"][0] + dx, 2), round(e["at"][1] + dy, 2)]
    return e


steps = []

# ---------- 1. un poste
p1 = [shift(ent("poste-seul", i), 3.5, -3.5) for i in ("p1", "app1", "data1", "biblio")]
p1[0]["label"] = "poste"
steps.append({
    "id": "poste-seul", "label": "Un poste", "chapter": "un poste", "title": "Un programme sur un poste",
    "body": ["L'appli Prêts est installée sur le poste du comptoir, dans sa fenêtre. Elle **affiche** les écrans, **décide** (le lecteur a-t-il le droit d'emprunter ?) et **stocke** les prêts sur le disque du poste."],
    "hud": [{"label": "machines", "value": 1}],
    "show": p1,
    "links": [L("app1", "data1")],
    "script": [
        wait(800), pulse("biblio:top"),
        send(["biblio", "app1", "data1"], label="prêt", reply="enregistré",
             explain=["La bibliothécaire saisit un prêt : l'**appli Prêts** affiche le formulaire.",
                      "L'appli vérifie les règles, puis écrit le prêt dans ses **données**, sur le disque du poste.",
                      "Le prêt est enregistré. Afficher, décider, stocker : tout se passe sur cette machine."]),
        wait(800),
        send(["biblio", "app1", "data1"], label="livre prêté ?", reply="oui, à Léa",
             explain=["Un peu plus tard, elle cherche si un livre est sorti.",
                      "L'appli lit ses données.",
                      "Elle retrouve le prêt : sur un seul poste, tout va bien."]),
        wait(2600),
    ],
})

# ---------- 2. plusieurs postes : le constat
steps.append({
    "id": "plusieurs-postes", "label": "Plusieurs postes", "chapter": "plusieurs postes",
    "title": "Plusieurs postes : les données ne se partagent pas",
    "body": ["Un deuxième comptoir ouvre : on installe l'appli sur un deuxième poste. Il a sa propre copie de l'appli, et ses propres données."],
    "callout": {"title": "le problème", "text": "Les données vivent sur chaque poste : impossible de les partager."},
    "hud": [{"label": "machines", "value": 1}, {"label": "données", "value": "1 copie"}],
    "show": [ent("poste-seul", i) for i in ("p1", "app1", "data1", "biblio")],
    "links": [L("app1", "data1")],
    "script": [
        wait(700),
        scene(say="Un deuxième comptoir ouvre : on installe l'appli sur un deuxième poste, avec ses propres données.",
              show=[ent("poste-seul", "p2"), ent("poste-seul", "app2"), ent("poste-seul", "data2", note=None),
                    ent("poste-seul", "collegue")],
              link=[L("app2", "data2")], hud=[hud("machines", 2), hud("données", "2 copies séparées", "r")], ms=900),
        pulse("biblio:top"),
        send(["biblio", "app1", "data1"], label="prêt", reply="enregistré",
             explain=STEPS["poste-seul"]["script"][2]["explain"]),
        wait(800), pulse("collegue:top"),
        send(["collegue", "app2", "data2"], label="livre prêté ?", reply="aucun prêt",
             explain=STEPS["poste-seul"]["script"][5]["explain"]),
        scene(say="Chaque poste a sa copie, et les copies ne se parlent pas.",
              set=[{"id": "data2", "note": "ignore le prêt du poste 1"}]),
        wait(2800),
    ],
})

# ---------- 3. deux tiers, client lourd
cl = copy.deepcopy(STEPS["client-lourd"])
cl.update({
    "chapter": "deux tiers", "label": "Deux tiers",
    "title": "Deux tiers : un client lourd, un serveur de données",
    "body": ["Les données quittent les postes : elles vont dans une **base de données**, sur un serveur. Chaque poste garde l'appli installée, qui affiche, décide et calcule : c'est le **client lourd**. Il demande les données au serveur : c'est le **client-serveur**.",
             "Un prêt saisi au poste 1 se voit au poste 3. Mais une nouvelle version de l'appli s'installe poste par poste."],
})
cl["show"] = [e for e in cl["show"]]
for e in cl["show"]:
    if e["id"] == "zdb":
        e["label"] = "serveur BDD"
cl["script"][1]["explain"] = [
    "Au poste 1, la bibliothécaire saisit un prêt dans l'**appli Prêts** installée sur le poste.",
    "L'appli fait elle-même le travail (les règles, la date de retour), puis envoie le prêt à la **base de données**, sur le serveur.",
    "La base confirme : le prêt est enregistré, au seul endroit que tous les postes lisent."]
steps.append(cl)

# ---------- 4. trois tiers, client léger
cg = copy.deepcopy(STEPS["client-leger"])
cg.update({
    "chapter": "trois tiers", "label": "Trois tiers",
    "title": "Trois tiers : un client léger, un serveur web, une base",
    "body": ["Sur les postes, un simple **navigateur**, déjà installé : c'est le **client léger**. Toujours du client-serveur, mais avec un **serveur web** entre les deux : l'appli Prêts y tourne, décide, et parle seule à la base.",
             "Trois rôles, trois places : **afficher** dans le navigateur, **décider** sur le serveur web, **stocker** dans la base. C'est l'architecture **trois tiers**."],
})
for e in cg["show"]:
    if e["id"] == "zweb":
        e["label"] = "serveur web (backend)"
steps.append(cg)

# ---------- 5. n tiers : on compte les machines (l'architecture complète dès le départ, Boris 22/11)
Z = 3.8
MAIL = [
    {"id": "zmail", "kind": "zone", "at": [11, 5], "size": [Z, Z], "label": "serveur de mails"},
    {"id": "mail", "kind": "node", "at": [11, 5], "tone": "y", "title": "Envoi des mails",
     "detail": "Le **serveur de mails** envoie les messages aux lecteurs. D'autres installations ajoutent, à la place ou en plus, une **file d'attente** de messages ou un **serveur d'intégration**, qui relie l'appli à d'autres logiciels."},
    ent("n-tiers", "lecteur", at=[14.5, 1.5]),
]
nt_show = [
    {"id": "zp", "kind": "zone", "at": [-9, 9], "size": [Z, Z], "label": "poste"},
    ent("n-tiers", "nav1", at=[-9, 9]),
    {"id": "zweb", "kind": "zone", "at": [-3, 3], "size": [Z, Z], "label": "serveur web"},
    {"id": "front", "kind": "node", "at": [-3, 3], "tone": "b", "title": "Serveur web", "sub": "en façade",
     "detail": "Le **serveur web en façade** reçoit toutes les demandes des navigateurs. Il envoie lui-même les fichiers qui ne changent pas (images, styles) et passe le reste au serveur d'application. On l'appelle souvent **reverse proxy**."},
    {"id": "zapp", "kind": "zone", "at": [3, -3], "size": [Z, Z], "label": "serveur d'application"},
    {"id": "appsrv", "kind": "node", "at": [3, -3], "tone": "v", "title": "Appli Prêts", "sub": "les règles", "roles": ["décider"],
     "detail": "Le **serveur d'application** fait tourner l'appli Prêts : il applique les règles de la bibliothèque. Il ne reçoit que ce que le serveur web lui passe."},
    {"id": "zdb", "kind": "zone", "at": [9, -9], "size": [4.2, 4.2], "label": "serveur BDD"},
    ent("n-tiers", "db", at=[9, -9]),
    ent("n-tiers", "biblio", at=[-13, 5]),
] + MAIL
NT_LINKS = [L("nav1", "front"), L("front", "appsrv"), L("appsrv", "db"), L("appsrv", "mail"), L("mail", "lecteur")]
steps.append({
    "id": "n-tiers", "label": "n tiers", "chapter": "n tiers", "title": "Le n tiers : on compte les machines",
    "body": ["Le « n » de **n tiers** compte les machines, les serveurs, pas les programmes. Ici, cinq : le poste, un serveur web en façade, le serveur d'application, la base de données et un serveur pour les mails.",
             "Une seule base, et chaque machine a sa tâche."],
    "callout": {"title": "idée clé", "text": "n tiers = le nombre de machines de l'architecture."},
    "hud": [{"label": "tiers", "value": 5}],
    "show": nt_show,
    "links": NT_LINKS,
    "script": [
        wait(800), pulse("biblio:top"),
        send(["biblio", "nav1", "front", "appsrv", "db"], label="prêt", reply="enregistré",
             explain=["La bibliothécaire saisit un prêt dans le **navigateur**.",
                      "Le navigateur l'envoie au **serveur web**, en façade.",
                      "Le serveur web passe la demande au **serveur d'application**, qui applique les règles.",
                      "Le serveur d'application écrit le prêt dans la **base de données**.",
                      "La confirmation remonte par les mêmes machines."]),
        wait(700),
        send(["appsrv", "mail", "lecteur"], tone="y", label="mail de retard",
             explain=["Chaque nuit, l'appli trouve les retards et confie les mails au **serveur de mails**, le cinquième tiers.",
                      "Il écrit à chaque **lecteur** concerné."]),
        wait(2800),
    ],
})

# ---------- 6. services externes : la même architecture, plus deux services chez d'autres
ext_show = copy.deepcopy(nt_show) + [
    {"id": "zbnf", "kind": "zone", "at": [-7, -7], "size": [Z, Z], "tone": "r", "label": "à la BnF"},
    ent("externes", "bnf", at=[-7, -7]),
    {"id": "zpay", "kind": "zone", "at": [-1, -13], "size": [Z, Z], "tone": "r", "label": "chez un prestataire"},
    ent("externes", "payx", at=[-1, -13]),
]
ex = copy.deepcopy(STEPS["externes"])
ex.update({
    "hud": [{"label": "chez vous", "value": "5 machines"}, {"label": "chez d'autres", "value": "2 services"}],
    "labels": "left",
    "show": ext_show,
    "links": NT_LINKS + [L("appsrv", "bnf"), L("appsrv", "payx")],
    "script": [
        wait(800), pulse("biblio:top"),
        send(["biblio", "nav1", "front", "appsrv", "bnf"], label="ISBN", reply="titre, auteur",
             explain=["La bibliothécaire ajoute un livre : elle saisit son numéro ISBN dans le **navigateur**.",
                      "Le navigateur l'envoie au serveur web…",
                      "… qui le passe à l'**appli Prêts**.",
                      "L'appli Prêts ne connaît pas ce livre : elle demande sa fiche au **catalogue de la BnF**.",
                      "La BnF répond avec le titre et l'auteur : personne n'a rien eu à retaper."]),
        wait(700),
        send(["biblio", "nav1", "front", "appsrv", "payx"], label="amende par carte", reply="payé",
             explain=["Un lecteur règle son amende par carte bancaire, au comptoir.",
                      "Le navigateur envoie le paiement au serveur web…",
                      "… qui le passe à l'**appli Prêts**.",
                      "Encaisser une carte est un métier : l'appli Prêts le confie au **prestataire de paiement**.",
                      "Le prestataire répond « payé »."]),
        send(["appsrv", "db"], label="amende réglée",
             explain=["C'est l'appli Prêts qui note l'amende réglée dans **sa** base : le prestataire n'y a pas accès."]),
        wait(3000),
    ],
})
steps.append(ex)

# ---------- 7. aller plus loin : services, micro-services
S = 5.6
svc_show = [
    {"id": "zp", "kind": "zone", "at": [-10, 10], "size": [3.8, 3.8], "label": "poste"},
    ent("n-tiers", "nav1", at=[-10, 10]),
    {"id": "zweb", "kind": "zone", "at": [-3.5, 3.5], "size": [S, S], "label": "service Prêts"},
    ent("n-tiers", "web", at=[-4.7, 4.7], roles=["décider"]),
    {"id": "dbp", "kind": "store", "at": [-2.3, 2.3], "tone": "n", "title": "Prêts", "roles": ["stocker"],
     "detail": "Chaque service garde **ses propres données** : ici, les prêts. Les autres services n'y touchent pas : ils demandent au service Prêts."},
    {"id": "zsearch", "kind": "zone", "at": [-3.5, -7], "size": [S, S], "label": "service Recherche"},
    ent("n-tiers", "search", at=[-4.7, -5.8]),
    {"id": "idx", "kind": "store", "at": [-2.3, -8.2], "tone": "n", "title": "Catalogue", "roles": ["stocker"]},
    {"id": "zpay", "kind": "zone", "at": [7, 3.5], "size": [S, S], "label": "service Paiement"},
    ent("n-tiers", "pay", at=[5.8, 4.7]),
    {"id": "dpay", "kind": "store", "at": [8.2, 2.3], "tone": "n", "title": "Amendes", "roles": ["stocker"]},
    {"id": "zmails", "kind": "zone", "at": [7, -7], "size": [3.8, 3.8], "label": "service Mails"},
    ent("n-tiers", "mails", at=[7, -7]),
    ent("n-tiers", "biblio", at=[-14, 6]),
    ent("n-tiers", "lecteur", at=[12, -10]),
]
steps.append({
    "id": "services", "label": "Services", "chapter": "aller plus loin", "title": "Aller plus loin : des services, chacun ses données",
    "body": ["Une grande application se découpe en **services** : Prêts, Recherche, Paiement, Mails. Chacun a une seule tâche et **ses propres données** ; ils se parlent par leurs API, comme avec un service externe.",
             "On parle d'architecture **orientée services**, ou de **micro-services** quand ils sont nombreux et petits."],
    "callout": {"title": "le prix", "text": "Plus de programmes à déployer et à surveiller : il faut des outils et une organisation pour ça."},
    "hud": [{"label": "services", "value": 4}, {"label": "bases", "value": 3}],
    "show": svc_show,
    "links": [L("nav1", "web"), L("web", "dbp"), L("web", "search"), L("search", "idx"), L("web", "pay"),
              L("pay", "dpay"), L("mails", "web"), L("mails", "lecteur")],
    "script": [
        wait(800), pulse("biblio:top"),
        send(["biblio", "nav1", "web", "search", "idx"], label="recherche", reply="2 exemplaires",
             explain=["La bibliothécaire cherche un livre dans le **navigateur**.",
                      "Le navigateur envoie la recherche au service **Prêts**.",
                      "Prêts ne cherche pas lui-même : il demande au service **Recherche**.",
                      "Recherche fouille **son** catalogue.",
                      "Il répond « 2 exemplaires », et la réponse remonte jusqu'à l'écran."]),
        wait(700),
        send(["web", "pay", "dpay"], label="amende", reply="réglée",
             explain=["Un lecteur paie son amende : Prêts confie l'encaissement au service **Paiement**.",
                      "Paiement note l'amende réglée dans **ses** données.",
                      "Il confirme à Prêts."]),
        wait(700),
        send(["mails", "web", "dbp"], label="retards ?", reply="3 retards",
             explain=["La nuit, le service **Mails** a besoin des retards. Il ne lit pas la base des prêts : il demande au service Prêts.",
                      "Prêts lit **ses** données.",
                      "Il répond : trois retards."]),
        send(["mails", "lecteur"], tone="y", label="mail de retard",
             explain=["Mails écrit à chaque **lecteur** concerné."]),
        wait(2800),
    ],
})

# ---------- 8. récap, avec la zone « aller plus loin »
rc = copy.deepcopy(STEPS["recap"])
keep = [e for e in rc["show"] if not e["id"].startswith("r4")]
for e in keep:
    if e["id"] == "r2z":
        e["label"] = "2 · deux tiers, client lourd"
    if e["id"] == "r3z":
        e["label"] = "3 · trois tiers, client léger"
r4 = [
    {"id": "r4z", "kind": "zone", "at": [10, -1], "size": [7.5, 7.5], "label": "4 · n tiers, ici 4"},
    {"id": "r4n", "kind": "node", "at": [7.2, 1.8], "size": [1.6, 1.6, 0.9], "tone": "b", "title": "Navigateur", "roles": ["afficher"]},
    {"id": "r4f", "kind": "node", "at": [9.1, -0.1], "size": [1.6, 1.6, 0.9], "tone": "b", "title": "Serveur web"},
    {"id": "r4w", "kind": "node", "at": [11, -2], "size": [1.6, 1.6, 0.9], "tone": "v", "title": "Serveur d'app", "roles": ["décider"]},
    {"id": "r4d", "kind": "store", "at": [12.9, -3.9], "tone": "n", "title": "BDD", "roles": ["stocker"]},
]
r5 = [
    {"id": "r5z", "kind": "zone", "at": [10.5, 10.5], "size": [7.5, 7.5], "label": "plus loin · services"},
    {"id": "r5a", "kind": "node", "at": [8.5, 12.5], "size": [1.6, 1.6, 0.9], "tone": "v", "title": "Prêts"},
    {"id": "r5b", "kind": "node", "at": [12.5, 12.5], "size": [1.6, 1.6, 0.9], "tone": "g", "title": "Recherche"},
    {"id": "r5c", "kind": "node", "at": [8.5, 8.5], "size": [1.6, 1.6, 0.9], "tone": "r", "title": "Paiement"},
    {"id": "r5d", "kind": "node", "at": [12.5, 8.5], "size": [1.6, 1.6, 0.9], "tone": "y", "title": "Mails"},
]
rc.update({
    "title": "La bibliothèque sous ses formes",
    "body": ["- **Un poste** : les trois rôles sur la même machine ; les données ne se partagent pas.\n- **Deux tiers**, client lourd : l'appli sur chaque poste, la base sur un serveur ; mise à jour poste par poste.\n- **Trois tiers**, client léger : afficher dans le navigateur, décider sur le serveur web, stocker dans la base.\n- **n tiers** : n compte les machines ; la base reste une seule.\n- **Plus loin** : des services, chacun sa tâche et ses données."],
    "hud": [{"label": "formes", "value": "4 + 1"}],
    "show": keep + r4 + r5,
    "links": [L("r2a", "r2d"), {"path": ["r3n", "r3w", "r3d"]}, {"path": ["r4n", "r4f", "r4w", "r4d"]},
              L("r5a", "r5b"), L("r5a", "r5c"), L("r5d", "r5a")],
})
steps.append(rc)

lesson = {
    "format": "bl-scenes/0.3", "id": "program-architectures",
    "title": BASE["title"], "lang": "fr", "kit": "feuillete",
    "legend": BASE["legend"], "steps": steps,
}
write(lesson, *outputs(HERE, "architectures.scene.json", "archi"))

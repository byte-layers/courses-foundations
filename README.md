# courses-foundations

Les contenus de base de byte_layers, pour qui débute : ce qu'est un ordinateur, ce que font ses programmes et comment ils se répartissent entre les machines. Un dossier par contenu, à plat, chacun avec son `.layers/`.

| Dossier | Contenu | Type |
|---|---|---|
| `computer-layers/` | L'ordinateur en couches, du matériel au premier script | bit, avec trois plays |
| `first-script-lab/` | Votre premier script, sur votre machine | lab |
| `code-editor/` | De l'éditeur de texte à l'éditeur de code | bit |
| `compiled-or-interpreted/` | Compilé ou interprété : du code source au programme qui tourne | bit |
| `dev-setup-lab/` | Votre poste de développeur : VS Code et un premier programme | lab |
| `program-architectures/` | Les architectures d'un programme, du poste seul au n tiers | bit |
| `virtual-machines-and-containers/` | Machines virtuelles et conteneurs : plusieurs machines sur une seule | bit |
| `intro-review/` | Quiz de fin d'introduction : du matériel aux conteneurs | bit |

Ensemble, ils forment l'introduction à l'informatique, à lire dans l'ordre du tableau. Chaque contenu a son tag, de la forme `<dossier>/vN`. Les bits demandent l'extension 0.8.0 (schémas animés au format `bl-scenes/0.3`, quiz et terminal sur le plateau) ; les labs, 0.4.0. Si vous essayez les commandes, les fichiers vont dans `~/byte-layers/`.

## Régénérer un schéma animé

Les fichiers `.layers/assets/*.scene.json` sont écrits par des scripts Python, rangés dans le dossier `scenes/` du contenu (hors de `.layers/`, donc non publiés) :

| Contenu | Script | Fichier écrit |
|---|---|---|
| `code-editor` | `scenes/editor.py`, `scenes/ide_plan.py` | `editor.scene.json`, `ide.scene.json` |
| `compiled-or-interpreted` | `scenes/trad_plan.py`, `scenes/compile.py` | `traduction.scene.json`, `compile.scene.json` |
| `program-architectures` | `scenes/archi.py` (lit `scenes/archi_base.json`) | `architectures.scene.json` |
| `virtual-machines-and-containers` | `scenes/vmct.py`, `scenes/vm_plan.py` | `vm-containers.scene.json`, `vm-plan.scene.json` |

On corrige le script, jamais le JSON à la main, puis on le relance depuis la racine du dépôt : `python3 program-architectures/scenes/archi.py`. Les scripts importent `tools/scenes/scene_kit.py` (copie du kit de la skill byte-layers-scenes) et `tools/scenes/paths.py`, qui dit où écrire ; avec `BL_SCENES` pointant sur `packages/scenes` d'un worktree du monorepo, la scène est aussi écrite dans `lessons/zz-<id>/` pour la valider et la capturer. `computer-layers/.layers/assets/os.scene.json` n'a pas de script : il se corrige directement.

Licence : CC BY-NC-SA 4.0.

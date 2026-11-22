# le script de l'auteur, écrit puis lancé (layers-lint)
cat > ranger.sh <<'FIN'
#!/bin/bash
# range le dossier
mkdir -p photos sauvegarde
mv IMG_001.jpg IMG_002.jpg photos/
cp facture.pdf sauvegarde/
rm -r tmp
FIN
bash ranger.sh

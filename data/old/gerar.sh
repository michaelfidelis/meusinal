
clear
echo "Gerando código..."
for i in *.png; do
    echo configuracoes[\'`echo $i | cut -d. -f1`\'] = cv2.imread\(\'data/`echo $i`\', 0\);
done >> data.txt
echo "Fim..."

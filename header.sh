for file in dfoil*chrom*
do
cp dfoil.#chromchrom.canis.txt headers.$file
done

for file in dfoil*chrom*
do
cat dfoil.#chromchrom.canis.txt ${file} > Canis.$file
done

for file in Canis*
do
python ../Dfoil.py --infile $file --out $file.out.txt --plot write --plot_path $file.png 
done

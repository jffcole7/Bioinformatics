#!/bin/sh

#kallisto index -i Hawaii.transcripts.idx combined.Hawaii.95.fa
WD=$(pwd)

cd /media/BigRAID/HawaiianTetragnathaVenomeAssemblies/Feb2016

for f1 in  *1.fq.gz
do 
	f2=${f1%%1.fq.gz}"2.fq.gz"
	~/transcriptome_programs/trinityrnaseq-2.2.0/util/align_and_estimate_abundance.pl --transcripts $WD/combined.Hawaii.95.fa \
	--seqType fq --left $f1 --right $f2 --est_method kallisto --output_dir $WD/abundance/${f1%%1.fq.gz}"output" --trinity_mode --prep_reference
	#kallisto quant -i $WD/Hawaii.transcripts.idx -o $WD/abundance/${f1%%1.fq.gz}"output" -b 100 $f1 $f2 
done

cd $WD



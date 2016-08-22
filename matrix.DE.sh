~/transcriptome_programs/trinityrnaseq-2.2.0/util/abundance_estimates_to_matrix.pl --est_method kallisto \
--out_prefix trans_counts \
--name_sample_by_basedir \
Tacuta/abundance.tsv \
Tpilosa/abundance.tsv 

~/transcriptome_programs/trinityrnaseq-2.2.0/util/abundance_estimates_to_matrix.pl --est_method kallisto \
--out_prefix gene_counts \
--name_sample_by_basedir \
Tacuta/abundance.tsv.genes \
Tpilosa/abundance.tsv.genes

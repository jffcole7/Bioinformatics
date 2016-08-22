~/transcriptome_programs/trinityrnaseq-2.2.0/util/abundance_estimates_to_matrix.pl --est_method kallisto \
--out_prefix trans_counts \
--name_sample_by_basedir \
TstelarobustaWaikamoi/abundance.tsv \
TstelarobustaWestmaui/abundance.tsv \
TpaludicolaMolokai/abundance.tsv \
TpaludicolaWestmaui/abundance.tsv

~/transcriptome_programs/trinityrnaseq-2.2.0/util/abundance_estimates_to_matrix.pl --est_method kallisto \
--out_prefix gene_counts \
--name_sample_by_basedir \
TstelarobustaWaikamoi/abundance.tsv.genes \
TstelarobustaWestmaui/abundance.tsv.genes \
TpaludicolaMolokai/abundance.tsv.genes \
TpaludicolaWestmaui/abundance.tsv.genes 

~/transcriptome_programs/trinityrnaseq-2.2.0/util/abundance_estimates_to_matrix.pl --est_method kallisto \
--out_prefix trans_counts \
--name_sample_by_basedir \
Tpilosa/abundance.tsv \
Tquasimodo1/abundance.tsv \
Tquasimodo2/abundance.tsv \
TstelarobustaWaikamoi/abundance.tsv \
TstelarobustaWestmaui/abundance.tsv \
TpaludicolaWestmaui/abundance.tsv \
TpaludicolaMolokai/abundance.tsv \
Tacuta/abundance.tsv


~/transcriptome_programs/trinityrnaseq-2.2.0/util/abundance_estimates_to_matrix.pl --est_method kallisto \
--out_prefix gene_counts \
--name_sample_by_basedir \
Tpilosa/abundance.tsv.genes \
Tquasimodo1/abundance.tsv.genes \
Tquasimodo2/abundance.tsv.genes \
TstelarobustaWaikamoi/abundance.tsv.genes \
TstelarobustaWestmaui/abundance.tsv.genes \
TpaludicolaWestmaui/abundance.tsv.genes \
TpaludicolaMolokai/abundance.tsv.genes \
Tacuta/abundance.tsv.genes

~/transcriptome_programs/trinityrnaseq-2.2.0/Analysis/DifferentialExpression/run_DE_analysis.pl  \
--matrix Spiny_vs_Web/trans_counts.counts.matrix --method voom --samples_file Spiny_vs_Web/Spiny_vs_Web.described.txt \
--output Spiny_vs_Web/

~/transcriptome_programs/trinityrnaseq-2.2.0/Analysis/DifferentialExpression/run_DE_analysis.pl  \
--matrix Spiny_vs_Web/gene_counts.counts.matrix --method voom --samples_file Spiny_vs_Web/Spiny_vs_Web.described.txt \
--output Spiny_vs_Web/

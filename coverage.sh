for BAM in *.sorted.bam
do
java -jar /home/brewerlab/transcriptome_programs/picard-tools-1.119/CollectAlignmentSummaryMetrics.jar I=$BAM O=$BAM.stats
done

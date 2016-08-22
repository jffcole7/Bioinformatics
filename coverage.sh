#for BAM in *.sorted.bam
#do
#java -jar /home/brewerlab/transcriptome_programs/picard-tools-1.119/CollectAlignmentSummaryMetrics.jar I=$BAM O=$BAM.stats
#done


for BAM in *.sorted.bam
do
java -Xmx4g -jar~/BAMStats-1.25/BAMStats-1.25.jar -i $BAM -o $BAM.BAMstats
done

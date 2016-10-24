#!/bin/bash
# goals of this program
# 1. input any number of fasta files
# 2. I will subset them for the longest isoform
# 3. I will then assume that each fasta file is nested under this direcory in subdirectories whose names (the subdirectories) identify the sample id
# 4. I will then append the sample id to the header and then concatenate all subsetted fasta files
# 5. I will then run a blast all vs all on that file
# 6. I will then cluster those results
# 7. Then I will align them
    # 7.5 I may also visualize those using R
# 8. Then I will do paml and MEME stuff to them

for f in $*
do
filename=$(basename "$f")
directory=$(dirname "$f")
echo $filename >>tmp.filename.txt
echo $directory>>tmp.directory.txt
done

uniqueFilenames=$(uniq -c tmp.filename.txt|wc -l)
uniqueDirectories=$(uniq -c tmp.directory.txt|wc -l)
rm tmp.filename.txt tmp.directory.txt

for f in $*
do
if [ "$uniqueFilenames" !=   "1" ]
then
    sampleID =$(basename "$f")

elif [ "$uniqueDirectories" != "1" ]
then
    sampleID =$(dirname "$f")
else
    echo "we were unable to determine which files contained sample id in filename or directoryname"
    exit

fi

cat $f |grep ">" |sed -e 's/>//g' > headers_of_interest.txt
cat headers_of_interest.txt |awk '{print $1,$5}'|cut -d':' -f1,3,8|awk -F':' '{print $2,$3}'|awk -F'|' '{print $1,$2 }'>preppedHeader.txt

echo 'transcripts<-read.table("preppedHeader.txt")'>tmp.R
echo 'aa <- transcripts[order(transcripts$V1, -abs(transcripts$V3) ), ]'>> tmp.R
echo 'write.table( aa[ !duplicated(aa$V1), ] ,file="longestIsoformID.txt",row.names=F,col.names=F,quote=F)'>>tmp.R


Rscript tmp.R
wc -l headers_of_interest.txt longestIsoformID.txt
rm tmp.R

awk '{print $1"|"$2}' longestIsoformID.txt > tmp.txt

python /media/BigRAID/JeffTemp/Bioinformatics/FasTool_v2.2.py -i $f -o $sampleID.longestIsoform.fasta -id tmp.txt

grep -c ">" Trinity.fasta.transdecoder.pep
grep -c ">" longestIsoform.Trinity.fasta
rm tmp.txt

sed -ie  "s/>/>$sampleID/g" $sampleID.longestIsoform.fasta

done

cat *longestIsoform* > All.samples.fasta









cat Trinity.fasta.transdecoder.pep |grep ">" |sed -e 's/>//g' > headers_of_interest.txt

cat headers_of_interest.txt |awk '{print $1,$5}'|cut -d':' -f1,3,8|awk -F':' '{print $2,$3}'|awk -F'|' '{print $1,$2 }'>preppedHeader.txt

echo 'transcripts<-read.table("preppedHeader.txt")'>tmp.R
echo 'aa <- transcripts[order(transcripts$V1, -abs(transcripts$V3) ), ]'>> tmp.R
echo 'write.table( aa[ !duplicated(aa$V1), ] ,file="longestIsoformID.txt",row.names=F,col.names=F,quote=F)'>>tmp.R
# this does the same thing but a one-liner
#printf 'transcripts<-read.table("preppedHeader.txt")transcripts<-read.table("preppedHeader.txt")\n aa <- transcripts[order(transcripts$V1, -abs(transcripts$V3) ), ] \n write.table( aa[ !duplicated(aa$V1), ] ,file="longestIsoformID.txt",row.names=F,col.names=F,quote=F)' >tmp.R


Rscript tmp.R
wc -l headers_of_interest.txt longestIsoformID.txt
rm tmp.R

awk '{print $1"|"$2}' longestIsoformID.txt > tmp.txt

python /media/BigRAID/JeffTemp/Bioinformatics/FasTool_v2.2.py -i Trinity.fasta.transdecoder.pep -o longestIsoform.Trinity.fasta -id tmp.txt

grep -c ">" Trinity.fasta.transdecoder.pep
grep -c ">" longestIsoform.Trinity.fasta
rm tmp.txt

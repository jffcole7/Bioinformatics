cysMotifAwise <- read.table("CysAwiseTemp.txt", header=F)
cysMotifTransDecod <- read.table("CysTransDecodTemp.txt", header=F)

subset(data.frame(table(cysMotifAwise$V2)),data.frame(table(cysMotifAwise$V2))$Freq>2)
subset(data.frame(table(cysMotifTransDecod$V2)),data.frame(table(cysMotifTransDecod$V2))$Freq>2)

transcriptTransDecod <- read.table("Transcript.transdecod.txt", header=F)
transcriptAwise <- read.table("Transcript.awise.txt", header=F)
 names(transcriptAwise) <- c("seq","len")
 names(transcriptTransDecod) <- c("len","seq")
 sharedORF<-merge(transcriptTransDecod,transcriptAwise)
 sharedORF$diff <- sharedORF$lenA -  sharedORF$lenT


 completeTransDecod <- read.table("complete.transdecod.txt", header=F)
 completeAwise <- read.table("complete.awise.txt", header=F)
 names(completeAwise) <- c("seq","len")
 names(completeTransDecod) <- c("len","seq")

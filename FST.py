def FST(allele1,allele2):
    allele1 =float(allele1)
    allele2 = float(allele2)

    diff = allele1 - allele2
    print diff
    diffSq = diff**2
    print diffSq
    summ = allele1 + allele2
    print summ
    avg = summ *0.5
    print avg
    denominator = 2 * avg * (1-avg)
    print denominator
    FST = diffSq / denominator
    return FST

print FST(0.4,0.3)

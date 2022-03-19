baseStrings = ["ensembleAtheismtrain.tsv -t ensembleAtheismtest.tsv"]
baseStrings.append("ensembleClimatetrain.tsv -t ensembleClimatetest.tsv")
baseStrings.append("ensembleFeminismtrain.tsv -t ensembleFeminismtest.tsv")
baseStrings.append("ensembleHillarytrain.tsv -t ensembleHillarytest.tsv")
baseStrings.append("ensembleLegalizationtrain.tsv -t ensembleLegalizationtest.tsv")
PBaseList = []
ParaList = []
aPBase = " -a "
aPVaList = ["0","1",'2','3','4']
mPBase = " -m "
mPVaList = ["O","M",'J','D','C','N','L',"DC",'I']
wPBase = " -w "
wPVaList = ["0","1",'2','3','4']
kPBase = " -k "
kPVaList = range(1,11,1)
dPBase = " -d "
dPVaList = ["Z","ID",'IL','3','4']
lPBase = " -L "
lPVaList = range(1,6,1)
bPBase = " -b "
bPVaList = range(1,6,1)
qPBase = " -q "
qPVaList = range(1,6,1)
rPBase = " -R "
rPVaList = range(1,6,1)
f = open("clList.txt", "w")

for base in baseStrings:
    para0 = base
    para01 = para0 + aPBase
    for aP in aPVaList:
        para1 = para01 + aP
        para11 = para1 + mPBase
        for mP in mPVaList:
            para2 = para11 + mP
            para21 = para2 + wPBase
            for wP in wPVaList:
                para3 = para21 + wP
                para31 = para3 + kPBase
                for kP in kPVaList:
                    para4 = para31 + kP.__str__()
                    para41 = para4 + dPBase
                    for dP in dPVaList:
                        para5 = para41 + dP
                        para51 = para5 + lPBase
                        for lP in lPVaList:
                            para6 = para51 + lP.__str__()
                            para61 = para6 + bPBase
                            for bP in bPVaList:
                                para7 = para61 + bP.__str__()
                                para71 = para7 + qPBase
                                for qP in qPVaList:
                                    para8 = para71 + qP.__str__()
                                    para81 = para8 + rPBase
                                    for rP in rPVaList:
                                        para9 = para81 + rP.__str__()
                                        para9 += ' | grap \"overall accuracy\"'
                                        print(para9, file=f)
f.close()


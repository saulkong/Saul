__author__ = 'xiaocong'

import itertools
class AssociationRules(object):
    def __init__(self,dataset):
        self.sup=0.4
        self.conf=0.8
        self.rawdatas=map(set,dataset)
        self.frequentset=[]
        self.frequentsetinfo={}
        self.rawdataslength=float(len(self.rawdatas))



    def CreatePrimarySet(self):
        """generate primary candidate set"""

        C1=[]
        for rawdata in self.rawdatas:
            for word in rawdata:
                if not [word] in C1:
                    C1.append([word])
        C1.sort()
        return map(frozenset,C1)

    def Scan(self,Ck):
        """scan candidate set and generate frequent set"""

        caninfo={}
        freqset=[]
        freqsetinfo={}
        for item in Ck:
            for rawdata in self.rawdatas:
                if item.issubset(rawdata):
                    if not caninfo.has_key(item):
                        caninfo[item]=1
                    else:
                        caninfo[item]+=1

        for key in caninfo:
            freq=caninfo[key]/self.rawdataslength
            if freq >= self.sup:
                freqset.append(key)
                freqsetinfo[key]=freq
                self.frequentsetinfo[key]=freq

        self.frequentset.append(freqset)

    def AprioriSetGen(self,C2,k):
        """merge frequent set into new frequent set """

        canset=[]
        for i in range(0,len(C2)):
            for j in range(i+1,len(C2)):
                L1=list(C2[i])[:k-2]
                L2=list(C2[j])[:k-2]
                L1.sort()
                L2.sort()
                if L1==L2:
                    canset.append(C2[i]|C2[j])
        return canset

    def Excute(self):
        """excuting"""
        C1=self.CreatePrimarySet()
        self.Scan(C1)
        k=2
        while(k <= 4):
            Ck=self.AprioriSetGen(self.frequentset[k-2],k)
            self.Scan(Ck)
            k+=1

        for set in self.frequentset:
            print 'frequent-set : %s' %set





    def Pruning(self):
        """pruning"""
        for i in range(1,len(self.frequentset)):
            for freqset in self.frequentset[i]:
                H1_len=len(freqset)
                for i in range(1,H1_len):
                    H1_child=map(frozenset,itertools.combinations(freqset,i))
                    for h1_childs in H1_child:
                        confi=self.frequentsetinfo[freqset]/self.frequentsetinfo[freqset-h1_childs]
                        if confi>self.conf:
                            print 'Stong Rule , %s passes in the case of %s ,confidence level is %f'%\
                                  (map(str,freqset),map(str,freqset-h1_childs),confi)



def ReadFile(file):
    """read file"""

    return [sorted(list(set(e.split())))for e in open(file).read().strip().split('\n')]

def main():
    filedata=ReadFile('/Users/xiaocong/Downloads/apriori_data_file.txt')
    run=AssociationRules(filedata)
    run.Excute()
    run.Pruning()



if __name__=='__main__':
    main()





















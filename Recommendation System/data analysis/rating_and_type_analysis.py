__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

from mongodb_conn import Mongodb_connect
import itertools
import codecs

connection=Mongodb_connect().conn()

coll=connection.doubaninfo  #collection name is doubaninfo



class Relation_between_Rating_and_Type(object):

    def __init__(self,dataset):
        self.sup=0.02
        self.conf=0.7
        self.rawdatas=map(set,dataset)
        self.frequentset=[]
        self.frequentsetinfo={}
        self.rawdataslength=float(len(self.rawdatas))
        self.write_to=codecs.open('/Users/xiaocong/Downloads/douban_confi.txt','a','utf-8')

    def CreatePrimaryset(self):
        """
        generate primary candidate set
        """

        C1=[]
        for rawdata in self.rawdatas:
            for word in rawdata:
                if not [word] in C1:
                    C1.append([word])
        return map(frozenset,C1)


    def Scan(self,Ck):
        """
            scan candidate set and generate frequent set
        """
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
            if freq>=self.sup:
                #print freq
                freqset.append(key)
                freqsetinfo[key]=freq
                self.frequentsetinfo[key]=freq
        self.frequentset.append(freqset)



    def RelationSetGen(self,C2,k):
        """
        merge frequent set into new frequent set
        """

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
        """
        excute
        """
        C1=self.CreatePrimaryset()
        self.Scan(C1)
        k=2
        while(k<=3):
            Ck=self.RelationSetGen(self.frequentset[k-2],k)
            self.Scan(Ck)
            k+=1

        for set in self.frequentset:
            print 'frequent-set : %s' % set

    def pruning(self):
        """pruning"""

        for i in range(1,len(self.frequentset)):
            for freqset in self.frequentset[i]:
                H1_len=len(freqset)
                for i in range(1,H1_len):
                    H1_child=map(frozenset,itertools.combinations(freqset,i))
                    for h1_childs in H1_child:
                        confi=self.frequentsetinfo[freqset]/self.frequentsetinfo[freqset-h1_childs]
                        if confi>self.conf:

                            freqset__=[]
                            freqset_minor_h1_childs=[]
                            for freqset_item in list(freqset):
                                #print freqset_item.encode('utf-8')
                                freqset__.append(freqset_item)
                            for freqset_minor_h1_childs_item in list(freqset-h1_childs):
                                #print freqset_minor_h1_childs_item
                                freqset_minor_h1_childs.append(freqset_minor_h1_childs_item)
                            print 'Strong Rule ,%s passes in the case of %s , confidence level is %f'%\
                                  (freqset__,freqset_minor_h1_childs,confi)
                            for i in range(len(freqset__)):
                                self.write_to.write(freqset__[i]+',')
                            self.write_to.write('\t')
                            for i in range(len(freqset_minor_h1_childs)):
                                self.write_to.write(freqset_minor_h1_childs[i]+',')
                            self.write_to.write('\t')
                            self.write_to.write(str(confi))
                            self.write_to.write('\n')






def GetData():
    """
    list film_type whose average_grading is above 7.5 from mongodb
    """

    film_type_list=[]
    collection=coll.find({'film_grading':{'$elemMatch':{'average_grading':{'$gte':'7.5'}}}})
    for item in collection:
        film_type_list.append(item['film_type'])

    return film_type_list


if __name__=='__main__':
    data=Relation_between_Rating_and_Type(GetData())
    data.Excute()
    data.pruning()
    data.write_to.close()



















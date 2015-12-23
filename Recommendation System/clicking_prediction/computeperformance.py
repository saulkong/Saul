__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

def Recall_Precision(users_items,test,K,rank):
    #return recall proportion and precision proportion
    hit=0
    all_recall=0
    all_precision=0
    for user in users_items.keys():
        if user in test:
            items_test=test[user]
            for i in range(len(rank[user])):
                item=rank[user][i].keys()[0]
                if item in items_test:
                    hit+=1
            all_recall+=len(items_test)
            all_precision+=K
    return hit/(all_recall*1.0),hit/(all_precision*1.0)

def Coverage(users_items,rank):
    recommend_items=set()
    all_items=set()
    for user in users_items.keys():
        for item in users_items[user]:
            all_items.add(item)
        for i in range(len(rank[user])):
            item=rank[user][i].keys()[0]
            recommend_items.add(item)
    return len(recommend_items)/(len(all_items)*1.0)



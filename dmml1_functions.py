# -*- coding: utf-8 -*-
"""
dmml 2020 assignment 1 
b naveen kumar reddy mds201909
kshitish krit nanda mds201915
"""
from collections import defaultdict
from itertools import combinations


def readtransactions(docword_filename: str, vocab_filename):
    '''
    input: filename like docword.kos.txt which contains docllist and wordlist
    output: D - number of documents in text collection
            W - number of words in the vocabulary
            N - total number of doc - word - count tuples starting from the next line
            transactions - dictionary of {doc1:{word1,word2}, doc2:{word2}}
    '''
    with open(docword_filename) as f:
        D = int(f.readline())
        W = int(f.readline())
        N = int(f.readline())
        transactions = defaultdict(set)
        docs_of_words = defaultdict(set)
        for line in f:
            transaction = list(map(int, line.split(' ')))
            transactions[transaction[0]].add(transaction[1])
            docs_of_words[transaction[1]].add(transaction[0])
    with open(vocab_filename) as g:
        vocabulary = defaultdict(str)
        line_counter = 1
        for line in g:
            vocabulary[line_counter] = line.strip()
            line_counter += 1
    return (transactions, vocabulary, docs_of_words)


def initialcandidates(docs_of_words):
    return(docs_of_words.keys())


def secondcandidates(F1):
    return(combinations(F1, 2))


def frequentitems(candidates, docs_of_words, min_sup, num_transactions):
    frequentitemlist = []
    min_sup_num = min_sup * num_transactions

    for candidate in candidates:
        if type(candidate) is int:
            if len(docs_of_words[candidate]) > min_sup_num:
                frequentitemlist.append(candidate)
        elif type(candidate) is tuple:
            set_intersection = docs_of_words[candidate[0]]
            for element in candidate[1:]:
                set_intersection = set_intersection & docs_of_words[element]
            if len(set_intersection) > min_sup_num:
                frequentitemlist.append(candidate)

    return frequentitemlist


def Kcandidates(Fk, k):
    '''
    let us assume the Fk is of this form
    [(1,2,3,4), (4,3,2,5), (2,5,3,1)]
    first i need to the inside elements and sort all the tuples
    [(1,2,3,4),(1,2,3,5),(2,3,,4,5)]
    [(1,2,3,4,5)]
    '''
    l = len(Fk)
    print("length of fk for k", l, k)
    candidates = []
    #F = sorted(list(F))
    for i in range(l):
        for j in range(i+1, l):
            f1 = Fk[i]
            f2 = Fk[j]
            if f1[:-1] == f2[:-1]:
                c = list(f1) + [f2[-1]]
                count = 0
                for s in combinations(c, k-1):

                    if s not in Fk:
                        break
                    else:
                        count += 1
                if count == k:
                    candidates.append(tuple(c))
            else:
                break

    return candidates


def apriori(min_sup, K, transactions, vocabulary, docs_of_words):
    answer = []
    num_transactions = len(transactions)
    k = 1

    C1 = initialcandidates(docs_of_words)
    F1 = frequentitems(C1, docs_of_words, min_sup, num_transactions)
    F1.sort()
    answer.append(F1)
    k += 1

    C2 = secondcandidates(F1)
    F2 = frequentitems(C2, docs_of_words, min_sup, num_transactions)
    answer.append(F2)
    k += 1

    Fk = F2
    while(k <= K and Fk != []):
        print("im inside", k)
        Ck = Kcandidates(Fk, k)

        if Ck is None:
            k += 1
        else:
            Fk = frequentitems(Ck, docs_of_words, min_sup, num_transactions)
            answer.append(Fk)
            k += 1
    return answer

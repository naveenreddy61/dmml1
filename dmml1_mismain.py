"""
dmml 2020 assignment 1 
b naveen kumar reddy mds201909
kshitish krit nanda mds201915
"""

from dmml1_mis import *

'''
parameters of MSapriori function:
LS = lowerst support
beta- 0 represents case of normal apriori algo 1 represents where every mis greater than LS is its own frequency
K = max size of itemset
'''

def numbersToWords(answer, vocabulary, outputfile):
    '''
    INPUT:  answer will be frequent itemsets of form list of lists
            ex-[[(0.1,1),(0.2,2),(0.3,3)],[[((0.1,1),(0.2,2))],[(0.1,1),(0.2,2)]]]
            vocabulary is dict of form {1:'a',2:'the'}
            outputfile is string which is where the output will be stored
    OUTPUT: out file will be opened with name outputfile and each number will be converted,
            to corresponding word which is stored vocabulary dictionary
    '''
    out = open(outputfile, "w")
    for i in range(0, len(answer)):
        if i == 0:
            # itemsets of size 1 is treated as a special case
            F = []
            for _,element1 in answer[0]:
                F.append(vocabulary[element1])
            out.write(str(F)+'\n')
        else:
            # take each sublist, get the words associated with each number inside the tuple,
            # check vocabulary and create a new list
            F = []
            for klist in answer[i]:
                F.append(list((vocabulary[element]
                     for _,element in klist)))
            out.write(str(F)+'\n')
    out.close()
    return


LS = 0.08
beta = 0.8
K = 5
phi  = 0.2
test_transactions,test_vocabulary, test_docs_of_words, test_count_of_words =readtransactions('docword.test.txt','vocab.test.txt')
num_test_transactions = len(test_transactions)
answer = MSapriori(test_transactions,test_docs_of_words,test_count_of_words,LS,beta,K,phi)
numbersToWords(answer, test_vocabulary, "test_word_mis_answer.txt")



'''
LS = 0.1
beta = 0.9
K = 6
phi  = 0.2
kos_transactions, kos_vocabulary, kos_docs_of_words, kos_count_of_words = readtransactions('docword.kos.txt','vocab.kos.txt')
num_kos_transactions = len(kos_transactions)
answer = MSapriori(kos_transactions,kos_docs_of_words,kos_count_of_words,LS,beta,K,phi)
numbersToWords(answer, kos_vocabulary, "kos_word_mis_answer.txt")
'''


'''
LS = 0.1
beta = 0.9
K = 6
phi  = 0.2
nips_transactions, nips_vocabulary, nips_docs_of_words, nips_count_of_words = readtransactions('docword.nips.txt','vocab.nips.txt')
num_nips_transactions = len(nips_transactions)
answer = MSapriori(nips_transactions,nips_docs_of_words,nips_count_of_words,LS,beta,K,phi)
numbersToWords(answer, nips_vocabulary, "nips_word_mis_answer.txt")
'''


'''
LS = 0.1
beta = 0.9
K = 6
phi  = 0.2
enron_transactions, enron_vocabulary, enron_docs_of_words, enron_count_of_words = readtransactions('docword.enron.txt','vocab.enron.txt')
num_enron_transactions = len(enron_transactions)
answer = MSapriori(enron_transactions,enron_docs_of_words,enron_count_of_words,LS,beta,K,phi)
numbersToWords(answer, enron_vocabulary, "enron_word_mis_answer.txt")
'''
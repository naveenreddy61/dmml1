from dmml1_functions import *

def numbersToWords(answer, vocabulary,outputfile):
    '''
    INPUT:  answer will be frequent itemsets of form list of lists
            ex-[[1,2,3],[(1,3),(2,4)],[(2,3,4)]]
            vocabulary is dict of form {1:'a',2:'the'}
            outputfile is string which is where the output will be stored
    OUTPUT: out file will be opened with name outputfile and each number will be converted,
            to corresponding word which is stored vocabulary dictionary
    '''
    out = open(outputfile,"w")
    for i in range(0,len(answer)):
        if i == 0:
            #itemsets of size 1 is treated as a special case
            F = []
            for element1 in answer[0]:
                F.append(vocabulary[element1])
            out.write(str(F)+'\n')
        else:
            # take each tuple, get the words associated with each number inside the tuple, 
            # check vocabulary and create a new list
            F= []
            for elementtuple in answer[i]:
                F.append(list((vocabulary[element] for element in elementtuple)))
            out.write(str(F)+'\n')
    out.close()
    return




MIN_SUP = 0.03
K = 4
transactions,vocabulary, docs_of_words = readtransactions('docword.test.txt','vocab.test.txt')
answer = apriori(MIN_SUP,K,transactions,vocabulary,docs_of_words)
numbersToWords(answer,vocabulary,"test_answer.txt")


'''
MIN_SUP = 0.1
K = 2
transactions,vocabulary, docs_of_words = readtransactions('docword.kos.txt','vocab.kos.txt')
answer = apriori(MIN_SUP,K,transactions,vocabulary,docs_of_words)
print(len(answer[0]),len(answer[1]))
numbersToWords(answer,vocabulary,"kos_words_answer.txt")
'''

'''
MIN_SUP = 0.5
K = 10
transactions,vocabulary, docs_of_words = readtransactions('docword.nips.txt','vocab.nips.txt')
answer = apriori(MIN_SUP,K,transactions,vocabulary,docs_of_words)
numbersToWords(answer,vocabulary,"nips_words_answer.txt")
'''


'''
MIN_SUP = 0.03
K = 10
transactions,vocabulary, docs_of_words = readtransactions('docword.enron.txt','vocab.enron.txt')
answer = apriori(MIN_SUP,K,transactions,vocabulary,docs_of_words)
numbersToWords(answer,vocabulary,"enron_words_10_015.txt")
'''
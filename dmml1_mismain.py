from dmml1_mis import *

LS = 0.08
beta = 0.8
K=5
'''
test_transactions,test_vocabulary, test_docs_of_words, test_count_of_words =readtransactions('docword.test.txt','vocab.test.txt')
num_test_transactions = len(test_transactions)
#print(MSapriori(test_transactions,test_docs_of_words,test_count_of_words,LS,beta,K))
#print(test_count_of_words)
#print(getMIS(test_docs_of_words,LS,beta,num_test_transactions))

kos_transactions, kos_vocabulary, kos_docs_of_words, kos_count_of_words = readtransactions('docword.kos.txt','vocab.kos.txt')
num_kos_transactions = len(kos_transactions)
#print(getMIS(kos_docs_of_words,LS,beta,num_kos_transactions))
outputfile = open("kos_mis_answer.txt","w")
for fk in MSapriori(kos_transactions,kos_docs_of_words,kos_count_of_words,LS,beta,K):
    outputfile.write(str(fk)+'\n')
outputfile.close()
'''
'''
LS = 0.08
beta = 0.8
K=5
enron_transactions, enron_vocabulary, enron_docs_of_words, enron_count_of_words = readtransactions('docword.enron.txt','vocab.enron.txt')
num_enron_transactions = len(enron_transactions)
#print(getMIS(kos_docs_of_words,LS,beta,num_kos_transactions))
outputfile = open("enron_mis_answer.txt","w")
for fk in MSapriori(enron_transactions,enron_docs_of_words,enron_count_of_words,LS,beta,K):
    outputfile.write(str(fk)+'\n')
outputfile.close()
'''
LS = 0.04
beta = 0.8
K=5
enron_transactions, enron_vocabulary, enron_docs_of_words, enron_count_of_words = readtransactions('docword.enron.txt','vocab.enron.txt')
num_enron_transactions = len(enron_transactions)
#print(getMIS(kos_docs_of_words,LS,beta,num_kos_transactions))
outputfile = open("enron_mis_answer.txt","w")
for fk in MSapriori(enron_transactions,enron_docs_of_words,enron_count_of_words,LS,beta,K):
    outputfile.write(str(fk)+'\n')
outputfile.close()

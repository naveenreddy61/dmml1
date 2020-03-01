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
        count_of_words = defaultdict(int)
        for line in f:
            transaction = list(map(int, line.split(' ')))
            transactions[transaction[0]].add(transaction[1])
            docs_of_words[transaction[1]].add(transaction[0])
            count_of_words[transaction[1]] += 1
    with open(vocab_filename) as g:
        vocabulary = defaultdict(set)
        line_counter = 1
        for line in g:
            vocabulary[line_counter].add(line.strip())
            line_counter += 1
    return (transactions, vocabulary, docs_of_words, count_of_words)


def getMIS(docs_of_words,LS,beta,num_transactions):
    MISofi  = []
    for word, doc_set in docs_of_words.items():
        Mi = (beta*len(doc_set))/num_transactions
        if Mi > LS:
            MISofi.append((Mi,word))
        else:
            MISofi.append((LS,word))
    MISofi.sort()
    return MISofi

def init_pass(M,count_of_words,num_transactions):
    '''
    M= [(0.1,3),(0.2,1),(0.4,5)]
    find 1st element which satisfies its MIS
    '''
    index = 0
    F = []
    for mis, element in M:
        if count_of_words[element] >= mis*num_transactions:
            found,found_mis = element,mis
            F.append((found_mis,found))
            break 
        else:
            index +=1
    for i in range(index+1,len(M)):
        if count_of_words[M[i][1]] >= found_mis*num_transactions:
            F.append(M[i])
    return(F)
assert(init_pass([(0.05,3),(0.06,4),(0.1,1),(0.2,2)],{3:6,4:3,1:9,2:25},100)==[(0.05, 3), (0.1, 1), (0.2, 2)])

def largeItemSetsOf1(F,count_of_words,num_transactions):
    L1 = []
    for mis, element in F:
        if count_of_words[element] >= mis*num_transactions:
            L1.append((mis,element))
    return L1
assert(largeItemSetsOf1([(0.05, 3), (0.1, 1), (0.2, 2)],{3:6,4:3,1:9,2:25},100)== [(0.05, 3), (0.2, 2)])

def level2_candidate_gen(F,count_of_words,num_transactions):
    C2 = []
    current_index = 0
    for (mis,element) in F:
        if count_of_words[element] >= mis*num_transactions:
            for i in range(current_index+1,len(F)):
                if count_of_words[F[i][1]] >= mis*num_transactions:
                    C2.append([(mis,element),F[i]])
            current_index +=1
        else:
            current_index += 1
    C2.sort()
    return C2
assert(level2_candidate_gen([(0.05, 3), (0.1, 1), (0.2, 2)],{3:6,4:3,1:9,2:25},100)==[[(0.05, 3), (0.1, 1)], [(0.05, 3), (0.2, 2)]])


def candidate_gen(Lprevious,k):
    # Lprevious will be list of lists
    # sub list will contain tuples of form(mis,element) 
    l = len(Lprevious)
    print("candidate for k = ", k, "l = ",l)
    candidates = []
    #F = sorted(list(F))
    for i in range(l):
        for  j in range(i+1,l):
            f1 = Lprevious[i]
            f2 = Lprevious[j]
            if f1[:-1] == f2[:-1]:
                c = f1 + [f2[-1]]
                candidates.append(c)
                for s in combinations(c, k-1):
                    if s[0][1] == c[0][1] or c[0][0] == c[1][0]:
                        if s not in Lprevious:
                            candidates[:-1]
                            break               
            else: 
                break    
    return candidates
#Lprevious = [[(0.1,1),(0.2,2),(0.3,3)],[(0.1,1),(0.2,2),(0.5,5)],[(0.1,1),(0.3,3),(0.4,4)],[(0.1,1),(0.3,3),(0.5,5)],[(0.1,1),(0.4,4),(0.5,5)],[(0.1,1),(0.4,4),(0.6,6)],[(0.2,2),(0.3,3),(0.5,5)]] 
#assert(candidate_gen(Lprevious,3)==[[(0.1, 1), (0.2, 2), (0.3, 3), (0.5, 5)], [(0.1, 1), (0.3, 3), (0.4, 4), (0.5, 5)], [(0.1, 1), (0.4, 4), (0.5, 5), (0.6, 6)]])

def MSapriori(transactions,docs_of_words,count_of_words,LS,beta,K):
    answer = []
    k = 1
    num_transactions = len(transactions)
    M = getMIS(docs_of_words,LS,beta,num_transactions)
    F = init_pass(M,count_of_words,num_transactions)
    L1 = largeItemSetsOf1(F,count_of_words,num_transactions)
    answer.append(L1)

    k = 2
    Lprevious = L1
    issubset = set.issubset
    while(k<=K and Lprevious != [] ):
        if k ==2:
            Ck = level2_candidate_gen(F,count_of_words,num_transactions)
        else:
            
            Ck = candidate_gen(Lprevious,k)
            # ck will be list of lists
        counts = defaultdict(int)
        for docId,docSet in transactions.items():
            for candidate in Ck:
                candidate_set = {element for mis,element in candidate}
                if issubset(candidate_set,docSet):
                    counts[tuple(candidate)] += 1
        Lk = []
        for candidate_tuple,count in counts.items():
            if count >= candidate_tuple[0][0]*num_transactions:
                candidate_list = [(mis,element) for (mis,element) in candidate_tuple]
                Lk.append(candidate_list)
        #print(k,'\n',Lk,'\n')
        answer.append(Lk)
        Lprevious = Lk
        k+=1
    return answer

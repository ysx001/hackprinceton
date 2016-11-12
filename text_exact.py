import proc_vision as pv
import proc_emotion as pe
import nltk

def text_extract(fd = r'C:\Users\Administrator\Desktop\2.jpg'):
    result_1 = pv.read_file(fd)
    result_2 = pe.read_file(fd)
    print result_2
    print result_1
    tags = result_1['description']['tags']
    emo = result_2[0]['scores'].keys()
    emo = emo[0:2]

    wsj = nltk.corpus.treebank.tagged_words(tagset='universal')
    word_tag_fd = nltk.FreqDist(wsj)
    word_list = word_tag_fd.most_common()
    verb_list = [wt[0] for (wt, _) in word_list if wt[1] == 'VERB']
    noun_list = [wt[0] for (wt, _) in word_list if wt[1] == 'NOUN']
    adj_list = [wt[0] for (wt, _) in word_list if wt[1] == 'ADJ']
    adv_list = [wt[0] for (wt, _) in word_list if wt[1] == 'ADV']
    
    verbs = '\n'.join([word for word in tags if (word in verb_list)])
    nouns = '\n'.join([word for word in tags if (word in noun_list)])
    adjs = '\n'.join([word for word in tags if (word in adj_list)] + emo)
    advs = '\n'.join([word for word in tags if (word in adv_list)])

    return verbs, nouns, adjs, advs

def main():
    print text_extract()

main()

##verbs, nouns, adjs, advs = text_extract()
##print(verbs)

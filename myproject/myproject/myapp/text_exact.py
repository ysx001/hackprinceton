import proc_vision as pv
import proc_emotion as pe
from nltk import FreqDist
from nltk import corpus
import random
import datetime

def text_extract(fd):
    try:
        result_1 = pv.read_file(fd)
        result_2 = pe.read_file(fd)
        tags = result_1['description']['tags']
        emo = []
        if len(result_2) > 0:
            emo = result_2[0]['scores'].keys()
            emo = emo[0:2]
        wsj = corpus.treebank.tagged_words(tagset='universal')
        word_tag_fd = FreqDist(wsj)
        word_list = word_tag_fd.most_common()
        verb_list = [wt[0] for (wt, _) in word_list if wt[1] == 'VERB']
        adv_list = [wt[0] for (wt, _) in word_list if wt[1] == 'ADV']
        adj_list = [wt[0] for (wt, _) in word_list if wt[1] == 'ADJ']
        noun_list = [wt[0] for (wt, _) in word_list if wt[1] == 'NOUN' and wt[0] not in adj_list and wt[0] not in verb_list]

        verbs = [word for word in tags if (word in verb_list)]
        nouns = [word for word in tags if (word in noun_list)]
        adjs = [word for word in tags if (word in adj_list)] + emo
        advs = [word for word in tags if (word in adv_list)]

        # Convert the poem
        random_count = 0
        n_sentences = 0
        nwords = [0] * 7

        sentences = [["The",5,1,6,3,"the",1],[5,1,6,3,5,"a",5,",",5,1],["is","a",5,1],[9,2,"!"],
                [1,4],[1,4,"like","a",5,1],[4,"like",5,1],["Why does the",1,4,"?"],[4,6,"like a",5,1],
                 [2,2,"and",2],["Where is the ",5,1],["All ",1,3,5,5,1],["Never",3, "a", 1]]

        noun = nouns
        abstrct_noun = ["adventure", "courage", "endurance", "desolation", "death","life", "love", "faith"]

        # abstrct_noun = ["action","work","noise","desolation","death","life","love","faith","anger","exhaustion"]
        trans_verb = verbs
        intrans_verb =["travel","sail","wave","grow","rise","fall","endure","die"]

        # intrans_verb = ["talk","gab","walk","run","stop","eat","grow","shrink","shop","work"]
        adj = adjs

        # adv = ["swiftly","calmly","quietly","roughly"]

        adv = ["swiftly","calmly","quietly","roughly"] + advs
        interjection = ["o","oh","ooh","ah","lord","god","damn"]
        t_list = [noun, abstrct_noun, trans_verb, intrans_verb, adj, adv, [], [], interjection]

        nline = random.randrange(2,6)
        poem = []
        for i in range(nline):
            a_sen = []
            prodduced_list = []
            a_sen = sentences[random.randrange(0,len(sentences))]
            for j in range(len(a_sen)):
                if type(a_sen[j]) is int:
                    a = t_list[a_sen[j]-1]
                    a_sen[j] = a[random.randrange(0,len(a))]
            poem.append(a_sen)

        # Join the poem
        p = []
        poem = ([' '.join(i) for i in poem])
        return poem
    except:
        poem = ["Failure, darkness, and darkness.\n","Hate, failure, and darkness.\n","Lord, hate!\n","Darkness, darkness, and hate.\n"]
        return poem

def count_all_lines():
    for i in range(len(nwords)):
        nwords[i] = len(t_list[i])

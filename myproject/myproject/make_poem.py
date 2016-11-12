import random
random_count = 0
n_sentences = 0
nwords = [0] * 7
# sentences = "The 5 1 6 3s the 1."
#     +"\n5, 5 1s 6 3 a 5, 5 1."
#     +"\n2 is a 5 1."
#     +"\n9, 2!"
#     +"\n1s 4!"
#     +"\nThe 1 4s like a 5 1."
#     +"\n1s 4 like 5 1s."
#     +"\nWhy does the 1 4?"
#     +"\n4 6 like a 5 1."
#     +"\n2, 2, and 2."
#     +"\nWhere is the 5 1?"
#     +"\nAll 1s 3 5, 5 1s."
#     +"\nNever 3 a 1."

sentences = [["The",5,1,6,3,"the",1],[5,1,6,3,5,"a",5,",",5,1],["is","a",5,1],[9,2,"!"],
            [1,4],[1,4,"like","a",5,1],[4,"like",5,1],["Why does the",1,4,"?"],[4,6,"like a",5,1],
             [2,2,"and",2],["Where is the ",5,1],["All ",1,3,5,5,1],["Never",3, "a", 1]]

noun = []
abstrct_noun = ["adventure", "courage", "endurance", "desolation", "death","life", "love", "faith"]
# abstrct_noun = ["action","work","noise","desolation","death","life","love","faith","anger","exhaustion"]
trans_verb = []
intrans_verb =["travel","sail","wave","grow","rise","fall","endure","die"]
#intrans_verb = ["talk","gab","walk","run","stop","eat","grow","shrink","shop","work"]
adj =[]
# adv = ["swiftly","calmly","quietly","roughly"]
adv = ["swiftly","calmly","quietly","roughly"]
interjection = ["o","oh","ooh","ah","lord","god","damn"]
t_list = [noun, abstrct_noun, trans_verb, intrans_verb, adj, adv, interjection]

def count_all_lines():
    for i in range(len(nwords)):
        nwords[i] = len(t_list[i])

def make_poem(a,b,c):
    t_list[0] = a
    t_list[2] = b
    t_list[4] = c
    nline = random.randrange(0,5)
    poem = []
    for i in range(nline):
        a_sen = []
        a_sen = sentences[random.randrange(0,len(sentences))]
        for j in range(len(a_sen)):
            if type(a_sen[j]) is int:
                a = t_list[a_sen[j]-1]
                a_sen[j] = a[random.randrange(0,len(a))]
        poem.append(a_sen)
    return poem

def main():
    print make_poem(["a"],["b"],["c"])

main()









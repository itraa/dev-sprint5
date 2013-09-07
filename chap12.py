# EX 12.4

def make_word_list(filename):
    word_list = list()
    fin = open(filename)
    for line in fin:
        word = line.strip().lower()
        word_list.append(word)
    return word_list

def anagrams(filename):
    word_list = make_word_list(filename)    
    d = dict()
    for word in word_list:
        t = list(word)
        t.sort()
        t = ''.join(t)
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d

#def print_anagrams(d):
#    for v in d.values():
#        if len(v) > 1:
#            print len(v), v


def print_desc_anagrams(d):
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v),v))
 
    t.sort(reverse=True)
    
    for x, y in t:
        print y

def get_n_letter_anagrams(d,n):

    s = {}
    for word, anagrams in d.iteritems():
        if len(word) == n:
            s[word] = anagrams    
    return s



d = anagrams('words.txt')
list_anagrams(d)
print_desc_anagrams(d)
n = 8
s = get_n_letter_anagrams(d,n)
print_desc_anagrams(s)
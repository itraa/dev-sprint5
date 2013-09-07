
import string
#it was a dark and stormy night

def process_file(filename,width=2):
    hist = dict()
    fp = open(filename)
    for line in fp:
        for word in line.split():
            process_line(line,width)

def move(prefix,word):
    return prefix[1:] + (word,)

def process_line(word,width=2):
    d = dict()
    prefix = tuple()

    if len(prefix) < width:
            prefix = prefix + (word,)
            return

    if d[prefix] not in d:
        d[prefix].append[word]
    else:        
        d[prefix] = [word]
    print d
    prefix = move(prefix,word)
            
 
process_file('phrase.txt')

# Not progressing well on this exercise, checked the solution but need to try and figure this out later!
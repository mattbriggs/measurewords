'''
    Graham Entity Extraction
    Matt Briggs V0.1 2018.07.20

    This is an entity extraction using bigrams and trigrams.
    Collocations are two or more words that tend to appear frequently together, 
    such as `United States`.This tacks a txt file (with a path) and returns a CSV of 
    bigrams/trigrams and their count in the text.

To use:
1. Save a clean text file as unicode text.
2. Update the variables: FILELOCATION, and OUTPUTLOCATION.
3. You can set the ratio variable in the main() routine. 30 will return 60 items. (2x30)
'''

import csv
from nltk.corpus import webtext
from nltk.corpus import stopwords
from nltk.collocations import BigramCollocationFinder
from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.metrics import TrigramAssocMeasures

# Values

FILELOCATION = r"c:\path\file.md"
OUTPUTLOCATION = r"C:\path\ngram.csv"

# Functions

def get_text_from_file(path):
    '''Return text from a text filename path'''
    textout = ""
    fh = open(path, "r", encoding="utf8")
    for line in fh:
        textout += line
    fh.close()
    return textout

def get_bigrams(filelocation, ratio):
    '''BigramCollocationFinder constructs two frequency distributions: one for each word, 
    and another for bigrams.'''
    words = [w.lower() for w in webtext.words(filelocation)]
    stopset = set(stopwords.words('english'))
    filter_stops = lambda w: len(w) < 3 or w in stopset
    bcf = BigramCollocationFinder.from_words(words)
    bcf.apply_word_filter(filter_stops)
    return bcf.nbest(BigramAssocMeasures.likelihood_ratio, ratio)


def get_trigrams(filelocation, ratio):
    '''In addition to BigramCollocationFinder, there's also TrigramCollocationFinder, which 
    finds triplets instead of pairs.'''
    words = [w.lower() for w in webtext.words(filelocation)]
    stopset = set(stopwords.words('english'))
    filter_stops = lambda w: len(w) < 3 or w in stopset
    tcf = TrigramCollocationFinder.from_words(words)
    tcf.apply_word_filter(filter_stops)
    tcf.apply_freq_filter(3)
    return tcf.nbest(TrigramAssocMeasures.likelihood_ratio, ratio)


def unpack_tuple_list(intuplelist):
    '''Take a tuple list and return a list of strings.'''
    outlist = []
    for i in intuplelist:
        roll = ""
        for j in i:
            roll += " " + j
            croll = roll.strip()
        outlist.append(croll)
    return outlist


def extract_grahams(filelocation, ratio):
    '''Utility function to reference the bigram and trigram routines. Returns a list.'''
    mine_bigrams = get_bigrams(filelocation, ratio)
    mine_trigrams = get_trigrams(filelocation, ratio)

    bi = unpack_tuple_list(mine_bigrams)
    tri = unpack_tuple_list(mine_trigrams)

    grahams = bi + tri

    return grahams


def get_counts(filelocation, inwordlist):
    '''With a list of strings, count the strings, and then return a list of lists.'''
    entity_count = []
    entity_count.append(["Entity", "Count"])
    inbody = get_text_from_file(filelocation)
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    for p in punctuation:
        body = inbody.replace(p,"")
    for w in inwordlist:
        c =  body.count(w)+1
        entity_count.append([w,c])
    return entity_count


def write_csv(outputlocation, inlist):
    csvout = open(outputlocation, 'w', newline="")
    csvwrite = csv.writer(csvout)
    for r in inlist:
        try:
            csvwrite.writerow(r)
        except Exception as e:
            print(e)
    csvout.close()


def main():
    '''With a text body in text, grab bigrams and trigrams, count their occurrence 
    in the text, and return a CSV.
     '''

    print("N-Grams mapping... ")
    entities = extract_grahams(FILELOCATION, 80)
    entity_count = get_counts(FILELOCATION, entities)
    write_csv(OUTPUTLOCATION, entity_count)
    print("Created an N-gram report to:." + OUTPUTLOCATION)

if __name__ == "__main__":
    main()
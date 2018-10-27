'''
    EntitySingle Module - Extract entities from a single file.
    Module returns noun and adjective clusters from a text.
    Matt Briggs
    v1.0 2018.08.21

    1. Update the FILELOCATION variable with the location of the txt or markdown file.
    2. Update the OUTPUTLOCATION variable with the location where you would like to save the report.
'''

import os
import csv
import datetime
import nltk


THISDATE = str(datetime.date.today())

FILELOCATION = r"c:\path\file.md"
OUTPUTLOCATION = r"C:\path\entityextraction_{}.csv".format(THISDATE)

def to_str(bytes_or_str):
    '''Converts files into UTF-8'''
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def get_textfromfile(path):
    '''Return text from a filename path'''
    textout = ""
    fh = open(path, "r", encoding="utf8")
    for line in fh:
        textout += line
    fh.close()
    textout = to_str(textout)
    return textout


def extract_chunks(sent):
    '''With a parsed sentence, return sets of entities.'''
    grammar = r"""
    NBAR:
        # Nouns and Adjectives, terminated with Nouns
        {<NN.*>*<NN.*>}

    NP:
        {<NBAR>}
        # Above, connected with in/of/etc...
        {<NBAR><IN><NBAR>}
    """
    chunker = nltk.RegexpParser(grammar)
    ne = set()
    chunk = chunker.parse(nltk.pos_tag(nltk.word_tokenize(sent)))
    for tree in chunk.subtrees(filter=lambda t: t.label() == 'NP'):
        ne.add(' '.join([child[0] for child in tree.leaves()]))
    return ne


def get_text_from_file(path):
    '''Return text from a text filename path'''
    textout = ""
    fh = open(path, "r", encoding="utf8")
    for line in fh:
        textout += line
    fh.close()
    return textout


def parse_sentences(incorpus):
    '''Take a body text and return sentences in a list.'''
    sentences = nltk.sent_tokenize(incorpus)
    return sentences


def extract_entities(inpath):
    '''Take a multisentence text and return a list of unique entities.'''
    corpus = get_text_from_file(inpath)
    breakdown = parse_sentences(corpus)
    entities = []
    for sent in breakdown:
        for i in extract_chunks(sent):
            entities.append(i)
    remove_dups = set(entities)
    entities = list(remove_dups)
    return entities



# The application

def main():
    print("Extracting entities...")
    records = []
    records.append(["Term", "Count", "Path", "Date"])

    # parse the file

    print("Getting file ... {}".format(FILELOCATION))
    
    corpus = get_textfromfile(FILELOCATION)
    record_terms = extract_entities(FILELOCATION)
    for term in record_terms:
        print(term)
        record = []
        record.append(term)
        record.append(corpus.count(term))
        record.append(FILELOCATION)
        record.append(THISDATE)
        records.append(record)

    # Generate CSV output

    csvout = open(OUTPUTLOCATION, 'w', newline="")
    csvwrite = csv.writer(csvout)
    for r in records:
        csvwrite.writerow(r)
    csvout.close()

    print("Created a report to: " + OUTPUTLOCATION)


if __name__ == "__main__":
    main()


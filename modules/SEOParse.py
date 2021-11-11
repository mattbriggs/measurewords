'''
    SEO Parser - Count Words
    Script will extract keywords and then score them for their possible SEO value.
    The script assumes a specific markdown schema used by docs.microsoft.com docs.
    Matt Briggs, 10.25.2018
    v.0.1

    1. Update the FILELOCATION variable with the location of the txt or markdown file.
    2. Update the OUTPUTLOCATION variable with the location where you would like to save the report.
'''

import os
import csv
import datetime
import nltk

THISDATE = str(datetime.date.today())

FILELOCATION = r"C:\Git\MS\azure-docs-pr\articles\azure-stack\azure-stack-monitor-health.md"
OUTPUTLOCATION = r"C:\data\measurewords\seoscore_{}.csv".format(THISDATE)


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


def make_SEO_dict(textcorpus, path):
    SEO_dict = {
        "title" : '',
        "heading1": '',
        "description" : "",
        "filename": "",
        "bodytitle" : "",
        "intro" : "",
        "imgtext": "",
        "imgfilename": ""
    }
    intostate = 0
    textlines = textcorpus.split("\n")
    SEO_dict["filename"] = os.path.basename(path).replace("-", " ")
    for l in textlines:
        if l.find("title:") > -1:
            SEO_dict['title'] = l[l.find("title:")+6:].strip()
        elif l.find("description:") > -1:
            SEO_dict['description'] = l[l.find("description:")+11:].strip()
        elif l.find("![") > -1:
             rawalttext = l[l.find("![")+3:l.find("]")].strip() + " "
             SEO_dict['imgtext'] += rawalttext
             imagepath = l[l.find("](")+2:l.find(")")].replace("-", " ").strip() + " "
             slashes = imagepath.split("/")
             rawfilenameext = slashes[len(slashes)-1]
             rawfilename = rawfilenameext[:rawfilenameext.find(".")] + " "
             SEO_dict['imgfilename'] += rawfilename
        elif l.find("# ") > -1:
             SEO_dict['heading1'] += l[l.find("# ")+1:].strip()
             intostate = 1
        elif intostate > 0:
            SEO_dict['intro'] += l
            intostate += 1
            if intostate > 2:
                intostate = 0
        elif l.find("## ") > -1:
            SEO_dict['bodytitle'] += l[l.find("## ")+2:].strip()
        elif l.find("### ") > -1:
            SEO_dict['bodytitle'] += l[l.find("### ")+3:].strip().strip()
    return SEO_dict


def score_SEO(SEO_dict, instring):
    score = 0

    if SEO_dict["title"].find(instring) > -1:
        score += 5
    if SEO_dict["heading1"].find(instring)  > -1:
        score += 5
    if SEO_dict["description"].find(instring) > -1: 
        score += 5
    if SEO_dict["filename"].find(instring)  > -1:
        score += 5
    if SEO_dict["bodytitle"].find(instring)  > -1:
        score += 3
    if SEO_dict["intro"].find(instring)  > -1:
        score += 3
    if SEO_dict["imgtext"].find(instring) > -1:
        score += 2
    if SEO_dict["imgfilename"].find(instring) > -1:
        score += 2

    return score


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


def main():
    print("Assessing SEO keywords.. ")
    SEO_keywords = []
    SEO_keywords.append(["Keyword", "Count", "SEO score"])
    bodytext =  get_textfromfile(FILELOCATION)
    seo_dict = make_SEO_dict(bodytext, FILELOCATION)

    corpus = get_textfromfile(FILELOCATION)
    record_terms = extract_entities(FILELOCATION)
    for term in record_terms:
        record = []
        record.append(term)
        record.append(corpus.count(term))
        record.append(score_SEO(seo_dict, term))
        SEO_keywords.append(record)

    # Generate CSV output

    csvout = open(OUTPUTLOCATION, 'w', newline="")
    csvwrite = csv.writer(csvout)
    for r in SEO_keywords:
        csvwrite.writerow(r)
    csvout.close()

    print("Saved report to: " + OUTPUTLOCATION)


if __name__ == "__main__":
    main()
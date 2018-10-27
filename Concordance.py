'''
    Concordance - Count Words
    Script to take a list of terms, and a text file, and then return a CSV with their
    counts.
    Matt Briggs, 8.3.2018
    v.0.1

    1. Update the TEXTBODY variable with the location of the txt or markdown file.
    2. Update the OUTPUTLOCATION variable with the location where you would like to save the report.
'''

import csv
import datetime

THISDATE = str(datetime.date.today())

TEXTBODY = r"c:\path\file.md"
OUTPUTLOCATION = r"C:\path\wordcounts_{}.csv".format(THISDATE)


def get_text_from_file(path):
    '''Return text from a text filename path'''
    textout = ""
    fh = open(path, "r", encoding="utf8")
    for line in fh:
        textout += line
    fh.close()
    return textout


def get_list_of_words(inwordlist):
    '''Return a list of only words.'''
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    newlist = []
    for w in inwordlist:
        for p in punctuation:
            w = w.replace(p,"")
        newlist.append(w)
    return newlist


def get_counts(corpus, wordlist):
    '''Take a path to a text file, and a path to a filelist, and then returns
     a list of counts: term and count.'''
    wordcount = []
    wordcount.append(["Term", "Count"])
    for w in wordlist:
        c = corpus.count(w)
        wordcount.append([w, c])
    return wordcount


def write_csv(outputlocation, inlist):
    '''Write the CSV file as output.'''
    csvout = open(outputlocation, 'w', newline="")
    csvwrite = csv.writer(csvout)
    for r in inlist:
        try:
            csvwrite.writerow(r)
        except Exception as e:
            print(e)
    csvout.close()


def main():
    print("Creating word count... ")
    fulltext =  get_text_from_file(TEXTBODY)
    fulltext = fulltext.replace("\n", " ")
    rawwordlist = fulltext.split(" ")
    wordlist = get_list_of_words(rawwordlist)
    uniquelist = set(wordlist)
    wordbody = " ".join(wordlist)
    wordcounts = get_counts(wordbody, uniquelist)
    write_csv(OUTPUTLOCATION, wordcounts)
    print("Created word count: " + OUTPUTLOCATION)


if __name__ == "__main__":
    main()
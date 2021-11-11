'''
    Part of Speech Extract
    Module returns the ratio of the parts-of-speech based on the Penn Treebank Project.
    Matt Briggs
    v1.0 2018.08.21

    1. Update the TEXTBODY variable with the location of the txt or markdown file.
    2. Update the OUTPUTLOCATION variable with the location where you would like to save the report.
'''

import os
import csv
import datetime
import nltk


THISDATE = str(datetime.date.today())

FILELOCATION = r"c:\path\file.md"
OUTPUTLOCATION = r"C:\path\partofspeech_{}.csv".format(THISDATE)

'''Alphabetical list of part-of-speech tags used in the Penn Treebank Project.'''

PENN_TOKENS = {
 "WRB": "Wh-adverb",
 "WP$": "Possessive wh-pronoun",
 "WDT": "Wh-determiner",
 "VBZ": "Verb, 3rd person singular present",
 "VBP": "Verb, non-3rd person singular present",
 "VBN": "Verb, past participle",
 "VBG": "Verb, gerund or present participle",
 "VBD": "Verb, past tense",
 "SYM": "Symbol",
 "RBS": "Adverb, superlative",
 "RBR": "Adverb, comparative",
 "PRP": "Personal pronoun",
 "POS": "Possessive ending",
 "PDT": "Predeterminer",
 "NNS": "Noun, plural",
 "NNP": "Proper noun, singular",
 "JJS": "Adjective, superlative",
 "JJR": "Adjective, comparative",
 "WP": "Wh-pronoun",
 "VB": "Verb, base form",
 "UH": "Interjection",
 "TO": "to",
 "RP": "Particle",
 "RB": "Adverb",
 "NN": "Noun, singular or mass",
 "MD": "Modal",
 "LS": "List item marker",
 "JJ": "Adjective",
 "IN": "Preposition or subordinating conjunction",
 "FW": "Foreign word",
 "EX": "Existential there",
 "DT": "Determiner",
 "CD": "Cardinal number",
 "CC": "Coordinating conjunction",
 "PRP$": "Possessive pronoun",
 "NNPS": "Proper noun, plural"

}


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


def parse_sentences(incorpus):
    '''Take a body text and return sentences in a list.'''
    sentences = nltk.sent_tokenize(incorpus)
    return sentences


def parse_words(insentence):
    '''Take a sentence and return tokens in the sentence.'''
    tokens = nltk.word_tokenize(insentence)
    tagged = nltk.pos_tag(tokens)
    return tagged


def make_model(incorpus):
    '''Take a text body and return a parsed model that contains a
    list of lists. Each sublist is a set of tuples that identify 
    the word and part-of-speech.'''
    my_body = parse_sentences(incorpus)
    model = []
    for sentence in my_body:
        my_tokens = parse_words(sentence)
        for t in my_tokens:
            model.append(t)
    return model


# The application

def main():
    '''Opens the file and then parses the sentences for part of speech 
    tokens, tallys them and creates the report.'''

    print("Starting...")
    tally = []
    tally.append(["Part-of-speech", "Ratio"])

    # parse the file

    print("Getting file ... {}".format(FILELOCATION))
    
    corpus = get_textfromfile(FILELOCATION)
    parsed_sentences = make_model(corpus)
    part_of_speech = {}
    for token in parsed_sentences:
        if token[1] in part_of_speech.keys():
            part_of_speech[token[1]] += 1
        else:
            part_of_speech[token[1]] = 1
    totalcount = sum(part_of_speech.values())
    for i in part_of_speech.keys():
        if i in PENN_TOKENS.keys():
            ratio = part_of_speech[i]/totalcount
            tally.append([PENN_TOKENS[i], "{:.2%}".format(ratio)])

    # Generate CSV output

    csvout = open(OUTPUTLOCATION, 'w', newline="")
    csvwrite = csv.writer(csvout)
    for r in tally:
        csvwrite.writerow(r)
    csvout.close()

    print("Creating your report at: " + OUTPUTLOCATION)


if __name__ == "__main__":
    main()

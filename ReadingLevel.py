'''
    Reading Level Report
    Script to measure the reading level of your text.
    Matt Briggs, 10/25/2018
    v.0.1

    1. Update the FILELOCATION variable with the location of the txt or markdown file.

Note: The script here is adapted from Python 2 code found in this blog post:
https://coolpythoncodes.com/flesch-index-python-script/ and repo https://github.com/Classicdude1/ReaderAbilityChecker

'''

import os

FILELOCATION = r"c:\path\file.md"

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


def main():
    '''This is the logic of the application.'''

    text=get_textfromfile(FILELOCATION)

    sentence=text.count(".") + text.count('!') + text.count(";") + text.count(":") + text.count("?")

    words=len(text.split())
    syllable=0

    for word in text.split():
        for vowel in ['a','e','i','o','u']:
            syllable += word.count(vowel)
        for ending in ['es','ed','e']:
            if word.endswith(ending):
                syllable -= 1
        if word.endswith('le'):
                syllable += 1

    G=round((0.39*words)/sentence+ (11.8*syllable)/words-15.59)

    if G >= 0 and G <=30:
        print('Score: {} The Readability level is College'.format(G))
    elif  G >= 50 and G <=60:
        print('Score: {} The Readability level is High School'.format(G))
    elif  G >= 90 and G <=100:
        print('Score: {} The Readability level is fourth grade'.format(G))
                
    print('This text has %d words' %(words))

if __name__ == "__main__":
    main()
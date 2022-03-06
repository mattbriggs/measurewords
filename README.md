# Measure your words

Matt Briggs  
https://github.com/mattbriggs

You can gain valuable insight into your writing by measuring your words. The measurement of your writing can be part of your writing practice, and sets the basis for creating tests when validating hypothesis about your writing.

## On a writing practice

The term *writing practice* comes from the writing process movement. A good introduction to the ideas of writing process is Peter Elbow's classic book, *[Writing Without Teachers](https://en.wikipedia.org/wiki/Peter_Elbow#Writing_Without_Teachers)*. 

A practice is the act of rehearsing a tacit skill or engaging in an activity again and again for the purpose of improving or mastering the skill. You have heard the phrase "practice makes perfect," or the term *practitioner*, a person actively engaged in an art, discipline, or profession. A practicing musicians runs scales. A practicing swimmer swims laps. A practicing writer writes words.

While a practitioner can eventually achieve mastery of their discipline, they are also concerned with continued growth and maintenance of their skills. The mindset of the practitioner is often the same as any ardent student. The continued growth of skills for a practitioner depends on a number of things such as frequency of practice, sources of new technique and ideas, and feedback to the products of their practice.

Jerry Seinfeld in [a recent interview](https://www.nytimes.com/2018/10/26/arts/television/jerry-seinfeld-interview.html) answered this question: "Do you think comedians learned the wrong lessons in that earlier era, and came away believing they could do whatever they wanted?"

"You can't do whatever you want. You can only do what works — if you want to have a career. What I do onstage is what the past 300 audiences decided worked. That's good, that's not good. You have to make the audience laugh a certain amount or they don't come back. That's why I wear a suit. It's a signal: I'm not loafing here. I'm about this."

As a process, a writing practice is a loop that includes generating work, presenting work, and then listening to an audience, and doing something with that response to go back to the beginning and produce more work.

With a writing practice, a writer writes regularly, but also seeks feedback on their product of her writing. A writer may need an editor, a first reader, an audience. A writer can also incorporate mechanical feedback mechanisms into their writing such as word count, ways of assessing how they use words by looking at word and term frequency, part of speech frequency, and the reading level of their work.

## Scripts to measure words

This repo contains Python scripts that you can run on text files to generate reports about your writing. These scripts are works in progress, and your feedback is welcome in helping improve both the code quality but also the usefulness of the algorithms.

This repo contains the following scripts in the `modules` folder:

- [Concordance](#concordance) (word count)
- [N-Gram](#n-gram) (word pair count)
- [Entity extraction](#entity-extraction) (keyword count)
- [Search engine keyword analysis](#search-engine-keyword-analysis) (scores keywords)
- [Parts-of-Speech](#parts-of-speech) (part-of-speech frequency)
- [Reading level](#reading-level) (reading grade level)

## SEO on-page score

The Search Engine keyword analysis has been adapted to a command line tool using the Python `CMD` module.

After you follow the steps in [Get started with the scripts](#get-started-with-the-scripts), you can use the SEO tool.

From the root directory for the repo, type:

```
python -m ./seoonpage/seoonpagecli.py
```

When the script loads, type:

```
keywords <full-path-to-your-markdownfile.md>
```

The script will return a table in the terminal ranking the keywords by prominence. For example:

```
Keyword scores for + <full-path-to-your-markdownfile.md>
+------+------------------+
| Rank | Keyword          |
+------+------------------+
|  1   | Azure Stack      |
|  2   | Topic test       |
|  3   | freight train    |
|  4   | Hanley Turner    |
|  5   | Kentucky boys    |
|  6   | racing season    |
|  7   | livery barn      |
|  8   | home town        |
|  9   | Churchhill Downs |
|  10  | sweet potatoes   |
+------+------------------+
```


## Modules

The following list explains each module.
### Concordance

**Script**: `Concordance.py `  
**Measure**:    word frequency  
**What it does**:   Extracts a list and count of words in your text.  
**How you can use it**:  Update the script with a text input file and the location of the output report. Open the resulting CSV file in a spreadsheet app and you can sort the resulting column from most common (highest count) to less common (lowest count).

The script orders and counts isolated strings (that is in this context **words**).

### N-gram

**Script**: `Ngram.py`  
**Measure**:   word pair frequency  
**What it does**:  Extracts frequent the most frequency word pairings from your document.  
**How you can use it**: Update the script with a text input file and the location of the output report. Open the resulting CSV file in a spreadsheet app and you can sort the resulting column from most common (highest count) to less common (lowest count).

"In the fields of computational linguistics and probability, an n-gram is a contiguous sequence of n items from a given sequence of text or speech. The items can be phonemes, syllables, letters, words or base pairs according to the application. The n-grams typically are collected from a text or speech corpus."
For more about N-grams, see [N-gram](https://en.wikipedia.org/wiki/N-gram).

This script collects frequent word pairs.

### Entity extraction

**Script**: `Entityextraction.py`  
**Measure**:   keyword frequency  
**What it does**:  Extracts a list of noun clusters from your text and counts their frequency.  
**How you can use it**:  Update the script with a text input file and the location of the output report. Open the resulting CSV file in a spreadsheet app and you can sort the resulting column from most common (highest count) to less common (lowest count).

The script uses the [Natural Language Toolkit](http://www.nltk.org/) to parse words and then tokenize them into parts-of-speech. It pulls any noun or adjective noun single word or cluster and then counts their frequency in the text.

### Search engine keyword analysis

**Script**: `SEOParse.py`  
**Measure**:    word frequency (scored for search engine optimization)  
**What it does**:  The script extracts a list of keywords and scores them using an approximation of an SEO algorithm.  
**How you can use it**:   Update the script with a text input file and the location of the output report. Open the resulting CSV file in a spreadsheet app and you can sort the resulting column from highest SEO score to the lowest SEO score.  

The script assumes that documents are written in markdown and follow the schema in `docs.microsoft.com` docs. This schema is loosely the following:

``` filename: the-name-of-the-file.md
    title: metadata of the document
    description: metadata description of the document.

    # H1 title

    Intro 1 paragraph

    Intro 2 paragraph

    ## H2 title

    Paragraph text.

    ![alt](the-name-of-image.png)

    ### H3 title

    Paragraph text.

    ### H3 title

    Paragraph text.

    ## H2 Title

    Last paragraph text. 
```

### Parts-of-Speech

**Script**: `PartsofSpeech.py`  
**Measure**:   parts-of-speech frequency  
**What it does**:  Measures the percentage of the parts of speech in your document.  
**How you can use it**:  Update the script with a text input file and the location of the output report. Open the resulting CSV file in a spreadsheet app. You can review each the ratio of each part of speech in your document.

The script uses the [Natural Language Toolkit](http://www.nltk.org/) to parse words and then tokenize them into parts-of-speech. In turn, the toolkist, prases sentences based on the Penn Treebank Project.

"The Penn Discourse Treebank (PDTB) is a large scale corpus annotated with information related to discourse structure and discourse semantics. While there are many aspects of discourse that are crucial to a complete understanding of natural language, the PDTB focuses on encoding discourse relations."  
You can find more information at [The Penn Discourse Treebank Project](https://www.seas.upenn.edu/~pdtb/):


### Reading Level

**Script**: `ReadingLevel.py`  
**Measure**:   Reading level  
**What it does**:  Measures the complexity of your document and scores it using a common reading level measure (Flesch Index).  
**How you can use it**:  Update the script with a text input file. The report will display in the console.

Flesch Reading Ease Formula is considered as one of the oldest and most accurate readability formulas. Rudolph Flesch, an author, writing consultant, and a supporter of the Plain English Movement, developed this formula in 1948.  You can find more information about the formula, at: http://www.readabilityformulas.com/flesch-reading-ease-readability-formula.php

Note: The script here is adapted from Python 2 code found in this blog post:
https://coolpythoncodes.com/flesch-index-python-script/

## Get started with the scripts

To run the scripts you will need to install a few of the prerequistes.

1. Install [Python 3.9](https://www.python.org/downloads/)
2. Install the dependent Python modules. From the root of the repository, type:
    ```
    pip install -r requirements.txt
    ```
3. Install the training models for the [Natural Language Toolkit (NLTK)](http://www.nltk.org). Run the following Python module from the root of the repository:
    ```
    python -m ./firstrun.py
    ```

## Providing feedback

Please file any feedback or issues as a [GitHub issue](https://github.com/mattbriggs/measurewords/issues) in the repository.

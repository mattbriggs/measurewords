'''Test for On Page SEO counter.'''

import os
import sys
stem = str(os.getcwd())
workingdir = stem + "\\seoonpage"
sys.path.insert(0,workingdir)
import seoonpage as SEO
import stoplist as SP

testtext = SEO.get_text_from_file("./seoonpage/testdata/dummy-text.md")

def test_get_top_ten():
    '''Function get_top_ten.'''
    test_dict = SEO.get_top_ten("./seoonpage/testdata/dummy-text.md")
    print(test_dict)
    topkey = test_dict[1]['keyword']

    assert topkey == "Azure Stack"

def test_get_text_from_file():
    pass

def test_print_dict_rank():
    pass

def test_make_SEO_dict():
    pass

def test_score_SEO():
    pass

def test_extract_chunks():
    pass

def test_parse_sentences():
    pass

def test_only_word_pairs():
    pass

def test_remove_blank():
    pass

def test_apply_stoplist():
    pass

def test_clean_keyword():
    pass

def test_extract_entities():
    pass

def test_get_top_ten():
    pass

def test_devrel_function():
    pass
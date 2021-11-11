''' On Page SEO counter

    This script will parse a markdown repository using an approximation
    of the GoogleBot keyword assessment. It will extract noun entities 
    with more than one word from each markdown topic, score each entity,
    and export the CSV.

    Input: config file (path to repo folder).
    Output: path to raw data report folder.

    Matt Briggs V0.1: 11.9.2021
'''

import json

import os
import sys
stem = str(os.getcwd())
workingdir = stem + "seoonpage"
sys.path.insert(0,workingdir)
import seoonpage as SEO
import devrelutilities as DR

ONPAGE_TABLE = [["page", "period", "on_page_rank", "keyword" ]]


def add_pageranks_table(indict):
    '''Insert the logic to process the return from the function.'''

    global ONPAGE_TABLE

    for k in indict.keys():
        record = []
        record.append(indict[k]["page"])
        record.append(DR.THISDATE)
        record.append(indict[k]["score rank"])
        record.append(indict[k]["keyword"])
        ONPAGE_TABLE.append(record)


def main():
    '''Make sure the config is updated. And run the script.
    '''

    config_file = open("config.json")
    config_str = config_file.read()
    config = json.loads(config_str)
    path_in = config["repoinput"]
    path_out = config["reportoutput"]
    filelist = DR.get_files(path_in)
    for f in filelist:
        try:
            print("Processing: {}".format(f))
            SEO_out = SEO.get_top_ten(f)
            add_pageranks_table(SEO_out)
        except Exception as e:
            print("A problem with: {} : {}".format(f, e))
    reportname = path_out + "onpage.csv"
    DR.write_csv(ONPAGE_TABLE,reportname)
    print("Completed processing.")


if __name__ == "__main__":
    main()

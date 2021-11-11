''' On Page SEO counter

    This script will parse a markdown repository using an approximation
    of the GoogleBot keyword assessment. It will extract noun entities 
    with more than one word from each markdown topic, score each entity,
    and export the CSV.

    Input: keywords <path to your markdown file>
    Output: top ten keywords in order of prevalence.

    Matt Briggs V0.0: X.X.2019
'''

import cmd
import os
import sys
stem = str(os.getcwd())
workingdir = stem + "\\seoonpage"
sys.path.insert(0,workingdir)
import seoonpage as SEO

APPVERSION = "Search Engine Optimization (SEO) On page keywords - Version 0.0.1.20190420\n"


class TagTerminal(cmd.Cmd):
    """Accepts commands via the normal interactive prompt or on the command line."""

    prompt = "> "

    def do_keywords(self, line):
        '''The main logic of the utility.'''

        try:
            SEO_out = SEO.get_top_ten(line)
            SEO.print_dict_rank(SEO_out)
            return
        except Exception as e:
            print ("There was some trouble.\nError code: {}".format(e))
            return

    def do_help(self, line):
        '''Type help to get help for the application.'''
        help_text = '''\nHelp for SEO On Page

Type `keywords` <filepath> such as:

keywords c:\git\yourrepo\markdownfile.md

        '''
        print(help_text)

    def do_quit(self, line):
        '''Type quit to exit the application.'''
        return True

    def do_exit(self, line):
        '''Type exit to exit the application.'''
        return True

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    TagTerminal().cmdloop(APPVERSION)
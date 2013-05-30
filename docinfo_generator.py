#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This module generated the docinfo xml file from a text file formatted using asciidoc format.

NOTE: This module is normally compatible python 2.6.6 (and later) and python3.

IMPORTANT: None of the following blocks are mandatory.

Revision history rules for an optimal docinfo generation (revinfo tag)
----------------------------------------------------------------------

To extract the revision history data, put it in a comment block (more than 3 "/").

Begin the block with one line only containing ":revinfo:"
Then for each revision history item is like this:
  -> a block begins with a "v" followed by the version number (only digits separated by a ".")
  -> followed by a ","
  -> followed optionally by the author's initials or name followed by a ","
  -> followed by the date of the modification
  -> followed by a ":"
  -> Then a bunch of lines for the comments over the remark

*Do NOT put a blank line between the blocks.*

The revision history ends with either:
 -> a blank line
 -> a comment line (a line beginning by more than 3 "/")
 -> a new block header (a line beginning by a ":something:"

Copyright rules for optimal docinfo generation (copyright tag)
--------------------------------------------------------------

To avoid any conflict with the asciidoc format, put the copyright in a comment block.

Begin the block with a line beginning with the ":copyright:" tag.
Then write the date followed by comma (",") and the company or author's name.
You can use multiple lines for this block, but the best practice is to put all in one line.


Legal notice rules for optimal docinfo generation (legalnotice tag)
-------------------------------------------------------------------

To avoid any conflict with the asciidoc format, put the legalnotice block in a comment block.

Begin the block with a line beginning with the ":legalnotice:" tag.
Then write each paragraph that you want beginning them by a dot (".") as the very first character of the line.
You can use multiple lines for each paragraph, but each new paragraph must begin with a dot.
Don't separate paragraph by a blank line!

Example of correctly interpreted block:
---------------------------------------

//////
:copyright:2013,Joseph HERLANT
:revinfo:
v1.2, Joseph HERLANT, 2013-02-22:
 These are my notes for 1.2 revision
 And a bunch of other informations
v1.1, 2013-01-03:
 this is a test for v1.1
 You will notice that there is no author here...
v1.0.1, Jojo, 2013-01-01: All in one line sample. All comment is on one line!
v1.0, JHE, 2013-01-02:
 Creation
 2nd line of modification remark...
:legalnotice:
.This is the first paragraph
of the legal notice.
. This is the second one!
. The next one
least but not last! :)
//////


After running this script to generate the XML file, generate
the HTML document using: 
`a2x -a docinfo -fxhtml test_asciidoc.txt`
Or the PDF document using:
`a2x -a docinfo -fxhtml test_asciidoc.txt`
'''

import re;
from os import path;

__author__     = "Joseph HERLANT"
__copyright__  = "Copyright 2013, Joseph HERLANT"
__credits__    = ["Joseph HERLANT"]
__license__    = "GPL"
__version__    = "0.4.0"
__maintainer__ = "Joseph HERLANT"
__email__      = "herlantj@gmail.com"
__status__     = "Development"


class docinfoitem(object):
    ''' This is an abstract class from what each class used to generate xml groups will inherit.
    '''
    def __init__(self):
        ''' As it is an abstract class, it cannot be implemented directly. '''
        raise AbstractClassError;
    
    def gen_xml_from_self(self, line_indent = '', ordered_list = []):
        ''' Generates the xml structure from the current object using the following method:
            - The top-level object xml tag will have the name of the class
            - Each sub objects xml tag will have the name of a member and its value

        WARNING: This will work only on non complex objects (only str, list of str, or numeric members)
        
        Input parameter:
           - line_indent is either one or more tab, whitespace or alike
           - ordered_list is the list of the elements you want to print in the order you want to.
               This is used in order to validated DTD that are sensitive to the xml tags order
               and for filtering.
        Returns:
            - An xml-formatted string
        '''
        # Cleaning up given indentation
        if not re.match('^\s*$', line_indent):
            line_indent = "";

        # Initializing given list if not already done
        if ordered_list == []:
##            print(self.__dict__);
            ordered_list = self.__dict__.keys()
            
        _result = "";
        _result += "\n"+ line_indent +"<"+ self.__class__.__name__ +">";
        for k in ordered_list:
            # For each member of the class, transform it to an xml tag if exists as a member of the class
            if k in self.__dict__.keys():
                if(type( self.__dict__[k] ) == list):
                   for list_item in self.__dict__[k]:
                       _result += "\n"+ line_indent +"\t<"+ k +"><![CDATA["+ list_item +"]]></"+ k +">";
                else:
                    _result += "\n"+ line_indent +"\t<"+ k +"><![CDATA["+ self.__dict__[k] +"]]></"+ k +">";
            else:
                print("WARNING: The given key named \""+ k + "\" does not exists as a member of the class.");
        _result += "\n"+ line_indent +"</"+ self.__class__.__name__ +">";
        return _result;
    
## TODO: implement this class
class legalnotice(docinfoitem):
    ''' Subclass containing legal notice data for the legalnotice tag.
    Inherits from docinfoitem abstract class.
    '''
    def __init__(self):
        ''' Class constructor... Initializing inner variables
        Input parameter: Nothing
        Returns: Nothing
        '''
        # Each item of a simpara is a paragraph in the end
        self.simpara = [];


class copyright(docinfoitem):
    ''' Subclass containing copyright data for the copyright tag.
    Inherits from docinfoitem abstract class.
    '''
    def __init__(self):
        ''' Class constructor... Initializing inner variables
        Input parameter: Nothing
        Returns: Nothing
        '''
        self.year = "1970";
        self.holder = "";


## TODO: Add author and editor classes...
##class author(docinfoitem):
##    ''' Subclass containing copyright data for the copyright tag.
##    Inherits from docinfoitem abstract class.
##    '''
##    def __init__(self):
##        ''' Class constructor... Initializing inner variables
##        Input parameter: Nothing
##        Returns: Nothing
##        '''
##        self.honorific = "";
##        self.firstname = "";
##        self.surname = "";
##        self.othername = {'role':'test'};
##        self.affiliation = affiliation();
##    class affiliation(docinfoitem):
##        ''' Subclass containing copyright data for the copyright tag.
##        Inherits from docinfoitem abstract class.
##        '''
##        def __init__(self):
##            ''' Class constructor... Initializing inner variables
##            Input parameter: Nothing
##            Returns: Nothing
##            '''
##            self.shortaffil = "";
##            self.jobtitle = "";
##            self.orgname = "";
##            self.orgdiv = "";

class revision(docinfoitem):
    ''' Subclass containing revision data for the revhistory tag.
    Inherits from docinfoitem abstract class.
    '''
    def __init__(self):
        ''' Class constructor... Initializing inner variables
        Input parameter: Nothing
        Returns: Nothing
        '''
        self.revnumber = "0";
        self.date = "0000-00-00";
        self.authorinitials = "";
        self.revremark = "";


    
class docinfo:
    ''' A class that will handle docinfo data '''
    def __init__(self):
        ''' Class constructor... Initializing inner variables
        Input parameter: Nothing
        Returns: Nothing
        '''
        self.authorgroup = [];  ## TODO: implement authorgroup tag
        self.copyright = copyright();
        self.legalnotice = legalnotice();
        self.revhistory = [];


    def gen_docinfo_filename(self, text_file_name):
        ''' Generates the output xml file for the docinfo module
        based on the file name
        Input parameter:
            text_file_name: name of the file to use as a base
        Returns:
            The name of the xml file to use with the docinfo norms
        '''
        return path.splitext(text_file_name)[0] + '-docinfo.xml';


    def get_revinfo_block(self, filecontent):
        ''' Extracts the revinfo block from the content of the text
        Input parameter:
            filecontent: Content of the text file in a string
        Returns: Nothing
        '''

        # This is how to find the beginning of the block
        strpattern_start_tag = '.*^:revinfo:\s*\n';
        # This is how to find the revinfo items as one piece
        str_pattern_block_content = '(^[v][0-9\.]+[,][^:]+:[^\n]*(?:\n[^:][^\n]+)*?)+' ;
        # This is the end of the block (means a line begining by /// or :something: or one blank line)
        str_pattern_end_of_block = '\n(?:\:\w+\:|/{3,}|\s*\n)';
        # These 3 blocks form a global pattern
        str_pattern_global = strpattern_start_tag + str_pattern_block_content + str_pattern_end_of_block;
        revinfo = re.compile(str_pattern_global, flags=re.MULTILINE|re.UNICODE|re.IGNORECASE|re.DOTALL);
        if revinfo.match(filecontent, re.MULTILINE) is None:
            print("No revInfo tag found");
        else:
            # If pattern matches, process data
            revinfo_data = revinfo.search(filecontent).groups(0)[0];
            self.get_revision_items(revinfo_data);


    def get_revision_items(self,revinfo_block):
        ''' Extracts each revision history item from a revinfo block
        and populate the revhistory self table with the items found
        Input parameter:
            revinfo_block: A revision history block extracted from a file content
        Returns: nothing
        '''

        # First part retrieves the revision items in an array of hashtables
        str_pattern_rev = "^v(?P<revision>[0-9\.]*)[,](?P<modifier>[^,]+[,])?(?P<daterev>[^\:]*)[:](?P<remarks>.*).*";
        rev = re.compile(str_pattern_rev, flags=re.UNICODE|re.IGNORECASE)
        global_rem=[];
        current_rem={};
        for item in revinfo_block.split('\n'):
            if rev.match(item) is None:
##                print("This is a remark line...");
                current_rem['remarks'] += item + "\n";
            else:
                if 'revision' in current_rem.keys():
                    global_rem.append(current_rem);
                current_rem = rev.search(item).groupdict();
        global_rem.append(current_rem);

        # Second part transforms the array of hashtables in an array of revision objects
        for remitem in global_rem:
            cur_rev = revision();
            cur_rev.revnumber = remitem['revision'].strip();
            cur_rev.date = remitem['daterev'].strip();
            if remitem['modifier'] is None:
                cur_rev.authorinitials = "";
            else:
                cur_rev.authorinitials = remitem['modifier'].strip().strip(',');
            cur_rev.revremark = remitem['remarks'].strip();
##            print cur_rev.gen_xml_from_self('\t');
            self.revhistory.append(cur_rev);
##        print global_rem;


    def get_copyright_content(self, filecontent):
        ''' Extracts the copyright block from the content of the text
        Input parameter:
            filecontent: Content of the text file in a string
        Returns: Nothing
        '''
        # This is how to find the beginning of the block
        strpattern_start_tag = '.*^:copyright:\s*\n*';
        # This is how to find the data as one piece
        str_pattern_block_content = '(?P<date>[^,]*)[,](?P<holder>.*?)' ;
        # This is the end of the block (means a line begining by /// or :something: or one blank line)
        str_pattern_end_of_block = '\n(?:\:\w+\:|/{3,}|\s*\n)';
        # These 3 blocks form a global pattern
        str_pattern_global = strpattern_start_tag + str_pattern_block_content + str_pattern_end_of_block;
        regexinfo = re.compile(str_pattern_global, flags=re.MULTILINE|re.UNICODE|re.IGNORECASE|re.DOTALL);
        if regexinfo.match(filecontent, re.MULTILINE) is None:
            print("No copyright tag found");
        else:
            # If pattern matches, process data
##            print(regexinfo.search(filecontent).groupdict());
            tmp_dict = regexinfo.search(filecontent).groupdict();
            self.copyright.year = tmp_dict['date'].strip();
            self.copyright.holder = tmp_dict['holder'].strip();
            del(tmp_dict);

    def get_legalnotice_content(self, filecontent):
        ''' Extracts the legal notice block from the content of the text
        Input parameter:
            filecontent: Content of the text file in a string
        Returns: Nothing
        '''
        # This is how to find the beginning of the block
        strpattern_start_tag = '.*^:legalnotice:\s*\n*';
        # This is how to find the data as one piece
        str_pattern_block_content = '(?P<simparas>^\..*?)' ;
        # This is the end of the block (means a line begining by /// or :something: or one blank line)
        str_pattern_end_of_block = '\n(?:\:\w+\:|/{3,}|\s*\n)';
        # These 3 blocks form a global pattern
        str_pattern_global = strpattern_start_tag + str_pattern_block_content + str_pattern_end_of_block;
        regexinfo = re.compile(str_pattern_global, flags=re.MULTILINE|re.UNICODE|re.IGNORECASE|re.DOTALL);
        if regexinfo.match(filecontent, re.MULTILINE) is None:
            print("No legal notice tag found");
        else:
            # If pattern matches, process data
            ## print(regexinfo.search(filecontent).groupdict());
            tmp_dict = regexinfo.search(filecontent).groupdict();
            ## print(tmp_dict['simparas'].strip().split("\n."));
            for tmp_item in tmp_dict['simparas'].strip().split("\n."):
                ## print(tmp_item.lstrip('.').strip());
                self.legalnotice.simpara.append(tmp_item.lstrip('.').strip());
            del(tmp_dict);
            del(tmp_item);

    def gen_xml_from_self(self, line_indent = ''):
        ''' Generates the xml structure from the current object
        Input parameter:
           line_indent is either one or more tab, whitespace or alike
        Returns:
            An xml-formatted string
        '''
##        TODO: implement these members too!
        # self.authorgroup = [];  # Not implemented yet
        # self.legalnotice = [];  # Not implemented yet
        
        if not re.match('^\s*$', line_indent):
            line_indent = "";
        _result = "";

        # Generating copyright tag
        _result += "\n"+ self.copyright.gen_xml_from_self(line_indent, ['year','holder']);
        
        # generating legalnotice tag
        _result += "\n"+ self.legalnotice.gen_xml_from_self(line_indent);

        # Generating revision history tags
        _result += "\n"+ line_indent +"<revhistory>";
        revision_items_list=['revnumber','date','authorinitials','revremark'];
        for revitem in self.revhistory:
            _result += "\n"+ revitem.gen_xml_from_self(line_indent + '\t', revision_items_list);
        _result += "\n"+ line_indent +"</revhistory>";
        _result += "\n";
        return _result;


def usage():
    print(" *********************************** ");
    print(__doc__);
    print(" *********************************** ");



def main():
    # Retrieving the data from the asciidoc text file
## TODO: use the arguments of the scripts to get this
    input_filename = 'samples/test_asciidoc.txt';
    f = open(input_filename, 'r');
    str_in = f.read();
    f.close();
    
    # This does it globally and print the table of hashtables to the screen.
    doc_item = docinfo();
    doc_item.get_revinfo_block(str_in);
    doc_item.get_copyright_content(str_in);
    doc_item.get_legalnotice_content(str_in);

    # writing output to the target file name
    out_f = open(doc_item.gen_docinfo_filename(input_filename), 'w');
    out_f.write(doc_item.gen_xml_from_self(''));
    out_f.close();

    print("XML file generation ended.");


if __name__ == '__main__':
    main();
    #run tests if called from command-line
##    print("# Usage explanations");
##    usage();
    
##    print("# ************** Unit tests... To be done. **************");
##    print("# Testing the 'revision' class:");
##    rev_item = revision();
##    print("# A non customized revhistory class item");
##    print rev_item.gen_xml_from_self('\t');



    # This is to check whether the generated xml conforms to the docbook's DTD
##    import libxml2;
##    dtd="""<!ELEMENT foo EMPTY>"""
##    instance=doc_item.gen_xml_from_self('');
##    dtd = libxml2.parseDTD("-//OASIS//DTD DocBook XML V4//EN",None);
##    ctxt = libxml2.newValidCtxt();
##    doc = libxml2.parseDoc(instance);
##    ret = doc.validateDtd(ctxt, dtd);
##    if ret != 1:
##        print("error doing DTD validation");
##    else:
##        print("Generated XML has a valid DTD!");
##
##    doc.freeDoc();
##    dtd.freeDtd();
##    del dtd;
##    del ctxt;
    pass;

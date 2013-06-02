asciidoc-tools
==============

These are the tools I develop to enhance my asciidoc experience

1. "docinfo_generator" module
-----------------------------

1.1. Modifications history
--------------------------

~~~~~
v1.0.0, Joseph HERLANT, 2013-06-01:
  As I don't have the utility of using the authorgroup tag (and that it is not rendered on PDF files), I didn't implement it.
  But if it is needed, don't hesitate to send me an email.
  Last change to get to 1.0.0 version: pass the source file name as an argument to the script.
v0.4.0, Joseph HERLANT, 2013-05-30: 
  Adding the support for the legalnotice tag.
  The "gen_xml_from_self" generic method now supports object members of type "list".
v0.3.1, Joseph HERLANT, 2013-05-11: Comments formatting minor modifications.
v0.3.0, Joseph HERLANT, 2013-05-11: Adding the support of the copyright tag.
v0.2.1, Joseph HERLANT, 2013-04-28: An xml tag test had been forgotten in the last commit. Correcting it.
v0.2.0, Joseph HERLANT, 2013-04-28: 
  Creating abstract class to have only one function that generate xml for each subclasses
  representing an xml block.
v0.1.1, Joseph HERLANT, 2013-04-21: Minor corrections in the code to include the support of multiline
v0.1.0, Joseph HERLANT, 2013-04-14: Creation. Only the revhistory tags generation and parsing is available.
~~~~~~

1.2. Using the docinfo_generator
--------------------------------

This module generated the docinfo xml file from a text file formatted using asciidoc format.

The resulting file will contain only the following tags:

 * revinfo       => tag for revision history table
 * copyright     => tag that will contain the name of the copyright's owner and the date of the copyright
 * legalnotice   => tag that will display the legal notice information

Command-line usage: `docinfo_generator.py [-h] asciidoc_input_file_name`

NOTE: This module is normally compatible python 2.6.6 (and later) 
and python 3.2.3 (other versions of python3 not tested but should work).

IMPORTANT: None of the following blocks are mandatory.

1.2.1. Revision history rules for an optimal docinfo generation (revinfo tag)
-----------------------------------------------------------------------------

To extract the revision history data, put it in a comment block (more than 3 "/").

Begin the block with one line only containing ":revinfo:"

Then for each revision history item is like this:

  * a block begins with a "v" followed by the version number (only digits separated by a ".")
  * followed by a ","
  * followed optionally by the author's initials or name followed by a ","
  * followed by the date of the modification
  * followed by a ":"
  * Then a bunch of lines for the comments over the remark

*Do NOT put a blank line between the blocks.*

The revision history ends with either:

  * a blank line
  * a comment line (a line beginning by more than 3 "/")
  * a new block header (a line beginning by a ":something:"

1.2.2. Copyright rules for optimal docinfo generation (copyright tag)
---------------------------------------------------------------------

To avoid any conflict with the asciidoc format, put the copyright in a comment block.

Begin the block with a line beginning with the ":copyright:" tag.

Then write the date followed by comma (",") and the company or author's name.

You can use multiple lines for this block, but the best practice is to put all in one line.


1.2.3. Legal notice rules for optimal docinfo generation (legalnotice tag)
--------------------------------------------------------------------------

To avoid any conflict with the asciidoc format, put the legalnotice block in a comment block.

Begin the block with a line beginning with the ":legalnotice:" tag.

Then write each paragraph that you want beginning them by a dot (".") as the very first character of the line.

You can use multiple lines for each paragraph, but each new paragraph must begin with a dot.

IMPORTANT: Don't separate paragraph by a blank line!

1.2.4. Example of correctly interpreted block
---------------------------------------------

~~~~~

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
last but not least! :)
//////

~~~~~

After running this script to generate the XML file, generate
the HTML document using: 

`a2x -a docinfo -fxhtml <asciidoc file name>`

Or the PDF document using:

`a2x -a docinfo -fxhtml <asciidoc file name>`


NOTE: As I am a beginner in python and in the development world,
don't hesitate to send me the errors I could have made
or the optimizations I could do.

NOTE: If you wish this script to be extended to include stuffs you would need,
don't hesitate to send me also a mail.

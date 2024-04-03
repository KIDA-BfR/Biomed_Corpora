"""

This script is can attempt to validate a submission file for the normalized gene list.  It simply tries to make sure the submission is in the correct form.  Since the results aren't supposed to be 'checked' by the submitters, it will no directly give examples of errors, but will try to identify them when possible.  This is intended to allow for some debugging and checking of system output before submission without looking at the submission files.

A submission to the normalized gene list track (GN) is a single file with three or four columns, separated by tabs.  The first column should be the PUBMED identifier of the abstract (integer), the second is an Entrez Gene Identifier (integer), the third is a span of text taken from the abstract.  This span of text should be free of any markup that is not in the raw abstract and should not have any carriage returns, line breaks, tabs, etc.  Also, no characters from the abstract should be removed from the text.  This means that an excerpt cannot span the title (which is set off by line breaks and a blank line) and the full text of the excerpt.  We are not setting particular limits on the excerpt length, but excerpts more than 255 characters will raise a warning in the validator.

There is an option to include a fourth column which is a number which ranges from 0 to 1.0 which reflects confidence (a 1 is absolute confidence) which can be used for additional analysis.  If submitters are willing, submissions to the track will be made publicly available in an anonymous form after the workshop to facilitate subsequence analysis.

This script is called:

% python bc2gnvalid.py 'submissionFilePath' 'testAbstractDirectory'

The 'submissionFilePath' is the file that will serve as a submission.

The 'testAbstractDirectory' is where the test documents are stored, the original .txt files named after their pubmed identifiers.


"""

import sys, os, string

flC = 0  # File line counts, how many nonempty lines
ilC = 0  # Incomplete line counts
ifC = 0  # ID failure counts
dlD = {} # Line repeat dictionary, pubmed+entrez -> count, duplicate line
reC = 0  # Repeat counts
elC = 0  # length of longest excerpt
cnC = 0  # Number of times a confidence number is present
cfC = 0  # Number of times the confidence numbers map to floats
aaC = 0  # Abstract absent count, when it couldn't find an abstract or perhaps open it; it should check permissions inside for each of these files, and if does exist and can't open then write error message and exit
mfC = 0  # Match failure count - how many times the excerpt is not found



if len(sys.argv) < 3:
    sys.exit("Error: Not enough arguments, please read the comments in the script")

subfile = sys.argv[1]
testDir = sys.argv[2]

if not os.path.isdir(testDir) or not os.access(testDir, os.R_OK):
    sys.exit("Error: The testAbstractDirectory does not seem to be a valid path, please read the comments in the script")

if not os.path.exists(subfile) or not os.access(subfile, os.R_OK):
    sys.exit("Error: The subfile cannot be found and/or read, please read the comments in the script")

SFO = open(subfile, "r")

for line in SFO.xreadlines():
    lineL = line.strip().split("\t")
    if not lineL:
        continue
    flC += 1
    if len(lineL) < 3 or len(lineL) > 4:
        ilC += 1
        continue
    try: pmid = string.atoi(lineL[0])
    except ValueError:
        ifC += 1
        continue
    try: geneid = string.atoi(lineL[1])
    except ValueError:
        ifC += 1
        continue
    if len(lineL[2]) > elC:
        elC = len(lineL[2])
    dkey = lineL[0] + "-" + lineL[1]
    if dlD.has_key(dkey):
        dlD[dkey] = dlD[dkey] + 1
    else:
        dlD[dkey] = 1
    if len(lineL) == 4:
        cnC += 1
        try:
            conffrac = string.atof(lineL[3])
            if conffrac <= 1.0 and conffrac >= 0.0:
                cfC += 1
        except ValueError:
            pass
    testFile = os.path.join(testDir, lineL[0] + ".txt")
    if not os.access(testFile, os.F_OK) or not os.access(testFile, os.R_OK):
        aaC += 1
        continue
    testText = open(testFile).read()
    if string.find(testText, lineL[2]) == -1:
        mfC += 1

if flC == 0:
    print "Error, empty file"

if ilC:
    print "Error, incomplete line error, the input file should have 3 (optionally 4, with confidence number) columns"
if ifC:
    print "Error, identifier error, the first item in each row should be a pubmed identifier, the second should be an EntrezGene identifier (for human)"

for dkey in dlD.keys():
    if dlD[dkey] > 1:
        reC += 1

if reC:
    print "Error: 'repeat error', each PUBMED identifier & Entrez Gene identifier pair should only appear once, no repeats"

if elC > 255:
    print "Error, long excerpt error, excerpts less than 256 characters long are encouraged, although this is not enforced"

if cnC and cnC != (flC - ilC - ifC):
    print "Error, inconsistent use of confidence numbers; if you are using the optional confidence numbers they should appear for every line"

if cnC != cfC:
    print "Error, inconsistent use of confidence numbers; if you are using the optional confidence numbers they should all be positive numbers between 0 and 1"
if aaC:
    print "Error, abstract absent error; cannot find appropriate abstract for a referenced PUBMED identifier in the testAbstractDirectory"
if mfC:
    print "Error, march failure error; cannot match an excerpt to the source abstract"


    
    













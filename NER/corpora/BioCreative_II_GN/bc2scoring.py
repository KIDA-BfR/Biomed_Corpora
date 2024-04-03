"""

This script is meant to score entries for the normalized gene list task for BioCreAtIvE 2 (2006-2007).  It was tested for python 4.0.  It certainly doesn't work for python versions earlier than 3.3.

It is called like this:

% python bc2scoring.py 'goldstandard' 'testfile'

'goldstandard' is the name of the goldstandard file
'testfile is the name of the genelist file to be tested


All output is to standard out, except error remarks which are to standard error.

The file formats are tab delimited with one pubmed/gene/excerpt entry per line with no header or line numbers.

goldstandard:
PMID   GeneID   Exceprt1   Excerpt2   Excerpt3 ...

testfile:
PMID   GeneID   Excerpt  OptionalConfidence

Note that only one text excerpt is required or examined (the first) for each line of the testfile.  The best match to an excerpt in then counted.  The output is as follows.

True Positive:
False Positive:
False Negative:
Precision:
Recall:
Gold File Errors:
Test File Errors:


- Alex Morgan, alexmo@stanford.edu

copyright  2006, MITRE Corporation

"""

import string, sys, os
from sets import Set

if len(sys.argv) != 3:
    sys.exit("Error with input format, should be of the form python bc2scoring.py 'goldstandard' 'testfile' ")

goldfile = sys.argv[1]
testfile = sys.argv[2]

if (not os.access(goldfile, os.R_OK)) or (not os.access(testfile, os.R_OK)) :
    sys.exit("Error with input files, check permissions and existence;  python bc2scoring.py 'goldstandard' 'testfile' ")


testFileErrors = 0
goldFileErrors = 0
truePositive = 0
falsePositive = 0
falseNegative = 0
missingExcerpts = 0

gfo = open(goldfile)
goldD = {}

for line in gfo.xreadlines():
    line = line.strip()
    lineL = line.split("\t")
    if len(lineL) < 3:
        print >>sys.stderr, "Error parsing GoldFile, ignoring line: " + repr(line)
        goldFileErrors += 1
        continue
    pmid = lineL[0]
    gnid = lineL[1]
    excerptL = lineL[2:]
    #print "%s %s %s " % (pmid, gnid, repr(excerptL))
    try:
        pmid = string.atoi(pmid)
        gnid = string.atoi(gnid)
    except:
        print >>sys.stderr, "Error parsing GoldFile, incorrect identifier, ignoring line: " + repr(line)
        goldFileErrors += 1
        continue
    dkey = "%d:%d" % (pmid, gnid)
    if goldD.has_key(dkey):
        print >>sys.stderr, "Error parsing GoldFile, repeated identifiers, ignoring line: " + repr(line)
        goldFileErrors += 1
        continue
    goldD[dkey] = excerptL


tfo = open(testfile)
testD = {}
   
for line in tfo.xreadlines():
    line = line.strip()
    lineL = line.split("\t")
    if len(lineL) < 3:
        print >>sys.stderr, "Error parsing TestFile, perhaps missing excerpt, line: " + repr(line)
        missingExcerpts += 1
        if len(lineL) < 2:
            continue
        excerpt = ""
    else:
        excerpt = lineL[2]
    pmid = lineL[0]
    gnid = lineL[1]
    try:
        pmid = string.atoi(pmid)
        gnid = string.atoi(gnid)
    except:
        print >>sys.stderr, "Error parsing TestFile, incorrect identifier, ignoring line: " + repr(line)
        testFileErrors += 1
        continue
    dkey = "%d:%d" % (pmid, gnid)
    if testD.has_key(dkey):
        print >>sys.stderr, "Error parsing TestFile, repeated identifiers, ignoring line: " + repr(line)
        testFileErrors += 1
        continue
    testD[dkey] = excerpt

sys.stderr.flush()

def keyCompare(a,b):
    ap, ag = map(string.atoi,a.split(":"))
    bp, bg = map(string.atoi,b.split(":"))
    if ap != bp: return cmp(ap,bp)
    else: return cmp(ag,bg)

    
idS = Set(testD.keys())
idS.update(goldD.keys())

idL = list(idS)
idL.sort(keyCompare)

outlineL = []


for id in idL:
    etype = None
    G = 0
    T = 0
    if goldD.has_key(id):
        G = 1
    if testD.has_key(id):
        T = 1
    if G and T:
        truePositive += 1
    if G and not T:
        falseNegative +=1
    if T and not G:
        falsePositive += 1

def recallF(TP, FP, FN):
    denom = TP + FN
    if denom == 0:
        return 1
    else: return float(TP)/denom

def precisionF(TP, FP, FN):
    denom = TP + FP
    if denom == 0:
        return 1
    else: return float(TP)/denom


print """

True Positive:   %5d
False Positive:  %5d
False Negative:  %5d
Precision:       %5.3f
Recall:          %5.3f
Gold File Errors:%5d
Test File Errors:%5d
Missing Excerpts:%5d""" % (truePositive, falsePositive, falseNegative, precisionF(truePositive, falsePositive, falseNegative), recallF(truePositive, falsePositive, falseNegative),  goldFileErrors, testFileErrors, missingExcerpts)



    

        

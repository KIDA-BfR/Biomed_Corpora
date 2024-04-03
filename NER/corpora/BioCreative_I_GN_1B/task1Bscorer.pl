#!/usr/local/perl

## This is the scoring script for Task 1B of the BioCreative Evaluation.
## It can be executed with 'perl task1Bscorer.pl <goldstandard> <eval file>'.
## The goldstandard file is a concatentation of all the gene list entries
## (*.gene_list) files for the gold standard, whereas the evaluation file is 
## a concatenation of all the submission files (each line contains a source 
## file name (e.g. fly_000145_testing), then a unique identifier 
## (e.g. FBgn0026412), and then an excerpt from the text (e.g. leucine
## aminopeptidase).


if ((scalar @ARGV > 2) or (scalar @ARGV < 1)) { die "Only one or two arguments possible.  The first is the name of the goldstandard file.  If there is a second it is the name of the file being evaluated.";}


if ( (scalar @ARGV) == 2) { open EVALFILE, "<$ARGV[1]" or die "Unable to open the file for evaluation (the second argument): '$ARGV[1]'" ;   }
else {EVALFILE = STDIN;}


open GOLDSTANDARD , "<$ARGV[0]";


%GoldStandard;
# Hash takes in a concatenation (with a space) of the file name and the gene name and then a boolean of whether or not that abstract contains a mention of that gene
%GSFiles; # To keep track of the total # of files from the goldstandard

$GSErrors = 0; # Gold Standard Errors
$EvalErrors = 0; # Eval File Errors


while (<GOLDSTANDARD>) {
  chomp;
  if (not $_) {next;}
  if  ( not /(\S+)\t(\S+)\t([YNX])\t([YN])/) {print "Error in input, excluding goldstandard line: '$_'\n"; $GSErrors++;}
  else {
    if ($4 eq "Y") {
      $GoldStandard{"$1 $2"} = 1;
      $GSFiles{$1} = 1;
    }
  }

}

%TruePositives;  # On the eval list and in the standard
%FalsePositives; # On the eval list, but not in the standard
%FalseNegatives; # Not on the val list, but in the standard
%Observed;



$MissingExcerpts = 0;


while (<EVALFILE>) {
  chomp;
  if  ( not /(\S+)\t(\S+)(.*)/) {print "Error in input, excluding evaluation file line: '$_'\n"; $EvalErrors++;}
  else {
    if ($Observed{"$1 $2"}) {
      print "Error, reproduced input in the evaluation file: $1 $2\n";
      $EvalErrors++;
      next;
    }
    $doc = $1;
    $gene = $2;
    $excerpt = $3;

    if ($excerpt !~ /\w/) {
      print "Missing excerpt in the evaluation file, should contain a piece of text indicating the gene mention: '$doc $gene'\n";}

    if ($GoldStandard{"$doc $gene"}) {
      #print "Yay $1 $2\n";
      if ($TruePositives{$1}) {$TruePositives{$1}++;}
      else {$TruePositives{$1} = 1;}
      delete $GoldStandard{"$doc $gene"};
    }
    else {
      if ($FalsePositives{$1} > 0) {$FalsePositives{$1}++;}
      else {$FalsePositives{$1} = 1;}
    }
    $Observed{"$doc $gene"} = 1;
 }
}


foreach $key (keys %GoldStandard) {
  $key =~ /(\S+) (\S+)/;
  if ($FalseNegatives{$1}) {$FalseNegatives{$1}++;}
  else {$FalseNegatives{$1} = 1;}
}
#print "\n";


$TotalFalseNegativeCount = 0;
$TotalFalsePositiveCount = 0;
$TotalTruePositiveCount = 0;

foreach $key (keys %FalseNegatives) {
  $TotalFalseNegativeCount += $FalseNegatives{$key};
}

foreach $key (keys %FalsePositives) {
  $TotalFalsePositiveCount += $FalsePositives{$key};
}

foreach $key (keys %TruePositives) {
  $TotalTruePositiveCount += $TruePositives{$key};
}

$TotalPrecision = 1.0 * $TotalTruePositiveCount / (1.0 * $TotalTruePositiveCount + $TotalFalsePositiveCount);

$TotalRecall = 1.0 * $TotalTruePositiveCount / (1.0 * $TotalTruePositiveCount + $TotalFalseNegativeCount);

print "Total True Positive Count $TotalTruePositiveCount\n";
print "Total False Positive Count $TotalFalsePositiveCount\n";
print "Total False Negative Count $TotalFalseNegativeCount\n";

printf "Total Precision:  %.3f  Total Recall: %.3f \n", $TotalPrecision, $TotalRecall;
print "Errors Reading Gold Standard: $GSErrors\nErrors Reading Evaluation File: $EvalErrors\n";
print "Missing Mention Excerpts: $MissingExcerpts\n";







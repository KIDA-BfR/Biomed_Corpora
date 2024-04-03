
Description of the resources provided for Task II of BioCreative

The results for the BioCreative task II are provided in XML format. To make it easier to use this data the evaluations from the database curators have been included.

The format is as follows:
<protein>
        <pmid></pmid>
                <idTask></idTask>
                        <nameProtein</nameProtein>
                                <dbId></dbId>
                                <sourceDb></sourceDb>
                                <goCode>
                                        <name></name>
                                        <code></code>
                                        <evidenceText></evidenceText>
                                </goCode>
                                        <eval_prot></eval_prot>
                                        <eval_go></eval_go>
                                        <comment></comment>
</protein>


This means that there is an entry like that for each of the predictions (everything in one file).

<protein>: the entry for a result

<pmid>: PubMed identificator.

<idTask>: the id of the task. That will be 2.1, 2.2 according to the task definition at
http://www.pdg.cnb.uam.es/BioLINK/BioCreative_task2.html.

<nameProtein>: a name for the protein.

<dbId>: The DB identifier of the protein.

<sourceDb>: This is the source DB that the identifier refers to.

<goCode>: the part of the GO predictions.

<name>: the name (or term) of the GO code.

<code>: The GO code.

<evidenceText>: The evidence text provided by the systems to (should) refer to the protein and relate it to the GO code. This text was extracted as it appears here from the full text version of the Journal of Biological Chemistry (provided by HighWire Press) in SGML format (the "strange" tags you may find there are due to the SGML format and can be ignored in most cases).

<eval_prot>: The judgement by the curator, taken into account if in the evidence text the correct protein appears.

<eval_go>: The judgement by the curator, taken into account if they are correctly predicted and the evidence text corresponds.

<comment>: Additional comments.

The curators evaluated:
- the GO terms (if they are correctly predicted and the evidence text corresponds)
- the proteins (if in the evidence text the correct protein appears)
- and they made additional comments

The scheme for both GO and proteins was "high" (meaning that GO or protein were correct), "generally" (for GO terms this means that they are not totally wrong but too general to be really useful for annotation, for protein this means that the specific protein is not there but a homologue from another organism or a reference to the protein family), and "low" (which means basically wrong).

For more information about Task II please refer to: http://www.pdg.cnb.uam.es/BioLINK/BioCreative_task2.html

To learn more about how the data were evaluated take a look to the handouts that were produced for the workshop and can be found here: http://www.pdg.cnb.uam.es/BioLINK/workshop_BioCreative_04/handout/index.html
The documents that refer specifically to the Task II evaluation are:
- http://www.pdg.cnb.uam.es/BioLINK/workshop_BioCreative_04/handout/orga/handouts_final_results_task2.pdf
- http://www.pdg.cnb.uam.es/BioLINK/workshop_BioCreative_04/handout/orga/handouts_final_results_task2_details_1.pdf
- http://www.pdg.cnb.uam.es/BioLINK/workshop_BioCreative_04/handout/orga/handouts_final_results_task2_details_2.pdf
- http://www.pdg.cnb.uam.es/BioLINK/workshop_BioCreative_04/handout/orga/handouts_final_results_task2_details_3.pdf

For more information about the systems that were applied by the participants the workshop papers are also included in the handouts.

If you have technical questions about the data please contact Eduardo Andrés León <leon@cnb.uam.es>.
If you have questions about the organization of BioCreative please contact Christian Blaschke <blaschke@cnb.uam.es>



# Biomed_Corpora
Collection of Biomedical corpora for NER, Relation Extraction and Question Answering

## Selected Biomed NER Corpora
| Dataset                                            | Source                                                                                   | Annotation scope        | Entity types                                                                                                                                                                                                                                                                                                                                                           | Linked identifiers (NEL)                                                                                                                                                                                 | Text size                             | Format                                       | Reference                                                                                                                                 |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| BioCreative I GN 1B (only gene id per abstract)    | MEDLINE                                                                                  | Abstracts               | gene                                                                                                                                                                                                                                                                                                                                                                   | gene identifiers                                                                                                                                                                                         | 5000 Abstracts                        | Plain text                                   | Hirschman et al., Bioinformatics 2005                                                                                                     |
| BioCreative II GN task                             | PubMed (MEDLINE)                                                                         | Abstracts               | Gene, protein                                                                                                                                                                                                                                                                                                                                                          | EntrezGene identifiers                                                                                                                                                                                   | 556                                   | tabular                                      | Morgan et al., Genome Biol 2008                                                                                                           |
| BioCreative II.5 Elsevier                          | PMC                                                                                      | Full-text               | Protein                                                                                                                                                                                                                                                                                                                                                                | Uniprot Ids                                                                                                                                                                                              | 595                                   | tabular                                      | Leitner et al., 2010                                                                                                                      |
| BioCreative III GN task                            | PMC, articles from BioMed Central (BMC) or Public Library of Science (PloS)              | Full-text               | Gene/ protein                                                                                                                                                                                                                                                                                                                                                          | EntrezGene identifiers                                                                                                                                                                                   | 1039                                  | tabular                                      | Lu et al., 2011                                                                                                                           |
| CellFinder                                         | PMC                                                                                      | Full-text               | anatomical parts, cell components, cell lines, cell types, genes/protein and species                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                          | 10                                    | Standoff (Brat)                              | Neves et al., LREC 2012                                                                                                                   |
| CDR (BC5CDR - Biocreative V CDR task)              | PubMed                                                                                   | Abstracts               | Disease, Chemical                                                                                                                                                                                                                                                                                                                                                      | MeSH                                                                                                                                                                                                     | 15000                                 | PubTator, BioC                               | Li et al., 2016                                                                                                                           |
| CHEMDNER (Biocreative IV Chemdner)                 | PubMed                                                                                   | Abstracts               | Chemical/ Drugs                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                          | 10000                                 | BioC                                         | Krallinger et al., 2015                                                                                                                   |
| Colorado Richly Annotated Full-text (CRAFT) Corpus | PubMed Open Access                                                                       | Full-text               | cell type, Chemical Entities of Biological Interest, DNA, Gene, NCBI Taxonomy, protein, RNA, Sequence                                                                                                                                                                                                                                                                  | Chemical Entities of Biological Interest, Cell Ontology, Entrez Gene, Gene Ontology (biological process, cellular component, and molecular function), NCBI Taxonomy, Protein Ontology, Sequence Ontology | 97                                    | XML (Knowtator)                              | Bada et al., BMC Bioinformatics 2012                                                                                                      |
| GENETAG (BioCreative II Gene Mention)              | MEDLINE                                                                                  | Abstracts and Full-text | Gene, Protein                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                          | 20000 sentences                       | Plain text                                   | Tanabe et al., BMC Bioinformatics 2005                                                                                                    |
| GENIA (term annotation)                            | MEDLINE (from articles with MeSH terms ‚human‘, ‚blood cell‘ and ‚transcription factor‘) | Abstracts and titles    | amino_acid, amino_acid_monomer, atom, body_part, carbohydrate, cell_component, cell_line, cell_type, Complex, DNA, domain_or_region, family_or_group, inorganic, lipid, molecule, mono_cell, multi_cell, nucleic_acid, nucleotide, other, other_artificial_source, other_organic_compound, peptide, polynucleotide, protein, RNA, substructure, subunit, tissue, virus | GENIA Ontology                                                                                                                                                                                           | ~2000 Abstracts                       | XML (PTB, gpxml)                             | Kim et al., Bioinformatics 2003                                                                                                           |
| GoldHamster                                        | PubMed (Medline)                                                                         | Abstracts               | in vivo, organs, primary cells, immortal cell lines, invertebrates, humans, in silico and other (models)                                                                                                                                                                                                                                                               |                                                                                                                                                                                                          | 1600                                  |                                              | Neves et al., Research Square 2022                                                                                                        |
| GREC (Gene Regulation Event Corpus)                | MEDLINE                                                                                  | Abstracts               | Proteins, Living systems, Nucleic, Acids, Processes, Experimental                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                          | 240 (167 E. Coli, 73 human)           | Standoff (BioNLP'09 Shared Task format), XML | Thompson et al., BMC Bioinformatics 2009                                                                                                  |
| JNLPBA                                             | MEDLINE (derived from the GENIA corpus)                                                  | Abstracts               | cell line, cell type, DNA, RNA, protein                                                                                                                                                                                                                                                                                                                                | GENIA Ontology                                                                                                                                                                                           | 2404 (2000 Train, 404 Test Abstracts) | Standoff, IOB2                               | Collier and Kim, Proceedings of the International Joint Workshop on Natural Language Processing in Biomedicine and its Applications, 2004 |
| LINNAEUS                                           | PMC                                                                                      | Full-text               | Species                                                                                                                                                                                                                                                                                                                                                                | NCBI Species Ids                                                                                                                                                                                         | 100                                   | Standoff                                     | Gerner et al., 2010                                                                                                                       |
| MedMentions                                        | PubMed                                                                                   | Titles and Abstracts    | gene function, disease, phenotype, structure, anatomy, drug, chemical entities                                                                                                                                                                                                                                                                                         | UMLS (Unified Medical Language System) ontology                                                                                                                                                          | ~4000                                 | PubTator                                     | Mohan and Li, AKBC 2019                                                                                                                   |
| NCBI Disease                                       | PubMed                                                                                   | Abstracts               | Disease                                                                                                                                                                                                                                                                                                                                                                | Identifiers for disease entities from the MeSH (Medical Subject Headings) and OMIM (Online Mendelian Inheritance in Man) databases                                                                       | 793                                   | text                                         | Dogan et al., J Biomed Inform. 2014                                                                                                       |
| OSIRIS                                             | PubMed                                                                                   | Abstracts               | Gene, variation                                                                                                                                                                                                                                                                                                                                                        | dbSNP                                                                                                                                                                                                    | 105                                   | XML                                          | Furlong et al. BMC Bioinform 2008                                                                                                         |
| PubMed Query Corpus                                | PubMed                                                                                   |                         | Abbreviations, Author name, Body Part, Cell or Cell component, Chemicals, drugs, Citation information, Devices, Disorders, Genes, proteins, molecular sequences, Journal name, Living Beings, Medical procedures, MEDLINE Title, Phenomenon, Process/ Function, Research procedures, Tissue                                                                            |                                                                                                                                                                                                          | 10.000 queries                        | Plain text                                   | Névéol et al., Journal of Biomedical Informatics 2011                                                                                     |
| SCAI Chemicals                                     | MEDLINE                                                                                  | Abstracts               | Chemical                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                          | 100                                   | CONLL                                        | Kolárik et al. 2008                                                                                                                       |
| SCAI Diseases                                      | MEDLINE (randomly selected using ‚Disease OR Adverse effect‘ in a PubMed query)          | Abstracts               | disease, adverse effect                                                                                                                                                                                                                                                                                                                                                | MeSH, MedDRA, ICD-10, SNOMED CT, UMLS                                                                                                                                                                    | 400                                   | CONLL                                        | Gurulingappa et al., LREC 2010                                                                                                            |
| SCAI IUPAC Chemicals                               | MEDLINE                                                                                  | Abstracts               | Chemical, Modifier                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                          | 463 (train), 1000 (test)              | CONLL                                        | Klinger et al. 2008                                                                                                                       |
| Species-800 (S800)                                 | MEDLINE                                                                                  | Abstracts               | Species                                                                                                                                                                                                                                                                                                                                                                | NCBI Taxonomy identifiers                                                                                                                                                                                | 800                                   | tabular                                      | Pafilis et al., 2013                                                                                                                      |
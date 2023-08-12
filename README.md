# Genetic variant data analysis

This repository contains scripts for the analysis of genetic variant data for chosen genes of interest. This work was completed as part of my MSc in Medical Immunology at the University of Pretoria, South Africa.

## Important terminology

DNA: DNA, short for deoxyribonucleic acid, is a molecule that contains the genetic instructions or blueprint for the development, functioning, and reproduction of all known living organisms.

Gene: A gene is a segment of DNA that contains instructions for producing a specific protein or performing a particular function within an organism.

Allele: An allele refers to one of the possible forms or variations of a specific gene. Genes are made up of DNA, and different alleles can exist within a population, representing different versions of the same gene.

Variant: A variant is a specific form or alteration of a gene or a DNA sequence. It refers to any difference or change in the DNA sequence when compared to a reference or normal sequence. 

Variant frequency: Variant frequency refers to the proportion or percentage of individuals in a population who carry a particular variant or genetic alteration.

Variant effect: Variant effect refers to the impact or consequence of a genetic variant on an organism.

Variant type: Variant type refers to the categorization or classification of genetic variants based on their characteristics.

rsID: An rsID number is a unique label ("rs" followed by a number) used by researchers and databases to identify a specific short-length variant.

## Data

The variant data used for this analysis was generated through a prior analysis of [1000 Genomes](https://www.internationalgenome.org/1000-genomes-summary/), [Human Genome Diversity Project](https://www.internationalgenome.org/data-portal/data-collection/hgdp) genomic data using a [Snakemake bioinformatics pipeline](https://github.com/Tuks-ICMM/Pharmacogenetic-Analysis-Pipeline).

**Include GnomAD**

## Analysis aim

The aim of this analysis was to determine the African population frequencies and potential pathogenic effects of genetic variants within genes that are associated with a medical condition known as neonatal [hypoxic ischemic encephalopathy](https://www.ucsfbenioffchildrens.org/conditions/neonatal-hypoxic-ischemic-encephalopathy).

Key research questions were:
1. Which African population groups are represented in the datasets and what is the distribution of sample sizes within each group?
2. What is the extent of shared and unique genetic variation within African population groups?
3. What is the distribution of variant type, novelty and frequency in the gene regions of interest? 
4. What are the differences in variant frequencies among population groups within Africa, and how do these frequencies compare to global populations?

## Methods 

A brief description of the methods used to answer the research questions are described below. Detailed descriptions of the methods are given in the relevant jupyter notebooks in the [Analysis](https://github.com/MeganHolborn/Genomics_data_analysis_internal/tree/main/Analysis) folder. 

1. Which African population groups are represented in the datasets and what is the distribution of sample sizes within each group? 

For this analysis, a sample is defined as a the ID of an individual from which genomic data was obtained. Sample data was grouped by ethnolinguistic classification and region. A bar plot was constructed to visualise the sample counts per population group. The regional distribution of samples was visualised using a pie chart. 

**Fix for understanding**

2. What is the extent of shared and unique genetic variation within Western, Eastern, Southern and Central Africa?

Variant frequency counts were determined for each African population group. The shared and unique genetic variation between the population groups was visualised using upset plots. An upset plot is a type of data visualization that is used to compare the overlap or intersection of multiple sets or categories.

3. What is the distribution of variant type, novelty and frequency in the gene regions of interest? 

Variant annotation information including type, rsID nomenclature and consequences were imported from Ensembl via API. Variant frequencies were calculated from the available allele count information. A variant was classified as potentially novel if rsID nomenclature for the variant did not exist. Variant type, novelty and frequency distributions were visualised using stacked bar plots. 

4. What are the differences in variant frequencies among population groups within Africa, and how do these frequencies compare to global populations?

Variant frequencies for African population groups were compared using Fisher's two-sided tests. Frequency differences between population groups were demarcated as significant if the p-value was below 0.05, after correction for multiple testing using the Bonferroni method. 

To compare variant frequencies of Africans to that of European, East Asian and South Asian populations, European, East Asian and South Asian variant frequency data was imported from the NCBI Allele Frequency Aggregator (ALFA) database via API. Variant frequency comparisons were performed using Fisher's two-sided tests as described above. 

## Results

The results of the analysis are provided in the [Results](https://github.com/MeganHolborn/Genomics_data_analysis_internal/tree/main/Results) folder.

## File structure

Scripts to process, analyse and visualise the data are included in the [Analysis](https://github.com/MeganHolborn/Genomics_data_analysis_internal/tree/main/Analysis) folder. 

The [Data](https://github.com/MeganHolborn/Genomics_data_analysis_internal/tree/main/Data) folder contains raw and processed data organised. The [Raw](https://github.com/MeganHolborn/Genomics_data_analysis_internal/tree/main/Data/Raw) data consists of genetic variant allele counts and frequencies for African super- and sub-population groups. Predicted variant effect data gathered from [Ensembl](https://www.ensembl.org/info/docs/tools/vep/index.html) and [PredictSNP2](https://loschmidt.chemi.muni.cz/predictsnp2/) are also included here. The [Processed](https://github.com/MeganHolborn/Genomics_data_analysis_internal/tree/main/Data/Processed) data consists of data that has been processed using scripts in the [Analysis/Data_preparation](https://github.com/MeganHolborn/Genomics_data_analysis_internal/tree/main/Analysis/Data_preparation) folder. 

Metadata on the samples and gene regions from which the data was generated can be found in the [Metadata](https://github.com/MeganHolborn/Genomics_data_analysis_internal/tree/main/Metadata) folder.

The results of the analysis are included in the [Results](https://github.com/MeganHolborn/Genomics_data_analysis_internal/tree/main/Results) folder.

[Utils](https://github.com/MeganHolborn/Genomics_data_analysis_internal/tree/main/Utils) contains all constants and functions generated for the analysis.
[Utils](https://github.com/MeganHolborn/Genomics_data_analysis_internal/tree/main/Utils) contains all constants and functions generated for the analysis.
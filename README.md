# HIE Genetic Data Analysis

This repository contains scripts for the analysis of variants in genes associated with hypoxic ischemic encephalopathy (HIE). This work was completed in partial fulfillment of a MSc Medical Immunology degree at the University of Pretoria by Megan A Holborn.

View a PDF summarising the findings [here](https://github.com/Tuks-ICMM/HIE_Genetic_data_analysis/blob/main/Report.pdf). 

# Table of Contents

1. [Background](#background)
    1.1. [Important terminology](#important-terminology)
    1.2. [Research questions](#research-questions)
    1.3. [Data retrieval](#data-retrieval)
    1.4. [Data preparation](#data-preparation)
    1.5. [Analysis](#analysis)
    1.6. [Findings](#findings)
2. [Installation and usage](#installation-and-usage)
3. [Acknowledgements](#acknowledgements)

# 1. Background

Hypoxic ischemic encephalopathy (HIE) is a type of brain injury resulting from a restriction in blood flow and oxygen delivery around the time of birth. [Prior studies](https://doi.org/10.1016/j.ygeno.2022.110508) on Asian, European and Latin American populations have revealed associations with HIE and genes involved in several biological functions, including programmed cell death and inflammation. To lay the groundwork for future research on the genetics of HIE on African populations, we assessed the frequency and potential effects of genetic variants within African populations in genes with potential relevance to HIE. The notebooks housed in this repository detail the analysis of these genetic variants using open-source genetic data on African populations. 

## 1.1. Important terminology

* `Gene`: A gene is a segment of DNA that contains instructions for producing a specific protein or performing a particular function within an organism.
* `Genetic variant`: A genetic variant is a specific alteration of a DNA sequence. It refers to any difference or change in the DNA sequence when compared to a reference or normal sequence. Genetic variants in the DNA encoding a gene can sometimes have detrimental effects on the gene's function.
* `Variant allele`: An allele refers to one of several possible versions of a variant that can exist within a population.
* `Variant allele frequency`: The frequency of a variant allele refers to the proportion of individuals in a population who carry that particular variant allele.
* `Deleterious variant allele`: A variant allele that is more likely to cause disease.

## 1.2. Research questions

The focus of this analysis was on understanding the frequency and predicted effects of genetic variants found in HIE genes of interest in the general African population. Specifically, the research addressed the following questions:

1. **Population Representation:** Which African ethnolinguistic population groups are represented by the genetic data, and what are the proportions of samples from Central, Southern, Eastern, and Western Africa?
2. **Genetic Variation:** To what extent is genetic variation shared or unique within African subpopulation groups?
3. **Rare Variants:** What is the distribution of rare variants within the different genes, and how do these distributions vary within African ethnolinguistic subpopulations? Additionally, do specific subpopulations exhibit a higher amount of rare variants compared to others?
4. **Deleterious Variants:** Which variants identified in African populations have deleterious effect prediction scores and are likely to contribute to disease? 
5. **Variant Frequency Comparisons:** How do the frequencies of variants in the genes of interest compare between African ethnolinguistic subpopulation groups, and between Africans and European, Asian, and Latin American populations?
6. **Disease-Associated Variants:** How many of the variants identified within the genes of interest in African populations have known disease phenotype associations? Of the variants with known disease associations, how many are deleterious, and which disease phenotypes are associated with these deleterious variants, whether common or rare in Africans? Furthermore, how do the frequencies of these deleterious variants with known disease associations compare across African subpopulation groups and between Africa and other global populations?

## 1.3. Data retrieval

* Open-source 1000 Genomes- and HGDP-sourced genetic data on African populations was retrieved from [GnomAD v3.1.2](https://gnomad.broadinstitute.org/news/2021-10-gnomad-v3-1-2-minor-release/) in Variant Call Format (.vcf). The data underwent processing steps not covered in detail in this repository. In brief, a [bioinformatics workflow](https://github.com/Tuks-ICMM/Pharmacogenetic-Analysis-Pipeline) was utilised to process the African genomic data, resulting in population-stratified variant counts for the genes of interest. The raw variant count data for African ethnolinguistic subpopulations and Africans overall is available in the [Data/Raw/SUB](https://github.com/Tuks-ICMM/HIE_Genetic_data_analysis/tree/main/Data/Raw/SUB) and [Data/Raw/SUPER](https://github.com/Tuks-ICMM/HIE_Genetic_data_analysis/tree/main/Data/Raw/SUPER) folders, respectively.

* To compare the variant allele count data for African populations, generated in-house from the GnomAD 1000 Genomes and HGDP datasets, with data from other global populations, variant count data for European, Asian, and Latin American populations was retrieved from the [NCBI ALFA database](https://www.ncbi.nlm.nih.gov/snp/docs/gsr/alfa/). The raw variant count data for these global populations is available in the [Data/Raw/ALFA](https://github.com/Tuks-ICMM/HIE_Genetic_data_analysis/tree/main/Data/Raw/ALFA) folder.

* Variant effect prediction data for variants identified in-house in African population groups was retrieved from the [Ensembl Variant Effect Predictor](https://www.ensembl.org/info/docs/tools/vep/index.html) using the [CADD v1.6](https://cadd.gs.washington.edu/score) tool. The raw data was stored in the [Data/Raw/VEP](https://github.com/Tuks-ICMM/HIE_Genetic_data_analysis/tree/main/Data/Raw/VEP) folder.

* Information on disease phenotype associated with the variant identified in-house in African populations was retrieved using [the Functional Annotation of Variants - Online Resource v2.0 (FAVOR)](https://favor.genohub.org/batch-annotation) tool. The raw data was stored in the [Data/Raw/PHENO](https://github.com/Tuks-ICMM/HIE_Genetic_data_analysis/tree/main/Data/Raw/PHENO) folder. 

## 1.4. Data preparation

The raw data, which was retrieved as described above, underwent preparation steps including:

* Selecting relevant features of interest
* Removing duplicate entries and handling null values
* Merging of data from several sources if applicable 
* Adding additional features
* Restructuring the data in a suitable format for further analysis

The prepared data is stored in the [Data/Processed](https://github.com/Tuks-ICMM/HIE_Genetic_data_analysis/tree/main/Data/Processed) folder. Additional information on the preparation process and code utilised can be found in the notebooks stored in the [Notebooks/Data_preparation](https://github.com/Tuks-ICMM/HIE_Genetic_data_analysis/tree/main/Notebooks/2-Data_preparation) folder.

## 1.5. Analysis

To answer each of the above research questions, relevant analyses were performed as documented in the Jupyter notebooks in the [Notebooks/Analysis](https://github.com/Tuks-ICMM/HIE_Genetic_data_analysis/tree/main/Notebooks/3-Analysis) folder. 

## 1.6. Findings

An overview of the findings of the analysis are available [here](https://github.com/Tuks-ICMM/HIE_Genetic_data_analysis/blob/main/Report.pdf). 

# 2. Installation and usage

The data analysis scripts in this repository was developed using Python 3.9.13.

To utilise the scripts, install the necessary Python dependencies by typing in the following terminal command:
`pip install -r requirements.txt`

# 3. Acknowledgements

Funding for this research was received from the Bill and Melinda Gates Foundation and the South African Medical Research Council. 
The project was supervised by Prof Michael S Pepper, Prof Fourie Joubert and Dr Juanita Mellet.
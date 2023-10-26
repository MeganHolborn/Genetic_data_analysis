# HIE Genetic Data Analysis

This repository contains scripts for the analysis of genetic variant data on genes associated with hypoxic ischemic encephalopathy (HIE). This work was completed in partial fulfillment of an MSc in Medical Immunology at the University of Pretoria by Megan A Holborn.

View a pdf summarising the methods and results [here](https://github.com/Tuks-ICMM/HIE_Genetic_data_analysis/blob/main/Results/Report/Report.pdf). 

## Content

1. [Background information](#background-information)
2. [Data acquisition](#data-acquisition)
3. [Data preparation and cleaning](#data-preparation-and-cleaning)
4. [Research questions](#research-questions)
4. [Methods](#methods)
5. [Findings](#findings)
6. [Acknowledgements](#acknowledgements)
7. [Important terminology](#important-terminology)

## Background information

Hypoxic ischemic encephalopathy (HIE) is a type of brain injury resulting from a restriction in blood flow and oxygen delivery around the time of birth. [Prior studies](https://doi.org/10.1016/j.ygeno.2022.110508) have revealed associations between suspected HIE and genes involved in several biological functions, including programmed cell death, inflammation and blood flow homeostasis. These studies have been performed on predominantly Asian and European populations with no studies published on African populations to date. African populations exhibit a high amount of genetic diversity, which often renders disease research findings from other global populations less applicable to Africans. This analysis aimed to assess the genetic variation within HIE-associated genes across African population groups to provide foundational data for a genetic association analysis involving African HIE patients and controls.

## Data acquisition

* African genomic data from the 1000 Genomes and Human Genome Diversity Project datasets was
retrieved from [GnomAD v3.1.2](https://gnomad.broadinstitute.org/news/2021-10-gnomad-v3-1-2-minor-release/) in Variant Call Format (.vcf). A [bioinformatics pipeline](https://github.com/Tuks-ICMM/Pharmacogenetic-Analysis-Pipeline) was utilised to process the African genomic data, resulting in population-stratified variant count information for genetic variants located in the genes of interest.
* Additional data on the impact of variants on gene functionality, processing and translation into proteins (consequences), along with predictions of the potential harm caused by variants (effect predictions) were retrieved from [Ensembl](https://www.ensembl.org/info/docs/tools/vep/index.html) and [PredictSNP2](https://loschmidt.chemi.muni.cz/predictsnp2/), respectively.

## Data preparation and cleaning

The acquired data underwent [preparation and cleaning steps](https://github.com/Tuks-ICMM/HIE_Genetic_data_analysis/tree/main/Notebooks/Data_preparation). This process entailed:

* Selecting relevant features of interest
* Removing duplicate entries and handling null values
* Merging of data from several sources if applicable 
* Adding additional features
* Restructuring the data in a suitable format for further analysis

## Research questions

1. Which African ethnolinguistic population groups are represented by the genetic data and what are the proportions of samples from Central, Southern, Eastern and Western African regions?
2. To what extent is genetic variation shared or unique within Central, Southern, Eastern and Western African populations within the genes of interest?
3. What is the prevalence of rare variants in the genes of interest within African populations, and do specific populations exhibit a higher rare variant burden?
4. Which of the variants with rare frequencies in African populations are most likely to contribute to disease, based on predicted effect on gene/protein structure and function?
5. How do frequencies of variants in the studied genes among Africans compare with those of Europeans/Asians?
6. Have any of the genetic variants within the genes of interest previously been associated with HIE? If so, are any of these variants present at significantly different frequencies in Africans compared to the population groups used in the HIE studies?

## Methods

The methods utilised to answer each research question are documented in the respective Jupyter notebook in the [Analysis and Visualisation folder](https://github.com/Tuks-ICMM/HIE_Genetic_data_analysis/tree/main/Notebooks/Analysis_and_Visualisation). 

## Findings

The findings of the analyses are documented [here](https://github.com/Tuks-ICMM/HIE_Genetic_data_analysis/blob/main/Results/Report/Report.pdf). 

## Acknowledgements

Funding for my MSc project was received from the Bill and Melinda Gates Foundation and the South African Medical Research Council. 

The project was supervised by Prof Michael S Pepper, Prof Fourie Joubert and Dr Juanita Mellet from the University of Pretoria.

## Important terminology

Allele: An allele refers to one of the possible forms or variations of a specific gene. Genes are made up of DNA, and different alleles can exist within a population, representing different versions of the same gene.

DNA: DNA, short for deoxyribonucleic acid, is a molecule that contains the genetic instructions or blueprint for the development, functioning, and reproduction of all known living organisms.

Gene: A gene is a segment of DNA that contains instructions for producing a specific protein or performing a particular function within an organism.

Genetic variant: A genetic variant is a specific form or alteration of a gene or a DNA sequence. It refers to any difference or change in the DNA sequence when compared to a reference or normal sequence. 

Genetic variant frequency: The frequency of a genetic variant refers to the proportion or percentage of individuals in a population who carry a particular variant or genetic alteration.

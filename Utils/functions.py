"""This module defines functions."""

# Import modules and packages

import os
import sys

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from requests import get
from scipy.stats import fisher_exact
from statsmodels.stats.multitest import multipletests

sys.path.append(r"C:\Users\User\Desktop\Megan\MSC2\Code\Genomics_data_analysis")
import Utils.constants as constants

# Functions for retrieving variant allele ALFA count information from the NCBI API


def get_ALFA_count_info(variant_id_number: str):
    """
    Retrieve ALFA allele counts from NCBI in JSON format
    """
    url = "https://api.ncbi.nlm.nih.gov/variation/v0/refsnp/{}/frequency".format(
        variant_id_number
    )
    request = get(url)
    if request.status_code != 200:
        raise Exception(f"Request failed: {request.status_code}")
    else:
        request_json = request.json()
    return request_json


def add_all_pops(populations, project):
    """
    Translate ALFA population code data into legible population names. Code copied from https://github.com/ncbi/dbsnp/blob/master/tutorials/Variation%20Services/Jupyter_Notebook/by_rsid.ipynb.
    """
    for p in populations:
        project["pops"][p["biosample_id"]] = p
    if "subs" in p:
        add_all_pops(p["subs"], project)


def get_metadata():
    """
    Retrieve ALFA allele count metadata
    """
    url = "https://api.ncbi.nlm.nih.gov/variation/v0/metadata/frequency"
    request = get(url)
    if request.status_code != 200:
        raise Exception(f"Request failed: {request.status_code}")
    else:
        request_json = request.json()
    return request_json


# Functions for altering dataframe information


def add_prefix_dataframe_col_names(dataframe, columns_list, prefix):
    """
    Rename columns in dataframe according to a given prefix
    """
    rename_dict = {}
    for line in columns_list:
        rename_dict[line] = prefix + line

    dataframe = dataframe.rename(columns=rename_dict)
    return dataframe


# Functions for performing calculations and statistical tests


def calculate_frequency(query_allele_count: int, total_count: int):
    """
    Calculate allele frequencies from count information
    """
    frequency = query_allele_count / total_count
    return frequency


def grouped_pop_allele_counts(
    count_df: pd.DataFrame, group_name: str, reg_filters=None, subpop_filters=None
):
    """
    Calculate summed allele counts for groups of populations
    """

    if reg_filters is not None:
        grouped_count = (
            count_df[reg_filters]
            .groupby(["ID", "REF", "ALT", "POS", "VAR_NAME", "GENE"])
            .sum(numeric_only=True)
            .reset_index()
            .assign(REG=group_name)
        )

    elif subpop_filters is not None:
        grouped_count = (
            count_df[subpop_filters]
            .groupby(["ID", "REF", "ALT", "POS", "VAR_NAME", "GENE"])
            .sum(numeric_only=True)
            .reset_index()
            .assign(SUB_POP=group_name)
        )

    else:
        grouped_count = (
            count_df.groupby(["ID", "REF", "ALT", "POS", "VAR_NAME", "GENE"])
            .sum(numeric_only=True)
            .reset_index()
            .assign(REG=group_name)
        )
    return grouped_count


def fishers_test(allele_count_df: pd.DataFrame, comparitors_list: list):
    """
    Perform a Fishers Exact Test on allele count information from comparison populations
    """
    fishers_results = pd.DataFrame()
    for index, row in allele_count_df.iterrows():
        fisher_variant_combination_results = pd.DataFrame()
        for combination in comparitors_list:
            first_pop = combination[0]
            second_pop = combination[1]
            alt_1 = row["ALT_CT_{}".format(first_pop)]
            ref_1 = row["REF_CT_{}".format(first_pop)]
            alt_2 = row["ALT_CT_{}".format(second_pop)]
            ref_2 = row["REF_CT_{}".format(second_pop)]
            oddsratio, pvalue = fisher_exact([[alt_1, alt_2], [ref_1, ref_2]])
            if "#CHROM" in fisher_variant_combination_results.columns:
                fisher_variant_combination_results["#CHROM"] = [row["#CHROM"]]
            fisher_variant_combination_results["ID"] = [row["ID"]]
            fisher_variant_combination_results["VAR_NAME"] = [row["VAR_NAME"]]
            fisher_variant_combination_results["REF"] = [row["REF"]]
            fisher_variant_combination_results["ALT"] = [row["ALT"]]
            fisher_variant_combination_results["GENE"] = [row["GENE"]]
            fisher_variant_combination_results["POS"] = [row["POS"]]
            fisher_variant_combination_results[
                "PVALUE_{}_{}".format(first_pop, second_pop)
            ] = [pvalue]
            fisher_variant_combination_results[
                "OR_{}_{}".format(first_pop, second_pop)
            ] = [oddsratio]
        fishers_results = pd.concat(
            [fishers_results, fisher_variant_combination_results]
        )
    return fishers_results


def multipletest_correction_percolumn(
    data: pd.DataFrame, columns: list, alpha_threshold: float, corr_method: str
):
    """
    Performs multiple testing correction of p-values for each column of a dataframe
    """
    multipletests_results = pd.DataFrame()
    for column in columns:
        multipletests_input = data[column]
        corrected_pvalues = multipletests(
            multipletests_input, alpha=alpha_threshold, method=corr_method
        )[1]
        multipletests_results["{}_FDR".format(column)] = corrected_pvalues
    multipletests_results = pd.concat(
        [
            data.reset_index(drop=True),
            multipletests_results.reset_index(drop=True),
        ],
        axis=1,
    )
    return multipletests_results


def multipletest_correction_wholedf(
    data: pd.DataFrame, columns: list, alpha_threshold: float, stats_method: str
):
    """
    Performs multiple testing correction of p-values for entire dataframe
    """
    multipletests_results = pd.DataFrame()
    data_melt = pd.melt(
        data, id_vars=["ID", "VAR_NAME", "REF", "ALT"], value_vars=columns
    )
    multipletests_input = data_melt[["value"]].values.flatten().tolist()
    corrected_pvalues = multipletests(
        multipletests_input, alpha=alpha_threshold, method=stats_method
    )
    multipletests_results["FDR"] = pd.DataFrame(corrected_pvalues[1])
    multipletests_results = pd.concat(
        [
            data_melt.reset_index(drop=True),
            multipletests_results["FDR"].reset_index(drop=True),
        ],
        axis=1,
    )
    multipletests_results_pivot = multipletests_results.pivot(
        index=["ID", "VAR_NAME", "REF", "ALT"], columns="variable", values="FDR"
    ).reset_index()
    return multipletests_results_pivot


def group_and_count(data: pd.DataFrame, group_columns: list):
    """
    Count and group dataframe by specified columns
    """
    group_and_count_data = data.groupby(group_columns).count()
    return group_and_count_data


def calculate_ccc(y_true, y_pred):
    # Raw data
    dct = {"y_true": y_true, "y_pred": y_pred}
    df = pd.DataFrame(dct)
    # Remove NaNs
    df = df.dropna()
    # Pearson product-moment correlation coefficients
    y_true = df["y_true"]
    y_pred = df["y_pred"]
    cor = np.corrcoef(y_true, y_pred)[0][1]
    # Means
    mean_true = np.mean(y_true)
    mean_pred = np.mean(y_pred)
    # Population variances
    var_true = np.var(y_true)
    var_pred = np.var(y_pred)
    # Population standard deviations
    sd_true = np.std(y_true)
    sd_pred = np.std(y_pred)
    # Calculate CCC
    numerator = 2 * cor * sd_true * sd_pred
    denominator = var_true + var_pred + (mean_true - mean_pred) ** 2
    ccc = numerator / denominator
    return ccc


# Plotting functions


def label_point(x, y, val, ax):
    """
    Add labels to scatterplot points
    """
    a = pd.concat({"x": x, "y": y, "val": val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point["x"] - 0.007, point["y"] + 0.002, str(point["val"]))


def create_plot(
    plot_type=None,
    palette=None,
    x=None,
    y=None,
    data=None,
    xlabel=None,
    ylabel=None,
    hue=None,
    order=None,
    dodge=True,
    legend_title=None,
    legend_loc="best",
    plot_title=None,
    horizontal_stack=False,
    ax=None,
):
    """
    Create a seaborn bar or scatter plot of choice with custom parameters
    """
    if plot_type == "barplot":
        # Construct barplot
        plot_output = sns.barplot(
            x=x,
            y=y,
            data=data,
            palette=palette,
            hue=hue,
            dodge=dodge,
            order=order,
            ax=ax,
        )

    elif plot_type == "scatterplot":
        # Construct scatterplot
        plot_output = sns.scatterplot(
            x=x,
            y=y,
            data=data,
            palette=palette,
            hue=hue,
            ax=ax,
        )

    elif plot_type == "stacked_barplot":
        # Construct stacked barplot
        if horizontal_stack == False:
            plot_output = data.plot(kind="bar", stacked=True, color=palette)
        else:
            plot_output = data.plot(kind="barh", stacked=True, color=palette)

    # Define plot title
    plt.title(label=plot_title)

    # Define x and y axes labels
    plot_output.set_ylabel(ylabel)
    plot_output.set_xlabel(xlabel)

    # Modify legend

    plt.legend(
        title=legend_title,
        loc=legend_loc,
    )
    return plot_output

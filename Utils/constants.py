"""This module defines constants."""

import pandas as pd

POPULATION_CLUSTERS = ["SUPER", "SUB"]

SUBPOP_RENAME = {
    "ACB": "African Caribbean",
    "ASW": "African American",
    "GWD": "Mandinka",
    "ESN": "Esan",
    "MSL": "Mende",
    "MbutiPygmy": "Mbuti Pygmy",
    "BiakaPygmy": "Biaka Pygmy",
    "Mandenka": "Mandenka",
    "Yoruba": "Yoruba",
    "San": "San",
    "BantuSouthAfrica": "Bantu South Africa",
    "BantuKenya": "Bantu Kenya",
    "YRI": "Yoruba",
    "LWK": "Luhya",
}
REGIONAL_CLASSIFICATION = {
    "African Caribbean": "ACB",
    "African American": "ASW",
    "Mandinka": "WA",
    "Esan": "WA",
    "Mende": "WA",
    "Mbuti Pygmy": "CA",
    "Biaka Pygmy": "CA",
    "Mandenka": "WA",
    "Yoruba": "WA",
    "San": "SA",
    "Bantu South Africa": "SA",
    "Bantu Kenya": "EA",
    "Luhya": "EA",
}

SMALL_FONT = 10
MEDIUM_FONT = 12
BIGGER_FONT = 14
LARGEST_FONT = 16

VARIANT_CLASSIFICATION = {
    "3_prime_UTR_variant": "untranslated region",
    "5_prime_UTR_variant": "untranslated region",
    "downstream_gene_variant": "upstream/downstream",
    "frameshift_variant": "frameshift",
    "inframe_deletion": "deletion",
    "intron_variant": "intronic",
    "missense_variant": "missense",
    "missense_variant | splice_region_variant": "splice site",
    "splice_donor_5th_base_variant | intron_variant": "splice site",
    "splice_donor_region_variant | intron_variant": "splice site",
    "splice_polypyrimidine_tract_variant | splice_region_variant | intron_variant": "splice site",
    "splice_region_variant | 5_prime_UTR_variant": "splice site",
    "splice_region_variant | intron_variant": "splice site",
    "splice_region_variant | splice_polypyrimidine_tract_variant | intron_variant": "splice site",
    "splice_region_variant | synonymous_variant": "splice site",
    "start_lost": "start lost",
    "stop_gained": "nonsense",
    "synonymous_variant": "synonymous",
    "upstream_gene_variant": "upstream/downstream",
    "unclassified": "unclassified",
}

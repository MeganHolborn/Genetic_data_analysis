"""This module defines constants."""

# Population classifications
POPULATION_CLUSTERS = ["SUPER", "SUB"]

# Renaming ethnolinguistic groups (subpopulations)
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

# Classifying ethnolinguistic groups by African region
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

# Renaming variant consequence classifications
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

# Defining a list of variants (with rsIDs) associated with HIE in the genes of interest.
# This information was retrieved from: https://doi.org/10.1016/j.ygeno.2022.110508.
HIE_VARIANT_RSIDS = [
    "rs2067853",
    "rs1217401",
    "rs2043211",
    "rs1001179",
    "rs1800896",
    "rs1071676",
    "rs1143623",
    "rs16944",
    "rs1800795",
    "rs1801133",
    "rs1808593",
    "rs2070744",
    "rs6517135",
    "rs1799964",
]

# Defining font sizes for plotting
SMALL_FONT = 10
MEDIUM_FONT = 12
BIGGER_FONT = 14
LARGEST_FONT = 16

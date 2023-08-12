"""This module defines constants."""

import os

import pandas as pd

HOME_PATH = str(os.path.dirname(os.getcwd()))

POPULATION_CLUSTERS = ["SUPER", "SUB"]

GENE_LOCATION_DF = pd.read_csv(
    os.path.join(
        HOME_PATH,
        "Metadata",
        "locations.csv",
    )
)
GENES = GENE_LOCATION_DF.location_name

SAMPLE_INFO_DF = pd.read_csv(
    os.path.join(
        HOME_PATH,
        "Metadata",
        "samples.csv",
    )
)
SUB_POPULATIONS = SAMPLE_INFO_DF.SUB.unique()
SUBPOP_RENAME = {
    "ACB": "African Caribbean",
    "ASW": "African American",
    "GWD": "Mandinka",
    "ESN": "Esan",
    "MSL": "Mende",
    "MbutiPygmy": "Mbuti Pygmy",
    "BiakaPygmy": "Biaka Pygmy",
    "Mandenka": "Mandenka",
    "Yoruba": "HGDP Yoruba",
    "San": "San",
    "BantuSouthAfrica": "Bantu South Africa",
    "BantuKenya": "Bantu Kenya",
    "YRI": "1000G Yoruba",
    "LWK": "Luhya",
}
REGIONAL_CLASSIFICATION = {
    "ACB": "ACB",
    "ASW": "ASW",
    "GWD": "WA",
    "ESN": "WA",
    "MSL": "WA",
    "MbutiPygmy": "CA MP",
    "BiakaPygmy": "CA BP",
    "Mandenka": "WA",
    "Yoruba": "WA",
    "San": "SA KS",
    "BantuSouthAfrica": "SA B",
    "BantuKenya": "EA",
    "YRI": "WA",
    "LWK": "EA",
}  # SA = South Africa, CA = Central Africa, WA = West Africa, EA = East Africa, ACB = African Carribean in Barbados, ASW = African American, KS = Khoi-San

LD_REGIONAL_CLASSIFICATION = {
    "ACB": "ACB",
    "ASW": "ASW",
    "GWD": "WA",
    "ESN": "WA",
    "MSL": "WA",
    "MbutiPygmy": "CA",
    "BiakaPygmy": "CA",
    "Mandenka": "WA",
    "Yoruba": "WA",
    "San": "SA",
    "BantuSouthAfrica": "SA",
    "BantuKenya": "EA",
    "YRI": "WA",
    "LWK": "EA",
}
# Create a list with variant IDs of interest
NESHIE_RSIDS = [
    "rs2067853",
    "rs1217401",
    "rs2043211",
    "rs1001179",
    "rs1961495",
    "rs1411040",
    "rs34004222",
    "rs13027659",
    "rs190148408",
    "rs79704487",
    "rs1800896",
    "rs3024490",
    "rs1800871",
    "rs1554286",
    "rs1518111",
    "rs1143623",
    "rs16944",
    "rs1071676",
    "rs1800795",
    "rs2069837",
    "rs1800796",
    "rs2066992",
    "rs2069832",
    "rs2069833",
    "rs1554606",
    "rs2069845",
    "rs1801133",
    "rs4846049",
    "rs1476413",
    "rs1801131",
    "rs9651118",
    "rs1808593",
    "rs2070744",
    "rs1800779",
    "rs6517135",
    "rs1799964",
    "rs1799724",
    "rs361525",
    "rs1800629",
]

SMALL_FONT = 8
MEDIUM_FONT = 12
BIGGER_FONT = 16

VARIANT_CLASSIFICATION = {
    "3_prime_UTR_variant": "3-prime UTR",
    "5_prime_UTR_variant": "5-prime UTR",
    "downstream_gene_variant": "downstream",
    "frameshift_variant": "exonic",
    "inframe_deletion": "exonic",
    "intron_variant": "intronic",
    "missense_variant": "exonic",
    "missense_variant | splice_region_variant": "splice region",
    "splice_donor_5th_base_variant | intron_variant": "splice donor",
    "splice_donor_region_variant | intron_variant": "splice donor",
    "splice_polypyrimidine_tract_variant | splice_region_variant | intron_variant": "splice region",
    "splice_region_variant | 5_prime_UTR_variant": "splice region",
    "splice_region_variant | intron_variant": "splice region",
    "splice_region_variant | splice_polypyrimidine_tract_variant | intron_variant": "splice region",
    "splice_region_variant | synonymous_variant": "splice region",
    "start_lost": "exonic",
    "stop_gained": "exonic",
    "synonymous_variant": "exonic",
    "upstream_gene_variant": "upstream",
    "unclassified": "unclassified",
}

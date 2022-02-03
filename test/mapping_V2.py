# -*- coding: utf-8 -*-
import pandas as pd

import json
from types import SimpleNamespace
import sys
from pathlib import Path
import json

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

ENA_schema = {
    "$schema": "http://json-schema.org/draft/2019-09/schema#",
    "required": [
        "sample_name",
        "collecting_institution",
        "geographic_location_(country_and/or_sea)",
        "isolate",
        "host_scientific_name",
        "host_common_name",
        "host_health_state",
        "host_sex",
        "host_subject_id",
        "instrument_model",
        "file_name",
        "sample_name",
        "tax_id",
        "scientific_name",
        "common_name",
        "sample_description",
        "library_source",
        "library_selection",
        "library_strategy",
        "library_layout"
    ],
    "type": "object",
    "properties": {
        "sample_name": {
            "examples": ["prov_rona_99"],
             "ontology": "GENEPIO_0000079",
             "type": "string",
             "description": "The user-defined name for the sample.",
             "clasification":"Database Identifiers",
             "genepio_label":"sequencing run sample identifier",

        },
        "collecting_institution": {
            "examples": ["Public Health Agency of Canada"],
             "ontology": "GENEPIO_0001651",
             "type": "string",
             "description": "The name of the agency that collected the original sample.",
             "genepio_label":"INSDC institution code",

        },
        "collection_date": {
          "examples": ["19/03/2020"],
          "ontology": "GENEPIO:0001174",
          "type": "string",
          "description": "The date on which the sample was collected. ",
          "format": "date",
          "genepio_label":"",

        },
        "receipt_date": {
          "examples": ["20/03/2020"],
          "ontology": "GENEPIO:0001179",
          "type": "string",
          "description": "The date on which the sample was received.",
          "format": "date",
          "genepio_label":"",

        },
        "geographic_location_(country_and/or_sea)": {
          "Enums": [
            "Afghanistan [GAZ:00006882]",
            "Albania [GAZ:00002953]",
            "Algeria [GAZ:00000563]",
            "American Samoa [GAZ:00003957]",
            "Andorra [GAZ:00002948]",
            "Angola [GAZ:00001095]",
            "Anguilla [GAZ:00009159]",
            "Antarctica [GAZ:00000462]",
            "Antigua and Barbuda [GAZ:00006883]",
            "Argentina [GAZ:00002928]",
            "Armenia [GAZ:00004094]",
            "Aruba [GAZ:00004025]",
            "Ashmore and Cartier Islands [GAZ:00005901]",
            "Australia [GAZ:00000463]",
            "Austria [GAZ:00002942]",
            "Azerbaijan [GAZ:00004941]",
            "Bahamas [GAZ:00002733]",
            "Bahrain [GAZ:00005281]",
            "Baker Island [GAZ:00007117]",
            "Bangladesh [GAZ:00003750]",
            "Barbados [GAZ:00001251]",
            "Bassas da India [GAZ:00005810]",
            "Belarus [GAZ:00006886]",
            "Belgium [GAZ:00002938]",
            "Belize [GAZ:00002934]",
            "Benin [GAZ:00000904]",
            "Bermuda [GAZ:00001264]",
            "Bhutan [GAZ:00003920]",
            "Bolivia [GAZ:00002511]",
            "Borneo [GAZ:00025355]",
            "Bosnia and Herzegovina [GAZ:00006887]",
            "Botswana [GAZ:00001097]",
            "Bouvet Island [GAZ:00001453]",
            "Brazil [GAZ:00002828]",
            "British Virgin Islands [GAZ:00003961]",
            "Brunei [GAZ:00003901]",
            "Bulgaria [GAZ:00002950]",
            "Burkina Faso [GAZ:00000905]",
            "Burundi [GAZ:00001090]",
            "Cambodia [GAZ:00006888]",
            "Cameroon [GAZ:00001093]",
            "Canada [GAZ:00002560]",
            "Cape Verde [GAZ:00001227]",
            "Cayman Islands [GAZ:00003986]",
            "Central African Republic [GAZ:00001089]",
            "Chad [GAZ:00000586]",
            "Chile [GAZ:00002825]",
            "China [GAZ:00002845]",
            "Christmas Island [GAZ:00005915]",
            "Clipperton Island [GAZ:00005838]",
            "Cocos Islands [GAZ:00009721]",
            "Colombia [GAZ:00002929]",
            "Comoros [GAZ:00005820]",
            "Cook Islands [GAZ:00053798]",
            "Coral Sea Islands [GAZ:00005917]",
            "Costa Rica [GAZ:00002901]",
            "Cote d'Ivoire [GAZ:00000906]",
            "Croatia [GAZ:00002719]",
            "Cuba [GAZ:00003762]",
            "Curacao [GAZ:00012582]",
            "Cyprus [GAZ:00004006]",
            "Czech Republic [GAZ:00002954]",
            "Democratic Republic of the Congo [GAZ:00001086]",
            "Denmark [GAZ:00005852]",
            "Djibouti [GAZ:00000582]",
            "Dominica [GAZ:00006890]",
            "Dominican Republic [GAZ:00003952]",
            "Ecuador [GAZ:00002912]",
            "Egypt [GAZ:00003934]",
            "El Salvador [GAZ:00002935]",
            "Equatorial Guinea [GAZ:00001091]",
            "Eritrea [GAZ:00000581]",
            "Estonia [GAZ:00002959]",
            "Eswatini [GAZ:00001099]",
            "Ethiopia [GAZ:00000567]",
            "Europa Island [GAZ:00005811]",
            "Falkland Islands (Islas Malvinas) [GAZ:00001412]",
            "Faroe Islands [GAZ:00059206]",
            "Fiji [GAZ:00006891]",
            "Finland [GAZ:00002937]",
            "France [GAZ:00003940]",
            "French Guiana [GAZ:00002516]",
            "French Polynesia [GAZ:00002918]",
            "French Southern and Antarctic Lands [GAZ:00003753]",
            "Gabon [GAZ:00001092]",
            "Gambia [GAZ:00000907]",
            "Gaza Strip [GAZ:00009571]",
            "Georgia [GAZ:00004942]",
            "Germany [GAZ:00002646]",
            "Ghana [GAZ:00000908]",
            "Gibraltar [GAZ:00003987]",
            "Glorioso Islands [GAZ:00005808]",
            "Greece [GAZ:00002945]",
            "Greenland [GAZ:00001507]",
            "Grenada [GAZ:02000573]",
            "Guadeloupe [GAZ:00067142]",
            "Guam [GAZ:00003706]",
            "Guatemala [GAZ:00002936]",
            "Guernsey [GAZ:00001550]",
            "Guinea [GAZ:00000909]",
            "Guinea-Bissau [GAZ:00000910]",
            "Guyana [GAZ:00002522]",
            "Haiti [GAZ:00003953]",
            "Heard Island and McDonald Islands [GAZ:00009718]",
            "Honduras [GAZ:00002894]",
            "Hong Kong [GAZ:00003203]",
            "Howland Island [GAZ:00007120]",
            "Hungary [GAZ:00002952]",
            "Iceland [GAZ:00000843]",
            "India [GAZ:00002839]",
            "Indonesia [GAZ:00003727]",
            "Iran [GAZ:00004474]",
            "Iraq [GAZ:00004483]",
            "Ireland [GAZ:00002943]",
            "Isle of Man [GAZ:00052477]",
            "Israel [GAZ:00002476]",
            "Italy [GAZ:00002650]",
            "Jamaica [GAZ:00003781]",
            "Jan Mayen [GAZ:00005853]",
            "Japan [GAZ:00002747]",
            "Jarvis Island [GAZ:00007118]",
            "Jersey [GAZ:00001551]",
            "Johnston Atoll [GAZ:00007114]",
            "Jordan [GAZ:00002473]",
            "Juan de Nova Island [GAZ:00005809]",
            "Kazakhstan [GAZ:00004999]",
            "Kenya [GAZ:00001101]",
            "Kerguelen Archipelago [GAZ:00005682]",
            "Kingman Reef [GAZ:00007116]",
            "Kiribati [GAZ:00006894]",
            "Kosovo [GAZ:00011337]",
            "Kuwait [GAZ:00005285]",
            "Kyrgyzstan [GAZ:00006893]",
            "Laos [GAZ:00006889]",
            "Latvia [GAZ:00002958]",
            "Lebanon [GAZ:00002478]",
            "Lesotho [GAZ:00001098]",
            "Liberia [GAZ:00000911]",
            "Libya [GAZ:00000566]",
            "Liechtenstein [GAZ:00003858]",
            "Line Islands [GAZ:00007144]",
            "Lithuania [GAZ:00002960]",
            "Luxembourg [GAZ:00002947]",
            "Macau [GAZ:00003202]",
            "Madagascar [GAZ:00001108]",
            "Malawi [GAZ:00001105]",
            "Malaysia [GAZ:00003902]",
            "Maldives [GAZ:00006924]",
            "Mali [GAZ:00000584]",
            "Malta [GAZ:00004017]",
            "Marshall Islands [GAZ:00007161]",
            "Martinique [GAZ:00067143]",
            "Mauritania [GAZ:00000583]",
            "Mauritius [GAZ:00003745]",
            "Mayotte [GAZ:00003943]",
            "Mexico [GAZ:00002852]",
            "Micronesia [GAZ:00005862]",
            "Midway Islands [GAZ:00007112]",
            "Moldova [GAZ:00003897]",
            "Monaco [GAZ:00003857]",
            "Mongolia [GAZ:00008744]",
            "Montenegro [GAZ:00006898]",
            "Montserrat [GAZ:00003988]",
            "Morocco [GAZ:00000565]",
            "Mozambique [GAZ:00001100]",
            "Myanmar [GAZ:00006899]",
            "Namibia [GAZ:00001096]",
            "Nauru [GAZ:00006900]",
            "Navassa Island [GAZ:00007119]",
            "Nepal [GAZ:00004399]",
            "Netherlands [GAZ:00002946]",
            "New Caledonia [GAZ:00005206]",
            "New Zealand [GAZ:00000469]",
            "Nicaragua [GAZ:00002978]",
            "Niger [GAZ:00000585]",
            "Nigeria [GAZ:00000912]",
            "Niue [GAZ:00006902]",
            "Norfolk Island [GAZ:00005908]",
            "North Korea [GAZ:00002801]",
            "North Macedonia [GAZ:00006895]",
            "North Sea [GAZ:00002284]",
            "Northern Mariana Islands [GAZ:00003958]",
            "Norway [GAZ:00002699]",
            "Oman [GAZ:00005283]",
            "Pakistan [GAZ:00005246]",
            "Palau [GAZ:00006905]",
            "Panama [GAZ:00002892]",
            "Papua New Guinea [GAZ:00003922]",
            "Paracel Islands [GAZ:00010832]",
            "Paraguay [GAZ:00002933]",
            "Peru [GAZ:00002932]",
            "Philippines [GAZ:00004525]",
            "Pitcairn Islands [GAZ:00005867]",
            "Poland [GAZ:00002939]",
            "Portugal [GAZ:00004126]",
            "Puerto Rico [GAZ:00006935]",
            "Qatar [GAZ:00005286]",
            "Republic of the Congo [GAZ:00001088]",
            "Reunion [GAZ:00003945]",
            "Romania [GAZ:00002951]",
            "Ross Sea [GAZ:00023304]",
            "Russia [GAZ:00002721]",
            "Rwanda [GAZ:00001087]",
            "Saint Helena [GAZ:00000849]",
            "Saint Kitts and Nevis [GAZ:00006906]",
            "Saint Lucia [GAZ:00006909]",
            "Saint Pierre and Miquelon [GAZ:00003942]",
            "Saint Martin [GAZ:00005841]",
            "Saint Vincent and the Grenadines [GAZ:02000565]",
            "Samoa [GAZ:00006910]",
            "San Marino [GAZ:00003102]",
            "Sao Tome and Principe [GAZ:00006927]",
            "Saudi Arabia [GAZ:00005279]",
            "Senegal [GAZ:00000913]",
            "Serbia [GAZ:00002957]",
            "Seychelles [GAZ:00006922]",
            "Sierra Leone [GAZ:00000914]",
            "Singapore [GAZ:00003923]",
            "Sint Maarten [GAZ:00012579]",
            "Slovakia [GAZ:00002956]",
            "Slovenia [GAZ:00002955]",
            "Solomon Islands [GAZ:00005275]",
            "Somalia [GAZ:00001104]",
            "South Africa [GAZ:00001094]",
            "South Georgia and the South Sandwich Islands [GAZ:00003990]",
            "South Korea [GAZ:00002802]",
            "South Sudan [GAZ:00233439]",
            "Spain [GAZ:00003936]",
            "Spratly Islands [GAZ:00010831]",
            "Sri Lanka [GAZ:00003924]",
            "State of Palestine [GAZ:00002475]",
            "Sudan [GAZ:00000560]",
            "Suriname [GAZ:00002525]",
            "Svalbard [GAZ:00005396]",
            "Swaziland [GAZ:00001099]",
            "Sweden [GAZ:00002729]",
            "Switzerland [GAZ:00002941]",
            "Syria [GAZ:00002474]",
            "Taiwan [GAZ:00005341]",
            "Tajikistan [GAZ:00006912]",
            "Tanzania [GAZ:00001103]",
            "Thailand [GAZ:00003744]",
            "Timor-Leste [GAZ:00006913]",
            "Togo [GAZ:00000915]",
            "Tokelau [GAZ:00260188]",
            "Tonga [GAZ:00006916]",
            "Trinidad and Tobago [GAZ:00003767]",
            "Tromelin Island [GAZ:00005812]",
            "Tunisia [GAZ:00000562]",
            "Turkey [GAZ:00000558]",
            "Turkmenistan [GAZ:00005018]",
            "Turks and Caicos Islands [GAZ:00003955]",
            "Tuvalu [GAZ:00009715]",
            "USA [GAZ:00002459]",
            "Uganda [GAZ:00001102]",
            "Ukraine [GAZ:00002724]",
            "United Arab Emirates [GAZ:00005282]",
            "United Kingdom [GAZ:00002637]",
            "Uruguay [GAZ:00002930]",
            "Uzbekistan [GAZ:00004979]",
            "Vanuatu [GAZ:00006918]",
            "Venezuela [GAZ:00002931]",
            "Viet Nam [GAZ:00003756]",
            "Virgin Islands [GAZ:00003959]",
            "Wake Island [GAZ:00007111]",
            "Wallis and Futuna [GAZ:00007191]",
            "West Bank [GAZ:00009572]",
            "Western Sahara [GAZ:00000564]",
            "Yemen [GAZ:00005284]",
            "Zambia [GAZ:00001107]",
            "Zimbabwe [GAZ:00001106]",
            "Not Applicable [GENEPIO:0001619]",
            "Not Collected [GENEPIO:0001620]",
            "Not Provided [GENEPIO:0001668]",
            "Missing [GENEPIO:0001618]",
            "Restricted Access [GENEPIO:0001810]"
          ],
          "ontology": "GENEPIO_0000118",
          "type": "string",
          "description": "The country of origin of the sample.",
          "examples": ["South Africa [GAZ:00001094]"],
          "genepio_label":"specimen collection location - country",

        },
        "geographic location (region and locality)": {
          "ontology": "GENEPIO:0100280",
          "type": "string",
          "description": "The county/region of origin of the sample.",
          "examples": ["Derbyshire"],
          "genepio_label":"",

        },
        "geographic location (latitude)": {
          "ontology": "OBI:0001620",
          "type": "string",
          "description": "The latitude coordinates of the geographical location of sample collection.",
          "examples": ["38.98 N"],
          "genepio_label":"",

        },
        "geographic location (longitude)": {
          "ontology": "OBI:0001621",
          "type": "string",
          "description": "The longitude coordinates of the geographical location of sample collection.",
          "examples": ["77.11 W"],
          "genepio_label":"",

        },
        "scientific_name": {
          "Enums": [
            "Coronaviridae [NCBITaxon:11118]",
            "Severe acute respiratory syndrome coronavirus 2 [NCBITaxon:2697049]",
            "Not Applicable [GENEPIO:0001619]",
            "Not Collected [GENEPIO:0001620]",
            "Not Provided [GENEPIO:0001668]",
            "Missing [GENEPIO:0001618]",
            "Restricted Access [GENEPIO:0001810]"
          ],
          "ontology": "GENEPIO:0001191",
          "type": "string",
          "description": "Taxonomic name of the organism.",
          "examples": ["Severe acute respiratory syndrome coronavirus 2 "],
          "genepio_label":"",

        },
        "isolate": {
          "ontology": "GENEPIO:0001644",
          "type": "string",
          "description": "Identifier of the specific isolate.",
          "examples": ["SARS-CoV-2/human/USA/CA-CDPH-001/2020"],
          "genepio_label":"isolate identifier",

        },
        "purpose_sampling": {
            "examples": ["Diagnostic testing"],
             "ontology":  "NCIT_C146997",
             "type": "string",
             "description": "The reason that the sample was collected.",
             "clasification":"Sample collection and processing"
        },
        "isolation source host-associated": {
          "Enums": [
            "Blood [UBERON:0000178]",
            "Fluid [UBERON:0006314]",
            "Fluid (Cerebrospinal (CSF)) [UBERON:0001359]",
            "Fluid (Pericardial) [UBERON:0002409]",
            "Fluid (Pleural) [UBERON:0001087]",
            "Fluid (Vaginal) [UBERON:0036243]",
            "Fluid (Amniotic) [UBERON:0000173]",
            "Saliva [UBERON:0001836]",
            "Tissue [UBERON:0000479]",
            "Not Applicable [GENEPIO:0001619]",
            "Not Collected [GENEPIO:0001620]",
            "Not Provided [GENEPIO:0001668]",
            "Missing [GENEPIO:0001618]",
            "Restricted Access [GENEPIO:0001810]"
          ],
          "ontology": "GENEPIO:0001211",
          "type": "string",
          "description": "A substance obtained from an anatomical part of an organism e.g. tissue, blood.",
          "examples": ["Blood [UBERON:0000178]"],
          "genepio_label":"",

        },
        "host common name": {
          "Enums": [
            "Human [NCBITaxon:9606]",
            "Bat [NCBITaxon:9397]",
            "Cat [NCBITaxon:9685]",
            "Chicken [NCBITaxon:9031]",
            "Civet [NCBITaxon:9673]",
            "Cow [NCBITaxon:9913]",
            "Dog [NCBITaxon:9615]",
            "Lion [NCBITaxon:9689]",
            "Mink [NCBITaxon:452646]",
            "Pangolin [NCBITaxon:9973]",
            "Pig [NCBITaxon:9825]",
            "Pigeon [NCBITaxon:8930]",
            "Tiger [NCBITaxon:9694]",
            "Not Applicable [GENEPIO:0001619]",
            "Not Collected [GENEPIO:0001620]",
            "Not Provided [GENEPIO:0001668]",
            "Missing [GENEPIO:0001618]",
            "Restricted Access [GENEPIO:0001810]"
          ],
          "ontology": "GENEPIO_0001724",
          "type": "string",
          "description": "The commonly used name of the host.",
          "examples": ["Human [NCBITaxon:9606]"],
          "genepio_label":"subject organism common name",

        },
        "host scientific name": {
          "Enums": [
            "Bos taurus [NCBITaxon:9913]",
            "Canis lupus familiaris [NCBITaxon:9615]",
            "Chiroptera [NCBITaxon:9397]",
            "Columbidae [NCBITaxon:8930]",
            "Felis catus [NCBITaxon:9685]",
            "Gallus gallus [NCBITaxon:9031]",
            "Homo sapiens [NCBITaxon:9606]",
            "Manis [NCBITaxon:9973]",
            "Manis javanica [NCBITaxon:9974]",
            "Neovison vison [NCBITaxon:452646]",
            "Panthera leo [NCBITaxon:9689]",
            "Panthera tigris [NCBITaxon:9694]",
            "Rhinolophidae [NCBITaxon:58055]",
            "Rhinolophus affinis [NCBITaxon:59477]",
            "Sus scrofa domesticus [NCBITaxon:9825]",
            "Viverridae [NCBITaxon:9673]",
            "Not Applicable [GENEPIO:0001619]",
            "Not Collected [GENEPIO:0001620]",
            "Not Provided [GENEPIO:0001668]",
            "Missing [GENEPIO:0001618]",
            "Restricted Access [GENEPIO:0001810]"
          ],
          "ontology": "GENEPIO_0001567",
          "type": "string",
          "description": "The taxonomic, or scientific name of the host.",
          "examples": ["Homo sapiens [NCBITaxon:9606]"],
          "genepio_label":"subject organism (host) taxonomic species",

        },
        "host_health_state": {
          "examples": [""],
           "ontology": "GENEPIO:0001156",
           "type": "string",
           "description": "Health status of the host at the time of sample collection.",
           "clasification":"Host information",
           "genepio_label":"",

         },
         "host_age": {
            "examples": ["e.g. 65 or 7 months, or unknown. Caution: the host age may be considered public health identifiable information. Consult the data steward before sharing. If the information is unknown or can not be shared, put unknown"],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "Patient age",
             "clasification":"Host information"
        },

         "host_sex": {
           "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "Gender or sex of the host.",
            "clasification":"Host information",
            "genepio_label":"",

          },
          "host_subject_id": {
            "examples": ["e.g. #131"],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "a unique identifier by which each subject can be referred to, de-identified.",
             "clasification":"Host information",
             "genepio_label":"",

           },
         "type exposure": {
          "examples": ["Date, Location e.g. type of gathering, Family cluster, etc."],
           "ontology": "GENEPIO:0001156",
           "type": "string",
           "description": "If the information is unknown or can not be shared, leave blank.",
           "clasification":"Host information",
           "genepio_label":"",

         },
         "subject exposure duration": {
            "examples": ["e.g. Patient infected while traveling in …."],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "If the information is unknown or can not be shared, leave blank.",
             "clasification":"Host information",
             "genepio_label":"",

        },
        "instrument_model": {
          "Enums": ["454 Genome Sequencer [GENEPIO:0001937]",
            "454 Genome Sequence 20 [OBI:0000689]",
            "454 Genome Sequencer FLX [OBI:0000702]",
            "454 Genome Sequencer FLX Titanium [GENEPIO:0001936]",
            "454 Genome Sequencer Junior [GENEPIO:0001938]",
            "AB SOLiD System [OBI:0000696]",
            "SOLiD 3 Plus System [OBI:0002007]",
            "SOLiD 4 [OBI:0002024]",
            "SOLiD 4hq System [GENPIO:0001928]",
            "SOLiD 5500 [GENPIO:0001929]",
            "SOLiD 5500xl [GENPIO:0001930]",
            "SOLiD PI System [GENPIO:0001931]",
            "SOLiD System 2.0 [GENPIO:0001932]",
            "SOLiD System 3.0 [GENPIO:0001933]",
            "HeliScope Single Molecule Sequencer [OBI:0000717]",
            "Illumina Genome Analyzer II [OBI:0000703]",
            "Genome Analyzer IIe [OBI:0002027]",
            "Genome Analyzer IIx [OBI:0002000]",
            "Illumina HiSeq Sequencer [GENPIO:0001939]",
            "Illumina HiSeq 1000 [OBI:0002022]",
            "Illumina HiSeq 2000 [OBI:0002001]",
            "Illumina HiSeq 2500 [OBI:0002002]",
            "Illumina HiSeq 3000 [OBI:0002048]",
            "Illumina HiSeq 4000 [OBI:0002049]",
            "Ion Torrent PGM [GENPIO:0001935]",
            "MiSeq [OBI:0002003]",
            "NextSeq 500 [OBI:0002021]",
            "PacBio RS II [OBI:0002012]",
          ],
          "ontology": "GENEPIO_0001921",
          "type": "string",
          "description": "The model of the sequencing instrument used.",
          "examples": ["Oxford Nanopore MinION "],
          "genepio_label":"sequencing instrument model",

        },
        "instrument_platform ": {
          "examples": ["MinIon"],
           "ontology": "GENEPIO:0001156",
           "type": "string",
           "description": "The model of the sequencing instrument used.",
           "genepio_label":"",

      },
      "file_name": {
            "examples": ["ABC123_S1_L001_R1_001.fastq.gz"],
            "ontology": "GENEPIO:0001476",
            "type": "string",
            "description": "The user-specified filename of the r1 FASTQ file.",
            "clasification":"Bioinformatics and QC metrics",
            "genepio_label":"",

      },
      "tax_id": {
            "examples": ["probably 2697049 in all cases"],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "The NCBITaxon identifier for the organism being sequenced.",
             "clasification":"Sample collection and processing",
             "genepio_label":"",

      },
      "scientific_name": {
            "examples": [""],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "The taxonomic name of the organism.",
             "clasification":"Sample collection and processing",
             "genepio_label":"",

      },
      "common_name": {
            "examples": [""],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "The common name of the organism.",
             "clasification":"Sample collection and processing",
             "genepio_label":"",

      },
      "sample_description": {
            "examples": [""],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "Free text description of the sample.",
             "clasification":"Sample collection and processing",
             "genepio_label":"",

      },
      "sample_storage_conditions": {
            "examples": ["24 degrees celsius"],
             "ontology": "NCIT_C115535",
             "type": "string",
             "description": "The name and version of a particular protocol used for sampling.",
             "clasification":"Sample collection and processing"
      },
      "library_source": {
        "Enums": ["5-methycytidine antibody method [GENPIO:0001941]",
          "CAGE method [GENPIO:0001942]",
          "CF-H method [GENPIO:0001943]",
          "CF-M method ]GENPIO:0001944]",
          "CF-S method [GENPIO:0001945]",
          "CF-T method [GENPIO:0001946]",
          "ChIP method ]GENPIO:0001947]",
          "DNAse method [GENPIO:0001948]",
          "HMPR method [GENPIO:0001949]",
          "Hybrid Selection Method [GENPIO:0001950]",
          "MBD2 protein methyl-CpG binding domain method [GENPIO:0001951]",
          "MF method [GENPIO:0001952]",
          "MNase method [GENPIO:0001953]",
          "MSLL method [GENPIO:0001954]",
          "PCR method [GENPIO:0001955]",
          "RACE method [GENPIO:0001956]",
          "RANDOM PCR method [GENPIO:0001957]",
          "RANDOM method [GENPIO:0001958]",
          "RT-PCR method [GENPIO:0001959]",
          "Reduced Representation method [GENPIO:0001960]",
          "Resctriction Digest method [GENPIO:0001961]",
          "cDNA method [GENPIO:0001962]",
          "other library method [GENPIO:0001964]",
          "size fractionation method [GENPIO:0001963]",
        ],
            "examples": ["METAGENOMIC"],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "Molecule type used to make the library.",
             "clasification":"Sequencing",
        },
        "library_selection": {
            "examples": ["RANDOM PCR"],
             "ontology": "GENPIO_0001940",
             "type": "string",
             "description": "Library capture method.",
             "clasification":"Sequencing",
             "genepio_label":"library selection",

        },
        "library_strategy": {
          "Enums": ["Bisultife-Seq strategy [GENPIO:0001975]",
            "CTS strategy [GENPIO:0001978]",
            "ChIP-Seq strategy [GENPIO:0001979]",
            "DNase-Hypersensitivity strategy [GENPIO:0001980]",
            "EST strategy [GENPIO:0001981]",
            "FL-cDNA strategy [GENPIO:0001983]",
            "MB-Seq strategy [GENPIO:0001984]",
            "MNase-Seq strategy [GENPIO:0001985]",
            "MRE-Seq strategy [GENPIO:0001986]",
            "MeDIP-Seq strategy [GENPIO:0001987]",
            "RNA-Seq strategy [GENPIO:0001990]",
            "WCS strategy [GENPIO:0001991]",
            "WGS strategy [GENPIO:0001992]",
            "WXS strategy [GENPIO:0001993]",
            "amplicon strategy [GENPIO:0001974]",
            "clone end strategy [GENPIO:0001976]",
            "clone strategy [GENPIO:0001977]",
            "finishing strategy [GENPIO:0001982]",
            "other library strategy [GENPIO:0001988]",
            "pool clone strategy [GENPIO:0001989]",
          ],
            "examples": ["WGS"],
             "ontology": "GENPIO_0001973",
             "type": "string",
             "description": "Overall sequencing strategy or approach.",
             "clasification":"Sequencing",
             "genepio_label":"library strategy",

        },
        "library_layout": {
            "examples": ["PAIRED"],
             "ontology":"GENPIO_0000001",
             "type": "string",
             "description": "Single or paired.",
             "clasification":"Sequencing",
             "genepio_label":"library library_layout",

        },
        "library_name": {
            "examples": ["e.g P17157_1007"],
             "ontology": "GENEPIO_0001995",
             "type": "string",
             "description": "The submitter's name for this library.",
             "clasification":"Sequencing",
             "genepio_label":"Library Name",
        },
        "nominal_length ": {
            "examples": ["350"],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "",
             "clasification":"Sequencing",
             "genepio_label":"",

        },
        "analysis_accession": {
          "examples": [""],
          "ontology": "GENEPIO:0001156",
          "type": "string",
          "description": "",
          "clasification":"Submission ENA",
          "genepio_label":"",

        },
        "study_accession": {
          "examples": ["e.g PRJEB39632"],
          "ontology": "GENEPIO:0001156",
          "type": "string",
          "description": "",
          "clasification":"Submission ENA",
          "genepio_label":"",

      },
      "secondary_study_accession": {
          "examples": ["e.g ERP123173"],
          "ontology": "GENEPIO:0001156",
          "type": "string",
          "description": "",
          "clasification":"Submission ENA",
          "genepio_label":"",

      },
      "sample_accession": {
          "examples": ["e.g SAMEA7098096"],
          "ontology": "GENEPIO:0001156",
          "type": "string",
          "description": "",
          "clasification":"Submission ENA",
          "genepio_label":"",

      },
      "secondary_sample_accession": {
          "examples": ["e.g ERS4858671"],
          "ontology": "GENEPIO:0001156",
          "type": "string",
          "description": "",
          "clasification":"Submission ENA",
          "genepio_label":"",

      },
      "experiment_accession": {
            "examples": ["e.g ERX4331406"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "run_accession": {
            "examples": ["e.g ERX4331406"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "submission_accession": {
            "examples": ["e.g ERA2794974"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "read_count": {
            "examples": ["e.g 837055"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "base_count": {
            "examples": ["e.g 503907110"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "center_name": {
            "examples": [" KAROLINSKA INSITUTET"],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "The name of the institution",
             "clasification":"Sample collection and processing",
             "genepio_label":"",

        },
        "first_public": {
          "examples": ["e.g 2020-08-07"],
          "ontology": "GENEPIO:0001156",
          "type": "string",
          "description": "",
          "clasification":"Submission ENA",
          "genepio_label":"",

      },
      "last_updated": {
          "examples": ["e.g 2020-07-29"],
          "ontology": "GENEPIO:0001156",
          "type": "string",
          "description": "",
          "clasification":"Submission ENA",
          "format":"date",
          "genepio_label":"",

      },
      "experiment_title": {
          "examples": ["e.g Illumina MiSeq paired end sequencing"],
          "ontology": "GENEPIO:0001156",
          "type": "string",
          "description": "",
          "clasification":"Submission ENA",
          "genepio_label":"",

      },
      "study_title": {
            "examples": ["e.g SARS-CoV-2 genomes from late April in Stockholm"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "study_alias": {
            "examples": ["e.g Sweden"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "experiment_alias": {
            "examples": ["e.g ena-STUDY-KAROLINSKA INSITUTET-29-07-2020-14:18:07:925-2092"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "run_alias": {
            "examples": ["e.g ena-EXPERIMENT-KAROLINSKA INSITUTET-29-07-2020-14:50:07:151-1"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "fastq_bytes": {
            "examples": ["e.g ena-RUN-KAROLINSKA INSITUTET-29-07-2020-14:50:07:151-1"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "fastq_md5": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "fastq_ftp": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "fastq_aspera": {
            "examples": ["e.g ftp.sra.ebi.ac.uk/vol1/fastq/ERR438/005/ERR4387385/ERR4387385_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR438/005/ERR4387385/ERR4387385_2.fastq.gz"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "fastq_galaxy": {
            "examples": ["e.g fasp.sra.ebi.ac.uk:/vol1/fastq/ERR438/005/ERR4387385/ERR4387385_1.fastq.gz;fasp.sra.ebi.ac.uk:/vol1/fastq/ERR438/005/ERR4387385/ERR4387385_2.fastq.gz"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "submitted_bytes": {
            "examples": ["e.g ftp.sra.ebi.ac.uk/vol1/fastq/ERR438/005/ERR4387385/ERR4387385_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR438/005/ERR4387385/ERR4387385_2.fastq.gz"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "submitted_md5": {
            "examples": ["e.g 139853010;166270048"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "submitted_ftp": {
            "examples": ["e.g d726a9abc918e2b43bd68b24c7d01b3a;f01eba1b2bad974bdf61b81b1ae8ac2a"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "submitted_aspera": {
            "examples": ["e.g ftp.sra.ebi.ac.uk/vol1/run/ERR438/ERR4387385/P17157_1007_S7_L001_R1_001.fastq.gz;ftp.sra.ebi.ac.uk/vol1/run/ERR438/ERR4387385/P17157_1007_S7_L001_R2_001.fastq.gz"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "submitted_galaxy": {
            "examples": ["e.g fasp.sra.ebi.ac.uk:/vol1/run/ERR438/ERR4387385/P17157_1007_S7_L001_R1_001.fastq.gz;fasp.sra.ebi.ac.uk:/vol1/run/ERR438/ERR4387385/P17157_1007_S7_L001_R2_001.fastq.gz"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "submitted_format": {
            "examples": ["e.g  ftp.sra.ebi.ac.uk/vol1/run/ERR438/ERR4387385/P17157_1007_S7_L001_R1_001.fastq.gz;ftp.sra.ebi.ac.uk/vol1/run/ERR438/ERR4387385/P17157_1007_S7_L001_R2_001.fastq.gz"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "sra_bytes": {
            "examples": ["e.g FASTQ;FASTQ"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "sra_md5": {
            "examples": ["e.g 260236789"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "sra_ftp": {
            "examples": ["e.g 2cf0d467d6dc4ae0a5473774d54c059c"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "sra_aspera": {
            "examples": ["e.g ftp.sra.ebi.ac.uk/vol1/err/ERR438/005/ERR4387385"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "sra_galaxy": {
            "examples": ["e.g fasp.sra.ebi.ac.uk:/vol1/err/ERR438/005/ERR4387385"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "broker_name": {
            "examples": ["P17157_1007"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "nominal_sdev": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },
        "first_created": {
            "examples": ["e.g 2020-08-07"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "genepio_label":"",

        },

    }
}


phage_schema= {
    "$schema": "http://json-schema.org/draft/2020-12/schema",
    "required": [
        "sample_name",
        "collecting_institution",
        "submitting_institution",
        "sample_collection_date",
        "geo_loc_country",
        "geo_loc_state",
        "organism",
        "isolate",
        "host_scientific_name",
        "host_disease",
        "sequencing_instrument_model",
        "sequencing_instrument_platform",
        "consensus_sequence_software_name",
        "consensus_sequence_software_version"
    ],
    "type": "object",
    "properties": {
        "sample_name": {
            "examples": ["prov_rona_99"],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "The user-defined name for the sample.",
             "clasification":"Database Identifiers"
        },
        "collecting_institution": {
            "examples": ["Public Health Agency of Canada"],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "The name of the agency that collected the original sample."
        },
        "submitting_institution": {
            "examples": ["Centers for Disease Control and Prevention"],
             "ontology": "GENEPIO:0001159",
             "type": "string",
             "description": "The name of the agency that generated the sequence."
        },
        "sample_collection_date": {
            "examples": ["3/19/2020"],
             "ontology": "GENEPIO:0001174",
             "type": "string",
             "description": "The date on which the sample was collected.",
             "format":"date"
        },
        "geo_loc_country": {
          "Enums": [
            "Afghanistan [GAZ:00006882]",
            "Albania [GAZ:00002953]",
            "Algeria [GAZ:00000563]",
            "American Samoa [GAZ:00003957]",
            "Andorra [GAZ:00002948]",
            "Angola [GAZ:00001095]",
            "Anguilla [GAZ:00009159]",
            "Antarctica [GAZ:00000462]",
            "Antigua and Barbuda [GAZ:00006883]",
            "Argentina [GAZ:00002928]",
            "Armenia [GAZ:00004094]",
            "Aruba [GAZ:00004025]",
            "Ashmore and Cartier Islands [GAZ:00005901]",
            "Australia [GAZ:00000463]",
            "Austria [GAZ:00002942]",
            "Azerbaijan [GAZ:00004941]",
            "Bahamas [GAZ:00002733]",
            "Bahrain [GAZ:00005281]",
            "Baker Island [GAZ:00007117]",
            "Bangladesh [GAZ:00003750]",
            "Barbados [GAZ:00001251]",
            "Bassas da India [GAZ:00005810]",
            "Belarus [GAZ:00006886]",
            "Belgium [GAZ:00002938]",
            "Belize [GAZ:00002934]",
            "Benin [GAZ:00000904]",
            "Bermuda [GAZ:00001264]",
            "Bhutan [GAZ:00003920]",
            "Bolivia [GAZ:00002511]",
            "Borneo [GAZ:00025355]",
            "Bosnia and Herzegovina [GAZ:00006887]",
            "Botswana [GAZ:00001097]",
            "Bouvet Island [GAZ:00001453]",
            "Brazil [GAZ:00002828]",
            "British Virgin Islands [GAZ:00003961]",
            "Brunei [GAZ:00003901]",
            "Bulgaria [GAZ:00002950]",
            "Burkina Faso [GAZ:00000905]",
            "Burundi [GAZ:00001090]",
            "Cambodia [GAZ:00006888]",
            "Cameroon [GAZ:00001093]",
            "Canada [GAZ:00002560]",
            "Cape Verde [GAZ:00001227]",
            "Cayman Islands [GAZ:00003986]",
            "Central African Republic [GAZ:00001089]",
            "Chad [GAZ:00000586]",
            "Chile [GAZ:00002825]",
            "China [GAZ:00002845]",
            "Christmas Island [GAZ:00005915]",
            "Clipperton Island [GAZ:00005838]",
            "Cocos Islands [GAZ:00009721]",
            "Colombia [GAZ:00002929]",
            "Comoros [GAZ:00005820]",
            "Cook Islands [GAZ:00053798]",
            "Coral Sea Islands [GAZ:00005917]",
            "Costa Rica [GAZ:00002901]",
            "Cote d'Ivoire [GAZ:00000906]",
            "Croatia [GAZ:00002719]",
            "Cuba [GAZ:00003762]",
            "Curacao [GAZ:00012582]",
            "Cyprus [GAZ:00004006]",
            "Czech Republic [GAZ:00002954]",
            "Democratic Republic of the Congo [GAZ:00001086]",
            "Denmark [GAZ:00005852]",
            "Djibouti [GAZ:00000582]",
            "Dominica [GAZ:00006890]",
            "Dominican Republic [GAZ:00003952]",
            "Ecuador [GAZ:00002912]",
            "Egypt [GAZ:00003934]",
            "El Salvador [GAZ:00002935]",
            "Equatorial Guinea [GAZ:00001091]",
            "Eritrea [GAZ:00000581]",
            "Estonia [GAZ:00002959]",
            "Eswatini [GAZ:00001099]",
            "Ethiopia [GAZ:00000567]",
            "Europa Island [GAZ:00005811]",
            "Falkland Islands (Islas Malvinas) [GAZ:00001412]",
            "Faroe Islands [GAZ:00059206]",
            "Fiji [GAZ:00006891]",
            "Finland [GAZ:00002937]",
            "France [GAZ:00003940]",
            "French Guiana [GAZ:00002516]",
            "French Polynesia [GAZ:00002918]",
            "French Southern and Antarctic Lands [GAZ:00003753]",
            "Gabon [GAZ:00001092]",
            "Gambia [GAZ:00000907]",
            "Gaza Strip [GAZ:00009571]",
            "Georgia [GAZ:00004942]",
            "Germany [GAZ:00002646]",
            "Ghana [GAZ:00000908]",
            "Gibraltar [GAZ:00003987]",
            "Glorioso Islands [GAZ:00005808]",
            "Greece [GAZ:00002945]",
            "Greenland [GAZ:00001507]",
            "Grenada [GAZ:02000573]",
            "Guadeloupe [GAZ:00067142]",
            "Guam [GAZ:00003706]",
            "Guatemala [GAZ:00002936]",
            "Guernsey [GAZ:00001550]",
            "Guinea [GAZ:00000909]",
            "Guinea-Bissau [GAZ:00000910]",
            "Guyana [GAZ:00002522]",
            "Haiti [GAZ:00003953]",
            "Heard Island and McDonald Islands [GAZ:00009718]",
            "Honduras [GAZ:00002894]",
            "Hong Kong [GAZ:00003203]",
            "Howland Island [GAZ:00007120]",
            "Hungary [GAZ:00002952]",
            "Iceland [GAZ:00000843]",
            "India [GAZ:00002839]",
            "Indonesia [GAZ:00003727]",
            "Iran [GAZ:00004474]",
            "Iraq [GAZ:00004483]",
            "Ireland [GAZ:00002943]",
            "Isle of Man [GAZ:00052477]",
            "Israel [GAZ:00002476]",
            "Italy [GAZ:00002650]",
            "Jamaica [GAZ:00003781]",
            "Jan Mayen [GAZ:00005853]",
            "Japan [GAZ:00002747]",
            "Jarvis Island [GAZ:00007118]",
            "Jersey [GAZ:00001551]",
            "Johnston Atoll [GAZ:00007114]",
            "Jordan [GAZ:00002473]",
            "Juan de Nova Island [GAZ:00005809]",
            "Kazakhstan [GAZ:00004999]",
            "Kenya [GAZ:00001101]",
            "Kerguelen Archipelago [GAZ:00005682]",
            "Kingman Reef [GAZ:00007116]",
            "Kiribati [GAZ:00006894]",
            "Kosovo [GAZ:00011337]",
            "Kuwait [GAZ:00005285]",
            "Kyrgyzstan [GAZ:00006893]",
            "Laos [GAZ:00006889]",
            "Latvia [GAZ:00002958]",
            "Lebanon [GAZ:00002478]",
            "Lesotho [GAZ:00001098]",
            "Liberia [GAZ:00000911]",
            "Libya [GAZ:00000566]",
            "Liechtenstein [GAZ:00003858]",
            "Line Islands [GAZ:00007144]",
            "Lithuania [GAZ:00002960]",
            "Luxembourg [GAZ:00002947]",
            "Macau [GAZ:00003202]",
            "Madagascar [GAZ:00001108]",
            "Malawi [GAZ:00001105]",
            "Malaysia [GAZ:00003902]",
            "Maldives [GAZ:00006924]",
            "Mali [GAZ:00000584]",
            "Malta [GAZ:00004017]",
            "Marshall Islands [GAZ:00007161]",
            "Martinique [GAZ:00067143]",
            "Mauritania [GAZ:00000583]",
            "Mauritius [GAZ:00003745]",
            "Mayotte [GAZ:00003943]",
            "Mexico [GAZ:00002852]",
            "Micronesia [GAZ:00005862]",
            "Midway Islands [GAZ:00007112]",
            "Moldova [GAZ:00003897]",
            "Monaco [GAZ:00003857]",
            "Mongolia [GAZ:00008744]",
            "Montenegro [GAZ:00006898]",
            "Montserrat [GAZ:00003988]",
            "Morocco [GAZ:00000565]",
            "Mozambique [GAZ:00001100]",
            "Myanmar [GAZ:00006899]",
            "Namibia [GAZ:00001096]",
            "Nauru [GAZ:00006900]",
            "Navassa Island [GAZ:00007119]",
            "Nepal [GAZ:00004399]",
            "Netherlands [GAZ:00002946]",
            "New Caledonia [GAZ:00005206]",
            "New Zealand [GAZ:00000469]",
            "Nicaragua [GAZ:00002978]",
            "Niger [GAZ:00000585]",
            "Nigeria [GAZ:00000912]",
            "Niue [GAZ:00006902]",
            "Norfolk Island [GAZ:00005908]",
            "North Korea [GAZ:00002801]",
            "North Macedonia [GAZ:00006895]",
            "North Sea [GAZ:00002284]",
            "Northern Mariana Islands [GAZ:00003958]",
            "Norway [GAZ:00002699]",
            "Oman [GAZ:00005283]",
            "Pakistan [GAZ:00005246]",
            "Palau [GAZ:00006905]",
            "Panama [GAZ:00002892]",
            "Papua New Guinea [GAZ:00003922]",
            "Paracel Islands [GAZ:00010832]",
            "Paraguay [GAZ:00002933]",
            "Peru [GAZ:00002932]",
            "Philippines [GAZ:00004525]",
            "Pitcairn Islands [GAZ:00005867]",
            "Poland [GAZ:00002939]",
            "Portugal [GAZ:00004126]",
            "Puerto Rico [GAZ:00006935]",
            "Qatar [GAZ:00005286]",
            "Republic of the Congo [GAZ:00001088]",
            "Reunion [GAZ:00003945]",
            "Romania [GAZ:00002951]",
            "Ross Sea [GAZ:00023304]",
            "Russia [GAZ:00002721]",
            "Rwanda [GAZ:00001087]",
            "Saint Helena [GAZ:00000849]",
            "Saint Kitts and Nevis [GAZ:00006906]",
            "Saint Lucia [GAZ:00006909]",
            "Saint Pierre and Miquelon [GAZ:00003942]",
            "Saint Martin [GAZ:00005841]",
            "Saint Vincent and the Grenadines [GAZ:02000565]",
            "Samoa [GAZ:00006910]",
            "San Marino [GAZ:00003102]",
            "Sao Tome and Principe [GAZ:00006927]",
            "Saudi Arabia [GAZ:00005279]",
            "Senegal [GAZ:00000913]",
            "Serbia [GAZ:00002957]",
            "Seychelles [GAZ:00006922]",
            "Sierra Leone [GAZ:00000914]",
            "Singapore [GAZ:00003923]",
            "Sint Maarten [GAZ:00012579]",
            "Slovakia [GAZ:00002956]",
            "Slovenia [GAZ:00002955]",
            "Solomon Islands [GAZ:00005275]",
            "Somalia [GAZ:00001104]",
            "South Africa [GAZ:00001094]",
            "South Georgia and the South Sandwich Islands [GAZ:00003990]",
            "South Korea [GAZ:00002802]",
            "South Sudan [GAZ:00233439]",
            "Spain [GAZ:00003936]",
            "Spratly Islands [GAZ:00010831]",
            "Sri Lanka [GAZ:00003924]",
            "State of Palestine [GAZ:00002475]",
            "Sudan [GAZ:00000560]",
            "Suriname [GAZ:00002525]",
            "Svalbard [GAZ:00005396]",
            "Swaziland [GAZ:00001099]",
            "Sweden [GAZ:00002729]",
            "Switzerland [GAZ:00002941]",
            "Syria [GAZ:00002474]",
            "Taiwan [GAZ:00005341]",
            "Tajikistan [GAZ:00006912]",
            "Tanzania [GAZ:00001103]",
            "Thailand [GAZ:00003744]",
            "Timor-Leste [GAZ:00006913]",
            "Togo [GAZ:00000915]",
            "Tokelau [GAZ:00260188]",
            "Tonga [GAZ:00006916]",
            "Trinidad and Tobago [GAZ:00003767]",
            "Tromelin Island [GAZ:00005812]",
            "Tunisia [GAZ:00000562]",
            "Turkey [GAZ:00000558]",
            "Turkmenistan [GAZ:00005018]",
            "Turks and Caicos Islands [GAZ:00003955]",
            "Tuvalu [GAZ:00009715]",
            "USA [GAZ:00002459]",
            "Uganda [GAZ:00001102]",
            "Ukraine [GAZ:00002724]",
            "United Arab Emirates [GAZ:00005282]",
            "United Kingdom [GAZ:00002637]",
            "Uruguay [GAZ:00002930]",
            "Uzbekistan [GAZ:00004979]",
            "Vanuatu [GAZ:00006918]",
            "Venezuela [GAZ:00002931]",
            "Viet Nam [GAZ:00003756]",
            "Virgin Islands [GAZ:00003959]",
            "Wake Island [GAZ:00007111]",
            "Wallis and Futuna [GAZ:00007191]",
            "West Bank [GAZ:00009572]",
            "Western Sahara [GAZ:00000564]",
            "Yemen [GAZ:00005284]",
            "Zambia [GAZ:00001107]",
            "Zimbabwe [GAZ:00001106]",
            "Not Applicable [GENEPIO:0001619]",
            "Not Collected [GENEPIO:0001620]",
            "Not Provided [GENEPIO:0001668]",
            "Missing [GENEPIO:0001618]",
            "Restricted Access [GENEPIO:0001810]"
          ],
          "ontology": "GENEPIO:0001181",
          "type": "string",
          "description": "The country of origin of the sample.",
          "examples": ["South Africa [GAZ:00001094]"]
        },
        "geo_loc_state": {
            "examples": ["Western Cape"],
             "ontology": "GENEPIO:0001185",
             "type": "string",
             "description": "The state/province/territory of origin of the sample."
        },
        "organism": {
          "Enums": [
            "Coronaviridae [NCBITaxon:11118]",
            "Severe acute respiratory syndrome coronavirus 2 [NCBITaxon:2697049]",
            "Not Applicable [GENEPIO:0001619]",
            "Not Collected [GENEPIO:0001620]",
            "Not Provided [GENEPIO:0001668]",
            "Missing [GENEPIO:0001618]",
            "Restricted Access [GENEPIO:0001810]"
          ],
          "ontology": "GENEPIO:0001191",
          "type": "string",
          "description": "Taxonomic name of the organism.",
          "examples": [
            "Severe acute respiratory syndrome coronavirus 2 [NCBITaxon:2697049]"
          ]
        },
        "isolate": {
            "examples": ["SARS-CoV-2/human/USA/CA-CDPH-001/2020"],
             "ontology":  "GENEPIO:0001644",
             "type": "string",
             "description": "Identifier of the specific isolate.",
             "clasification":"Sample collection and processing"
        },
        "purpose_sampling": {
            "examples": ["Diagnostic testing"],
             "ontology":  "NCIT_C146997",
             "type": "string",
             "description": "The reason that the sample was collected.",
             "clasification":"Sample collection and processing"
        },
        "host_scientific_name": {
          "Enums": [
            "Bos taurus [NCBITaxon:9913]",
            "Canis lupus familiaris [NCBITaxon:9615]",
            "Chiroptera [NCBITaxon:9397]",
            "Columbidae [NCBITaxon:8930]",
            "Felis catus [NCBITaxon:9685]",
            "Gallus gallus [NCBITaxon:9031]",
            "Homo sapiens [NCBITaxon:9606]",
            "Manis [NCBITaxon:9973]",
            "Manis javanica [NCBITaxon:9974]",
            "Neovison vison [NCBITaxon:452646]",
            "Panthera leo [NCBITaxon:9689]",
            "Panthera tigris [NCBITaxon:9694]",
            "Rhinolophidae [NCBITaxon:58055]",
            "Rhinolophus affinis [NCBITaxon:59477]",
            "Sus scrofa domesticus [NCBITaxon:9825]",
            "Viverridae [NCBITaxon:9673]",
            "Not Applicable [GENEPIO:0001619]",
            "Not Collected [GENEPIO:0001620]",
            "Not Provided [GENEPIO:0001668]",
            "Missing [GENEPIO:0001618]",
            "Restricted Access [GENEPIO:0001810]"
          ],
          "ontology": "GENEPIO:0001387",
          "type": "string",
          "description": "The taxonomic, or scientific name of the host.",
          "examples": ["Homo sapiens [NCBITaxon:9606]"]
        },
        "host_health_state": {
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "Health status of the host at the time of sample collection.",
        },
        "host_gender": {
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "Gender or sex of the host.",
        },
        "host_subject_id": {
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "a unique identifier by which each subject can be referred to, de-identified, e.g. #131",
        },

        "host_disease": {
          "Enums": [
            "COVID-19 [MONDO:0100096]",
            "Not Applicable [GENEPIO:0001619]",
            "Not Collected [GENEPIO:0001620]",
            "Not Provided [GENEPIO:0001668]",
            "Missing [GENEPIO:0001618]",
            "Restricted Access [GENEPIO:0001810]"
          ],
          "ontology": "GENEPIO:0001391",
          "type": "string",
          "description": "The name of the disease experienced by the host.",
          "examples": ["COVID-19 [MONDO:0100096]"]
        },
        "sequencing_instrument_model": {
          "Enums": [
            "Illumina sequencing instrument [GENEPIO:0100105]",
            "Illumina Genome Analyzer [GENEPIO:0100106]",
            "Illumina Genome Analyzer II [GENEPIO:0100107]",
            "Illumina Genome Analyzer IIx [GENEPIO:0100108]",
            "Illumina HiScanSQ [GENEPIO:0100109]",
            "Illumina HiSeq [GENEPIO:0100110]",
            "Illumina HiSeq X [GENEPIO:0100111]",
            "Illumina HiSeq X Five [GENEPIO:0100112]",
            "Illumina HiSeq X Ten [GENEPIO:0100113]",
            "Illumina HiSeq 1000 [GENEPIO:0100114]",
            "Illumina HiSeq 1500 [GENEPIO:0100115]",
            "Illumina HiSeq 2000 [GENEPIO:0100116]",
            "Illumina HiSeq 2500 [GENEPIO:0100117]",
            "Illumina HiSeq 3000 [GENEPIO:0100118]",
            "Illumina HiSeq 4000 [GENEPIO:0100119]",
            "Illumina iSeq [GENEPIO:0100120]",
            "Illumina iSeq 100 [GENEPIO:0100121]",
            "Illumina NovaSeq [GENEPIO:0100122]",
            "Illumina NovaSeq 6000 [GENEPIO:0100123]",
            "Illumina MiniSeq [GENEPIO:0100124]",
            "Illumina MiSeq [GENEPIO:0100125]",
            "Illumina NextSeq [GENEPIO:0100126]",
            "Illumina NextSeq 500 [GENEPIO:0100127]",
            "Illumina NextSeq 550 [GENEPIO:0100128]",
            "Illumina NextSeq 2000 [GENEPIO:0100129]",
            "Pacific Biosciences sequencing instrument [GENEPIO:0100130]",
            "PacBio RS [GENEPIO:0100131]",
            "PacBio RS II [GENEPIO:0100132]",
            "PacBio Sequel [GENEPIO:0100133]",
            "PacBio Sequel II [GENEPIO:0100134]",
            "Ion Torrent sequencing instrument [GENEPIO:0100135]",
            "Ion Torrent PGM [GENEPIO:0100136]",
            "Ion Torrent Proton [GENEPIO:0100137]",
            "Ion Torrent S5 XL [GENEPIO:0100138]",
            "Ion Torrent S5 [GENEPIO:0100139]",
            "Oxford Nanopore sequencing instrument [GENEPIO:0100140]",
            "Oxford Nanopore GridION [GENEPIO:0100141]",
            "Oxford Nanopore MinION [GENEPIO:0100142]",
            "Oxford Nanopore PromethION [GENEPIO:0100143]",
            "BGI Genomics sequencing instrument [GENEPIO:0100144]",
            "BGI SEQ-500 [GENEPIO:0100145]",
            "MGI sequencing instrument [GENEPIO:0100146]",
            "MGI DNBSEQ-T7 [GENEPIO:0100147]",
            "MGI DNBSEQ-G400 [GENEPIO:0100148]",
            "MGI DNBSEQ-G400RS FAST [GENEPIO:0100149]",
            "MGI DNBSEQ-G50 [GENEPIO:0100150]",
            "Not Applicable [GENEPIO:0001619]",
            "Not Collected [GENEPIO:0001620]",
            "Not Provided [GENEPIO:0001668]",
            "Missing [GENEPIO:0001618]",
            "Restricted Access [GENEPIO:0001810]"
          ],
          "ontology": "GENEPIO:0001452",
          "type": "string",
          "description": "The model of the sequencing instrument used.",
          "examples": ["Oxford Nanopore MinION [GENEPIO:0100142]"]
        },
        "sequencing_instrument_platform": {
            "examples": ["MinIon"],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "The model of the sequencing instrument used."
        },
        "consensus_sequence_software_name": {
            "examples": ["Ivar"],
             "ontology": "GENEPIO:0001463",
             "type": "string",
             "description": "The name of software used to generate the consensus sequence."
        },
        "consensus_sequence_software_version": {
            "examples": ["1.3"],
             "ontology": "GENEPIO:0001469",
             "type": "string",
             "description": "The version of the software used to generate the consensus sequence."
        },
        "submitting_lab_sequence_id": {
            "examples": [""],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "Sample ID given by the submitting laboratory"
        },
        "bioproject_umbrella_accession_ENA": {
            "examples": ["PRJNA623807"],
             "ontology":  "GENEPIO:0001133",
             "type": "string",
             "description": "The INSDC umbrella accession number of the BioProject to which the BioSample belongs.",
             "clasification":"Database Identifiers"
        },
       "bioproject_accession_ENA": {
            "examples": ["PRJNA12345"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "The INSDC accession number of the BioProject(s) to which the BioSample belongs.",
            "clasification":"Database Identifiers"
        },
        "biosample_accession_ENA": {
            "examples": ["SAMN14180202"],
             "ontology": "GENEPIO:0001139",
             "type": "string",
             "description": "The identifier assigned to a BioSample in INSDC archives.",
             "clasification":"Database Identifiers"
            },
        "sra_accession": {
            "examples": ["SRR11177792"],
             "ontology": "GENEPIO:0001142",
             "type": "string",
             "description": "The Sequence Read Archive (SRA), European Nucleotide Archive (ENA) or DDBJ Sequence Read Archive (DRA) identifier linking raw read data, methodological metadata and quality control metrics submitted to the INSDC.",
             "clasification":"Database Identifiers"
            },
        "genBank/ENA/DDBJ_accession": {
            "examples": ["MN908947.3"],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "The GenBank/ENA/DDBJ identifier assigned to the sequence in the INSDC archives.",
             "clasification":"Database Identifiers"
            },
        "gisaid_accession": {
            "examples": ["EPI_ISL_123456"],
             "ontology": "GENEPIO:0001147",
             "type": "string",
             "description": "The GISAID accession number assigned to the sequence.",
             "clasification":"Database Identifiers"
            },
        "virus_name": {
            "examples": ["hCoV-19/Canada/prov_rona_99/2020"],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "The user-defined GISAID virus name assigned to the sequence.",
             "clasification":"Database Identifiers"
            },
        "collecting_institution_email": {
            "examples": ["johnnyblogs@lab.ca"],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "The email address of the contact responsible for follow-up regarding the sample.",
             "clasification":"Sample collection and processing"
            },
        "collecting_institution_address": {
            "examples": ["655 Lab St, Vancouver, British Columbia, V5N 2A2, Canada"],
             "ontology": "GENEPIO:0001158",
             "type": "string",
             "description": "The mailing address of the agency submitting the sample.",
             "clasification":"Sample collection and processing"
            },
        "submitting_institution_email": {
            "examples": ["RespLab@lab.ca"],
            "ontology": "GENEPIO:0001165",
            "type": "string",
            "description": "The email address of the contact responsible for follow-up regarding the sequence.",
            "clasification":"Sample collection and processing"
            },
        "submitting_institution_address": {
            "examples": ["123 Sunnybrooke St, Toronto, Ontario, M4P 1L6, Canada"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "The mailing address of the agency submitting the sequence.",
            "clasification":"Sample collection and processing"
            },
        "sample_received_date": {
            "examples": ["3/21/2020"],
            "ontology": "GENEPIO:0001179",
            "type": "string",
            "description": "The date on which the sample was received.",
            "format":"date",
            "clasification":"Sample collection and processing"
            },
        "results_emission_date": {
            "examples": ["3/23/2020"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "The date on which the results were emitted.",
            "format":"date",
            "clasification":"Sample collection and processing"
            },
        "geo_loc_region": {
            "examples": ["Derbyshire"],
            "ontology": "GENEPIO:0100280",
            "type": "string",
            "description": "The county/region of origin of the sample.",
            "clasification":"Sample collection and processing"
            },
        "geo_loc_city": {
            "examples": ["Vancouver"],
            "ontology": "GENEPIO:0001189",
            "type": "string",
            "description": "The city of origin of the sample.",
            "clasification":"Sample collection and processing"
            },
        "geo_loc_latitude": {
            "examples": ["38.98 N"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "The latitude coordinates of the geographical location of sample collection.",
            "clasification":"Sample collection and processing"
            },
        "geo_loc_longitude": {
            "examples": ["77.11 W"],
            "ontology": "OBI:0001621",
            "type": "string",
            "description": "The longitude coordinates of the geographical location of sample collection.",
            "clasification":"Sample collection and processing"
            },
        "anatomical_material": {
          "Enums": [
            "Blood [UBERON:0000178]",
            "Fluid [UBERON:0006314]",
            "Fluid (Cerebrospinal (CSF)) [UBERON:0001359]",
            "Fluid (Pericardial) [UBERON:0002409]",
            "Fluid (Pleural) [UBERON:0001087]",
            "Fluid (Vaginal) [UBERON:0036243]",
            "Fluid (Amniotic) [UBERON:0000173]",
            "Saliva [UBERON:0001836]",
            "Tissue [UBERON:0000479]",
            "Not Applicable [GENEPIO:0001619]",
            "Not Collected [GENEPIO:0001620]",
            "Not Provided [GENEPIO:0001668]",
            "Missing [GENEPIO:0001618]",
            "Restricted Access [GENEPIO:0001810]"
          ],
          "ontology": "GENEPIO:0001211",
          "type": "string",
          "description": "A substance obtained from an anatomical part of an organism e.g. tissue, blood.",
          "examples": ["Blood [UBERON:0000178]"]
          },
          "anatomical_part": {
            "Enums": [
              "Anus [UBERON:0001245]",
              "Duodenum [UBERON:0002114]",
              "Eye [UBERON:0000970]",
              "Intestine [UBERON:0000160]",
              "Lower respiratory tract [UBERON:0001558]",
              "Bronchus [UBERON:0002185]",
              "Lung [UBERON:0002048]",
              "Bronchiole [UBERON:0002186]",
              "Alveolar sac [UBERON:0002169]",
              "Pleural sac [UBERON:0009778]",
              "Pleural cavity [UBERON:0002402]",
              "Trachea [UBERON:0003126]",
              "Rectum [UBERON:0001052]",
              "Skin [UBERON:0001003]",
              "Stomach [UBERON:0000945]",
              "Upper respiratory tract [UBERON:0001557]",
              "Anterior Nares [UBERON:2001427]",
              "Esophagus [UBERON:0001043]",
              "Ethmoid sinus [UBERON:0002453]",
              "Nasal Cavity [UBERON:0001707]",
              "Middle Nasal Turbinate [UBERON:0005921]",
              "Inferior Nasal Turbinate [UBERON:0005922]",
              "Nasopharynx (NP) [UBERON:0001728]",
              "Oropharynx (OP) [UBERON:0001729]",
              "Not Applicable [GENEPIO:0001619]",
              "Not Collected [GENEPIO:0001620]",
              "Not Provided [GENEPIO:0001668]",
              "Missing [GENEPIO:0001618]",
              "Restricted Access [GENEPIO:0001810]"
            ],
            "ontology": "GENEPIO:0001214",
            "type": "string",
            "description": "An anatomical part of an organism e.g. oropharynx. ",
            "examples": ["Nasopharynx (NP) [UBERON:0001728]"]
        },
        "body_product": {
          "Enums": [
            "Breast Milk [UBERON:0001913]",
            "Feces [UBERON:0001988]",
            "Mucus [UBERON:0000912]",
            "Semen [UBERON:0006530]",
            "Sputum [UBERON:0007311]",
            "Sweat [UBERON:0001089]",
            "Tear [UBERON:0001827]",
            "Urine [UBERON:0001088]",
            "Not Applicable [GENEPIO:0001619]",
            "Not Collected [GENEPIO:0001620]",
            "Not Provided [GENEPIO:0001668]",
            "Missing [GENEPIO:0001618]",
            "Restricted Access [GENEPIO:0001810]"
          ],
          "ontology": "GENEPIO:0001216",
          "type": "string",
          "description": "A substance excreted/secreted from an organism e.g. feces, urine, sweat.",
          "examples": ["Feces [UBERON:0001988]"]
        },
        "environmental_material": {
          "Enums": [
            "Air vent [ENVO:03501208]",
            "Banknote [ENVO:00003896]",
            "Bed rail [ENVO:03501209]",
            "Building Floor [ENVO:01000486]",
            "Cloth [ENVO:02000058]",
            "Control Panel [ENVO:03501210]",
            "Door [ENVO:03501220]",
            "Door Handle [ENVO:03501211]",
            "Face Mask [OBI:0002787]",
            "Face Shield [OBI:0002791]",
            "Food [FOODON:00002403]",
            "Food Packaging [FOODON:03490100]",
            "Glass [ENVO:01000481]",
            "Handrail [ENVO:03501212]",
            "Hospital Gown [OBI:0002796]",
            "Light Switch [ENVO:03501213]",
            "Locker [ENVO:03501214]",
            "N95 Mask [OBI:0002790]",
            "Nurse Call Button [ENVO:03501215]",
            "Paper [ENVO:03501256]",
            "Particulate Matter [ENVO:01000060]",
            "Plastic [ENVO:01000404]",
            "PPE Gown [GENEPIO:0100025]",
            "Sewage [ENVO:00002018]",
            "Sink [ENVO:01000990]",
            "Soil [ENVO:00001998]",
            "Stainless Steel [ENVO:03501216]",
            "Tissue Paper [ENVO:03501217]",
            "Toilet Bowl [ENVO:03501218]",
            "Water [ENVO:00002006]",
            "Wastewater [ENVO:00002001]",
            "Window [ENVO:03501219]",
            "Wood [ENVO:00002040]",
            "Not Applicable [GENEPIO:0001619]",
            "Not Collected [GENEPIO:0001620]",
            "Not Provided [GENEPIO:0001668]",
            "Missing [GENEPIO:0001618]",
            "Restricted Access [GENEPIO:0001810]"
          ],
          "ontology": "GENEPIO:0001223",
          "type": "string",
          "description": "A substance obtained from the natural or man-made environment e.g. soil, water, sewage, door handle, bed handrail, face mask.",
          "examples": ["Face Mask [OBI:0002787]"]
        },
        "environmental_site": {
          "Enums": [
            "Acute care facility [ENVO:03501135]",
            "Animal house [ENVO:00003040]",
            "Bathroom [ENVO:01000422]",
            "Clinical assessment centre [ENVO:03501136]",
            "Conference venue [ENVO:03501127]",
            "Corridor [ENVO:03501121]",
            "Daycare [ENVO:01000927]",
            "Emergency room (ER) [ENVO:03501145]",
            "Family practice clinic [ENVO:03501186]",
            "Group home [ENVO:03501196]",
            "Homeless shelter [ENVO:03501133]",
            "Hospital [ENVO:00002173]",
            "Intensive Care Unit (ICU) [ENVO:03501152]",
            "Long Term Care Facility [ENVO:03501194]",
            "Patient room [ENVO:03501180]",
            "Prison [ENVO:03501204]",
            "Production Facility [ENVO:01000536]",
            "School [ENVO:03501130]",
            "Sewage Plant [ENVO:00003043]",
            "Subway train [ENVO:03501109]",
            "Wet market [ENVO:03501198]",
            "Not Applicable [GENEPIO:0001619]",
            "Not Collected [GENEPIO:0001620]",
            "Not Provided [GENEPIO:0001668]",
            "Missing [GENEPIO:0001618]",
            "Restricted Access [GENEPIO:0001810]"
          ],
          "ontology": "GENEPIO:0001232",
          "type": "string",
          "description": "An environmental location may describe a site in the natural or built environment e.g. hospital, wet market, bat cave.",
          "examples": ["Hospital [ENVO:00002173]"]
        },
        "collection_device": {
          "Enums": [
            "Air filter [ENVO:00003968]",
            "Blood Collection Tube [OBI:0002859]",
            "Bronchoscope [OBI:0002826]",
            "Collection Container [OBI:0002088]",
            "Collection Cup [GENEPIO:0100026]",
            "Fibrobronchoscope Brush [OBI:0002825]",
            "Filter [GENEPIO:0100103]",
            "Fine Needle [OBI:0002827]",
            "Microcapillary tube [OBI:0002858]",
            "Micropipette [OBI:0001128]",
            "Needle [OBI:0000436]",
            "Serum Collection Tube [OBI:0002860]",
            "Sputum Collection Tube [OBI:0002861]",
            "Suction Catheter [OBI:0002831]",
            "Swab [GENEPIO:0100027]",
            "Urine Collection Tube [OBI:0002862]",
            "Virus Transport Medium [OBI:0002866]",
            "Not Applicable [GENEPIO:0001619]",
            "Not Collected [GENEPIO:0001620]",
            "Not Provided [GENEPIO:0001668]",
            "Missing [GENEPIO:0001618]",
            "Restricted Access [GENEPIO:0001810]"
          ],
          "ontology": "GENEPIO:0001234",
          "type": "string",
          "description": "The instrument or container used to collect the sample e.g. swab.",
          "examples": ["Swab [GENEPIO:0100027]"]
        },
        "collection_method": {
          "Enums": [
            "Amniocentesis [NCIT:C52009]",
            "Aspiration [NCIT:C15631]",
            "Suprapubic Aspiration [GENEPIO:0100028]",
            "Tracheal Aspiration [GENEPIO:0100029]",
            "Vacuum Aspiration [GENEPIO:0100030]",
            "Biopsy [OBI:0002650]",
            "Needle Biopsy [OBI:0002651]",
            "Filtration [OBI:0302885]",
            "Air Filtration [GENEPIO:0100031]",
            "Lavage [OBI:0600044]",
            "Bronchoalveolar Lavage (BAL) [GENEPIO:0100032]",
            "Gastric Lavage [GENEPIO:0100033]",
            "Lumbar Puncture [NCIT:C15327]",
            "Necropsy [MMO:0000344]",
            "Phlebotomy [NCIT:C28221]",
            "Rinsing [GENEPIO:0002116]",
            "Saline gargle (mouth rinse and gargle) [GENEPIO:0100034]",
            "Scraping [GENEPIO:0100035]",
            "Swabbing [GENEPIO:0002117]",
            "Finger Prick [GENEPIO:0100036]",
            "Washout Tear Collection [GENEPIO:0100038]",
            "Not Applicable [GENEPIO:0001619]",
            "Not Collected [GENEPIO:0001620]",
            "Not Provided [GENEPIO:0001668]",
            "Missing [GENEPIO:0001618]",
            "Restricted Access [GENEPIO:0001810]"
          ],
          "ontology": "GENEPIO:0001241",
          "type": "string",
          "description": "The process used to collect the sample e.g. phlebotomy, necropsy.",
          "examples": ["Bronchoalveolar Lavage (BAL) [GENEPIO:0100032]"]
        },
        "collection_protocol": {
            "examples": ["SC2SamplingProtocol 1.2"],
             "ontology": "GENEPIO:0001243",
             "type": "string",
             "description": "Conditions at which sample was stored, usually storage temperature, duration and location",
             "clasification":"Sample collection and processing"
        },
        "sample_storage_conditions": {
            "examples": ["24 degrees celsius"],
             "ontology": "NCIT_C115535",
             "type": "string",
             "description": "The name and version of a particular protocol used for sampling.",
             "clasification":"Sample collection and processing"
        },
        "specimen_processing": {
          "Enums": [
            "Virus Passage [GENEPIO:0100039]",
            "RNA Re-Extraction (Post RT-PCR) [GENEPIO:0100040]",
            "Specimens Pooled [OBI:0600016]",
            "Not Applicable [GENEPIO:0001619]",
            "Not Collected [GENEPIO:0001620]",
            "Not Provided [GENEPIO:0001668]",
            "Missing [GENEPIO:0001618]",
            "Restricted Access [GENEPIO:0001810]"
          ],
          "ontology": "GENEPIO:0001253",
          "type": "string",
          "description": "Any processing applied to the sample during or after receiving the sample. ",
          "examples": ["Virus Passage [GENEPIO:0100039]"]
        },
        "lab_host": {
          "Enums": [
            "293/ACE2 Cell Line [GENEPIO:0100041]",
            "Caco2 Cell Line [BTO:0000195]",
            "Calu3 Cell Line [BTO:0002750]",
            "EFK3B Cell Line [GENEPIO:0100042]",
            "HEK293T Cell Line [BTO:0002181]",
            "HRCE Cell Line [GENEPIO:0100043]",
            "Huh7 Cell Line [BTO:0001950]",
            "LLCMk2 Cell Line [CLO:0007330]",
            "MDBK Cell Line [BTO:0000836]",
            "NHBE Cell Line [BTO:0002924]",
            "PK-15 Cell Line [BTO:0001865]",
            "RK-13 Cell Line [BTO:0002909]",
            "U251 Cell Line [BTO:0002035]",
            "Vero Cell Line [BTO:0001444]",
            "Vero E6 Cell Line [BTO:0004755]",
            "Vero E6/TMPRSS2 Cell Line [GENEPIO:0100044]",
            "Not Applicable [GENEPIO:0001619]",
            "Not Collected [GENEPIO:0001620]",
            "Not Provided [GENEPIO:0001668]",
            "Missing [GENEPIO:0001618]",
            "Restricted Access [GENEPIO:0001810]"
          ],
          "ontology": "GENEPIO:0001255",
          "type": "string",
          "description": "Name and description of the laboratory host used to propagate the source organism or material from which the sample was obtained.",
          "examples": ["Vero E6 Cell Line [BTO:0004755]"]
        },
        "passage_number": {
            "examples": ["3"],
             "ontology": "GENEPIO:0001261",
             "type": "string",
             "description": "Number of passages.",
             "clasification":"Sample collection and processing"
        },
        "passage_method": {
            "examples": ["AVL buffer+30%EtOH lysate received from Respiratory Lab. P3 passage in Vero-1 via bioreactor large-scale batch passage. P3 batch derived from the SP-2/reference lab strain."],
             "ontology": "GENEPIO:0001264",
             "type": "string",
             "description": "Description of how organism was passaged.",
             "clasification":"Sample collection and processing"
        },
        "biomaterial_extracted": {
          "Enums": [
            "mRNA (cDNA) [OBI:0002754]",
            "RNA (Total) [OBI:0000895]",
            "RNA (Poly-A) [OBI:0000869]",
            "RNA (Ribo-Depleted) [OBI:0002627]",
            "Not Applicable [GENEPIO:0001619]",
            "Not Collected [GENEPIO:0001620]",
            "Not Provided [GENEPIO:0001668]",
            "Missing [GENEPIO:0001618]",
            "Restricted Access [GENEPIO:0001810]"
          ],
          "ontology": "GENEPIO:0001266",
          "type": "string",
          "description": "The biomaterial extracted from samples for the purpose of sequencing.",
          "examples": ["RNA (Total) [OBI:0000895]"]
        },
        "tax_id": {
            "examples": ["probably 2697049 in all cases"],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "The NCBITaxon identifier for the organism being sequenced.",
             "clasification":"Sample collection and processing"
        },
        "scientific_name": {
            "examples": [""],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "The taxonomic name of the organism.",
             "clasification":"Sample collection and processing"
        },
        "common_name": {
            "examples": [""],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "The common name of the organism.",
             "clasification":"Sample collection and processing"
        },
        "sample_description": {
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "Free text description of the sample.",
             "clasification":"Sample collection and processing"
        },

        "center_name": {
            "examples": [" KAROLINSKA INSITUTET"],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "The name of the institution",
             "clasification":"Sample collection and processing"
        },

        "virus_id": {
            "examples": [""],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "The user-defined name for the sample.",
             "clasification":"Database Identifiers"
        },
        "host_common_name": {
          "Enums": [
            "Human [NCBITaxon:9606]",
            "Bat [NCBITaxon:9397]",
            "Cat [NCBITaxon:9685]",
            "Chicken [NCBITaxon:9031]",
            "Civet [NCBITaxon:9673]",
            "Cow [NCBITaxon:9913]",
            "Dog [NCBITaxon:9615]",
            "Lion [NCBITaxon:9689]",
            "Mink [NCBITaxon:452646]",
            "Pangolin [NCBITaxon:9973]",
            "Pig [NCBITaxon:9825]",
            "Pigeon [NCBITaxon:8930]",
            "Tiger [NCBITaxon:9694]",
            "Not Applicable [GENEPIO:0001619]",
            "Not Collected [GENEPIO:0001620]",
            "Not Provided [GENEPIO:0001668]",
            "Missing [GENEPIO:0001618]",
            "Restricted Access [GENEPIO:0001810]"
          ],
          "ontology": "GENEPIO:0001386",
          "type": "string",
          "description": "The commonly used name of the host.",
          "examples": ["Human [NCBITaxon:9606]"]
        },
        "outbreak": {
            "examples": ["Date, Location e.g. type of gathering, Family cluster, etc."],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "If the information is unknown or can not be shared, leave blank.",
             "clasification":"Host information"
        },
        "additional_host_information": {
            "examples": ["e.g. Patient infected while traveling in …."],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "If the information is unknown or can not be shared, leave blank.",
             "clasification":"Host information"
        },
        "host_age": {
            "examples": ["e.g. 65 or 7 months, or unknown. Caution: the host age may be considered public health identifiable information. Consult the data steward before sharing. If the information is unknown or can not be shared, put unknown"],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "Patient age",
             "clasification":"Host information"
        },
        "host_age_unit": {
            "examples": ["years"],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "The units used to measure the host's age.",
             "clasification":"Host information"
        },
        "host_age_bin": {
            "examples": ["20-30"],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "The age category of the host at the time of sampling.",
             "clasification":"Host information"
        },
        "host_gender": {
            "examples": ["Male, Female, or unknown.Caution: the host gender may be considered public health identifiable information. Consult the data steward before sharing. If the information is unknown or can not be shared, put unknown"],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "Gender",
             "clasification":"Host information"
        },
        "purpose_of_sequencing": {
          "Enums": [
            "Baseline surveillance (random sampling) [GENEPIO:0100005]",
            "Targeted surveillance (non-random sampling) [GENEPIO:0100006]",
            "Priority surveillance projects [GENEPIO:0100007]",
            "Screening for Variants of Concern (VOC) [GENEPIO:0100008]",
            "Sample has epidemiological link to Variant of Concern (VoC) [GENEPIO:0100273]",
            "Sample has epidemiological link to Omicron Variant [GENEPIO:0100274]",
            "Longitudinal surveillance (repeat sampling of individuals) [GENEPIO:0100009]",
            "Re-infection surveillance [GENEPIO:0100010]",
            "Vaccine escape surveillance [GENEPIO:0100011]",
            "Travel-associated surveillance [GENEPIO:0100012]",
            "Domestic travel surveillance [GENEPIO:0100013]",
            "Interstate/ interprovincial travel surveillance [GENEPIO:0100275]",
            "Intra-state/ intra-provincial travel surveillance [GENEPIO:0100276]",
            "International travel surveillance [GENEPIO:0100014]",
            "Surveillance of international border crossing by air travel or ground transport [GENEPIO:0100015]",
            "Surveillance of international border crossing by air travel [GENEPIO:0100016]",
            "Surveillance of international border crossing by ground transport [GENEPIO:0100017]",
            "Surveillance from international worker testing [GENEPIO:0100018]",
            "Cluster/Outbreak investigation [GENEPIO:0100019]",
            "Multi-jurisdictional outbreak investigation [GENEPIO:0100020]",
            "Intra-jurisdictional outbreak investigation [GENEPIO:0100021]",
            "Research [GENEPIO:0100022]",
            "Viral passage experiment [GENEPIO:0100023]",
            "Protocol testing [GENEPIO:0100024]",
            "Not Applicable [GENEPIO:0001619]",
            "Not Collected [GENEPIO:0001620]",
            "Not Provided [GENEPIO:0001668]",
            "Missing [GENEPIO:0001618]",
            "Restricted Access [GENEPIO:0001810]"
          ],
          "ontology": "GENEPIO:0001445",
          "type": "string",
          "description": "The reason that the sample was sequenced.",
          "examples": ["Baseline surveillance (random sampling) [GENEPIO:0100005]"]
        },
        "purpose_of_sequencing_details": {
          "Enums": [
            "Screened for S gene target failure (S dropout)",
            "Screened for mink variants",
            "Screened for B.1.1.7 variant",
            "Screened for B.1.135 variant",
            "Screened for P.1 variant",
            "Screened due to travel history",
            "Screened due to close contact with infected individual",
            "Assessing public health control measures",
            "Determining early introductions and spread",
            "Investigating airline-related exposures",
            "Investigating temporary foreign worker",
            "Investigating remote regions",
            "Investigating health care workers",
            "Investigating schools/universities",
            "Investigating reinfection"
          ],
          "ontology": "GENEPIO:0001446",
          "type": "string",
          "description": "The description of why the sample was sequenced providing specific details.",
          "examples": ["Screened for S gene target failure (S dropout)"]
        },
        "sequencing_date": {
            "examples": ["4/26/2021"],
             "ontology": "GENEPIO:0001447",
             "type": "string",
             "description": "The date the sample was sequenced.",
             "format":"date",
             "clasification":"Sequencing"
        },
        "rna_extraction_Protocol": {
            "examples": [""],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "",
             "clasification":"Sequencing"
        },
        "library_kit": {
            "examples": [""],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "",
             "clasification":"Sequencing"
        },
        "library_name": {
            "examples": ["e.g P17157_1007"],
             "ontology": "GENEPIO_0001995",
             "type": "string",
             "description": "The submitter's name for this library.",
             "clasification":"Sequencing",
             "genepio_label":"Library Name",
        },
        "enrichment_protocol": {
            "examples": [""],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "",
             "clasification":"Sequencing"
        },
        "if_enrichment_protocol_is_other_specify": {
            "examples": [""],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "",
             "clasification":"Sequencing"
        },
        "amplicon protocol": {
            "examples": [""],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "",
             "clasification":"Sequencing"
        },
        "if_amplicon_protocol_if_other_especify": {
            "examples": [""],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "",
             "clasification":"Sequencing"
        },

        "amplicon_version": {
            "examples": [""],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "",
             "clasification":"Sequencing"
        },
        "amplicon_size": {
            "examples": ["300bp"],
             "ontology": "GENEPIO:0001449",
             "type": "string",
             "description": "The length of the amplicon generated by PCR amplification.",
             "clasification":"Sequencing"
        },

        "was_phix_used?": {
            "examples": [""],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "",
             "clasification":"Sequencing"
        },

        "number_of_samples_in_run": {
            "examples": [""],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "",
             "clasification":"Sequencing"
        },

        "flowcell_kit": {
            "examples": [""],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "",
             "clasification":"Sequencing"
        },

        "runID": {
            "examples": [""],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "",
             "clasification":"Sequencing"
        },

        "sequencing_platforms": {
            "examples": [""],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "",
             "clasification":"Sequencing"
        },

        "library_preparation_kit": {
            "examples": ["Nextera XT"],
             "ontology": "GENEPIO:0001450",
             "type": "string",
             "description": "The name of the DNA library preparation kit used to generate the library being sequenced.",
             "clasification":"Sequencing"
        },

        "flow_cell_barcode": {
            "examples": ["FAB06069"],
             "ontology": "GENEPIO:0001451",
             "type": "string",
             "description": "The barcode of the flow cell used for sequencing.",
             "clasification":"Sequencing"
        },
        "sequencing_protocol_name": {
            "examples": ["1D_DNA_MinION, ARTIC Network Protocol V3"],
             "ontology": "GENEPIO:0001453",
             "type": "string",
             "description": "The name and version number of the sequencing protocol used.",
             "clasification":"Sequencing"
        },
        "sequencing_protocol": {
            "examples": ["Genomes were generated through amplicon sequencing of 1200 bp amplicons with Freed schema primers. Libraries were created using Illumina DNA Prep kits, and sequence data was produced using Miseq Micro v2 (500 cycles) sequencing kits."],
             "ontology": "GENEPIO:0001454",
             "type": "string",
             "description": "The protocol used to generate the sequence.",
             "clasification":"Sequencing"
        },
        "sequencing_kit_number": {
            "examples": ["AB456XYZ789"],
             "ontology": "GENEPIO:0001455",
             "type": "string",
             "description": "The manufacturer's kit number.",
             "clasification":"Sequencing"
        },
        "amplicon_pcr_primer_scheme": {
            "examples": ["https://github.com/joshquick/artic-ncov2019/blob/master/primer_schemes/nCoV-2019/V3/nCoV-2019.tsv"],
             "ontology": "GENEPIO:0001456",
             "type": "string",
             "description": "The specifications of the primers (primer sequences, binding positions, fragment size generated etc) used to generate the amplicons to be sequenced.",
             "clasification":"Sequencing"
        },
        "library_source": {
            "examples": ["METAGENOMIC"],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "Molecule type used to make the library.",
             "clasification":"Sequencing"
        },
        "library_selection": {
            "examples": ["RANDOM PCR"],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "Library capture method.",
             "clasification":"Sequencing"
        },
        "library_strategy": {
            "examples": ["WGS"],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "Overall sequencing strategy or approach.",
             "clasification":"Sequencing"
        },
        "library_layout": {
            "examples": ["PAIRED"],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "Single or paired.",
             "clasification":"Sequencing"
        },
        "library_name": {
            "examples": ["P17157_1007"],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "Name of the used library",
             "clasification":"Sequencing"
        },
        "nominal_length ": {
            "examples": ["350"],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "",
             "clasification":"Sequencing"
        },

        "raw_sequence_data_processing_method": {
            "examples": ["Porechop 0.2.3"],
            "ontology": "GENEPIO:0001458",
            "type": "string",
            "description": "The method used for raw data processing such as removing barcodes, adapter trimming, filtering etc.",
            "clasification":"Bioinformatics and QC metrics"
        },
        "dehosting_method": {
            "examples": ["Nanostripper"],
            "ontology": "GENEPIO:0001459",
            "type": "string",
            "description": "The method used to remove host reads from the pathogen sequence.",
            "clasification":"Bioinformatics and QC metrics"
        },
        "assembly": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Bioinformatics and QC metrics"
        },
        "if_assembly_other": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Bioinformatics and QC metrics"
        },
        "assembly_params": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Bioinformatics and QC metrics"
        },
        "variant_Calling": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Bioinformatics and QC metrics"
        },
          "if_variant_Calling_other": {
                "examples": [""],
                "ontology": "GENEPIO:0001156",
                "type": "string",
                "description": "",
                "clasification":"Bioinformatics and QC metrics"
        },
        "variant_Calling_params": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Bioinformatics and QC metrics"
        },
        "consensus_sequence_filepath": {
            "examples": ["/User/Documents/RespLab/Data/ncov123assembly.fasta"],
            "ontology": "GENEPIO:0001462",
            "type": "string",
            "description": "The filepath of the consesnsus sequence file.",
            "clasification":"Bioinformatics and QC metrics"
        },
        "consensus_sequence_software_name": {
            "examples": ["Ivar"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "The name of software used to generate the consensus sequence.",
            "clasification":"Bioinformatics and QC metrics"
        },
        "if_consensus_other": {
            "examples": ["1.3"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "The version of the software used to generate the consensus sequence.",
            "clasification":"Bioinformatics and QC metrics"
        },
        "consensus_sequence_software_version": {
            "examples": ["1.3"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "The version of the software used to generate the consensus sequence.",
            "clasification":"Bioinformatics and QC metrics"
        },
        "consensus_criteria": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Bioinformatics and QC metrics"
        },
        "quality_control_metrics": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Bioinformatics and QC metrics"
        },
        "breadth_of_coverage_value": {
            "examples": ["95%"],
            "ontology": "GENEPIO:0001472",
            "type": "string",
            "description": "The percentage of the reference genome covered by the sequenced data, to a prescribed depth.",
            "clasification":"Bioinformatics and QC metrics"
        },
        "depth_of_coverage_value": {
            "examples": ["400x"],
            "ontology": "GENEPIO:0001474",
            "type": "string",
            "description": "The average number of reads representing a given nucleotide in the reconstructed sequence.",
            "clasification":"Bioinformatics and QC metrics"
        },
        "depth_of_coverage_threshold": {
            "examples": ["100x"],
            "ontology":  "GENEPIO:0001475",
            "type": "string",
            "description": "The threshold used as a cut-off for the depth of coverage.",
            "clasification":"Bioinformatics and QC metrics"
        },
        "sequence_file_R1_fastq": {
            "examples": ["ABC123_S1_L001_R1_001.fastq.gz"],
            "ontology": "GENEPIO:0001476",
            "type": "string",
            "description": "The user-specified filename of the r1 FASTQ file.",
            "clasification":"Bioinformatics and QC metrics"
        },
        "sequence_file_R2_fastq": {
            "examples": ["ABC123_S1_L001_R2_001.fastq.gz"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "The user-specified filename of the r2 FASTQ file.",
            "clasification":"Bioinformatics and QC metrics"
        },
        "r1_fastq_filepath": {
            "examples": ["/User/Documents/RespLab/Data/"],
            "ontology": "GENEPIO:0001478",
            "type": "string",
            "description": "The filepath of the r1 FASTQ file.",
            "clasification":"Bioinformatics and QC metrics"
        },
        "r2_fastq_filepath": {
            "examples": ["/User/Documents/RespLab/Data/"],
            "ontology": "GENEPIO:0001479",
            "type": "string",
            "description": "The filepath of the r2 FASTQ file.",
            "clasification":"Bioinformatics and QC metrics"
        },
        "fast5_filename": {
            "examples": ["batch1a_sequences.fast5"],
            "ontology": "GENEPIO:0001480",
            "type": "string",
            "description": "The user-specified filename of the FAST5 file.",
            "clasification":"Bioinformatics and QC metrics"
        },
        "fast5_filepath": {
            "examples": ["/User/Documents/RespLab/Data/"],
            "ontology": "GENEPIO:0001481",
            "type": "string",
            "description": "The filepath of the FAST5 file.",
            "clasification":"Bioinformatics and QC metrics"
        },
        "number_of_base_pairs_sequenced": {
            "examples": ["387566"],
            "ontology": "GENEPIO:0001482",
            "type": "string",
            "description": "The number of total base pairs generated by the sequencing process.",
            "clasification":"Bioinformatics and QC metrics"
        },
        "consensus_genome_length": {
            "examples": ["38677"],
            "ontology": "GENEPIO:0001483",
            "type": "string",
            "description": "Size of the assembled genome described as the number of base pairs.",
            "clasification":"Bioinformatics and QC metrics"
        },
        "ns_per_100_kbp": {
            "examples": ["300"],
            "ontology": "GENEPIO:0001484",
            "type": "string",
            "description": "The number of N symbols present in the consensus fasta sequence, per 100kbp of sequence.",
            "clasification":"Bioinformatics and QC metrics"
        },
        "reference_genome_accession": {
            "examples": ["NC_045512.2"],
            "ontology": "GENEPIO:0001485",
            "type": "string",
            "description": "A persistent, unique identifier of a genome database entry.",
            "clasification":"Bioinformatics and QC metrics"
        },
        "bioinformatics_protocol": {
            "examples": ["https://www.protocols.io/groups/cphln-sarscov2-sequencing-consortium/members"],
            "ontology": "GENEPIO:0001489",
            "type": "string",
            "description": "The name  of the bioinformatics protocol used.",
            "clasification":"Bioinformatics and QC metrics"
        },
        "if_bioinformatic_protocol_is_other_specify": {
            "examples": ["https://www.protocols.io/groups/cphln-sarscov2-sequencing-consortium/members"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "The name  of the bioinformatics protocol used.",
            "clasification":"Bioinformatics and QC metrics"
        },
        "bioinformatic_protocol_version": {
            "examples": ["https://www.protocols.io/groups/cphln-sarscov2-sequencing-consortium/members"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "The version number of the bioinformatics protocol used.",
            "clasification":"Bioinformatics and QC metrics"
        },
        "commercial/open-source/both": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Bioinformatics and QC metrics"
        },
        "preprocessing": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Bioinformatics and QC metrics"
        },
        "if_preprocessing_other": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Bioinformatics and QC metrics"
        },
        "preprocessing_params": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Bioinformatics and QC metrics"
        },
        "mapping": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Lineage and Variant information"
        },
        "if_mapping_other": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Lineage and Variant information"
        },
        "Mapping_params": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Lineage and Variant information"
        },
        "lineage/clade_name": {
            "examples": ["B.1.1.7"],
            "ontology": "GENEPIO:0001500",
            "type": "string",
            "description": "The name of the lineage or clade.",
            "clasification":"Lineage and Variant information"
        },
        "lineage/clade_analysis_software_name": {
            "examples": ["Pangolin"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "The name of the software used to determine the lineage/clade.",
            "clasification":"Lineage and Variant information"
        },
        "if_lineage_identification_other": {
            "examples": ["Other than Pangolin"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "The name of the software used to determine the lineage/clade.",
            "clasification":"Lineage and Variant information"
        },
        "lineage/clade_analysis_software_version": {
            "examples": ["2.1.10"],
            "ontology":"GENEPIO:0001502",
            "type": "string",
            "description": "The version of the software used to determine the lineage/clade.",
            "clasification":"Lineage and Variant information"
        },
        "variant_designation": {
          "Enums": [
            "Variant of Interest (VOI) [GENEPIO:0100082]",
            "Variant of Concern (VOC) [GENEPIO:0100083]",
            "Variant Under Monitoring (VUM) [GENEPIO:0100279]"
          ],
          "ontology": "GENEPIO:0001503",
          "type": "string",
          "description": "The variant classification of the lineage/clade i.e. variant, variant of concern.",
          "examples": ["Variant of Concern (VOC) [GENEPIO:0100083]"]
        },
        "variant_evidence": {
            "examples": ["lineage-defining mutations: ORF1ab (K1655N), Spike (K417N, E484K, N501Y, D614G, A701V), N (T205I), E (P71L)"],
            "ontology":  "GENEPIO:0001504",
            "type": "string",
            "description": "The evidence used to make the variant determination.",
            "clasification":"Lineage and Variant information"
        },
        "gene_name_1": {
          "Enums": [
            "E gene (orf4) [GENEPIO:0100151]",
            "M gene (orf5) [GENEPIO:0100152]",
            "N gene (orf9) [GENEPIO:0100153]",
            "Spike gene (orf2) [GENEPIO:0100154]",
            "orf1ab (rep) [GENEPIO:0100155]",
            "orf1a (pp1a) [GENEPIO:0100156]",
            "nsp11 [GENEPIO:0100157]",
            "nsp1 [GENEPIO:0100158]",
            "nsp2 [GENEPIO:0100159]",
            "nsp3 [GENEPIO:0100160]",
            "nsp4 [GENEPIO:0100161]",
            "nsp5 [GENEPIO:0100162]",
            "nsp6 [GENEPIO:0100163]",
            "nsp7 [GENEPIO:0100164]",
            "nsp8 [GENEPIO:0100165]",
            "nsp9 [GENEPIO:0100166]",
            "nsp10 [GENEPIO:0100167]",
            "RdRp gene (nsp12) [GENEPIO:0100168]",
            "hel gene (nsp13) [GENEPIO:0100169]",
            "exoN gene (nsp14) [GENEPIO:0100170]",
            "nsp15 [GENEPIO:0100171]",
            "nsp16 [GENEPIO:0100172]",
            "orf3a [GENEPIO:0100173]",
            "orf3b [GENEPIO:0100174]",
            "orf6 (ns6) [GENEPIO:0100175]",
            "orf7a [GENEPIO:0100176]",
            "orf7b (ns7b) [GENEPIO:0100177]",
            "orf8 (ns8) [GENEPIO:0100178]",
            "orf9b [GENEPIO:0100179]",
            "orf9c [GENEPIO:0100180]",
            "orf10 [GENEPIO:0100181]",
            "orf14 [GENEPIO:0100182]",
            "SARS-COV-2 5' UTR [GENEPIO:0100183]",
            "Not Applicable [GENEPIO:0001619]",
            "Not Collected [GENEPIO:0001620]",
            "Not Provided [GENEPIO:0001668]",
            "Missing [GENEPIO:0001618]",
            "Restricted Access [GENEPIO:0001810]"
          ],
          "ontology": "GENEPIO:0001507",
          "type": "string",
          "description": "The name of the gene used in the diagnostic RT-PCR test.",
          "examples": ["E gene (orf4) [GENEPIO:0100151]"]
        },
        "Protocol_SARS-CoV-2_detection": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Pathogen diagnostic testing"
        },
        "%qc_filtered": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Pathogen diagnostic testing"
        },
        "%reads_host": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Pathogen diagnostic testing"
        },
        "%reads_virus": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Pathogen diagnostic testing"
        },
        "%unmapped": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Pathogen diagnostic testing"
        },
        "% genome _greater_10x": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Pathogen diagnostic testing"
        },
        "mean_depth_of_coverage_value": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Pathogen diagnostic testing"
        },
        "%Ns": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Pathogen diagnostic testing"
        },
        "Number_of_variants_(AF_greater_75%)": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Pathogen diagnostic testing"
        },
        "Numer_of_variants_with_effect": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Pathogen diagnostic testing"
        },
        "reference_genome_accession": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Pathogen diagnostic testing"
        },
        "diagnostic_pcr_protocol_1": {
            "examples": ["PCREGene 2.0"],
            "ontology": "GENEPIO:0001508",
            "type": "string",
            "description": "The name and version number of the protocol used for diagnostic marker amplification.",
            "clasification":"Pathogen diagnostic testing"
        },
        "diagnostic_pcr_Ct_value_1": {
            "examples": ["21"],
            "ontology": "GENEPIO:0001509",
            "type": "string",
            "description": "The Ct value result from a diagnostic SARS-CoV-2 RT-PCR test.",
            "clasification":"Pathogen diagnostic testing"
        },
        "gene_name_2": {
          "Enums": [
            "E gene (orf4) [GENEPIO:0100151]",
            "M gene (orf5) [GENEPIO:0100152]",
            "N gene (orf9) [GENEPIO:0100153]",
            "Spike gene (orf2) [GENEPIO:0100154]",
            "orf1ab (rep) [GENEPIO:0100155]",
            "orf1a (pp1a) [GENEPIO:0100156]",
            "nsp11 [GENEPIO:0100157]",
            "nsp1 [GENEPIO:0100158]",
            "nsp2 [GENEPIO:0100159]",
            "nsp3 [GENEPIO:0100160]",
            "nsp4 [GENEPIO:0100161]",
            "nsp5 [GENEPIO:0100162]",
            "nsp6 [GENEPIO:0100163]",
            "nsp7 [GENEPIO:0100164]",
            "nsp8 [GENEPIO:0100165]",
            "nsp9 [GENEPIO:0100166]",
            "nsp10 [GENEPIO:0100167]",
            "RdRp gene (nsp12) [GENEPIO:0100168]",
            "hel gene (nsp13) [GENEPIO:0100169]",
            "exoN gene (nsp14) [GENEPIO:0100170]",
            "nsp15 [GENEPIO:0100171]",
            "nsp16 [GENEPIO:0100172]",
            "orf3a [GENEPIO:0100173]",
            "orf3b [GENEPIO:0100174]",
            "orf6 (ns6) [GENEPIO:0100175]",
            "orf7a [GENEPIO:0100176]",
            "orf7b (ns7b) [GENEPIO:0100177]",
            "orf8 (ns8) [GENEPIO:0100178]",
            "orf9b [GENEPIO:0100179]",
            "orf9c [GENEPIO:0100180]",
            "orf10 [GENEPIO:0100181]",
            "orf14 [GENEPIO:0100182]",
            "SARS-COV-2 5' UTR [GENEPIO:0100183]",
            "Not Applicable [GENEPIO:0001619]",
            "Not Collected [GENEPIO:0001620]",
            "Not Provided [GENEPIO:0001668]",
            "Missing [GENEPIO:0001618]",
            "Restricted Access [GENEPIO:0001810]"
          ],
          "ontology": "GENEPIO:0001510",
          "type": "string",
          "description": "The name of the gene used in the diagnostic RT-PCR test.",
          "examples": ["RdRp gene (nsp12) [GENEPIO:0100168]"]
        },
        "diagnostic_pcr_protocol_2": {
            "examples": ["PCRRdRpGene 3.0"],
            "ontology": "GENEPIO:0001511",
            "type": "string",
            "description": "The name and version number of the protocol used for diagnostic marker amplification.",
            "clasification":"Pathogen diagnostic testing"
        },
        "diagnostic_pcr_Ct_value_2": {
            "examples": ["36"],
            "ontology": "GENEPIO:0001512",
            "type": "string",
            "description": "The cycle threshold (CT) value result from a diagnostic SARS-CoV-2 RT-PCR test.",
            "clasification":"Pathogen diagnostic testing"
        },
        "analysis_author": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Contributor Acknowledgement"
        },
        "author_submitter": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Contributor Acknowledgement"
        },
        "submitter": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"enter your GISAID-Username"
        },
        "authors": {
            "examples": [""],
            "ontology": "GENEPIO:0001517",
            "type": "string",
            "description": "",
            "clasification":"Contributor Acknowledgement"
        },
        "tax_id": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Sample collection and processing"
        },
        "scientific_name": {
            "examples": [""],
             "ontology": "GENEPIO:0001156",
             "type": "string",
             "description": "",
             "clasification":"Sample collection and processing"
        },
        "common_name": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Sample collection and processing"
        },
        "library_source": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Sequencing"
        },
        "library_selection": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Sequencing"
        },
        "library_strategy": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Sequencing"
        },
        "library_layout": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Sequencing"
        },
        "library_name": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Sequencing"
        },
        "nominal_length": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Sequencing"
        },
        "analysis_accession": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "study_accession": {
            "examples": ["e.g PRJEB39632"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "secondary_study_accession": {
            "examples": ["e.g ERP123173"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "sample_accession": {
            "examples": ["e.g SAMEA7098096"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "secondary_sample_accession": {
            "examples": ["e.g ERS4858671"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "experiment_accession": {
            "examples": ["e.g ERX4331406"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "run_accession": {
            "examples": ["e.g ERX4331406"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "submission_accession": {
            "examples": ["e.g ERA2794974"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "read_count": {
            "examples": ["e.g 837055"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "read_length": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "base_count": {
            "examples": ["e.g 503907110"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "first_public": {
            "examples": ["e.g 2020-08-07"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "last_updated": {
            "examples": ["e.g 2020-07-29"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA",
            "format":"date"
        },
        "experiment_title": {
            "examples": ["e.g Illumina MiSeq paired end sequencing"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "study_title": {
            "examples": ["e.g SARS-CoV-2 genomes from late April in Stockholm"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "study_alias": {
            "examples": ["e.g Sweden"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "experiment_alias": {
            "examples": ["e.g ena-STUDY-KAROLINSKA INSITUTET-29-07-2020-14:18:07:925-2092"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "run_alias": {
            "examples": ["e.g ena-EXPERIMENT-KAROLINSKA INSITUTET-29-07-2020-14:50:07:151-1"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "fastq_bytes": {
            "examples": ["e.g ena-RUN-KAROLINSKA INSITUTET-29-07-2020-14:50:07:151-1"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "fastq_md5": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "fastq_ftp": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "fastq_aspera": {
            "examples": ["e.g ftp.sra.ebi.ac.uk/vol1/fastq/ERR438/005/ERR4387385/ERR4387385_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR438/005/ERR4387385/ERR4387385_2.fastq.gz"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "fastq_galaxy": {
            "examples": ["e.g fasp.sra.ebi.ac.uk:/vol1/fastq/ERR438/005/ERR4387385/ERR4387385_1.fastq.gz;fasp.sra.ebi.ac.uk:/vol1/fastq/ERR438/005/ERR4387385/ERR4387385_2.fastq.gz"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "submitted_bytes": {
            "examples": ["e.g ftp.sra.ebi.ac.uk/vol1/fastq/ERR438/005/ERR4387385/ERR4387385_1.fastq.gz;ftp.sra.ebi.ac.uk/vol1/fastq/ERR438/005/ERR4387385/ERR4387385_2.fastq.gz"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "submitted_md5": {
            "examples": ["e.g 139853010;166270048"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "submitted_ftp": {
            "examples": ["e.g d726a9abc918e2b43bd68b24c7d01b3a;f01eba1b2bad974bdf61b81b1ae8ac2a"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "submitted_aspera": {
            "examples": ["e.g ftp.sra.ebi.ac.uk/vol1/run/ERR438/ERR4387385/P17157_1007_S7_L001_R1_001.fastq.gz;ftp.sra.ebi.ac.uk/vol1/run/ERR438/ERR4387385/P17157_1007_S7_L001_R2_001.fastq.gz"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "submitted_galaxy": {
            "examples": ["e.g fasp.sra.ebi.ac.uk:/vol1/run/ERR438/ERR4387385/P17157_1007_S7_L001_R1_001.fastq.gz;fasp.sra.ebi.ac.uk:/vol1/run/ERR438/ERR4387385/P17157_1007_S7_L001_R2_001.fastq.gz"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "submitted_format": {
            "examples": ["e.g  ftp.sra.ebi.ac.uk/vol1/run/ERR438/ERR4387385/P17157_1007_S7_L001_R1_001.fastq.gz;ftp.sra.ebi.ac.uk/vol1/run/ERR438/ERR4387385/P17157_1007_S7_L001_R2_001.fastq.gz"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "sra_bytes": {
            "examples": ["e.g FASTQ;FASTQ"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "sra_md5": {
            "examples": ["e.g 260236789"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "sra_ftp": {
            "examples": ["e.g 2cf0d467d6dc4ae0a5473774d54c059c"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "sra_aspera": {
            "examples": ["e.g ftp.sra.ebi.ac.uk/vol1/err/ERR438/005/ERR4387385"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "sra_galaxy": {
            "examples": ["e.g fasp.sra.ebi.ac.uk:/vol1/err/ERR438/005/ERR4387385"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "broker_name": {
            "examples": ["P17157_1007"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "nominal_sdev": {
            "examples": [""],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "first_created": {
            "examples": ["e.g 2020-08-07"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "",
            "clasification":"Submission ENA"
        },
        "type": {
            "examples": ["betacoronavirus"],
            "ontology": "GENEPIO:0001156",
            "type": "string",
            "description": "default must remain 'betacoronavirus'",
            "clasification":"Database Identifiers"
        }
    }
}


ENA_schema.keys()

properties = ENA_schema['properties']

properties_phage = phage_schema['properties']

phage_df = pd.DataFrame.from_dict(properties_phage)

ENA_df = pd.DataFrame.from_dict(properties)

ENA_df.columns

ENA_df['geographic_location_(country_and/or_sea)']['Enums'];

p_col = phage_df.columns
lista_phage = p_col.tolist()

ENA_col = ENA_df.columns
lista_ENA = ENA_col.tolist()

# +

df = pd.DataFrame(lista_phage, columns = ['PHA4GE'])

# +

df_2 = pd.DataFrame(lista_ENA, columns = ['ENA'])
# -

#result = pd.concat([df, df_2], axis=1)
#result = df.merge(df_2, left_on ='PHA4GE', right_on = "ENA")
#result = df.merge(df_2, left_on=None)
result = df.join(df_2)

result

phage_df


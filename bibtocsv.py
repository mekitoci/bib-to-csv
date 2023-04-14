import bibtexparser
import csv

with open("sample.bib", encoding="UTF-8") as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

to_csv = bib_database.entries

keys = to_csv[0].keys()
with open("journal-list.csv", "w", newline="", encoding="UTF-8") as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(to_csv)

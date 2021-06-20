import csv
import pandas
from columns import *

data = pandas.read_csv("Obligatorisches Fach Informatik.csv")

dups = []
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[CONTACT][i] == data[CONTACT][j]:
            if (data.iloc[i, 1:].fillna(0) != data.iloc[j, 1:].fillna(0)).any():
                raise Exception("Duplicate contact with different data")
            dups.append(j)

data = data.drop(dups)
print("Ignored duplicate rows based on contact: {}".format(dups))

before = len(data)
data = data.drop_duplicates()
print("Ignored {} further duplicates".format(before - len(data)))

data = data.drop(columns=CONTACT)

data.to_csv("Obligatorisches Fach Informatik anonymized.csv",
            index=False, float_format="%.0f", quoting=csv.QUOTE_ALL, line_terminator="\r\n")

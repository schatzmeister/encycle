#! python3
# -*- coding: utf-8 -*-
"""Tools for generating lemma-description pairs from an input."""

# TODOs:
# * read from .txt files (?)
# * read from console
# * load from json
# * dump data to json
# * allow for processing entries with additional information

import openpyxl as xl
from collections import OrderedDict

def read_sheet(path):
    """Read excel sheet.
    
    Read lemma-description-pairs into an ordered dict and return it.
    """

    workbook = xl.load_workbook(path)
    sheet = workbook.get_sheet_by_name('Tabula')
    entries = OrderedDict()
    
    for row in sheet.iter_rows(row_offset=1):
        if row[0].value is None:
            continue
        elif len(str(row[0].value)) == 1:
            continue
        else:
            entries[row[0].value] = row[4].value
        
    return entries

import os
import subprocess
import sys
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
from collections import defaultdict


def xml_first():
    # pdf2xml to get the xml first
    try:
        obj = subprocess.Popen(
            ["pdftohtml", "-xml", "canopy_technical_test_input.pdf", "canopy_technical_test_output.xml"],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        out, err = obj.communicate()
    except:
        print("an exception occured " + str(sys.exc_info()))


def xml_to_dataframe(xml_root, table_cell_props, total_no_of_rows):
    # table data is with font size 3.
    # each cell data is determined with 'LEFT' attribute reference.
    table_data = defaultdict(list)
    # col_vs_cell_prop = list(zip(range(len(table_cell_props.keys())), table_cell_props.keys()))

    row_num = 0
    for item in xml_root.findall('./page'):
        prev_cell_prop = sys.maxsize
        for child in item:
            if child.tag == 'text' and child.attrib['font'] == '3':
                for cell_prop in table_cell_props:
                    # check for the range to see which column it fits
                    if int(child.attrib['left']) < int(prev_cell_prop):
                        row_num += 1
                    if int(child.attrib['left']) in range(int(cell_prop) - 30, int(cell_prop) + 30):
                        table_data[table_cell_props[cell_prop]].append({str(row_num): child.text})
                    prev_cell_prop = child.attrib['left']

                    # prev_cell_prop = child.attrib['left']
    print(table_data)


def parse_xml_file():
    # check whether xml file has been created or not
    if os.path.isfile('./canopy_technical_test_output.xml'):
        table_headings = list()
        table_headings_references = dict()

        # create element tree object
        tree = ET.parse('canopy_technical_test_output.xml')
        # get root element
        root = tree.getroot()

        # table uses different format styles. Here in the example, font size 2 and 3 has been used for table.
        # font '2' : table heading
        # font '3': table data
        # the entire logic is based on referencing 'LEFT' attribute of table cell properties.

        no_of_rows = 0
        for item in root.findall('./page'):
            for child in item:
                if child.tag == 'text':
                    if child.attrib['font'] == '2':
                        table_headings.append(child.text)
                        table_headings_references[child.attrib['left']] = child.text
                    elif child.attrib['font'] == '3':
                        no_of_rows += 1
        xml_to_dataframe(root, table_headings_references, no_of_rows)
    else:
        print('You need to generate the xml file')


if __name__ == '__main__':
    # xml_first()
    parse_xml_file()

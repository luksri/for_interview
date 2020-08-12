import os
import subprocess
import sys
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
from dateutil.parser import parse


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

    df = pd.DataFrame('', index=range(total_no_of_rows),
                      columns=['Booking Date', 'Txn Date', 'Booking Text', 'Value Date',
                               'Debit', 'Credit', 'Balance'])

    row_num = -1
    for item in xml_root.findall('./page'):
        prev_cell_prop = sys.maxsize
        for child in item:
            if child.tag == 'text' and child.attrib['font'] == '3':
                if int(child.attrib['left']) < int(prev_cell_prop):
                    row_num += 1
                for cell_prop in table_cell_props:
                    # check for the range to see which column it fits
                    if int(child.attrib['left']) in range(int(cell_prop) - 55, int(cell_prop) + 55):
                        # print(df.loc[row_num, table_cell_props[cell_prop]], child.text)
                        if df.loc[row_num, table_cell_props[cell_prop]]:
                            df.loc[row_num, table_cell_props[cell_prop]] += '\r\n' + child.text
                        else:
                            df.loc[row_num, table_cell_props[cell_prop]] = child.text
                    prev_cell_prop = child.attrib['left']
    return df


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
        return xml_to_dataframe(root, table_headings_references, no_of_rows)
    else:
        print('You need to generate the xml file')
        return


def format_date(entry):
    try:
        obj = parse(entry)
        return obj.strftime('%Y/%m/%d')
    except:
        # print('exception is ' + str(sys.exc_info()))
        pass


def format_int(entry):
    try:
        entry = entry.replace(',', '')
        entry = int(float(str(entry)))
        return entry
    except:
        # print('exception is ' + str(sys.exc_info()))
        pass


def format_output(df):
    df['Booking Date'] = df['Booking Date'].map(format_date)
    df['Txn Date'] = df['Txn Date'].map(format_date)
    df['Value Date'] = df['Value Date'].map(format_date)
    df['Debit'] = df['Debit'].map(format_int)
    df['Credit'] = df['Credit'].map(format_int)
    df['Balance'] = df['Balance'].map(format_int)
    df.to_excel('output.xlsx', index=False)


if __name__ == '__main__':
    xml_first()
    df = parse_xml_file()
    df.replace('', np.nan, inplace=True)
    df.dropna(axis=0, how='all', inplace=True)
    df.replace(np.nan, '', inplace=True)
    if not df.empty:
        format_output(df)
    print("you can check the output now")

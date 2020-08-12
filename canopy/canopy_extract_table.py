import os
import subprocess
import sys
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
from dateutil.parser import parse


def generate_pdf_to_xml():
    """
    Function to create the xml from a PDF using Poppler utilities.
    :return: None. Generates the xml file in the current working directory.
    """
    # pdf2xml to get the xml first
    try:
        obj = subprocess.Popen(
            ["pdftohtml", "-xml", "canopy_technical_test_input.pdf", "canopy_technical_test_output.xml"],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        out, err = obj.communicate()
    except Exception as e:
        print("an exception occured " + str(e))


def pdf_table_recreate(xml_root, table_cell_props, total_no_of_rows):
    """
    Function to recreate the table in PDF. Table contents have fixed attributes in xml such as
    'font' -  3 is for table data. Rest can be ignored.
    For Recreation, we should take a reference. In XML:
        <text top="XXX" left="XXX" width="XXX" height="XXX" font="X">
    This function considered 'LEFT' as reference to fill the table data. In order to fill all the columns of the table,
    we extracted the 'LEFT' attributes of the table headings. while processing the each xml tag, each of the 'LEFT' value
    is compared whether it falls in certain range. For example: this function considered 'LEFT'-55 and 'LEFT'+55 as range.
    if true, we fill the table with the data.

    :param xml_root: XML object
    :param table_cell_props: a dict of table headings with their 'LEFT' attribute values.
    :param total_no_of_rows: no of rows table data in xml file.
    :return: returns Pandas Dataframe contains entire table data.
    """
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
                        if df.loc[row_num, table_cell_props[cell_prop]]:
                            df.loc[row_num, table_cell_props[cell_prop]] += '\r\n' + child.text
                        else:
                            df.loc[row_num, table_cell_props[cell_prop]] = child.text
                    prev_cell_prop = child.attrib['left']
    return df


def parse_xml_file():
    """
    Function to parse the xml file. Table contents have fixed attributes in xml such as
    'font' - 2 is for table headings. Rest can be ignored.
    :return: pandas Dataframe with recreated table data
    """
    # check whether xml file has been created or not
    if os.path.isfile('./canopy_technical_test_output.xml'):
        table_headings = list()
        table_headings_references = dict()

        # create element tree object
        tree = ET.parse('canopy_technical_test_output.xml')
        # get root element
        root = tree.getroot()

        no_of_rows = 0
        for item in root.findall('./page'):
            for child in item:
                if child.tag == 'text':
                    if child.attrib['font'] == '2':
                        table_headings.append(child.text)
                        table_headings_references[child.attrib['left']] = child.text
                    elif child.attrib['font'] == '3':
                        no_of_rows += 1
        return pdf_table_recreate(root, table_headings_references, no_of_rows)
    else:
        print('You need to generate the xml file')
        return


def format_date(entry):
    """
    Function to format the date in YYYY/mm/dd
    :param entry: pandas series element to change the format
    :return: date as string
    """
    try:
        obj = parse(entry)
        return obj.strftime('%Y/%m/%d')
    except Exception as e:
        # print('exception is ' + str(e))
        pass


def format_int(entry):
    """
     Function to format the float of number to integer
    :param entry: pandas series element to change the format
    :return: int
    """
    try:
        entry = entry.replace(',', '')
        entry = int(float(str(entry)))
        return entry
    except Exception as e:
        # print('exception is ' + str(e))
        pass


def format_output(df):
    """
    Function to format the recreated table according to problem statement.
    :param df: pandas dataframe contains recreated table data
    :return: None. output is written to excel sheet.
    """
    df['Booking Date'] = df['Booking Date'].map(format_date)
    df['Txn Date'] = df['Txn Date'].map(format_date)
    df['Value Date'] = df['Value Date'].map(format_date)
    df['Debit'] = df['Debit'].map(format_int)
    df['Credit'] = df['Credit'].map(format_int)
    df['Balance'] = df['Balance'].map(format_int)
    df.to_excel('output.xlsx', index=False)


if __name__ == '__main__':
    generate_pdf_to_xml()
    df = parse_xml_file()
    df.replace('', np.nan, inplace=True)
    df.dropna(axis=0, how='all', inplace=True)
    df.replace(np.nan, '', inplace=True)
    if not df.empty:
        format_output(df)
    print("you can check the output now")

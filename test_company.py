'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import sys
import os
import numpy as np

cabin_block = {}
cabin_block_index = 0
number_of_passengers = 0
formatted_inputs = []
number_of_blocks = 0
max_of_rows = 0
original_shape = {}
blocks_with_window = []
rows = []
cols = []


def create_blocks(row, col):
    global cabin_block_index
    cabin_block[cabin_block_index] = np.full((row, col), '---', dtype=str)
    cabin_block_index = cabin_block_index + 1


def get_inputs():
    global number_of_passengers
    global formatted_inputs
    inputs = sys.stdin.readlines()
    formatted_inputs = []
    for each in inputs:
        if '\n' in each:
            formatted_inputs.append(each[:each.find(r'\n')])
        else:
            formatted_inputs.append(each)

    number_of_passengers = int(formatted_inputs.pop(0))


def fill_blocks():
    global formatted_inputs
    global number_of_blocks
    global max_of_rows
    global original_shape
    global rows
    global cols

    number_of_blocks = len(formatted_inputs)
    # rows = []
    # cols = []

    for i in range(0, len(formatted_inputs)):
        each = formatted_inputs[i].replace(' ', ',')
        each = each.split(',')
        cols.append(int(each[0]))
        rows.append(int(each[1]))
        original_shape[i] = (int(each[1]), int(each[0]))

    max_of_rows = max(rows)
    for each in cols:
        create_blocks(max_of_rows, int(each))


def fill_window_blocks():
    global blocks_with_window

    if (len(cabin_block.keys()) == 1):
        blocks_with_window = [0]
    else:
        blocks_with_window = [0, len(cabin_block.keys()) - 1]

    block_count = 0

    for each_block in blocks_with_window:
        shape_of_block = original_shape[each_block]
        max_allowed_fill = shape_of_block[0]  # cant fill more than the dimesion

        block_data = cabin_block[each_block]

        if shape_of_block[0] == 1 and shape_of_block[1] == 1:
            to_fill = 'A'
        else:
            to_fill = 'W'

        for row_id in range(0, shape_of_block[0]):

            if row_id > max_allowed_fill:
                break
            else:
                # print('enterd to else part')
                # print(block_data[row_id][0])
                if block_count == 0:
                    block_data[row_id][0] = to_fill
                else:
                    block_data[row_id][-1] = to_fill
        block_count = block_count + 1
        block_data = []


def fill_aisle_seats():
    window_block_count = 0
    for each_block in range(0, len(cabin_block.keys())):
        shape_of_block = original_shape[each_block]
        max_allowed_fill = shape_of_block[0]

        block_data = cabin_block[each_block]

        for row_id in range(0, shape_of_block[0]):
            if row_id > max_allowed_fill:
                break
            else:
                # if window block
                # print(blocks_with_window)
                if each_block in blocks_with_window:
                    if window_block_count == 0:
                        col_id = shape_of_block[1] - 1
                        window_block_count = window_block_count + 1
                    else:
                        col_id = 0

                    if block_data[row_id][col_id] == '-':
                        block_data[row_id][col_id] = 'A'
                    else:
                        pass
                # if not a window block
                else:
                    block_data[row_id][0] = 'A'
                    block_data[row_id][-1] = 'A'

        block_data = []


def fill_center_seats():
    for each_block in range(0, len(cabin_block.keys())):
        shape_of_block = original_shape[each_block]
        max_allowed_fill = shape_of_block[0]

        block_data = cabin_block[each_block]
        for row_id in range(0, shape_of_block[0]):
            if row_id > max_allowed_fill:
                break
            else:
                for col_id in range(0, shape_of_block[1]):
                    if block_data[row_id][col_id] == '-':
                        block_data[row_id][col_id] = 'C'
                    else:
                        pass
    block_data = []


def fill_AWC():
    fill_window_blocks()
    fill_aisle_seats()
    fill_center_seats()


def fill_passengers():
    global number_of_passengers

    pass_count = 0
    while (number_of_passengers):
        '''if pass_count <10:
            pass_string = '00'+str(pass_count)

        elif pass_count < 100:
            pass_string = '0'+ str(pass_count)

        else:
            pass_string = str(pass_count)'''
        pass_has_to_be_in = ['A', 'W', 'C']
        pass_string = pass_count
        # iterate through row wise
        # print(pass_count)

        for each in pass_has_to_be_in:
            print(pass_string)
            try:
                for row_id in range(0, max_of_rows):
                    #                   print('entered 2')
                    try:
                        # try for the rowwise
                        for each_block in range(0, len(cabin_block.keys())):
                            #                          print('entered 3')
                            try:
                                # try for all the blocks
                                data_block = cabin_block[each_block]
                                shape_is = original_shape[each_block]
                                for col_id in range(0, shape_is[1]):
                                    #                                 print('entered 4')
                                    # aisle seat fist
                                    #                                print(row_id,col_id)
                                    try:
                                        if data_block[row_id][col_id] == each:
                                            data_block[row_id][col_id] = pass_string
                                        else:
                                            pass
                                    except:  # breaks at index out of bound error
                                        ## if there is no aisle seat skip to next block
                                        break

                            except:
                                ## skip to next row
                                break
                    except:
                        continue
            except:
                continue

        '''for each_block in range(0, len(cabin_block.keys())):
            block_data = cabin_block[each_block]
            shape_of_block = original_shape[each_block]


            #for row_id in range()

            block_data = []
        '''
        pass_count = pass_count + 1
        number_of_passengers = number_of_passengers - 1


get_inputs()
fill_blocks()
fill_AWC()
fill_passengers()
print(cabin_block)
# Strathclyde University
# CS814 - Artificial Intellgience For Autonomous Systems
# Lab 1
# Exercise 2 : The Great Python Triangle Challenge of 2019

import math

# This function reads in a text file that contains a triangle
def read_triangle_from_file(path, file_name):
    # Construct fully specified name
    file_to_open = path + file_name
    # Open the file in read mode
    file = open(file_to_open, "r")
    # Prepare empty list into which we'll inject the data from the file
    triangle_list = []
    # Step through each line in in the source file
    for line in file:
        # Split each item in the line into a seperate list element
        line_list_of_string = line.split()
        # The file is read as a list of strings, so convert it to a list of integers
        line_list_of_int = list(map(int, line_list_of_string))
        # Append the resulting list for that line to the triangle_list to create a list of lists that is triangular in shape
        triangle_list.append(line_list_of_int)
    return triangle_list

# This function applies what I can see is the most efficient way of finding the optimal route through the triangle that creates the maximum result
def roll_up_triangle_from_bottom(source_triangle):
    # Create empty lists (that will ultimately be a list of lists) into which I'm going to write:
    # A. A triangle that represents what I'm calling the "rolled up sum" working up through the levels of the triangle;
    # B. The "solution" chosen to create the maximum rolled up sum at each level in the triangle - not sure if I'm going to need this, but I'm capturing it anyhow!
    rolled_up_sum_triangle = []
    solution_triangle = []

    # This for descending loop counts backwards from the bottom row of the triangle to the top
    triangle_depth = len(source_triangle)
    for line_counter in range(triangle_depth, 0, -1):
        # Create empty lists so that we can build a new row that will ultimately be inserted to build the traingle up in layers
        solution_line_builder = []
        rolled_up_sum_line_builder = []
        if line_counter == triangle_depth:
            # We are at base of the triangle, so just capture the entire row of values to create the bottom row of the rolled up summ triangle
            rolled_up_sum_line_builder = source_triangle[line_counter - 1]
            # We can also construct a placeholder row for the bottom row of the solution triangle...
            for i in range(0, line_counter):
                solution_line_builder.append(0)
        else:
            # We are dealing with a row other than the bottom row!
            # So we need to step through each item in that row from left to right
            for line_position in range(0, line_counter):
                # First we pluck the number out of the list at this position in the row
                this_number = source_triangle[line_counter - 1][line_position]
                # Them we sum it with both of the two rolled up sum options from the row below
                option1_position = line_position
                option2_position = line_position + 1
                option1_number = this_number + rolled_up_sum_triangle[0][option1_position]
                option2_number = this_number + rolled_up_sum_triangle[0][option2_position]
                # Then we set the rolled up sum at this position to the maximum of option 1 or 2, and record the option position we chose
                if option1_number >= option2_number:
                    solution_line_builder.append(option1_position)
                    rolled_up_sum_line_builder.append(option1_number)
                else:
                    solution_line_builder.append(option2_position)
                    rolled_up_sum_line_builder.append(option2_number)
        # Insert the new row into the start of the rolled up sum list to build the triangle back up from bottom to top
        rolled_up_sum_triangle.insert(0, rolled_up_sum_line_builder)
        solution_triangle.insert(0, solution_line_builder)
        max_sum = rolled_up_sum_triangle[0][0]
    return rolled_up_sum_triangle, solution_triangle, max_sum
    
# This function then decodes the solution triangle into a set of coordinates that walks you through the optimal solution, it also publishes a "masked version" of the source triangle
def build_solution(source_triangle, solution_triangle):
    # Create empty solution list
    solution = []
    source_triangle_masked = []
    next_element = 0
    rolling_sum = 0
    for row_counter in range(0, len(source_triangle)):
        # Build the solution description
        element_value = source_triangle[row_counter][next_element]
        rolling_sum = rolling_sum + element_value
        solution_element = { 'row': row_counter + 1, 'element': next_element + 1, 'value': element_value, 'rolling_sum': rolling_sum }
        solution.append(solution_element)
        # Create a "masked" version of the source triangle for visualisation purposes
        source_triangle_masked_line_builder = []
        for element_count in range(0, len(source_triangle[row_counter])):
            if element_count == next_element:
                source_triangle_masked_line_builder.append(source_triangle[row_counter][next_element])
            else:
                source_triangle_masked_line_builder.append(0)
        source_triangle_masked.append(source_triangle_masked_line_builder)
        # Key step is to point the next iteration to the element from the next row that was used to generate the optimal result
        next_element = solution_triangle[row_counter][next_element]
    return solution, source_triangle_masked

def print_triangle(triangle):
    # Scan the triangle to figure out the maximum number of characters in an element
    maximum_value = 0
    triangle_depth = len(triangle)
    for row in range(0, triangle_depth):
        maximum_value_in_row = max(triangle[row])
        if maximum_value_in_row > maximum_value:
            maximum_value = maximum_value_in_row
    maximum_digits = int(math.log10(maximum_value)) + 1
    print('Maximum value found:', maximum_value, ' digits: ', maximum_digits)
    # Calculate the cell spacing
    cell_spacing = maximum_digits - 2
    # Calulcate the offset
    if maximum_digits <= 2:
        offset = 0
    else:
        offset = 1
    # Print each line out applying initial ident and spacing as appropriate
    for row_count in range (0, triangle_depth):
        indent = (triangle_depth - row_count - 1) * (maximum_digits - offset)
        print(' ' * indent, end='', sep='')
        spacer = 0
        if maximum_digits <= 2:
            spacer = maximum_digits
        else:
            spacer = maximum_digits - 2
        for element_count in range(0, len(triangle[row_count])):
            if triangle[row_count][element_count] == 0:
                element = '[' + (' ' * (maximum_digits - 2)) + ']'
            else:
                element = str(triangle[row_count][element_count]).zfill(maximum_digits)
            print(element, ' ' * (spacer), end='', sep='')
        print('', flush=True)
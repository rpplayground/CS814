import io

def open_triangle_file(file_name):
    # Construct fully specified name
    file_path = "c:/Users/Barry/Documents/GitHub/CS814/Exercise2Triangle/"
    file_to_open = file_path + file_name
    # Open the file in read mode
    file = open(file_to_open, "r")
    # Prepare empty list into which we'll inject the data from the file
    triangle_list = []
    # Step through each line in in the source file
    for line in file:
        # Split each item in the line into a seperate list element
        line_list = line.split()
        # Append the resulting list for that line to the triangle_list to create a list of lists that is triangular in shape
        triangle_list.append(line_list)
    return triangle_list

triangle_list_from_file = open_triangle_file("triangle_numbers_2.txt")

def roll_up_triangle_from_bottom(source_triangle):
    # Create empty list (that will ultimately be a list of lists) into which I'm going to write:
    # A. The rolled up sum working up through the levels of the triangle;
    # B. The "solution" chosen to create the maximum rolled up sum at each level in the triangle - not sure if I'm going to need this, but I'm capturing it anyhow!
    rolled_up_sum_triangle = []
    solution_triangle = []

    # This for loop counts backwards from the bottom of the triangle to the top
    triangle_depth = len(source_triangle)
    for line_counter in range(triangle_depth, 0, -1):
        # Create empty lists so that we can build each row from scratch
        solution_line_builder = []
        rolled_up_sum_line_builder = []
        if line_counter == triangle_depth:
            # We are at base of the triangle, so just capture the entire row of values to create the bottom row of the rolled up summ triangle
            rolled_up_sum_line_builder = list(map(int, source_triangle[line_counter - 1]))
            # We can also construct a redundant solution row for the bottom row of the triangle...
            for i in range(0, line_counter):
                solution_line_builder.append(0)
        else:
            # We are walkindealing with a row other than the bottom row!
            # So we need to step through each item in that row from left to right
            for line_position in range(0, line_counter):
                # First we pluck the number out of the list at this position in the row
                this_number = int(source_triangle[line_counter][line_position])
                # Them we sum it with both of the two rolled up sum options from the row below
                option1_position = line_position
                option2_position = line_position + 1
                option1_number = this_number + int(rolled_up_sum_triangle[0][option1_position])
                option2_number = this_number + int(rolled_up_sum_triangle[0][option2_position])
                # Then we set the rolled up sum at this position to the maximum of option 1 or 2, and record the option position we chose
                if option1_number >= option2_number:
                    solution_line_builder.append(option1_position)
                    rolled_up_sum_line_builder.append(option1_number)
                else:
                    solution_line_builder.append(option2_position)
                    rolled_up_sum_line_builder.append(option2_number)
        # Insert the new row into the start of the rolled up sum list to build the triangle back up from bottom to top
        rolled_up_sum_triangle.insert(0, rolled_up_sum_line_builder)
        # print(rolled_up_sum_line_builder)
        solution_triangle.insert(0, solution_line_builder)
    return rolled_up_sum_triangle, solution_triangle
    
rolled_up_sum_triangle, solution_triangle = roll_up_triangle_from_bottom(triangle_list_from_file)

def build_solution(source_triangle, solution_triangle):
    solution = []
    next_element = 0
    for row_counter in range(0, len(source_triangle)):
        solution.append(source_triangle[row_counter][next_element])
        next_element = solution_triangle[row_counter][next_element]
    return solution

solution_path = build_solution(triangle_list_from_file, solution_triangle)

print('--- Source triangle:')
for i in range (0, len(triangle_list_from_file)):
    print(triangle_list_from_file[i])
print('--- Maximum sum:', rolled_up_sum_triangle[0][0])
print('--- Solution:')
print(solution_path)
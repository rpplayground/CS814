import io

def open_triangle_file(file_name):
    file_path = "c:/Users/Barry/Documents/GitHub/CS814/Exercise2Triangle/"
    file_to_open = file_path + file_name
    print("Opening file:", file_to_open)
    file = open(file_to_open, "r")
    line_counter = 1
    triangle_list = []
    for line in file:
        line_list = line.split()
        triangle_list.append(line_list)
    return triangle_list

triangle_list_from_file = open_triangle_file("triangle_numbers_2.txt")

def find_maximum_path(triangle_list):
    number_of_lines = len(triangle_list)
    print("Number of lines to process:", number_of_lines)
    position_in_line = 1
    seed_number = int(triangle_list[0][0])
    path_list = [seed_number]
    running_total = seed_number
    for line_counter in range(1, number_of_lines):
        next_line_counter = line_counter + 1
        first_number_position = position_in_line
        second_number_position = position_in_line + 1
        first_number = int(triangle_list[next_line_counter - 1][first_number_position - 1])
        second_number = int(triangle_list[next_line_counter -1][second_number_position - 1])
        if first_number >= second_number:
            position_in_line = first_number_position
            next_number = first_number
        else:
            position_in_line = second_number_position
            next_number = second_number
        print('Index: ', next_line_counter, position_in_line, next_number)
        path_list.append(next_number)
        print('Path list: ', path_list)
        running_total = running_total + next_number
        print('Running total: ', running_total)
    return path_list

solution_pathway = find_maximum_path(triangle_list_from_file)

print(solution_pathway)



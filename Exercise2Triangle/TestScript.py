from TriangleFunctions import *

triangle_list_from_file = read_triangle_from_file("c:/Users/Barry/Documents/GitHub/CS814/Exercise2Triangle/", "triangle_numbers_1.txt")

rolled_up_sum_triangle, solution_triangle, max_sum = roll_up_triangle_from_bottom(triangle_list_from_file)

solution_path, source_triangle_masked = build_solution(triangle_list_from_file, solution_triangle)

print_triangle(triangle_list_from_file)

print_triangle(rolled_up_sum_triangle)

print_triangle(source_triangle_masked)

print('--- Maximum sum:', rolled_up_sum_triangle[0][0])
print('--- Solution:')
for i in range (0, len(solution_path)):
    print(solution_path[i])
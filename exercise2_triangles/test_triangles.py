import exercise2_triangles.triangle_functions

def test_file_load():
    path_string = "C:/Users/Barry/Documents/GitHub/CS814/exercise2_triangles/"
    file_name = "triangle_numbers_0.txt"
    expected_output_0 = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
    assert exercise2_triangles.triangle_functions.read_triangle_from_file(path_string, file_name) == expected_output_0
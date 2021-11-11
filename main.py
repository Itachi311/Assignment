from itertools import permutations


def sudoku(list_of_colors: list):
    """

    :param list_of_colors:list
    """
    result_matrix = []
    matrix_size = len(list_of_colors)
    if list_of_colors:
        for permutation in permutations(list_of_colors, matrix_size):
            if not result_matrix:  # The first permutation is added
                result_matrix.append(list(permutation))
                continue

            is_valid_list = []
            for row in result_matrix:
                is_valid = all(permutation[index] != row[index] for index in range(matrix_size))
                is_valid_list.append(is_valid)

            if all(is_valid_list):
                result_matrix.append([perm for perm in permutation])
    else:
        return -1

    return result_matrix


if __name__ == '__main__':
    test_cases =[
        ["red", "blue", "yellow", "green", "black", "white"],
        ["red", "blue", "yellow"],
        [],
        [1, 2, 3, 4, 5, 6],
    ]
    for test in test_cases:
        print(sudoku(test))


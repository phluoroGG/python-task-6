from PIL import Image
import numpy as np
import copy


def calc_avg_black(array, _low_bound_x=0, _high_bound_x=0, _low_bound_y=0, _high_bound_y=0):
    if _high_bound_x == 0:
        _high_bound_x = len(array[0])
    if _high_bound_y == 0:
        _high_bound_y = len(array)
    black_count = 0
    for _col in range(_low_bound_x, _high_bound_x):
        for _row in range(_low_bound_y, _high_bound_y):
            if not array[_row][_col]:
                black_count += 1
    return black_count / (_high_bound_x - _low_bound_x) / (_high_bound_y - _low_bound_y)


def find_max_length(array):
    max_length = 0
    for _row in range(len(array)):
        max_length = max(len(array[_row]), max_length)
    return max_length


def draw_number(array, number, bias_x, bias_y):
    if number == 0:
        array[bias_y][bias_x] = False
        array[bias_y][bias_x + 1] = False
        array[bias_y][bias_x + 2] = False
        array[bias_y + 1][bias_x + 2] = False
        array[bias_y + 2][bias_x + 2] = False
        array[bias_y + 3][bias_x + 2] = False
        array[bias_y + 4][bias_x + 2] = False
        array[bias_y + 5][bias_x + 2] = False
        array[bias_y + 6][bias_x + 2] = False
        array[bias_y + 7][bias_x + 2] = False
        array[bias_y + 7][bias_x + 1] = False
        array[bias_y + 7][bias_x] = False
        array[bias_y + 6][bias_x] = False
        array[bias_y + 5][bias_x] = False
        array[bias_y + 4][bias_x] = False
        array[bias_y + 3][bias_x] = False
        array[bias_y + 2][bias_x] = False
        array[bias_y + 1][bias_x] = False
    elif number == 1:
        array[bias_y + 2][bias_x] = False
        array[bias_y + 1][bias_x + 1] = False
        array[bias_y][bias_x + 2] = False
        array[bias_y + 1][bias_x + 2] = False
        array[bias_y + 2][bias_x + 2] = False
        array[bias_y + 3][bias_x + 2] = False
        array[bias_y + 4][bias_x + 2] = False
        array[bias_y + 5][bias_x + 2] = False
        array[bias_y + 6][bias_x + 2] = False
        array[bias_y + 7][bias_x + 2] = False
    elif number == 2:
        array[bias_y + 1][bias_x] = False
        array[bias_y][bias_x] = False
        array[bias_y][bias_x + 1] = False
        array[bias_y][bias_x + 2] = False
        array[bias_y + 1][bias_x + 2] = False
        array[bias_y + 2][bias_x + 2] = False
        array[bias_y + 3][bias_x + 2] = False
        array[bias_y + 4][bias_x + 1] = False
        array[bias_y + 5][bias_x] = False
        array[bias_y + 6][bias_x] = False
        array[bias_y + 7][bias_x] = False
        array[bias_y + 7][bias_x + 1] = False
        array[bias_y + 7][bias_x + 2] = False
    elif number == 3:
        array[bias_y][bias_x] = False
        array[bias_y + 3][bias_x] = False
        array[bias_y + 7][bias_x] = False
        array[bias_y][bias_x + 1] = False
        array[bias_y + 3][bias_x + 1] = False
        array[bias_y + 7][bias_x + 1] = False
        array[bias_y][bias_x + 2] = False
        array[bias_y + 1][bias_x + 2] = False
        array[bias_y + 2][bias_x + 2] = False
        array[bias_y + 3][bias_x + 2] = False
        array[bias_y + 4][bias_x + 2] = False
        array[bias_y + 5][bias_x + 2] = False
        array[bias_y + 6][bias_x + 2] = False
        array[bias_y + 7][bias_x + 2] = False
    elif number == 4:
        array[bias_y][bias_x] = False
        array[bias_y + 1][bias_x] = False
        array[bias_y + 2][bias_x] = False
        array[bias_y + 3][bias_x] = False
        array[bias_y + 4][bias_x] = False
        array[bias_y + 4][bias_x + 1] = False
        array[bias_y][bias_x + 2] = False
        array[bias_y + 1][bias_x + 2] = False
        array[bias_y + 2][bias_x + 2] = False
        array[bias_y + 3][bias_x + 2] = False
        array[bias_y + 4][bias_x + 2] = False
        array[bias_y + 5][bias_x + 2] = False
        array[bias_y + 6][bias_x + 2] = False
        array[bias_y + 7][bias_x + 2] = False
    elif number == 5:
        array[bias_y][bias_x] = False
        array[bias_y][bias_x + 1] = False
        array[bias_y][bias_x + 2] = False
        array[bias_y + 1][bias_x] = False
        array[bias_y + 2][bias_x] = False
        array[bias_y + 3][bias_x] = False
        array[bias_y + 3][bias_x + 1] = False
        array[bias_y + 3][bias_x + 2] = False
        array[bias_y + 4][bias_x + 2] = False
        array[bias_y + 5][bias_x + 2] = False
        array[bias_y + 6][bias_x + 2] = False
        array[bias_y + 7][bias_x + 2] = False
        array[bias_y + 7][bias_x + 1] = False
        array[bias_y + 7][bias_x] = False
    elif number == 6:
        array[bias_y][bias_x] = False
        array[bias_y + 1][bias_x] = False
        array[bias_y + 2][bias_x] = False
        array[bias_y + 3][bias_x] = False
        array[bias_y + 4][bias_x] = False
        array[bias_y + 5][bias_x] = False
        array[bias_y + 6][bias_x] = False
        array[bias_y + 7][bias_x] = False
        array[bias_y][bias_x + 2] = False
        array[bias_y + 3][bias_x + 2] = False
        array[bias_y + 4][bias_x + 2] = False
        array[bias_y + 5][bias_x + 2] = False
        array[bias_y + 6][bias_x + 2] = False
        array[bias_y + 7][bias_x + 2] = False
        array[bias_y][bias_x + 1] = False
        array[bias_y + 3][bias_x + 1] = False
        array[bias_y + 7][bias_x + 1] = False
    elif number == 7:
        array[bias_y][bias_x] = False
        array[bias_y][bias_x + 1] = False
        array[bias_y][bias_x + 2] = False
        array[bias_y + 1][bias_x + 2] = False
        array[bias_y + 2][bias_x + 2] = False
        array[bias_y + 3][bias_x + 1] = False
        array[bias_y + 4][bias_x + 1] = False
        array[bias_y + 5][bias_x] = False
        array[bias_y + 6][bias_x] = False
        array[bias_y + 7][bias_x] = False
    elif number == 8:
        array[bias_y][bias_x] = False
        array[bias_y + 1][bias_x] = False
        array[bias_y + 2][bias_x] = False
        array[bias_y + 3][bias_x] = False
        array[bias_y + 4][bias_x] = False
        array[bias_y + 5][bias_x] = False
        array[bias_y + 6][bias_x] = False
        array[bias_y + 7][bias_x] = False
        array[bias_y][bias_x + 2] = False
        array[bias_y + 1][bias_x + 2] = False
        array[bias_y + 2][bias_x + 2] = False
        array[bias_y + 3][bias_x + 2] = False
        array[bias_y + 4][bias_x + 2] = False
        array[bias_y + 5][bias_x + 2] = False
        array[bias_y + 6][bias_x + 2] = False
        array[bias_y + 7][bias_x + 2] = False
        array[bias_y][bias_x + 1] = False
        array[bias_y + 3][bias_x + 1] = False
        array[bias_y + 7][bias_x + 1] = False
    elif number == 9:
        array[bias_y][bias_x] = False
        array[bias_y + 1][bias_x] = False
        array[bias_y + 2][bias_x] = False
        array[bias_y + 3][bias_x] = False
        array[bias_y + 7][bias_x] = False
        array[bias_y][bias_x + 2] = False
        array[bias_y + 1][bias_x + 2] = False
        array[bias_y + 2][bias_x + 2] = False
        array[bias_y + 3][bias_x + 2] = False
        array[bias_y + 4][bias_x + 2] = False
        array[bias_y + 5][bias_x + 2] = False
        array[bias_y + 6][bias_x + 2] = False
        array[bias_y + 7][bias_x + 2] = False
        array[bias_y][bias_x + 1] = False
        array[bias_y + 3][bias_x + 1] = False
        array[bias_y + 7][bias_x + 1] = False


def draw_numbers(array, _number, _row, _col):
    un = _number % 10
    dec = _number // 10
    bias_x = _col * 11 + 2
    bias_y = _row * 11 + 2
    draw_number(array, un, bias_x + 5, bias_y)
    if dec != 0:
        draw_number(array, dec, bias_x, bias_y)


def to_crossword(name_photo, cell_count):
    img = Image.open(name_photo)
    img = img.convert('1')
    colormap = np.asarray(img)
    x_size = colormap.shape[1]
    y_size = colormap.shape[0]
    if cell_count > x_size and cell_count > y_size:
        exit(-1)

    is_x_wider = x_size >= y_size
    coeff_x, coeff_y = 1, 1
    if is_x_wider:
        x_cell_count = cell_count
        cell_size = x_size // x_cell_count
        x_rem = x_size % x_cell_count
        y_cell_count = y_size // cell_size
        y_rem = y_size % cell_size
        coeff_y = max(y_rem // y_cell_count, 1)
    else:
        y_cell_count = cell_count
        cell_size = y_size // y_cell_count
        y_rem = y_size % y_cell_count
        x_cell_count = x_size // cell_size
        x_rem = x_size % cell_size
        coeff_x = max(x_rem // x_cell_count, 1)

    avg_black = calc_avg_black(colormap)
    value_map = []
    for i in range(x_cell_count):
        value_map.append([])
        for j in range(y_cell_count):
            low_bound_x = cell_size * i + min(coeff_x * i, x_rem)
            high_bound_x = cell_size * (i + 1) + min(coeff_x * (i + 1), x_rem)
            low_bound_y = cell_size * j + min(coeff_y * j, y_rem)
            high_bound_y = cell_size * (j + 1) + min(coeff_y * (j + 1), y_rem)
            curr_avg_black = calc_avg_black(colormap, low_bound_x, high_bound_x, low_bound_y, high_bound_y)
            is_below_average = curr_avg_black < avg_black
            value_map[i].append(is_below_average)
    array_values = np.array(value_map).transpose()

    horiz_values = []
    for col in range(x_cell_count):
        horiz_values.append([])
        val = 0
        for row in range(y_cell_count):
            if not array_values[row][col]:
                val += 1
            elif val != 0:
                horiz_values[col].append(val)
                val = 0
        if val != 0:
            horiz_values[col].append(val)

    vert_values = []
    for row in range(y_cell_count):
        vert_values.append([])
        val = 0
        for col in range(x_cell_count):
            if not array_values[row][col]:
                val += 1
            elif val != 0:
                vert_values[row].append(val)
                val = 0
        if val != 0:
            vert_values[row].append(val)

    max_horiz_length = find_max_length(horiz_values)
    max_vert_length = find_max_length(vert_values)
    x_len = (len(array_values[0]) + max_vert_length) * 11 + 1
    y_len = (len(array_values) + max_horiz_length) * 11 + 1
    array_crossword = []
    for i in range(y_len):
        array_crossword.append([])
        for j in range(x_len):
            array_crossword[i].append(i % 11 != 0 and j % 11 != 0)
    for row in range(max_horiz_length * 11):
        for col in range(max_vert_length * 11):
            array_crossword[row][col] = False

    for col in range(len(horiz_values)):
        for row in range(len(horiz_values[col])):
            number = horiz_values[col][len(horiz_values[col]) - row - 1]
            draw_numbers(array_crossword, number, max_horiz_length - row - 1, col + max_vert_length)
    for row in range(len(vert_values)):
        for col in range(len(vert_values[row])):
            number = vert_values[row][len(vert_values[row]) - col - 1]
            draw_numbers(array_crossword, number, row + max_horiz_length, max_vert_length - col - 1)

    array_solved_crossword = copy.deepcopy(array_crossword)
    for col in range(max_vert_length, max_vert_length + len(value_map)):
        for row in range(max_horiz_length, max_horiz_length + len(value_map[0])):
            for i in range(10):
                for j in range(10):
                    array_solved_crossword[row * 11 + j + 1][col * 11 + i + 1] \
                        = value_map[col - max_vert_length][row - max_horiz_length]

    image_crossword = Image.fromarray(np.array(array_crossword)).convert('1')
    image_solved_crossword = Image.fromarray(np.array(array_solved_crossword)).convert('1')
    image_crossword.save("static/crossword.png")
    image_solved_crossword.save("static/solved_crossword.png")

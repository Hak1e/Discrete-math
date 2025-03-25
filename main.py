def invert_nums(n):
    r = ""
    for ch in n:
        if ch == "0":
            r += "1"
        else:
            r += "0"
    return r


def fill_num(n, max_length):
    return "0" + "0" * (max_length - len(n)) + n


def bin_sum(n1, n2, max_length):
    result = ""
    i = max_length
    p = 0
    while i >= 0:
        a = int(n1[i])
        b = int(n2[i])
        if a + b + p == 2:
            result += "0"
            p = 1
        elif a + b + p == 3:
            result += "1"
            p = 1
        else:
            result += f"{a + b + p}"
            p = 0
        i -= 1
    if p == 1:
        result += "1"
    return result[::-1]


def add_one(value, max_index):
    result = ""
    p = 1
    while max_index >= 0:
        a = int(value[max_index])
        if a + p == 2:
            result += "0"
            p = 1
        elif a + p == 3:
            result += "1"
            p = 1
        else:
            result += f"{a + p}"
            p = 0
        max_index -= 1
    return result[::-1]


def obr_code_sum(n1, n2, max_length):
    result = bin_sum(n1, n2, max_length)

    if len(result) > max_length + 1:
        print("-" * (max_length + 1))
        print(f"{result} (переполнение)")
        result = result[1:]
        print()
        print(f"{result}\n{'0' * (len(result) - 1) + '1'}")
        new_result = ""
        i = len(result) - 1
        p = 1
        while i >= 0:
            a = int(result[i])
            if a + p == 2:
                new_result += "0"
                p = 1
            elif a + p == 3:
                new_result += "1"
                p = 1
            else:
                new_result += f"{a + p}"
                p = 0
            i -= 1
        result = new_result[::-1]
    print("=" * (max_length + 1))
    return result


def obr_code(v1, sign, v2):
    print("Обратный код")
    bin_v1 = bin(abs(v1))[2:]
    bin_v2 = bin(abs(v2))[2:]

    if sign == "+":
        dec_r = v1 + v2
        print(f"{v1} {sign} {v2} = {dec_r}")
    else:
        dec_r = v1 - v2
        print(f"{v1} {sign} {v2} = {dec_r}")

    r_len = dec_r.bit_length()
    max_length = max(len(bin_v1), len(bin_v2), r_len)
    bin_v1 = fill_num(bin_v1, max_length)
    bin_v2 = fill_num(bin_v2, max_length)
    if v1 < 0:
        bin_v1 = invert_nums(bin_v1)

    if v2 < 0:
        bin_v2 = invert_nums(bin_v2)

    if sign == "-":
        bin_v2 = invert_nums(bin_v2)

    print(f"{bin_v1} ({v1})")

    print(f"{bin_v2} ({v2})")
    print(obr_code_sum(bin_v1, bin_v2, max_length))


def dop_code_sum(n1, n2, max_length, need_correction):
    result = bin_sum(n1, n2, max_length)
    if len(result) > max_length + 1:
        result = result[1:]
    if need_correction:
        print("-" * (max_length + 1))
        print(f"{result}\n{'0' * (len(result) - 1) + '1'} (коррекция)")
        result = add_one(result, len(result) - 1)
    print("=" * (max_length + 1))
    return result


def dop_code(v1, sign, v2):
    print("Дополнительный код")
    bin_v1 = "0" + bin(abs(v1))[2:]
    bin_v2 = "0" + bin(abs(v2))[2:]
    need_correction = False
    if sign == "+":
        dec_r = v1 + v2
        print(f"{v1} {sign} {v2} = {dec_r}")
    else:
        dec_r = v1 - v2
        print(f"{v1} {sign} {v2} = {dec_r}")

    result_len = dec_r.bit_length()
    max_length = max(len(bin_v1), len(bin_v2), result_len)
    bin_v1 = fill_num(bin_v1, max_length)
    bin_v2 = fill_num(bin_v2, max_length)
    if v1 < 0:
        bin_v1 = invert_nums(bin_v1)
        bin_v1 = add_one(bin_v1, max_length)

    if v2 < 0:
        bin_v2 = invert_nums(bin_v2)
        bin_v2 = add_one(bin_v2, max_length)

    if sign == "-":
        bin_v2 = invert_nums(bin_v2)
        need_correction = True

    print(f"{bin_v1}")

    print(f"{bin_v2}")
    print(dop_code_sum(bin_v1, bin_v2, max_length, need_correction))


def fill_list(value, values_list, max_length, max_nums_len):
    result = []
    i = abs(len(str(value)) - max_length)
    if value < 0:
        result.append("1")
        if len(values_list) < max_nums_len:
            for _ in range(i):
                result.append("1100")
    else:
        result.append("0")
        if len(values_list) < max_nums_len:
            for _ in range(i):
                result.append("0011")
    for num in values_list:
        bin_value = bin(num)[2:]
        bin_value = "0" * (max_length - len(bin_value)) + bin_value
        if value < 0:
            bin_value = invert_nums(bin_value)
        result.append(bin_value)
    return result[::-1]


def izb_3(v1, sign, v2):
    print("Код с избытком 3")
    max_length = 4
    v1_lst = []
    v2_lst = []
    for num in str(abs(v1)):
        v1_lst.append(int(num) + 3)
    for num in str(abs(v2)):
        v2_lst.append(int(num) + 3)
    if sign == "+":
        result_nums_count = v1 + v2
    else:
        result_nums_count = v1 - v2
    result_lst = []
    for num in str(abs(result_nums_count)):
        result_lst.append(int(num))
    max_num_count = max(len(v1_lst), len(v2_lst), len(result_lst))
    bin_v1 = fill_list(v1, v1_lst, max_length, max_num_count)
    bin_v2 = fill_list(v2, v2_lst, max_length, max_num_count)
    if sign == "-":
        new_bin_v2 = []
        for value in bin_v2:
            tetrada = ""
            for num in value:
                if num == "0":
                    tetrada += "1"
                else:
                    tetrada += "0"
            new_bin_v2.append(tetrada)
        bin_v2 = new_bin_v2.copy()
    bin_v1.reverse()
    for i in bin_v1:
        print(i, end=" ")
    print()
    bin_v2.reverse()
    for i in bin_v2:
        print(i, end=" ")
    print()
    flagged_tetrada = []
    lst_len = len(bin_v1)
    list_position = lst_len - 1
    bin_result = []
    p = 0
    while list_position >= 0:
        result = ""
        str_value = bin_v1[list_position]
        i = len(str_value) - 1
        while i >= 0:
            a = int(bin_v1[list_position][i])
            b = int(bin_v2[list_position][i])
            if a + b + p == 2:
                result += "0"
                p = 1
            elif a + b + p == 3:
                result += "1"
                p = 1
            else:
                result += f"{a + b + p}"
                p = 0
            i -= 1
        bin_result.append(result[::-1])
        if p == 1:
            flagged_tetrada.append(list_position)
        list_position -= 1
    print("-" * (len(bin_result) * 4))
    bin_result.reverse()
    for i in bin_result:
        print(i, end=" ")
    print()
    if p == 1:
        list_position = len(bin_result) - 1
        new_bin_result = []
        while list_position >= 0:
            result = ""
            str_value = bin_result[list_position]
            i = len(str_value) - 1
            while i >= 0:
                a = int(bin_result[list_position][i])
                if a + p == 2:
                    result += "0"
                    p = 1
                elif a + p == 3:
                    result += "1"
                    p = 1
                else:
                    result += f"{a + p}"
                    p = 0
                i -= 1
            new_bin_result.append(result[::-1])
            if p == 1:
                flagged_tetrada.append(list_position)
            list_position -= 1
        new_bin_result.reverse()
        bin_result = new_bin_result.copy()
        print("Избыток 1")
        print("-" * (len(bin_result) * 4))
        for i in bin_result:
            print(i, end=" ")
        print()

    list_position = len(bin_result) - 1
    new_bin_result = []
    added_values = []
    sign_digit = bin_result[0]
    while list_position > 0:
        result = ""
        str_value = bin_result[list_position]
        if list_position in flagged_tetrada:
            add_tetrada = "0011"
        else:
            add_tetrada = "1101"
        added_values.append(add_tetrada)
        i = len(str_value) - 1
        p = 0
        while i >= 0:
            a = int(bin_result[list_position][i])
            b = int(add_tetrada[i])
            if a + b + p == 2:
                result += "0"
                p = 1
            elif a + b + p == 3:
                result += "1"
                p = 1
            else:
                result += f"{a + b + p}"
                p = 0
            i -= 1
        new_bin_result.append(result[::-1])
        list_position -= 1
    bin_result = new_bin_result.copy()
    bin_result.append(sign_digit)
    bin_result.reverse()
    added_values.append(0)
    added_values.reverse()
    for i in added_values:
        print(i, end=" ")
    print()
    print("=" * (len(bin_result) * 4))
    for i in bin_result:
        print(i, end=" ")


def main():
    print("Пример входных данных:\n\
    1 + -3\n\
    -1 + 3\n\
    1 - 3\n\
    1 - -3")
    input_data = input("Введите данные: ").split()
    v1 = int(input_data[0])
    sign = input_data[1]
    v2 = int(input_data[2])

    obr_code(v1, sign, v2)
    print()
    if not (int(input_data[0]) > 0 and input_data[1] == "+" and int(input_data[2]) > 0):
        dop_code(v1, sign, v2)
        print()
    izb_3(v1, sign, v2)


if __name__ == "__main__":
    main()

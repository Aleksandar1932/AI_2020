def swap_list(input_list):
    result = [(item2, item1) for item1, item2 in input_list]
    return result


if __name__ == '__main__':
    list_1 = [('a', 1), ('b', 2), ('c', 3)]
    print(swap_list(list_1))


def common_element(set_1, set_2):
    common_set = set()

    for elements in set_1:
        if elements in set_2:
            common_set.add(elements)
    return common_set

set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}

common_element_set = common_element(set_1, set_2)   
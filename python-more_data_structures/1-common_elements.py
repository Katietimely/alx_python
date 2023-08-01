#!/usr/bin/python3

def common_element(set_1, set_2):
    common_set = set()

    for elements in set_1:
        if elements in set_2:
            common_set.add(elements)



    return common_set

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }

common_element_set = common_element(set_1, set_2)   
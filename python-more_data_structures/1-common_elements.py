#!/usr/bin/python3

def common_element(set_1, set_2):
    common_set = set()

    for elements in set_1:
        if elements in set_2:
            common_set.add(elements)
    return common_set

if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Perl"}
    c_set = common_element(set_1, set_2)
    print(sorted(list(c_set)))
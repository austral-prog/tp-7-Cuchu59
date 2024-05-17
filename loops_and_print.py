def enumerate_list(list):
    colors = []
    a = 0
    for element in list:
        if element:
            colors.append(f"{a}. {element}")
            a += 1 
    return colors


def enumerate_backwards(list):
    new_list = []
    for element in enumerate_list(list):
        backw_el = element[:3] + element[-1:-len(element)+2:-1] 
        new_list.append(backw_el)
    return new_list

def index_of_by_index(word, list, index):
    last_index = -1
    if word in list[index:]:
        last_index = index + list[index:].index(word)
    return last_index


def index_of_empty(list):
    if "" in list:
        return list.index("") # es literalmente lo que hace el metodo ".index" 
    return -1


def index_of(word, list):
    index = -1
    if word in list:
        index = list.index(word)
    return index



def put(word, list):
    empty_i = index_of_empty(list)
    if empty_i != -1:
        list[empty_i] = word    
    
    return [empty_i, list]
    

def remove(word, list):
    rems = 0
    for item in list:
        if item == word:
            rems += 1
    return rems

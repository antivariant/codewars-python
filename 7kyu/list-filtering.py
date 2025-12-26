def filter_list(l):
    res = []
    for el in l:
        if type(el)==int:
            res.append(el)
    return res

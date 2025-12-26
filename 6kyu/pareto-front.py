def is_dominant(lst, tup_ind):
    for tup in lst:
        if all(x<=y for x,y in zip(tup, lst[tup_ind])):
            if tup == lst[tup_ind]:
                continue
            return False
    return True                   


def pareto_front(datapoints: list[tuple]) -> set[tuple]: 
    pareto = set()
    for tupl_index in range(0, len(datapoints)):
        if is_dominant(datapoints, tupl_index):
            pareto.add(datapoints[tupl_index])    
    return pareto

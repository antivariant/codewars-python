# Number Sequence: Smarandache descrescendo symmetric sequence


def solve(n, bound):
    res=[]
    stop=False
    for line in range(1, bound+1):
        line_list=[]
        for x in range(1, line):
            if x>=bound:
                stop=True
                break
            line_list.append(x)
        for x in range(line,0,-1):
            if stop or x>=bound:
                break
            line_list.append(x)
        res.append(line_list)
    oneline=[el for line in res for el in line]
    oneline.pop(0)
    res_list=[oneline[i] for i in range(n-1, len(oneline), n)]    
    return sum(res_list)

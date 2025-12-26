def count(s):
    res = {}
    for char in s:
        cnt = res.get(char, 0)
        res[char] = cnt + 1
    return res

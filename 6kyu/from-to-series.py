# From..To..Series #3: from char a to char b. Find a substring that contains most char c

import re

def find_sub(s, a, b, c):
    pattern = r"[^\w\s.,\(\)\[\]\{\}]"
    st = re.sub(pattern,'', s)
    mx=0
    sbstr=''
    for i in range(0, len(st)):
        start = st.find(a, i)
        if start==-1:
            break
        nexta = st.find(a, start+1)
        if nexta==-1:
            nexta = len(st)
        end = st.find(b, start+1, nexta)
        if end==-1:
            continue
        cnt = st.count(c, start, end)
        if(cnt>mx):
            mx=cnt
            sbstr=st[start:end+1]
    return sbstr      

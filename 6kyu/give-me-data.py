import re

def has_permission(user_info, accessing_data):
    pattern = re.compile(rf"(\*|{accessing_data})(_)(allow|deny)")
    all_results=[]
    acc = False
    for rule in user_info:
        results = re.findall(pattern, rule)
        all_results.extend(results)

    results_sorted = sorted(all_results, key=lambda x: (x[0], x[2]))
    
    for result in results_sorted:
        if result[0]=='*' and result[2]=='allow':
            acc = True
        if result[0]=='*' and result[2]=='deny':
            acc = False
        if result[0]==accessing_data and result[2]=='allow':
            acc = True
        if result[0]==accessing_data and result[2]=='deny':
            acc = False
    return acc

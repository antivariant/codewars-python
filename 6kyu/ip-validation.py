import re    
def is_valid_IP(strng):
    if '\n' in strng:
        return False
    pattern_numbers = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    match = re.match(pattern_numbers, strng)
    if(not match):
        return False
    for part in strng.split('.'):
        intpart = int(part)
        if(intpart<0 or intpart>255):
            return False
        if(len(part)>1 and part[0]=='0'):
            return False
    return True

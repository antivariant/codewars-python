# Alright, detective, one of our colleagues successfully observed our target person, 
# Robby the robber. We followed him to a secret warehouse, where we assume to find all 
# the stolen stuff. The door to this warehouse is secured by an electronic combination lock.
# Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

# The keypad has the following layout:

# ┌───┬───┬───┐
# │ 1 │ 2 │ 3 │
# ├───┼───┼───┤
# │ 4 │ 5 │ 6 │
# ├───┼───┼───┤
# │ 7 │ 8 │ 9 │
# └───┼───┼───┘
#     │ 0 │
#     └───┘


''' Что известно?
1) Перемещения: 
   влево=-1
   вправо=+1
   вверх=-3
   вниз=+3
   * проверить на граничные значения 0-10 после перемещения
2) Как определить номер строки? (x+0.1)/3 
(1-0.1)/3=0.3 (2-0.1)/3=0.63 (3-0.1)/3=0.9666
(4-0.1)/3=1.3 (5-0.1)/3=1.63 (6-0.1)/3=1.9666
и так далее
3) Как определить, что у 1 нет лева, у 3 нет права и т.п.? Если по 3 и 4 есть смена строки 
4) Исключения 0 и 8  
5) Находждение всех комбинаций элементов массивов - это Recursive Cartesian Product
''' 

def get_pins(pin):
    src_pads = [vars(int(p)) for p in pin]
    result = cart_prod(src_pads)
    print(result)
    return result
    
    
# row number by pad
def row_n(num):
    if num==0:
        return 3
    else:
        return int((num-0.1)/3)

# pad variations
def vars(pad):
    result=[pad]
    pad_row=row_n(pad)
    # short enclosure, cool synthax
    row_n(pad+1)==pad_row and pad+1<10 and result.append(pad+1) # right
    row_n(pad-1)==pad_row and pad-1>0 and result.append(pad-1) # left
    row_n(pad+3)==pad_row+1 and pad+3<10 and pad!=8 and result.append(pad+3) # under
    row_n(pad-3)==pad_row-1 and pad-3>0 and result.append(pad-3) # above
    if pad==8:
        result.append(0)
    if pad==0:
        result.append(8)    
    return result       

# combinations = Recursive Cartesian Product
def cart_prod(vars):
    res=[]
    def dfs(ar, index):
        if index==len(vars):
            res.append(ar)
            return
        for sar in vars[index]:
            dfs(ar+str(sar), index+1)    # concat sting representation
    dfs("",0)
    return(res) 
    

if(__name__== "__main__"):
        get_pins("11") # ["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
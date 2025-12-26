import re

def remove_wrong_words(wordlist_original, main_word):
    wordlist = [word for word in wordlist_original if len(set(word))==4 and word!=main_word]
    return wordlist

def find_word(wordlist=[], word=""):
    pattern = re.compile(rf"""(({word[0]}|\w)({word[1]}{word[2]}{word[3]}))
                         |(({word[0]})({word[1]}|\w)({word[2]}{word[3]}))
                         |(({word[0]}{word[1]})({word[2]}|\w)({word[3]}))
                         |(({word[0]}{word[1]}{word[2]})({word[3]}|\w))""", re.VERBOSE)
    found = list(filter(lambda x: re.search(pattern, x), wordlist))
    return found
    
        

def mutations(alice, bob, word, first):
    cmpl = [remove_wrong_words(alice, word), remove_wrong_words(bob, word)]
    turn = first
    move = 0
    prev_lose = False
    while True:
        move = move + 1
        res = find_word(cmpl[turn], word)
        found = len(res)>0
        if not found and move==1: #0 = next move
            prev_lose = True
            turn = int(not turn)
            continue
        elif found and move==1:
            cmpl[turn].remove(res[0])
            if res[0] in cmpl[int(not turn)]:
                cmpl[int(not turn)].remove(res[0])
            prev_lose = False
            word = res[0]
            turn = int(not turn)
            continue
        elif not found and move==2 and not prev_lose: #1 0 = 0
            return first
        elif found and move==2 and prev_lose: #0 1 = 1
            return int (not first)
        elif not found and prev_lose: #(...)0 0 = -1
            return -1
        elif not found and not prev_lose:
            return int(not turn)
        elif found and not prev_lose and move>2: #...1 1 = next move
            cmpl[turn].remove(res[0])
            if res[0] in cmpl[int(not turn)]:
                cmpl[int(not turn)].remove(res[0])
            word = res[0]            
            turn = int(not turn)
            prev_lose = False
            continue
        elif found and prev_lose and move>2:
            return int(turn)

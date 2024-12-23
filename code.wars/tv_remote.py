# ------ 'TV remote' kata -------------


def tv_remote(word):
    
    pos = [0, 0]
    pos_cur = pos.copy()
    move = 0
    btn = ['abcde123',
           'fghij456',
           'klmno789',
           'pqrst.@0',
           'uvwxyz_/']

    for ch in word:   
        for st in btn:
            col = st.find(ch)
            if col >= 0 :
                pos[0] = btn.index(st)
                pos[1] = col
                move += 1 + abs(pos_cur[0] - pos[0]) + abs(pos_cur[1] - pos[1])                        
                pos_cur = pos.copy()
                  
    return move

print(tv_remote('codewars'))
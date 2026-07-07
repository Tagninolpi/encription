def scramble (sentence:str,inverse=False):
    s = f"{sentence}$"
    l= len(s)
    # create table
    table = []
    for i in range(l):
        s2 = s[i:l] + s[0:i]
        table.append(s2)
    '''
    abc$
    bc$a
    c$ab
    $abc
    '''
    #sort in order
    sorted_table = sorted(table,reverse=inverse)
    '''
    $abc
    abc$
    bc$a
    c$ab
    '''
    bwt = ""
    #bwt_order = ""
    for sentence in sorted_table:
        bwt += sentence[l-1]
        #bwt_order += sentence[0]
    
    # => c$ab
    return bwt[:len(bwt)]

def add_numbers(scrambled:str,reversed :bool):
    real_matrix = []
    matrix = []
    for letter in scrambled:
        if reversed:
            matrix.append(f"{letter}{scrambled.count(letter)-real_matrix.count(letter)-1}")
            real_matrix.append(f"{letter}")
        else:
            matrix.append(f"{letter}{real_matrix.count(letter)}")
            real_matrix.append(f"{letter}")
    #print(real_matrix)
    #print(matrix)
    return matrix

def descramble(scrambled:str,inverse = False):
    count_fix = add_numbers(scrambled,inverse)
    bwt_order = sorted(count_fix,reverse=inverse)
    #print(count_fix)
    #print(bwt_order)
    origine = ""
    #print(scrambled.count("$")-1)
    if inverse:
        btw_o_letter = f"${0}"
    else:
        btw_o_letter = f"${scrambled.count("$")-1}"
    for i in range(len(count_fix)):
        index = count_fix.index(btw_o_letter)
        letter = bwt_order[index]
        origine += letter[0]
        btw_o_letter = letter
        #print(index+1)
        #print(letter)
    return origine[:len(origine)-1]

def multi_scbl(sentence,pattern):
    new = sentence
    for i in range(len(pattern)):
        if pattern[i]>1:
            if pattern[i]-2:
                new = descramble(new,True)
            else:
                new = scramble(new,True)
        else:
            if pattern[i]:
                new = descramble(new)
            else:
                new = scramble(new)
        print(new)
    return new

def multi_scrb_normale(sentence,nb,pos):
    scbr_list = []
    for i in range(nb):
        scbr_list.append(pos)
    for i in range(nb):
        scbr_list.append(pos+1)
    print(scbr_list)
    return multi_scbl(sentence,scbr_list)

s = "hello "

#multi_scbl(s,[0,0])
multi_scrb_normale(s,5,0)


scr = scramble("do you like riddles?")
rep = descramble(scr) 
print(f"'{scr}'")
print(rep)
#'eiuet! yunv$mla siyilaaooo  '
#'eueo?kb a$mvc  dyloo '

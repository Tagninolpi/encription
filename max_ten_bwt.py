def scramble (sentence:str,index,inverse=False):
    s = sentence+str(index)
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
    x = bwt[:len(bwt)]
    print(x)
    return x

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

def descramble(scrambled:str,index,inverse = False):
    count_fix = add_numbers(scrambled,inverse)
    bwt_order = sorted(count_fix,reverse=inverse)
    #print(count_fix)
    #print(bwt_order)
    origine = ""
    #print(scrambled.count("$")-1)
    btw_o_letter = f"{str(index)}0"

    for i in range(len(count_fix)):
        index = count_fix.index(btw_o_letter)
        letter = bwt_order[index]
        origine += letter[0]
        btw_o_letter = letter
        #print(index+1)
        #print(letter)
    x = origine[:len(origine)-1]
    print(x)
    return x

s = "test"
def multi_scr(sentence,nb,rev):
    s = sentence
    for i in range(nb):
        s = scramble(s,i,rev)
    for i in range(0,nb,-1):
        print(i)
        s = descramble(s,i,rev)
    
multi_scr(s,2,False)
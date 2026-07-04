def scramble (sentence:str,index,inverse=False):
    s = sentence+str(index)#test0
    l= len(s) # 5
    table = []
    for i in range(l): #0,1,2,3,4
        s2 = s[i:l] + s[0:i]
        # [0:5][]
        # test0
        table.append(s2)
    '''
    abc0
    bc0a
    c0ab
    0abc
    '''
    #sort in order
    sorted_table = sorted(table,reverse=inverse)
    '''
    0abc
    abc0
    bc0a
    c0ab
    '''
    bwt = ""
    #bwt_order = ""
    for sentence in sorted_table:
        bwt += sentence[l-1]
        #bwt_order += sentence[0]
    
    # => c0ab
    x = bwt[:len(bwt)]
    #print(x)
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
    #print(x)
    return x

# s = "test"
# def multi_scr(sentence,nb,rev):
#     s = sentence
#     for i in range(nb):
#         s = scramble(s,i,rev)
#     for i in range(0,nb,-1):
#         print(i)
#         s = descramble(s,i,rev)

# s0 = scramble(s,0,False)   
# print(s0)
# s1 = scramble(s0,1,True)
# print(s1)
# ds1 = descramble(s1,1,True)
# print(ds1)
# ds0 = descramble(ds1,0,False)
# print(ds0)
# #multi_scr(s,2,False)


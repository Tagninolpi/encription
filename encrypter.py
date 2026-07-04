import random as r
def scramble (sentence:str,index,inverse=False):
    s = sentence+str(index)
    l= len(s)
    table = []
    for i in range(l):
        s2 = s[i:l] + s[0:i]
        table.append(s2)
    sorted_table = sorted(table,reverse=inverse)
    bwt = ""
    for sentence in sorted_table:
        bwt += sentence[l-1]
    x = bwt[:len(bwt)]
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
    return matrix

def descramble(scrambled:str,index,inverse = False):
    count_fix = add_numbers(scrambled,inverse)
    bwt_order = sorted(count_fix,reverse=inverse)
    origine = ""
    btw_o_letter = f"{str(index)}0"
    for i in range(len(count_fix)):
        index = count_fix.index(btw_o_letter)
        letter = bwt_order[index]
        origine += letter[0]
        btw_o_letter = letter
    x = origine[:len(origine)-1]
    return x

def get_bit_list_from_number(num):
    rest = num
    bits =[]
    while rest >0:
        bit = rest.bit_length() - 1
        bits.append(bit)
        rest -= 2**bit
    return bits

def create_bit(number):
    bit_list = get_bit_list_from_number(number)
    if not(len(bit_list)==0):
        result = ""
        for bit_pos in range(max(bit_list)+1,0,-1):
            if bit_pos-1 in bit_list:
                result +="1"
            else:
                result +="0"
        return result
    else:
        return "0"

def get_digit(bit):
    result = 0
    for i in range(len(bit)):
        if bit[i] == "1":
            result += 2**(len(bit)-i-1)
    return result
 
def encrypt(sentence: str, bit_key: str, encripts):
    sent = sentence
    indices = range(len(bit_key)) if encripts else range(len(bit_key) - 1, -1, -1)
    for i in indices:
        bit = bit_key[i]
        if bit == "0":
            sent = scramble(sent, i, True) if encripts else descramble(sent, i, True)
        else:
            sent = scramble(sent, i, False) if encripts else descramble(sent, i, False)
    return sent



playing = True
while playing :
    sentence = str(input("Write a sentence you wish to encrypt(no numbers): "))
    bit_number =0
    if len(sentence)>0:
        if set(sentence).isdisjoint(set("0123456789")):
            bit_number = input("Choose a number between 521-1023: ")
            if type(bit_number) =="int":
                if not(len(bit_number) >0) or not(bit_number>=512 and bit_number<=1023):
                    bit_number = r.randrange(512,1023)
                    print(f"Your number is not valid, the random number generated for you is : {bit_number}")
            else:
                bit_number = r.randrange(512,1023)
                print(f"Your number is not valid, the random number generated for you is : {bit_number}")
            bit_key = create_bit(bit_number)
            print(f"Your sentence is :'{sentence}'")
            print(f"Your encryption number is : {bit_number}, it is associated to the 'bit key' : {bit_key}")
            encrypt_s = encrypt(sentence,bit_key,True)
            print(f"Your encryted sentence is :'{encrypt_s}'")
        else:
            print("Numbers are not alowed!")
    else:
        print("You need to write something!")
    print("__________________________________________________")

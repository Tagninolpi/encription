import math as m

# give bit from digit 
def get_bit_list_from_number(num):
    rest = num
    bits =[]
    while rest >0:
        bit = rest.bit_length() - 1 # instead of 'bit = m.floor(m.log2(rest))' to get precise high numbers 
        bits.append(bit)
        rest -= 2**bit # - closest bit value
    #print(bits)
    return bits

def create_bit(number):
    bit_list = get_bit_list_from_number(number)
    if not(len(bit_list)==0):
        result = ""
        for bit_pos in range(max(bit_list)+1,0,-1):
            #print(bit_pos)
            if bit_pos-1 in bit_list:
                result +="1"
            else:
                result +="0"
        return result
    else:
        return "0"

#give digit from bit
def get_digit(bit):
    result = 0
    for i in range(len(bit)):
        if bit[i] == "1":
            result += 2**(len(bit)-i-1)
        #print(i,bit[i],2**(len(bit)-i-1),result)
    return result
                

# for i in range(10000):
#     print(f"res:{i}:{get_digit(create_bit(i))}")
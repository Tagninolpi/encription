import math as m

# give bit from digit 
def get_bit_list_from_number(num):
    rest = num
    bits =[]
    while rest >0:
        bit = m.floor(m.log2(rest)) # bit calculation
        bits.append(bit)
        rest -= 2**bit # - closest bit value
    #print(bits)
    return bits

def create_bit(bit_list):
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
def get_diggit(bit):
    print(bit)
    result = 0
    for i in range(len(bit),0,-1):
        if bit[i-1] == "1":
            result += 2**(i)-1
    return result
                



for i in range(4):
    print(f"res:{i}:{get_diggit(create_bit(get_bit_list_from_number(i)))}")
print(2**1-1)

'''
8bits = 1 byte = (00000000 to 11111111) = binary

11111111 = 255 decimal = 8 bits

signed integer = 31 bit (1 bit for + or - sign)


2 ** [bit] -1 


'''

count = 0
iBit  = None

while True:
    total_bits = input('Enter bit: ')
    print(f'bits : {total_bits}')
    print("-----------------------")
   
    if total_bits == "end":
        print("End Program")
        break
    else:
        try:
            iBit = int(total_bits)
        except:
            print("Only Numeric!")
            continue
    
    if iBit == 31:
        print("Signed integer")  
    elif iBit == 8:
        print("8 bit")    
    if iBit != None:
        start = -(pow(2 , iBit))
        end = (pow(2 , iBit)) - 1
        print(f' Signed value is: {start} to {end}')
    count = count + 1

        

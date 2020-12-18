
'''
8bits = 1 byte = (00000000 to 11111111) = binary

11111111 = 255 decimal = 8 bits

integer = 31bits (signed + unsigned) = (+ or -) 1bit


2 ** [bit] -1 


'''

count = 0

while True:
    total_bits = input('Enter bit: ')
    print(f'input is: {total_bits}')
    print("-----------------------")
    try:
        iBit = int(total_bits)
    except:
        print("Only Numeric!")
        continue
    if iBit == None:
        deci = 2 ** iBit - 1
        print(f'Decimal value is: {deci}')
    if iBit == "end":
        break
    count = count + 1

    
        


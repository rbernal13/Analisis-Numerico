import struct

def float_to_hex(num):
    num_hex = hex(struct.unpack('<I', struct.pack('<f',num))[0])
    return num_hex

def double_to_hex(num):
    num_hex = hex(struct.unpack('<Q',struct.pack('<d',num))[0])
    return num_hex

n1 = 17.5
n2 = 9.4

#print("Numero a convertir: ", n1)
#rsltd = float_to_hex(n1)
#print("Float a Hex (32-Bit): ", rsltd)
#rsltd = double_to_hex(n1)
#print("Double a Hex (64-Bit): ", rsltd)

print("Numero a convertir: ", n2)
rsltd = float_to_hex(n2)
print("Float a Hex (32-Bit): ", rsltd)
rsltd = double_to_hex(n2)
print("Double a Hex (64-Bit): ", rsltd)


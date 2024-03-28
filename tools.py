def to_binary(file_name):
    binary_data = []
    with open(file_name, 'rb') as f:
        byte = f.read(1)
        while byte:
            binary_data += format(int.from_bytes(byte, 'big'), '08b')
            byte = f.read(1)
    return binary_data


def reverse_string(s):
    return s[::-1]


def list_to_string(lst):
    string = ''
    for el in lst:
        string += str(el)
    return string


def to_bits(lst):
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    return lst


def bits_to_bytes(bits):
    bytes = bytearray()
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        bytes.append(int(''.join(str(bit) for bit in byte), 2))
    return bytes

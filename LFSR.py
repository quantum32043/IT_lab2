from tools import *

class LFSR:
    def __init__(self, polynom_degree):
        self.polynom_degree = polynom_degree

    def generate_key(self, register_value, key_length):
        register_value = reverse_string(register_value)
        for i in range(key_length):
            xored_bit = register_value[2] ^ register_value[24]
            key = register_value[-1]
            for j in range(len(register_value) - 1):
                register_value[j] = register_value[j - 1]
            register_value[0] = xored_bit
        return register_value

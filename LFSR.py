from tools import *

class LFSR:
    def __init__(self, polynom_degree):
        self.polynom_degree = polynom_degree

    def generate_key(self, register_value, key_length):
        key = []
        register_value = list(reverse_string(register_value))
        for i in range(key_length):
            xored_bit = int(register_value[self.polynom_degree[0]]) ^ int(register_value[self.polynom_degree[1]])
            key.append(register_value[-1])
            for j in range(len(register_value) - 1, 0, -1):
                register_value[j] = register_value[j - 1]
            register_value[0] = xored_bit
        return key

from tools import *


class LFSR:
    def __init__(self, polynom_degree):
        self.key = []
        self.polynom_degree = polynom_degree

    def get_key(self):
        return self.key

    def generate_key(self, register_value, text):
        self.key.clear()
        register_value = list(reverse_string(register_value))
        for i in range(len(text)):
            xored_bit = int(register_value[self.polynom_degree[0]]) ^ int(register_value[self.polynom_degree[1]])
            self.key.append(register_value[-1])
            for j in range(len(register_value) - 1, 0, -1):
                register_value[j] = register_value[j - 1]
            register_value[0] = xored_bit
        return to_bits(self.key)

    def encrypt(self, register_value, plain_text):
        plain_text = to_bits(list(plain_text))
        self.key = self.generate_key(register_value, plain_text)
        cipher_text = []
        for i in range(len(plain_text)):
            cipher_text.append(plain_text[i] ^ self.key[i])
        return cipher_text

    # def decrypt(self, register_value, cipher_text):
    #     cipher_text = to_bits(list(cipher_text))
    #     self.key = self.generate_key(register_value, cipher_text)
    #     plain_text = []
    #     for i in range(len(cipher_text)):
    #         plain_text.append(cipher_text[i] ^ self.key[i])
    #     return plain_text

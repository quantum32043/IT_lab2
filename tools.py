def file_to_binary(file_name):
    data = ""
    with open(file_name, 'rb') as f:
        data = "".join(format(i, "b") for i in f.read())
    return data


def reverse_string(s):
    return s[::-1]
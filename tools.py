def file_to_binary(file_name):
    data = ""
    with open(file_name, 'rb') as f:
        data = "".join(format(i, "b") for i in f.read())
    return list(data)


def reverse_string(s):
    return s[::-1]


def lisxt_to_string(lst):
    string = ''
    for el in lst:
        string += str(el)
    return string
def hex_to_bytes(v, l = 0):
    bytes = []
    while v > 0:
        byte = v % 256
        v = v >> 8
        bytes.append(byte)
    bytes.reverse()

    if l != 0 and len(bytes) < l:
        delta = l - len(bytes)
        for i in range(delta):
            bytes.append(0)

    return bytes

def hex_to_hex_string(v, l = 0):
    string = hex(v)[2:]
    if l != 0 and len(string) < l:
        delta = l - len(string)
        string += "0" * delta
    return string

def hex_string_to_bytes(v, l = 0):
    bytes = []
    for i in range(0, len(s), 2):
        val = s[i:i+2]
        bytes.append(int(val, 16))

    if l != 0 and len(bytes) < l:
        delta = l - len(bytes)
        for i in range(delta):
            bytes.append(0)

    return bytes

def hex_string_to_hex(v):
    
    pass

def bytes_to_hex_string(b):

    pass

def bytes_to_hex(b):

    pass



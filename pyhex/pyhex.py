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
    return int(v, 16)   

def bytes_to_hex_string(b, l = 0):
    hex_string = ""
    count = 0
    for i, b in enumerate(b):
        hex_string += "%02x" % b
        count += 1

    for i in range(l - count):
        hex_string += "00"

    return hex_string

def bytes_to_hex(v):
    val = 0
    length = len(v)
    for i, b in enumerate(v):
        val = val | (b << ((length - i - 1) * 8))
    return val

def to_hex(v, l = 0):
    pass

def to_hex_string(v, l = 0):
    pass

def to_bytes(v, l = 0):
    pass


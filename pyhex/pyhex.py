def hex_to_bytes(v, l = 0):
    bytes = []
    count = 0
    while v > 0:
        byte = v % 256
        v = v >> 8
        bytes.append(byte)
        count += 1
    bytes.reverse()

    for i in range(l - count):
        bytes.append(0)

    return bytes

def hex_to_hex_string(v, l = 0):
    hex_string = hex(v)[2:]
    length = len(hex_string)
    for i in range(l - length):
        hex_string += "00"
    return hex_string

def hex_string_to_bytes(v, l = 0):
    bytes = []
    count = 0
    for i in range(0, len(s), 2):
        val = s[i:i+2]
        bytes.append(int(val, 16))
        count += 1

    for i in range(l - count):
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

def to_hex(v):
    if type(v) == type([]):
        return bytes_to_hex(v)
    elif type(v) == type(""):
        return hex_string_to_hex(v)
    elif type(v) == type(0):
        return v
    else:
        raise Exception("Unsupported input type: " + str(type(v)))

def to_hex_string(v, l = 0):
    if type(v) == type([]):
        return bytes_to_hex_string(v, l)
    elif type(v) == type(""):
        return v
    elif type(v) == type(0):
        return hex_to_hex_string(v, l)
    else:
        raise Exception("Unsupported input type: " + str(type(v)))

def to_bytes(v, l = 0):
    if type(v) == type([]):
        return v
    elif type(v) == type(""):
        return hex_string_to_bytes(v, l)
    elif type(v) == type(0):
        return hex_to_bytes(v, l)
    else:
        raise Exception("Unsupported input type: " + str(type(v)))


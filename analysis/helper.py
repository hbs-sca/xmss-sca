

'''
 * containing functionality that is reused, but is independent of dpa and SHA256
'''

import numpy as np

"""
 * loading traces from a binary file (uint8)
 * number of traces is parsed from file name
"""
def load_traces(file_name):
    f = open(file_name, "r")
    a = np.fromfile(f, dtype=np.uint8)
    file_length = len(a)
    [_, num_traces] = file_name.split("_")
    num_traces = int(num_traces.split(".")[0])
    size_per_trace = file_length/num_traces
    a = a.reshape((num_traces, size_per_trace))
    return [a, num_traces, size_per_trace]

"""
 * loading secret data from text file
 * content is just used for checking if the recovered key is correct
"""
def load_secret_data(file_name):
    f = open(file_name, "r")
    secretSeed = f.readline().split("=")[1].strip()
    secretIv = f.readline().split("=")[1].strip()
    secretDelta = f.readline().split("=")[1].strip()
    secretT2 = f.readline().split("=")[1].strip()
    return [secretSeed, secretIv, secretDelta, secretT2]

"""
 * converting an 4-element byte array to unsigned int
"""
def byte_to_int_array(arr):
    return byte_to_int(arr[0], arr[1], arr[2], arr[3])

"""
 * converting 4 bytes to unsigned int
"""
def byte_to_int(b0,b1,b2,b3):
    return b3 + (b2 << 8) + (b1 << 16) + (b0 << 24)

"""
 * converting unsigned integer to 4-element byte array
"""
def int_to_byte(i):
    return [(i>>24)&0xFF,(i>>16)&0xFF,(i>>8)&0xFF,i&0xFF]


'''
 * converting P x 4-dim byte matrix to P-dim int vector
'''
def byte_array_to_int_vec(x):
    x = np.array(x, dtype=np.uint32)
    return x[:, 3] + (x[:, 2]<<8) + (x[:, 1]<<16) + (x[:, 0]<<24)

'''
 * converting a P-dim int vector to a Px4-dim byte matrix
'''
def int_to_byte_vec(x):
    res = np.zeros([len(x), 4], dtype=np.uint8)
    res[:, 0] = (x >> 24)&0xFF
    res[:, 1] = (x >> 16)&0xFF
    res[:, 2] = (x >> 8)&0xFF
    res[:, 3] = x&0xFF
    return res


'''
 * comparing a hex string with an uint array
'''
def compareBytes(iv_str, arr):
    for i in range(0, len(arr)):
        iv_substr = iv_str[2+i*8:2+(i+1)*8]
        if arr[i] != int(iv_substr, 16):
            #print "mismatch", hex(arr[i]), "!=", iv_substr
            return False
    return True

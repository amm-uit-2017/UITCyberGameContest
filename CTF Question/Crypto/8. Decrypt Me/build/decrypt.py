def tumbler1(data):
    cipher = ""
    for byte in data:
        cipher+=chr(ord(byte) ^ ord('N'))   
    return cipher 

def tumbler2(data):
    cipher = ""
    for byte in data:
        cipher+=chr(ord(byte) ^ ord('I'))   
    return cipher 

def tumbler3(data):
    cipher = ""
    for byte in data:
        cipher+=chr(ord(byte) ^ ord('A'))   
    return cipher 

def tumbler4(data):
    cipher = ""
    for byte in data:
        cipher+=chr(ord(byte) ^ ord('V'))   
    return cipher 

def tumbler5(data):
    cipher = ""
    for byte in data:
        cipher+=chr(ord(byte) ^ ord('U'))   
    return cipher

def encrypt(data):
    return tumbler1(tumbler2(tumbler4(tumbler3(tumbler5(data)))))

def decrypt(data):
    return tumbler5(tumbler3(tumbler4(tumbler2(tumbler1(data))))) 



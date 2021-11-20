# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
# file_in = open("encrypted.bin", "rb")
# nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
# key = get_random_bytes(16)
# # let's assume that the key is somehow available again
# cipher = AES.new(key, AES.MODE_EAX, nonce)
# data = cipher.decrypt_and_verify(ciphertext, tag)

# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes

# key = get_random_bytes(16)
# cipher = AES.new(key, AES.MODE_EAX)
# ciphertext, tag = cipher.encrypt_and_digest(data)

# file_out = open("encrypted.bin", "wb")
# [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
# file_out.close()


from Crypto.Cipher import AES

def aes_encECB(key, msg):
    cipher = AES.new(key, AES.MODE_ECB)
    print(key)
    print(cipher)
    print(msg)
    #return msg
    return cipher.encrypt(msg)
    
def aes_decryECB(key, c_text):
    cipher = AES.new(key, AES.MODE_ECB)
    print(cipher)
    print(c_text)
    #return msg
    return cipher.decrypt(c_text)


#num1 = "0b00000000000000000000000000000000"

#enMsg = aes_enc(num1.encode("utf8"), 'Testing_Out@this^string123456789'.encode("utf8"))

#enMsg = aes_enc('\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00'.encode("utf8"), 'Testing_Out@this^string123456789'.encode("utf8"))
# 16 Bytes = 128bits
# Testing_Out@this^string123456789

print('Encryption begins:\n')
enMsg = aes_encECB(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 'Testing_Out@this^string123456789'.encode("utf8"))
print('Ciphertext is: ',enMsg)

print('\n')
print('For testing purpose, decryption begins:\n')
decryMsg = aes_decryECB(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', b'p?\xa02\xfe\xd9\x84a\x1f\x11\xba\x87\xf7\xe1\x19\x04\xabW\xdf\xd3\xbf\xbc\x12\xea\xbb\xe0\x7f\xb1\x8d\xf0\xb59')

print('Type of decrymsg is')
print(type(decryMsg))
cleandecryMsg = str(decryMsg)
cleanMsg = cleandecryMsg.replace('b','').replace("'",'')
print('Original text is: ', cleanMsg)


print('\n')
print('Q1b - Decryption with 2 swopped blocks:\n')
swopMsg = aes_decryECB(b'\x00\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x70\x00\x00\x00\x00', b'p?\xa02\xfe\xd9\x84a\xe0\x11\xba\x87\xf7\xe1\x19\x04\xabW\xdf\xd3\xbf\xbc\x12\xea\xbb\x1f\x7f\xb1\x8d\xf0\xb59')

print('The return plaintext, P1, is: ',swopMsg)

print('\n')
print('Q1c - Decryption with the last bit of C being changed:\n')
lastBitCMsg = aes_decryECB(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', b'p?\xa02\xfe\xd9\x84a\x1f\x11\xba\x87\xf7\xe1\x19\x04\xabW\xdf\xd3\xbf\xbc\x12\xea\xbb\xe0\x7f\xb1\x8d\xf0\xb5a')

print('With the last bit of C being changed, the return plaintext, P2, is: ',lastBitCMsg)


print('\n')
print('End of playtime]\n')

# readMyFile = open('www.fileformat.info/format/bmp/sample/43ab63cb34cc4486b09f559a225ce28e/BLK.BMP','r').read()
# print(readMyFile)
# picMsg = aes_enc(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', readMyFile)
# print('Ciphertext is: ',picMsg)

# print('The return ciphertext, Q2, is: ',picMsg)


# readMyFile = open('www.fileformat.info/format/bmp/sample/43ab63cb34cc4486b09f559a225ce28e/BLK.BMP','r').read()
# print(readMyFile)
# picMsg = aes_enc(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', readMyFile)
# print('Ciphertext is: ',picMsg)

# print('The return ciphertext, Q2, is: ',picMsg)

"""
O/p:

Encryption begins:

b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
<Crypto.Cipher._mode_ecb.EcbMode object at 0x000001F2BDC1C8E0>
b'Testing_Out@this^string123456789'
Ciphertext is:  b'p?\xa02\xfe\xd9\x84a\x1f\x11\xba\x87\xf7\xe1\x19\x04\xabW\xdf\xd3\xbf\xbc\x12\xea\xbb\xe0\x7f\xb1\x8d\xf0\xb59'


For testing purpose, decryption begins:

<Crypto.Cipher._mode_ecb.EcbMode object at 0x000001F2BF9EF610>
b'p?\xa02\xfe\xd9\x84a\x1f\x11\xba\x87\xf7\xe1\x19\x04\xabW\xdf\xd3\xbf\xbc\x12\xea\xbb\xe0\x7f\xb1\x8d\xf0\xb59'
Type of decrymsg is
<class 'bytes'>
Original text is:  Testing_Out@this^string123456789


Q1b - Decryption with 2 swopped blocks:

<Crypto.Cipher._mode_ecb.EcbMode object at 0x000001F2BF9EFBB0>
b'p?\xa02\xfe\xd9\x84a\xe0\x11\xba\x87\xf7\xe1\x19\x04\xabW\xdf\xd3\xbf\xbc\x12\xea\xbb\x1f\x7f\xb1\x8d\xf0\xb59'
The return plaintext, P1, is:  b'\x1a\xf7|\xaaP\xca\x10}\x9b8\xbe\x93v\xfcu\xd1\x9a}o\n\x01\xd1\xb7\x92 i<\xf7\xf3\xe7;}'


Q1c - Decryption with the last bit of C being changed:

<Crypto.Cipher._mode_ecb.EcbMode object at 0x000001F2BF9EFCA0>
b'p?\xa02\xfe\xd9\x84a\x1f\x11\xba\x87\xf7\xe1\x19\x04\xabW\xdf\xd3\xbf\xbc\x12\xea\xbb\xe0\x7f\xb1\x8d\xf0\xb5a'
With the last bit of C being changed, the return plaintext, P2, is:  b'Testing_Out@this\x85\x92\xea\x1f\xcde\xa5\xeb\xb7\xdbf\xb8\xacF\xba\xe4'


End of playtime]
"""
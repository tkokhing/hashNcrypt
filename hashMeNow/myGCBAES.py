"""
Blocks (in Hex) of Ciphertext
0x89 0x31 0x32 0x95 0x6d 0x26 0xdd 0x5b 0xe 0x29 0x86 0xfc 0xb6 0xf5 0xf6 0x67 

0x8e 0xdc 0x6b 0xe2 0x67 0x88 0x8d 0x68 0xc0 0xac 0x98 0x25 0xd4 0x5a 0xc4 0x6c 

0x46 0xa2 0x5f 0x8b 0x2a 0x78 0xc2 0xca 0x7c 0x35 0xa 0xfa 0xd4 0xab 0x3c 0x79 

"""

from Crypto.Cipher import AES
# from base64 import b64encode
# from Crypto.Random import get_random_bytes

def aes_encGCM(holyKey, msg, useIV):
    cipher = AES.new(holyKey, AES.MODE_GCM, useIV)
    theNonce = cipher.nonce
    # print('The input Key is', holyKey)
    # print('The input Message  is', msg)
    # print('The generated Cipher is', cipher)
    # print('The generated Cipher Nonce is', cipher.nonce)
    theCtext, theTag  = cipher.encrypt_and_digest(msg) 
    return theCtext, theTag, theNonce


#   !!! learnt something new !!! 
    # the above returns two items, 
    # :Return:
    # a tuple with two items:
    # - the ciphertext, as ``bytes``
    # - the MAC tag, as ``bytes``
            
#   previously was only using this 
#   return cipher.encrypt(msg)
    # this returns one item, 
    # :Return:
    # - the ciphertext, as ``bytes``

# def aes_decryGCM(holyKey, c_text, testTag, testNonce):
#    cipher = AES.new(holyKey, AES.MODE_GCM, testNonce)



def aes_decryGCM(holyKey, c_text, testTag, testNonce):
    try:
        cipher = AES.new(holyKey, AES.MODE_GCM, testNonce)
        # print('The input ciphertext is', c_text)
        # print('The generated Cipher is', cipher)
    # .decrypt_and_verify
        return cipher.decrypt_and_verify(c_text, testTag)
    except ValueError as er_msg:
        print('Incorrect decryption with error message [', er_msg,']')
# :Return: the plaintext as ``bytes`` or 
# ``None`` when the ``output`` parameter specified a location for the result.



theholyKey = b'\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF'

theholyIV = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

theMsg = 'LovingItCybersecurityReengineeringMyLifeAmazing!'
# 48 char for the message

# TESTING. 
# The above returns exact same ciphertext for first 32 char, plus "addition" 
# for the addition message trailing 16 chars 
# Interesting!  
# theMsg = 'LovingItCybersecurityReengineer!'
# 32 char for the message
# theMsg = 'LovingItC'

print('Trial 1')
print('Encryption begins:')
thisCtext, thisTag, thisNonce = aes_encGCM(theholyKey, theMsg.encode("utf8"), theholyIV)
print('The generated Nonce is: ',thisNonce)
print('The generated Tag is: ',thisTag)
print('The generated Ciphertext is: ',thisCtext)
print(type(thisCtext))
print('\nVerify decryption begins:')
# format ---> def aes_decryGCM(holyKey, c_text, testTag):
# decryMsg = aes_decryGCM(theholyKey, thisCtext, thisTag, thisNonce)
# cleandecryMsg = str(decryMsg)
# cleanMsg = cleandecryMsg.replace('b','').replace("'",'')
# print('Decrpyted text is: ', cleanMsg)
# print(decryMsg)
# print(type(decryMsg))

print('\nTrial 2')
print('Swap the the ﬁrst and third blocks of C:\n')

i = 0
print('Blocks (in Hex) of Ciphertext')
for byte in thisCtext:
    print(hex(byte), end=' ')

    i += 1
    if (i%16 == 0):
        print('\n')
print('Total Bytes size is: ',i,'\n')


print('Decryption of Swap the the ﬁrst and third blocks of C begins')
myString = '46a25f8b2a78c2ca7c350afad4ab3c798edc6be267888d68c0ac9825d45ac46c893132956d26dd5b0e2986fcb6f5f667'
#print(type(myString))

# hexString = hex(int(myString))
# print(type(hexString))
clueCipText = bytes.fromhex(myString)

decryMsg = aes_decryGCM(theholyKey, clueCipText, thisTag, thisNonce)
cleandecryMsg = str(decryMsg)
cleanMsg = cleandecryMsg.replace('b','').replace("'",'')
print('Decrpyted text is: ', cleanMsg)



print('\nTrial 3')
print('Remove of third block of C:\n')
print('Decryption of first and second blocks of original ciphertext begins')
myString = '893132956d26dd5b0e2986fcb6f5f6678edc6be267888d68c0ac9825d45ac46c'
#print(type(myString))

# hexString = hex(int(myString))
# print(type(hexString))
clueCipText = bytes.fromhex(myString)

decryMsg = aes_decryGCM(theholyKey, clueCipText, thisTag, thisNonce)
cleandecryMsg = str(decryMsg)
cleanMsg = cleandecryMsg.replace('b','').replace("'",'')
print('Decrpyted text is: ', cleanMsg)


print('\nTrial 4')
print('Change the last bit of C (from 0x79 to 0x78 )\n')
myString = '893132956d26dd5b0e2986fcb6f5f6678edc6be267888d68c0ac9825d45ac46c46a25f8b2a78c2ca7c350afad4ab3c78'

clueCipText = bytes.fromhex(myString)

decryMsg = aes_decryGCM(theholyKey, clueCipText, thisTag, thisNonce)
cleandecryMsg = str(decryMsg)
cleanMsg = cleandecryMsg.replace('b','').replace("'",'')
print('Decrpyted text is: ', cleanMsg)


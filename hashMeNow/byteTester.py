"""
The bottom part of the program is written to test whether the cipher functions
 returns what class type, say Byte, interpreting it in Hex and Decimal, and its size.
 Of each byte, what class type is it.   

"""
from Crypto.Cipher import AES

def aes_decry(key, c_text, useIV):
    cipher = AES.new(key, AES.MODE_CBC, useIV)
    return cipher.decrypt(c_text)


def determineBYTE(testByte):
    # this function takes in Class type [BYTE], test it and display the breakdown in Interger and HEX format. Return NIL
    print('\n')
    print('-------------------------------------')
    print('function --> determineBYTE(testByte):')
    print('-------------------------------------')
    print('\nByte form (in Interger) are: ') 
    i = 0
    for byte in testByte:
        print(int(byte), end=' ')
        # print(len(byte))
        i += 1
    print('\nTotal Bytes size is: ',i)
    # The above DOES print out 64 Bytes of Hash key which is gen by SHA512 
    # Therefore it is correct!!!!


    print('\nByte form (in Hex) are: ') 
    i = 0
    for byte in testByte:
        print(hex(byte), end=' ')

        i += 1
    print('\nTotal Bytes size is: ',i)

    print('\n-------------------------------------')
    print('function --> determineBYTE(testByte):')
    print('-------------------------------------')
    print('\n\n\n')

# For testing, using few hex as test
# cipText = ['87', 'F3', '48', 'FF', '79']

cipText = ['87', 'F3', '48', 'FF', '79', 'B8', '11', 'AF', '38', '57', 'D6', '71', '8E', '5F', '0F', '91', '7C', '3D', '26', 'F7', '73', '77', '63', '5A', '5E', '43', 'E9', 'B5', 'CC', '5D', '05', '92', '6E', '26', 'FF', 'C5', '22', '0D', 'C7', 'D4', '05', 'F1', '70', '86', '70', 'E6', 'E0', '17']

length_cipText = len(cipText)

thisKey = b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'
cipTextList = "\\x"
tempMsg = ""
tempStr = ""

hex_val = '4120717569636b2062726f776e20666f78'
# b'A quick brown foxA quick brown foxA quick brown foxA quick brown foxA quick brown foxA quick brown fox'




for i in range (0, length_cipText):
    print(i)

    # Alternate method appending \x in front of every Hex keys, this will also work. Dinosaur way...
    # cipKey = cipTextList + str(cipText[i])
    
    cipKey = str(cipText[i])

    # Breaking up the IV from the Ciphertext
    # Clue is IV for CBC must be 16 Bytes, hence it is the first 16 Hex from the question 
    if i < 16:
        useIVKey = tempMsg + cipKey
        tempMsg = useIVKey 
    else:
        useC_text = tempStr + cipKey
        tempStr = useC_text 

print('Hex IV to use is ',useIVKey,' with class type :', type(useIVKey))
print('Hex Cipthertext is ', useC_text,' with class type :',type(useC_text))

print('Byte IV to use is: ', bytes.fromhex(useIVKey))
print('Byte Cipthertext is ', bytes.fromhex(useC_text))

decryMsg = aes_decry(thisKey, bytes.fromhex(useC_text), bytes.fromhex(useIVKey))

# The other method of \x<hex keys> will also work
# decryMsg = aes_decry(b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01', b'\x7C\x3D\x26\xF7\x73\x77\x63\x5A\x5E\x43\xE9\xB5\xCC\x5D\x05\x92\x6E\x26\xFF\xC5\x22\x0D\xC7\xD4\x05\xF1\x70\x86\x70\xE6\xE0\x17', b'\x87\xF3\x48\xFF\x79\xB8\x11\xAF\x38\x57\xD6\x71\x8E\x5F\x0F\x91')
print(type(decryMsg))

cleandecryMsg = str(decryMsg)
cleanMsg = cleandecryMsg.replace('b','').replace("'",'')
print('Decrpyted text is: ', cleanMsg)

## Decrpyted text is:  Another secret!  And another.

answer = bytes.fromhex(hex_val) # this is equal to the line below
# answer = bytes.fromhex(hashStr1)

determineBYTE(answer)

byteString = b'0xe'
print(type(byteString))
myString = '0xe'

print('Hex 0xe length is',len(myString))

if (len(myString) == 3):
    myString = myString[0:2] + '0'+ myString[2]

print('Beautified myString is', myString)
myString = '0x2e'

print('Hex 0x2e length is', len(myString))

print('\n')
print(answer[0])
print('\n')
print(answer[1])
print('\n')
print(answer[2])
print('\n')
print(type(answer[2]))


# """

# What if the HEX are 0xe (4 bits only, auto leaving out the 0 in front) and not 0xFe
# T.B.C 

# print('\nQ1(b):')
# print('Swap the the ﬁrst and third blocks of C:\n')

# i = 0
# print('Blocks (in Hex) of Ciphertext')
# for byte in thisCtext:
#     if byte.bit_length() == 4:
#         print('4444', end= ' ')
    
#     # if (len(myString) == 3):
#     #     myString = myString[0:2] + '0'+ myString[2]
#     #     print(myString, end=' ')
#     #     print('3>',hex(byte), end=' ')
#     else:
#         print(hex(byte), end=' ')


#     i += 1
#     if (i%16 == 0):
#         print('\n')
# print('Total Bytes size is: ',i)
# # b'\x96\xb\x10\xb8\x2e\xc\xc7\x7c\x9\x7d\xd1\xa8\xea\xb3\xa3\x31\xd1\xe8\x6d\xe3\x70\xbe\x89\x79\xc7\xa4\x9f\x38\x9c\x7c\xe5\x2f\x7b\x90\x46\xb6\x4b\x5c\xf7\xfc\x79\x75\x5e\xb1\x93\xf0\x6b\x6d'
# # 96b10b82ecc77c97dd1a8eab3a331d1e86de370be8979c7a49f389c7ce52f7b9046b64b5cf7fc79755eb193f06b6d


# """

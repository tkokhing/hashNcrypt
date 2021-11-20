"""
# Findings:
The message and IV is not 16 Bytes will return the same error. No mistake, message returns this error
    raise ValueError("Incorrect IV length (it must be %d bytes long)" %
ValueError: Incorrect IV length (it must be 16 bytes long)

However, the Key, tested as 16 and 32 Bytes, did not give any error.

With trials above not giving any error, the return TAG is 16 Bytes 

"""

# the program works. It is tested using easier str pattern
import codecs
import hashlib
import timeit as tm
from Crypto.Cipher import AES

# 16 bytes of IV and KEY
iniIV = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
holyKey = b'\x0B\x0B\x0B\x0B\x0B\x0B\x0B\x0B\x00\x00\x00\x00\x00\x00\x00\x00'

# Set reference template string here

# hex_val = '4120717569636b2062726f776e20666f784120717569636b2062726f776e20666f784120717569636b2062726f776e20666f784120717569636b2062726f776e20666f784120717569636b2062726f776e20666f784120717569636b2062726f776e20666f78'
# b'A quick brown foxA quick brown foxA quick brown foxA quick brown foxA quick brown foxA quick brown fox'


# myStr1 = 'a quick grey fox' 
myStr1 =   'deaacadabaeacddc' # Testing of codes using with easier string pattern

def aes_encCBC(key, msg,useIV):
    cipher = AES.new(key, AES.MODE_CBC, useIV)
    # print('The key is', key)
    # print('The AES function returns is', cipher)
    return cipher.encrypt(msg)
    

def aes_decryCBC(key, c_text, useIV):
    cipher = AES.new(key, AES.MODE_CBC, useIV)
    # print('The AES function return is', cipher)
    return cipher.decrypt(c_text)

def findSameTag(tagToFind):

    start = tm.default_timer()

    # character list to run in loop, gen every hash to compare and contrast    
    # charList = 'abcdefghijklmnopqrstuvwxyz '
    charList = 'abcde' # Testing of codes using with easier charlist pattern 

    len_charList = len(charList)
    checkStr1 = str(tagToFind)
    # print('checkStr1 is: ',checkStr1, 'with class type ',type(checkStr1))

    foundStr = False    # Boolean for breaking loop when comparison is True

    # Constructing 16 bytes of char string2 for comparison
    for a in range (0,len_charList):
        if (foundStr == False):
            for b in range (0,len_charList):
                if (foundStr == False):
                    for c in range (0,len_charList):
                        if (foundStr == False):
                            for d in range (0,len_charList):
                                if (foundStr == False):
                                    for e in range (0,len_charList):
                                        if (foundStr == False):
                                            for f in range (0,len_charList):
                                                if (foundStr == False):
                                                    for g in range (0,len_charList):
                                                        if (foundStr == False):
                                                            for h in range (0,len_charList):
                                                                if (foundStr == False):
                                                                    for i in range (0,len_charList):
                                                                        if (foundStr == False):
                                                                            for j in range (0,len_charList):
                                                                                if (foundStr == False):
                                                                                    for k in range (0,len_charList):
                                                                                        if (foundStr == False):
                                                                                            for l in range (0,len_charList):
                                                                                                if (foundStr == False):
                                                                                                    for m in range (0,len_charList):
                                                                                                        if (foundStr == False):
                                                                                                            for n in range (0,len_charList):
                                                                                                                if (foundStr == False):
                                                                                                                    for o in range (0,len_charList):
                                                                                                                        if (foundStr == False):
                                                                                                                            for p in range (0,len_charList):
                                                                                                                                
                                                                                                                                # Gen the str2 for creating test tag
                                                                                                                                myStr2 = str(charList[a]) + str(charList[b]) + str(charList[c]) + str(charList[d]) + str(charList[e]) + str(charList[f]) + str(charList[g]) + str(charList[h]) + str(charList[i]) + str(charList[j]) + str(charList[k]) + str(charList[l]) + str(charList[m]) + str(charList[n]) + str(charList[o]) + str(charList[p])   
                                                                                                                                # Run 2 cycle of CBC to gen the test tag
                                                                                                                                c_TWO = aes_encCBC(holyKey,myStr2.encode("utf8"),iniIV)
                                                                                                                                testTag = aes_encCBC(holyKey,myStr1.encode("utf8"),c_TWO)
                                                                                                                                # print(myStr2)

                                                                                                                                checkStr2 = str(testTag)  # string to contain n bits for comparison, empty it from beginning
                                                                                                                                                                    
                                                                                                                                if (checkStr1 == checkStr2):
                                                                                                                                    # when found, break the entire loop
                                                                                                                                    foundStr = True
                                                                                                                                    break

    end = tm.default_timer()
    print('Time taken is: ' + str(end - start))

    if foundStr == False:
        print('No match found')
    else:
        print(' Match found!')
        print(' String 1 ',myStr1, ' with tag [', checkStr1,']')
        print(' String 2 (test string) ',myStr2,' with tag [', checkStr2,']')
 

# main program starts here
print('Encryption begins:\n')

# Run 2 cycle of CBC to gen the tag
c_ONE = aes_encCBC(holyKey,myStr1.encode("utf8"),iniIV)
print('The c_ONE is', c_ONE, 'with class type',type(c_ONE) )

theTag = aes_encCBC(holyKey,myStr1.encode("utf8"),c_ONE)
print('The tag is', theTag, 'with class type',type(theTag) )

# Function takes in theTag to finding another same tag
findSameTag(theTag)

# def aes_decryCBC(key, c_text, useIV):
preC_ONE = aes_decryCBC(holyKey, c_ONE, iniIV)
print(preC_ONE)
print(type(preC_ONE))

# Tested at the second stage using initial IV to decrypt, it does not work.
# decryMsg = aes_decryCBC(holyKey, theTag, iniIV)
decryMsg = aes_decryCBC(holyKey, theTag, c_ONE)
print(decryMsg)
print(type(decryMsg))

i = 0
print('\nByte form (in Hex) are: \n') 
for byte in preC_ONE:
    print(chr(byte), end='')
    i += 1
print('\nTotal Bytes size is: ',i)

i = 0
print('\nByte form (in Hex) are: \n') 
for byte in decryMsg:
    print(chr(byte), end='')
    i += 1
print('\nTotal Bytes size is: ',i)

byte_array = bytearray(decryMsg)
hexadecimal_string = byte_array.hex()
print(hexadecimal_string)

cleanMsg = decryMsg.hex()
# cleandecryMsg = str(decryMsg)
# cleanMsg = cleandecryMsg.replace('b','').replace("'",'')
print('Decrpyted text is: ', cleanMsg)

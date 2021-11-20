import hashlib
import timeit as tm

def sameBitHash(num):

    start = tm.default_timer()
    s = 0   # counter for byte size to check
    checkStr1 = ''  # string to contain n bits for comparison, empty it from beginning 
    
    
    # Set reference template string 1 here
    myStr1 = "jdyci" 

    # character list to run in loop, gen every hash to compare and contrast    
    charList = 'abcdefghijklmnopqrstuvwxyz'
    len_charList = len(charList)

    # construct reference string 1 and its hash
    hashStr1 = hashlib.sha512(myStr1.encode()).hexdigest()
    answer = bytes.fromhex(hashStr1)

    # form checkStr1 for comparison
    for byte in answer:
        # print(hex(byte), end=' ')
        while s != num:
            checkStr1 = checkStr1 + str(hex(answer[s]))
            s += 1
        else:
            break

    foundStr = False    # Boolean for breaking loop when comparison is True

    for i in range (0,len_charList):
        if (foundStr == False):
            for j in range (0,len_charList):
                if (foundStr == False):
                    for k in range (0,len_charList):
                        if (foundStr == False):
                            for l in range (0,len_charList):
                                if (foundStr == False):
                                    for m in range (0,len_charList):
                                        t = 0   # counter for byte size to check
                                        checkStr2 = ''  # string to contain n bits for comparison, empty it from beginning

                                        # construct the random generated string and its hash
                                        myStr2 = str(charList[i]) + str(charList[j]) + str(charList[k]) + str(charList[l]) + str(charList[m])
                                        hashStr2 = hashlib.sha512(myStr2.encode()).hexdigest()
                                        
                                        # convert hash to bytes, form checkStr2 for comparison
                                        answer = bytes.fromhex(hashStr2)
                                        for byte in answer:
                                            while t != num:
                                                checkStr2 = checkStr2 + str(hex(answer[t]))
                                                t += 1
                                                                             
                                        if (checkStr1 == checkStr2):
                                            # when found, break the entire loop
                                            foundStr = True
                                            break

    end = tm.default_timer()
    print('Time taken is: ' + str(end - start))

    if foundStr == False:
        print('No match found')
    else:
        print(' String 1 [', myStr1,'] and hash [', hashStr1, ']')
        print(' String 2 [', myStr2,'] and hash [', hashStr2, ']')

        print(num*8,' bits of leftmost for string 1 is (in HEX)', checkStr1)
        print(num*8,' bits of leftmost for string 2 is (in HEX)', checkStr2)

def findPreImage(hexValue,num):
    start = tm.default_timer()
    checkStr1 = ''
    s = 0

    # character list to run in loop, gen every hash to compare and contrast    
    charList = 'abcdefghijklmnopqrstuvwxyz'
    len_charList = len(charList)

    # print(type(hexValue))
    # print(hexValue)

    answer = bytes.fromhex(hexValue)
    # print(answer)

    for byte in answer:
        # print(hex(byte), end=' ')
        # print('What is byte????', byte)
        while s != num:
            checkStr1 = checkStr1 + str(hex(answer[s]))
            s += 1
        else:
            break

    # print(checkStr1)
    foundStr = False    # Boolean for breaking loop when comparison is True

    for i in range (0,len_charList):
        if (foundStr == False):
            for j in range (0,len_charList):
                if (foundStr == False):
                    for k in range (0,len_charList):
                        if (foundStr == False):
                            for l in range (0,len_charList):
                                if (foundStr == False):
                                    for m in range (0,len_charList):
                                        t = 0   # counter for byte size to check
                                        checkStr2 = ''  # string to contain n bits for comparison, empty it from beginning

                                        # construct the random generated string and its hash
                                        myStr2 = str(charList[i]) + str(charList[j]) + str(charList[k]) + str(charList[l]) + str(charList[m])
                                        hashStr2 = hashlib.sha512(myStr2.encode()).hexdigest()
                                        
                                        # convert hash to bytes, form checkStr2 for comparison
                                        answer = bytes.fromhex(hashStr2)
                                        for byte in answer:
                                            while t != num:
                                                checkStr2 = checkStr2 + str(hex(answer[t]))
                                                t += 1
                                                                             
                                        if (checkStr1 == checkStr2):
                                            # when found, break the entire loop
                                            foundStr = True
                                            break

    
    end = tm.default_timer()
    print('Time taken is: ' + str(end - start))

    if foundStr == False:
        print('No match found')
    else:
        print('Preimage of [', hexValue,'] is [', myStr2, '] with its hash [', hashStr2,']')


# program starts here

print('\nFor leftmost 8 bit collision\n')
sameBitHash(1)
print('\nFor leftmost 16 bit collision\n')
sameBitHash(2)


print('\nFor preimage 0x00\n')
findPreImage("00",1)

print('\nFor preimage 0x000x00\n')
findPreImage("0000",2)
# test with findPreImage("00000000",4), 
# For preimage 0x000x00

# Time taken is: 74.8975507
# No match found

# string = "Hello World"




# # string with encoding 'utf-8'
# arr = bytes(string, 'utf-8')
# arr2 = bytes(string, 'ascii')

# print(arr,'\n')
# print(arr2,'\n')

# # actual bytes in the the string
# for byte in arr:
#     print(byte, end=' ')
# print("\n")
# for byte in arr2:
#     print(byte, end=' ')


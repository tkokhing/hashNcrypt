# Not the best out there but personally I am glad that I figured this out yeah!
# Above All

from random import randbytes as rnd

numList = []
repeatedNumList = []
numCountList = []
maxNumList = []
# print(bin(128))
xRandom = rnd(512)


# print('\nByte form (in Hex) are: \n') 
i = 0
for byte in xRandom:
    # print(bin(byte), end=' ')
    print('{0:3d}' .format(i+1), ') Randomly generated number :{0:5d}'. format(int(byte)),', reduced number: {0:5d}'. format(int(byte)%128))
    numX = int(byte)%128

    # inserting reduced number into numList
    numList.insert(i,numX)
    i += 1

# Since random is not in sequence, sort them in order to make comparison 
sorted_numList = sorted(numList)

# compute length for loop
listLength = len(sorted_numList)
# Added a trailing impossible number at the end for completing entire loop x+1
sorted_numList.insert(i,1000)

numCounter = 1
repeatedNumCounter = 0 
# t = 0

for i in range (0,listLength):
    # if (x  == (x+1)), add counter
    if sorted_numList[i] == sorted_numList[i+1]:
        # print(t, i,'Repeated reduced numbers', sorted_numList[i])
        # t += 1
        # if that number is not inside repeatedNumList, it is the first occurrance 
        # write number into repeatedNumList
        # start counting repeatedNumCounter for indexing List purpose
        # add 1 to numCounter
        if sorted_numList[i] not in repeatedNumList:
            repeatedNumList.insert(repeatedNumCounter, sorted_numList[i])
            repeatedNumCounter += 1
            numCounter += 1
      
        # if that word is already inside repeatedNumList, 
        # add numCounter
        else:
            numCounter += 1
            
    # if (x  != (x+1)), 2 possibilities 
    #       Either end of repeated words, 
    #       or start of solo new word 
    else: 
        # if there are already same number found
        # write to total count of the same number into numCoutlist [] 
        # at position by repeatedNumCounter
        # once written, reset numCounter to 1 for next use

#        t += 1
        if numCounter >= 2: 
            #print(t, i,'Last Repeated            reduced numbers', sorted_numList[i])
            repeatedNumList.insert(repeatedNumCounter, sorted_numList[i])
            numCountList.insert(repeatedNumCounter, numCounter)
            numCounter = 1

        # sequence of single word, reset numCounter to prepare for new repeated number
        else: 
            # print(t, i,'Solo            reduced numbers', sorted_numList[i])
            repeatedNumList.insert(repeatedNumCounter, sorted_numList[i])
            numCountList.insert(repeatedNumCounter, numCounter)
            repeatedNumCounter += 1
            numCounter = 1

for x in range (0, repeatedNumCounter):
    maxNumList.insert(x,[numCountList[x], repeatedNumList[x]]) 

# Sort by highest repeating numbers that are generated, for display purpose
maxNumList.sort(reverse=True)

# for counter checking
cnt = 0 
print('\n','Discounting all duplicates, total count of random number generated is: ', repeatedNumCounter)
print('(No. )  Gen Number:  [# of times]')
for i in range (0,repeatedNumCounter):
    print('({0:^4d})'. format(i+1),' {0:^10d}:'. format(maxNumList[i][1]), ' [{0:^5d}]'. format(maxNumList[i][0]))
    # for counter checking
    cnt = cnt + maxNumList[i][0]

# for counter checking
print('Counter checking by summing up [# of times]: ', cnt) 


# Below are for printing out to check 
# print('The last word in sortedWordList is: ',sorted_numList[-1])
# print('\n','The repeatedWorkList: ', repeatedNumList)
# print('\n','The numCountList: ', numCountList)
# print('\n','The repeatedNumCounter is: ', repeatedNumCounter)
# print('\n','The last numCounter is: ', numCounter)
# print('\n','The maxNumList is: ', maxNumList)

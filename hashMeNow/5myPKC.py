import timeit as tm
import math 
import random

def is_prime(n: int) -> bool:
    # This is function is modified by code found in Wiki on Primility test prime number. 
    # It is not the best prime number tester
    # The function returns when testing stuck in the loop for long duration, hence possible prime 
    start = tm.default_timer()
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5

    while i ** 2 <= n:

        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        end = tm.default_timer()
        if ((end - start) > 0.05794069999999999):
            break

    return True

def possiblePrimePair(minPrime):
    # numX is for primility test function is_prime(), where RSA ideally requires 
    #  numX to be 200 char space or 200 X 8 bits space, i.e. is 2^1600.
    # For testing purpose, numX is set lower, + 17 (or any other odd number) 
    # is to makes sure numX (always even) starts indeed as a odd number. 
    # All prime number are all odd
    numX = 2**minPrime + 17
    step = 100
    primeCounter = 0
    primeList = []

    for i in range (numX, numX + step):
 
        if (is_prime(i) == False):
            print('Testing prime...')

        else:
            # print('\n\n\nS/n (', x,')  is a possible prime: ', i,'\n\n\n')
            # when is_prime() return True, write prime number to primeList 
            primeList.insert(0,i)
            primeCounter +=1
            # when two prime numbers are computed, break the loop
            if (primeCounter == 2):
                break

    p = primeList[1]
    q = primeList[0]

    # print('\n\n\nA possible prime, p: ', primeList[1],'\n\n\n')
    # print('\n\n\nA possible prime, q: ', primeList[0],'\n\n\n')

    pMinus = p - 1
    qMinus = q - 1 

    # print('\n\n\n p - 1: ', pMinus,'\n\n\n')
    # print('\n\n\n q - 1: ', qMinus,'\n\n\n')

    
    # n = p X q
    pq = math.prod(primeList)

    # below line equals to (p-1)(q-1)
    # lecture uses Greek letter Phi Φ for this number
    pqMinus = math.prod(primeList) - p - q + 1
    
    print('n = (p)(q) =', pq)
    # print('(p-1)(q-1) =', pqMinus)

    return p, q, pq, pqMinus

def rabinMiller(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    s = n - 1
    t = 0
    i = 0
    while s % 2 == 0:
        # print('s is')
        s = s // 2 # s div 2
        t = t + 1
    for trial in range(0, 10):
        a = random.randrange(2, n-1)
        # print('a is')
        x = 0
        x = pow(a, s, n) # a^s mod n
        # print('x is')
        if x != 1:
            # i = 0
            while x != (n - 1):
                # print('x in while is')
                if i == t - 1:
                    return False
                else:
                    return True
        
        else:
            i = i + 1
            x = pow(x, 2, n) # x^2 mod n
    return True


def computeModula(mydividend,mydivisor):
    print('Numerator is', mydividend)
    print('Denominator is', mydivisor)

    return mydividend%mydivisor


def Gen(minPrime):
    p, q, pq, pqMinus = possiblePrimePair(minPrime)
    
    print('Two possible prime, p: [', p, '] and q: [',q,'] generated using using 6k+-1 optimization')
    print('Testing primes using rabin miller')
    
    pResult = rabinMiller(p)
    qResult = rabinMiller(q)

    if (pResult == False and qResult == False):
        print('Change value of minPrime')
        returnAnswer = False
    else:
        eTest = 11
        e = findWholeNumber_e(pqMinus,eTest)

        print('Initial testing e is ', eTest, '. Computed suitable small e is', e)
        d = findWholeNumber_d(pqMinus, e)
        print('Computed RSA Keys,e: [', e,'] and d is: [', d, '] \n\n\n')

        returnAnswer = [] 
        returnAnswer.insert(0,p)
        returnAnswer.insert(1,q)
        returnAnswer.insert(2,pq)
        returnAnswer.insert(3,e)
        returnAnswer.insert(4,d)

    return returnAnswer

def findWholeNumber_e(pqMinus,eTest):
# Since numX can change to find possible sets of primes p and q, 
# eTest to test the criteria gcd (e, (p-1)(q-1)) = 1, 
# by incrementing by 1 each time. If criteria met, returns e
    e = 0
    while e != 1:
        e = gcd(pqMinus,eTest)
        if e != 1:
            eTest += 1
    return eTest

def gcd(a, b):
    while a != 0:
        a, b = b%a, a
    return b

def findWholeNumber_d(testPairMinus, e):
    #    e x d mod (p-1)(q-1) = 1, or written in long division maths equals to 
    #    e x d / (p-1)(q-1) = Quotient X with remainder (1) 
    #  ((e x d)) - 1)/ (p-1)(q-1) = X with remainder 0   *** eqn ONE 
    #    X must be a whole number act as a factor. X = {1, 2, 3, ... infinity}
    #   (e x d) = X(p-1)(q-1) + 1
    #        d  = (X(p-1)(q-1) + 1)/e  *** eqn TWO
    #    e must also be a whole number, i.e. modulas return must be 0, no remainder
    #    Value of X, quotX, is should be the smallest factor (eqn ONE), 
    #    thus refValueX (loop from 1 to 9) to determine d which satisfies (p-1)(q-1)

    quotX = 1
    t = 1
    refValueX = 10
    # print('i am here')
    while (quotX < refValueX):
        quotX += 1
        t += 1
        # refer numerator of eqn TWO 
        answer = (1 + quotX*testPairMinus)

        # refer numerator of eqn TWO, remainder must be 0
        testD = answer%e
        if (testD == 0): 
            print('Possible possible RSA Key, d, is: ', answer//e, ' when x: ', quotX)
            quotX = 1000
            # break
    # This is to test if a d can be computed within refValueX    
    if (t == refValueX):
        print('Computed RSA Key, d = ',answer//e, ' is wrong. Either reduce message length, choose another set of primes or prime offset, or increase refValueX',)
        returnAnswer = False            
        print('This is tester t', t)
    else:
        print('This is tester t', t)
        returnAnswer = answer//e
    return returnAnswer

##### Main program starts here #####


# minPrime refers to bits of 2, 2^minPrime, in order to gen Prime pairs
minPrime = 11
returnAnswer = Gen(minPrime)

if returnAnswer == False:
    print('Prime test failed, end of program')

else:
    
    print(returnAnswer)
    m = 1234567
    p = returnAnswer[0]
    q = returnAnswer[1]
    pq = returnAnswer[2]
    e = returnAnswer[3]
    d = returnAnswer[4]
    print(m**returnAnswer[3])
    print('Encryting and Decrypting message', m,' with RSA Key,e,: ', returnAnswer[3], ' with d: ', returnAnswer[4])

    # cText = computeModula(m**returnAnswer[3],returnAnswer[2])
            # x = pow(a, s, n) # a^s mod n
    cText = pow(m,e,pq)
    print('Ciphertext is:', cText)

    pText =pow(cText,d,pq)

    print('Plaintext is:',pText)

    # pTextp = ((cText**d))%p

    # print('Plaintext (using modular of p) is:',pTextp)

    # pTextq = ((cText**d))%q

    # print('Plaintext (using modular of q) is:',pTextq)

    # print(pTextp*pTextq)


# print('\n\n\nHello... n = p X q:', pq,'\n\n\n')

# pqMinus is (p-1)(q-1)
# criteria for e must satisfy gcd (e, (p-1)(q-1)) = 1 and should be small
# Thus function findWholeNumber_e to find a suitable e
# eTest = 12 will NOT satisfy 
# testing values of numX = 2**11 + 17 which generates p = 2069, q = 2081



# gen(minPrime)
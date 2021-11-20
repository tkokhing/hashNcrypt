import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

sumBinomial = 0

for i in range (17,151):
    sumBinomial = sumBinomial + (nCr(150,i) * (0.05**i) * (0.95**(150-i)))

print(sumBinomial)

# using 1 - p 
sumBinomial = 0

for i in range (0,134):
    sumBinomial = sumBinomial + (nCr(150,i) * (0.95**i) * (0.05**(150-i)))

print(sumBinomial)


# find exactly 17 out of 150 active
# find exactly 133 out of 150 inactive

# find exactly 17 out of 150 active
sumBinomial = 0
sumBinomial = sumBinomial + (nCr(150,17) * (0.05**17) * (0.95**(133)))
print('Exactly 17 active: ',sumBinomial)


# find exactly 133 out of 150 inactive
sumBinomial = 0
sumBinomial = sumBinomial + (nCr(150,133) * (0.95**133) * (0.05**(17)))
print('Exactly 133 inactive: ',sumBinomial)

# Conclusion: So there is no need to do 1 - {probability of 133 out of 155 inactive}
# Also my Power to NCr was conceptually wrong. 
# Seriously wrong. NCr , N = 133, r = 0 <towards 133>... This means 
# that it will reach 133 out of 133 which is everyone. This is seriously conceptually 
# fatally wrong. <<<This wrong programming was already been overwritten>>>   

#if __name__ == '__main__':
# ans = nCr(4,0)
# print(ans)
# ans = nCr(4,1)
# print(ans)
# ans = nCr(4,2)
# print(ans)
# ans = nCr(4,3)
# print(ans)
# ans = nCr(4,4)
# print(ans)


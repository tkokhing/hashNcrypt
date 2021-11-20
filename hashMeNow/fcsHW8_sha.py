# This is individual work

# The length of the string when shorten does not affected the ley length.  

import hashlib
import hmac

# Trial 1 asked using SHA1
hashed = hashlib.sha1("LovingItCybersecurityReengineeringMyLife".encode()).hexdigest()
print('Using SHA1, the hash of "LovingItCybersecurityReengineeringMyLife" is \n', hashed)
print('Key Length is: ', len(hashed))
#


hashed = hashlib.sha1("51.505-Foundations-of-Cybersecurity-MSSd".encode()).hexdigest()
print('Using SHA1, the hash of "51.505-Foundations-of-Cybersecurity-MSSd" is \n', hashed)
print('Key Length is: ', len(hashed))



# Testing out other hashes

hashed = hashlib.md5("LovingItCybersecurityReengineeringMyLife".encode()).hexdigest()
print('Using MD5, the hash of "LovingItCybersecurityReengineeringMyLife" is \n', hashed)
print('Key Length is: ', len(hashed))

hashed = hashlib.md5("51.505-Foundations-of-Cybersecurity-MSSd".encode()).hexdigest()
print('Using MD5, the hash of "51.505-Foundations-of-Cybersecurity-MSSd" is \n', hashed)
print('Key Length is: ', len(hashed))


# Testing out other hashes
hashed = hashlib.sha256("LovingItCybersecurityReengineeringMyLife".encode()).hexdigest()
print('Using SHA256, the hash of "LovingItCybersecurityReengineeringMyLife" is \n', hashed)
print('Key Length is: ', len(hashed))

hashed = hashlib.sha256("51.505-Foundations-of-Cybersecurity-MSSd".encode()).hexdigest()
print('Using SHA256, the hash of "51.505-Foundations-of-Cybersecurity-MSSd" is \n', hashed)
print('Key Length is: ', len(hashed))



# Testing out other hashes
hashed = hashlib.sha384("LovingItCybersecurityReengineeringMyLife".encode()).hexdigest()
print('Using SHA384, the hash of "LovingItCybersecurityReengineeringMyLife" is \n', hashed)
print('Key Length is: ', len(hashed))

hashed = hashlib.sha384("51.505-Foundations-of-Cybersecurity-MSSd".encode()).hexdigest()
print('Using SHA384, the hash of "51.505-Foundations-of-Cybersecurity-MSSd" is \n', hashed)
print('Key Length is: ', len(hashed))




# Trial 2 asked using SHA256
print('\n')
print('\n')
print('\n')
hashed = hashlib.sha256("Hi There".encode()).hexdigest()
print('Using SHA256, the hash of "Hi There" is \n', hashed)
print('Key Length is: ', len(hashed))
print('Class Type of SHA 256 Hashed is ',type(hashed))


hashed = hashlib.sha256(b'\x48\x69\x20\x54\x68\x65\x72\x65').hexdigest()
print('Using SHA256, the hash of "Hi There" in type out in Hex is \n', hashed)
print('Key Length is: ', len(hashed))

# Using SHA256, the hash of "Hi There" is
#  cc6d5896d770101ef0280c943a2d3c3f24cd5b11464a5186daf7a238477162ac
# Key Length is:  64
# Using SHA256, the hash of "Hi There" is
#  cc6d5896d770101ef0280c943a2d3c3f24cd5b11464a5186daf7a238477162ac
# Key Length is:  64


# 0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b 
# Above is the key provided, which will not work if simply put in the function 
# Below is the key in Byte added with \x in front
# This works as per the description in hmac.py
# \x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b 

hashMAC = hmac.new(b'\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b',b"Hi There",hashlib.sha256)
# hashed = hashlib.sha256(b'\x48\x69\x20\x54\x68\x65\x72\x65').hexdigest()

print('Using hmac.new with SHA256, the test vector of "Hi There" in type out in Hex is \n', hashMAC)
print(type(hashMAC))
print('Block Size is: ', hashMAC.block_size)
print('Digest Size is: ', hashMAC.digest_size)
# Above output is //
# Using SHA256, the test vector of "Hi There" in type out in Hex is
#  <hmac.HMAC object at 0x0000021BE3D46180> 
# <class 'hmac.HMAC'>
# Block Size is:  64
# Digest Size is:  32


 
# hexadecimal_string = hashMAC.hex()
# print('The hash in Hex is: ', hexadecimal_string)
# Above cannot work with hmac.new,unlike hmac.digest 


hashMAC = hmac.digest(b'\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b',b"Hi There",hashlib.sha256)

print('Using hmac.digest with SHA256, the test vector on message "Hi There" in hmac.HMAC object form is \n', hashMAC)
print(type(hashMAC))

# Interesting finding, block_size and digest_size are not available after using hmac.digest unlike hmac.new
# print('Block Size is: ', hashMAC)
# Using SHA256, the test vector of "Hi There" in type out in Hex is
#  b'\x19\x8a`~\xb4K\xfb\xc6\x99\x03\xa0\xf1\xcf+\xbd\xc5\xba\n\xa3\xf3\xd9\xae<\x1cz;\x16\x96\xa0\xb6\x8c\xf7'
# <class 'bytes'>

# Below is wrong
# print(hashMAC.HMAC.digest_size)

# some_bytes = b'\x19\x8a`~\xb4K\xfb\xc6\x99\x03\xa0\xf1\xcf+\xbd\xc5\xba\n\xa3\xf3\xd9\xae<\x1cz;\x16\x96\xa0\xb6\x8c\xf7'
hexadecimal_string = hashMAC.hex()
print('The hash in Hex is: ', hexadecimal_string)


# SHA512 

hashMAC = hmac.new(b'\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b',b"Hi There",hashlib.sha512)
print('Using SHA512, the test vector on message "Hi There" in hmac.HMAC object form is \n', hashMAC)
print(type(hashMAC))
print('Block Size is: ', hashMAC.block_size)
print('Digest Size is: ', hashMAC.digest_size)


hashMAC = hmac.digest(b'\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b',b"Hi There",hashlib.sha512)
print('Using SHA512, the test vector on message "Hi There" in hmac.HMAC object form is \n', hashMAC)
print(type(hashMAC))
print('Block Size is: ', hashMAC)
hexadecimal_string = hashMAC.hex()
print('The SHA512 hash in Hex is: ', hexadecimal_string)


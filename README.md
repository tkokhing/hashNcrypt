## hashNcrypt
Just some work on hashing and en/decrypt, for colab

# latest Upload - 5myPKC.py 
- This is derived for testing RSA enc and dec. By playing different values of minPrime, to generate diff values of  prime number. For  of up to the length 2^17 (17 bits), instead of the desire 200 bits and more. The relationship between, message length, length of RSA keys e and d, correspond to a successful Decryption were measured using the following values.

The message size (length) was tested started from 12345 to 12345567890. It was obsserved that the encryption and decryption timing got longer. 

As the length of the message increases, the primes p and q must also correspondingly increased in other to generate suitable RSA keys e and d. 

Comparing the RSA key lengths, e should be smaller so that the encryption will be faster, while the decryption requires more processing which in turns to security of the message during transmission.

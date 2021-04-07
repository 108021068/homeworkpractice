import hashlib
import hmac
import sys
import binascii

passwordList = []
with open ('passwordList.txt', 'r')as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        passwordList.append(currentPlace)
    #print(passwordList)
if len (sys.argv) ==2:
    msg = sys.argv[1].encode()
    hashValue = hashlib.sha1(msg)

if len(sys.argv)>1:
    msg= sys.argv[1].encode()
    hashvalue = hashlib.sha256(msg)
    print(hashvalue)
    print(hashvalue.hexdigest().upper())

if len(sys.argv)>1:
    msg= sys.argv[1].encode()
    hashvalue = hashlib.sha512(msg)

    print(hashvalue)
    print(hashvalue.hexdigest().upper())

if len(sys.argv)>1:
    msg= sys.argv[1].encode()
    hashvalue = hashlib.sha1(msg)
    print(hashvalue)
    print(hashvalue.hexdigest().upper())

if len(sys.argv)>1:
    msg= sys.argv[1].encode()
    hashvalue = hashlib.md5(msg)
    print(hashvalue)
    print(hashvalue.hexdigest().upper())

import hashlib
import sys
md5fortext = []
sha1fortext = []
sha256fortext = []
sha512fortext = []
text = []
if len(sys.argv) == 2:
    msg = sys.argv[1].encode('utf-8')
    #sha256做的 hash 值
    hashvaluetosha256 = hashlib.sha256(msg)
    print(hashvaluetosha256)
    print(hashvaluetosha256.hexdigest().upper())
    print()
    #md5做的 hash 值
    hashvaluetomd5 = hashlib.md5(msg)
    print(hashvaluetomd5)
    print(hashvaluetomd5.hexdigest().upper())
    print()
    #sha1做的 hash 值
    hashvaluetosha1 = hashlib.sha1(msg)
    print(hashvaluetosha1)
    print(hashvaluetosha1.hexdigest().upper())
    print()
    #sha512做的 hash 值
    hashvaluetosha512 = hashlib.sha512(msg)
    print(hashvaluetosha512)
    print(hashvaluetosha512.hexdigest().upper())
    print()

f = open('D://10-million-password-list-top-100.txt')
for line in f:
    text.append(line.split("\n")[0])
    sha256fortext.append(hashlib.sha256(line.split("\n")[0].encode()).hexdigest().upper())
    sha1fortext.append(hashlib.sha1(line.split("\n")[0].encode()).hexdigest().upper())
    sha512fortext.append(hashlib.sha512(line.split("\n")[0].encode()).hexdigest().upper())
    md5fortext.append(hashlib.md5(line.split("\n")[0].encode()).hexdigest().upper())
    #print(hashfortext)

if len(sys.argv) > 2:
    if sys.argv[1] == "-c":  
        for i in range(len(text)):
            if sys.argv[2] == sha1fortext[i]: 
                print("<password is",text[i],"><sha1 Hash>")
            elif sys.argv[2] == sha256fortext[i]: 
                print("<password is",text[i],"><sha256 Hash>")
            elif sys.argv[2] == sha512fortext[i]: 
                print("<password is",text[i],"><sha512 Hash>")
            elif sys.argv[2] == md5fortext[i]: 
                print("<password is",text[i],"><md5 Hash>")

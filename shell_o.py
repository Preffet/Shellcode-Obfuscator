import binascii
import random
# paste your shellcode here, make sure you follow the
# character count per line and don't forget the b !
payload = bytes(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        #... your byte string goes here
        b"\x00\x00\x00\x00")

k = binascii.hexlify(payload).decode('utf-8')
random.seed(1)
au = [random.choice("0123456789abcdef") + i for i in k]

f = "\\x" + "\\x".join(au)
chunks = [f[i:i+60] for i in range(0, len(f), 60)]
input = "\"" + "\"\n\"".join(chunks)

print(input)


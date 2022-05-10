from random import * 
key=["."]*25 
encription=[] 
for i in range(0,25):
  num=randint(0,25) 
  assign="false" 
  exit="false" 
  while exit=="false": 
    for x in range(0,25): 
      if key[x]==num:
        num=randint(0,25)
        assign="false"
        break
      else:
        assign="true" 
    if assign=="true":
      key.insert(i, num) 
      exit="true"
      
for v in range(0,25):
  key.remove(".")
strKey=''.join([str(item) for item in key])
def encrypt(key, msg):
    encryped = []
    print("Key: "+ key)
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encryped.append(chr((msg_c-key_c) % 126))
    return ''.join(encryped)

def decrypt(key, encryped):
    msg = []
    for i, c in enumerate(encryped):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c + key_c) % 126))
    return ''.join(msg)
message=input("Message: ")
useKey=input("Key: ")
if userKey!="":
	strKey=userKey
encriptStr=encrypt(strKey,message)
print("Encrypted: "+ encriptStr)
decrypted=decrypt(strKey,message)
decryptStr=decrypt(strKey,encriptStr)
print("Original text): "+ decryptStr)
print("Decrypted: "+ decryptStr)

import base64
#set1 convert hex string -> bytes -> base 64
def converter(hex_string):
     hex2byte = bytes.fromhex(hex_string)
     #output is "I'm killing your brain like a poisonous mushroom"
     b64_encoded = base64.b64encode(hex2byte).decode()
     return b64_encoded
     #output is SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t



def xor(inputString, compareByte):
     
     inputByte = bytes.fromhex(inputString)
     compareByte = bytes.fromhex(compareByte)

     result = bytes([x^y for x,y in zip(inputByte, compareByte)])

     


     
     return result.hex()
    

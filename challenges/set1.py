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
    

def findKey(hexString):
     
     byteSequence = bytes.fromhex(hexString)
     eFrequencyList = []
     eSum= 0
     #ETAOIN SHRDLU

     for i in range(256):
         eSum= 0
         for bit in byteSequence:
            if (bit^i) == ord('e'):
                eSum += 2
            elif (bit^i) == (ord('t')):
                eSum += 2
            elif (bit^i) == (ord('a')):
                eSum += 2
            elif (bit^i) == (ord('o')):
                eSum += 2
            elif (bit^i) == (ord('i')):
                eSum += 2
            elif (bit^i) == (ord('n')):
                eSum += 1
            elif (bit^i) == (ord('s')):
                eSum += 1
            elif (bit^i) == (ord('h')):
                eSum += 1
            elif (bit^i) == (ord('r')):
                eSum += 1
            elif (bit^i) == (ord('d')):
                eSum += 1
            elif (bit^i) == (ord('l')):
                eSum += 1
            elif (bit^i) == (ord('u')):
                eSum += 1
        
            


         eFrequencyList.append(eSum)
    
     maxIndex =  (eFrequencyList.index(max(eFrequencyList)))

     decryption = bytes([bit^maxIndex for bit in byteSequence])

     return decryption






          
          



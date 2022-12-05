import codecs
import pickle
from cryptography.fernet import Fernet
from AESencryptfunc import * #import AESencryptfunc module to use functions created for this program
import math #import math module to use function such as ceiling

#check that script is running with the two text files as the two parameters or else quit
# if len(sys.argv) is not 3:#takes in two arguments for the plaintext.txt file name and cipherhex.txt file name
#     sys.exit("Error, script needs two command-line arguments. (Plaintext.txt File and cipherhex.txt File)")

# # set passphrase to be a 16 characters, 16 characters * 8 bits = 128 bits strength
# PassPhrase="thisiskeyforaess"
# while(len(PassPhrase)!=16):
#     print("Enter in the 16 character passphrase to encrypt your text file %s" %sys.argv[1])
#     PassPhrase=input()#takes in user input of char, eg. "Iwanttolearnkung"
#     if(len(PassPhrase)<16):#check if less than 16 characters, if so add one space character until 16 chars
#         while(len(PassPhrase)!=16):
#             PassPhrase=PassPhrase+"\00"
#     if(len(PassPhrase)>16):#check if bigger than 16 characters, if so then truncate it to be only 16 chars from [0:16]
#         print("Your passphrase was larger than 16, truncating passphrase.")
#         PassPhrase=PassPhrase[0:16]

#open plaintext.txt file to read and encrypt
def encrypt():
    PassPhrase = "thisiskeyforaess"


    while (len(PassPhrase) != 16):
        # print("Enter in the 16 character passphrase to encrypt your text file %s" %
        #     sys.argv[1])
        # PassPhrase = input()  # takes in user input of char, eg. "Iwanttolearnkung"
        if (len(PassPhrase) < 16):  # check if less than 16 characters, if so add one space character until 16 chars
            while (len(PassPhrase) != 16):
                PassPhrase = PassPhrase+"\00"
        # check if bigger than 16 characters, if so then truncate it to be only 16 chars from [0:16]
        if (len(PassPhrase) > 16):
            print("Your passphrase was larger than 16, truncating passphrase.")
            PassPhrase = PassPhrase[0:16]
    with codecs.open('plaintext1.txt', encoding='utf-8') as f:
        input = f.read()
    message=(input)
    # dbfile = open('examplePickle', 'rb')
    # fernet = pickle.load(dbfile)
    # decMessage = fernet.decrypt(encMessage).decode()
    # print(message)
    # p1=""
    # # for i in message:
    # #     print(ord(i))
    # for i in message:
    #     k=ord(i)
    #     if k==10:
    #         continue
    #     if k==13:
    #         k=10
    #     quotient=int(k/123)
    #     remainder=k%123
    #     quotient+=123
    #     # print(k, c1, c)
    #     # print(c1)
    #     p1=p1+chr(remainder)
    #     p1=p1+chr(quotient)
    #     # print(p1)
    key = Fernet.generate_key()
    f = open("key.txt", "a")
    # Instance the Fernet class with the key
    key1 = str(key, 'UTF-8')

    f.write(key1)
    f1 = open('key.txt', 'r')
    p11 = f1.read()
    res = bytes(p11, 'utf-8')
    # Instance the Fernet class with the key

    fernet = Fernet(res)
    # print(fernet)

    # then use the Fernet class instance
    # to encrypt the string string must
    # be encoded to byte string before encryption
    encMessage = fernet.encrypt(message.encode())

    # print("original string: ", message)
    # print("encrypted string: ", encMessage)

    # decrypt the encrypted string with the
    # Fernet instance of the key,
    # that was used for encrypting the string
    # encoded byte string is returned by decrypt method,
    # so decode it to string with decode methods
    # print(type(encMessage))
    p1 = str(encMessage, 'UTF-8')
    # print(p1)
    # decMessage = fernet.decrypt(encMessage).decode()

    # print("decrypted string: ", decMessage)
    message=p1

    # printing the encoded string
    # print("The encoded string in base64 format is : ",)
    # print(str_enc)

    # printing the original decoded string
    # print("The decoded string is : ",)
    # print(str_enc.decode('utf8', 'strict'))

    # message1=message.encode(encoding='utf8')
    # message = "f39f9072434b929bb49644ab2b21b76a"
    print("Inside your plaintext message is:\n%s\n" % message)
    # file.close()

    message=BitVector(textstring=message)
    message=message.get_bitvector_in_hex()
    replacementptr=0
    while(replacementptr<len(message)):
        if(message[replacementptr:replacementptr+2]=='0a'):
            message=message[0:replacementptr]+'0d'+message[replacementptr:len(message)]
            replacementptr=replacementptr+4
        else:
            replacementptr=replacementptr+2

    message=BitVector(hexstring=message)
    message=message.get_bitvector_in_ascii()
    #set up some parameters
    start=0#set starting pointer for the part to encrypt of the plaintext
    end=0#set ending pointer for the part to encrypt of the plaintex
    length=len(message)#check the entire size of the message
    loopmsg=0.00#create a decimal value
    loopmsg=math.ceil(length/16)+1#use formula to figure how long the message is and how many 16 character segmentss must be encrypted
    outputhex=""#setup output message in hex

    #need to setup roundkeys here
    PassPhrase=BitVector(textstring=PassPhrase)
    roundkey1=findroundkey(PassPhrase.get_bitvector_in_hex(),1)
    roundkey2=findroundkey(roundkey1,2)
    roundkey3=findroundkey(roundkey2,3)
    roundkey4=findroundkey(roundkey3,4)
    roundkey5=findroundkey(roundkey4,5)
    roundkey6=findroundkey(roundkey5,6)
    roundkey7=findroundkey(roundkey6,7)
    roundkey8=findroundkey(roundkey7,8)
    roundkey9=findroundkey(roundkey8,9)
    roundkey10=findroundkey(roundkey9,10)
    roundkeys=[roundkey1,roundkey2,roundkey3,roundkey4,roundkey5,roundkey6,roundkey7,roundkey8,roundkey9,roundkey10]

    #set up FILEOUT to write
    FILEOUT = open('ciphertext.txt', 'w')

    # set up the segement message loop parameters
    for y in range(1, loopmsg): # loop to encrypt all segments of the message
        if(end+16<length): #if the end pointer is less than the size of the message, then set the segment to be 16 characters
            plaintextseg = message[start:end + 16]
        else: #or else if the end pointer is equal to or greator than the size of the message
            plaintextseg = message[start:length]
            for z in range(0,((end+16)-length),1): #run a while loop to pad the message segement to become 16 characters, if it is 16 already the loop will not run
                plaintextseg = plaintextseg+"\00"
                #plaintextseg2=BitVector(textstring=plaintextseg)
                #print(plaintextseg2.get_bitvector_in_hex())

        #add round key zero/ find round key one
        bv1 = BitVector(textstring=plaintextseg)
        bv2 = PassPhrase
        resultbv=bv1^bv2
        myhexstring = resultbv.get_bitvector_in_hex()

        for x in range(1, 10):  # loop through 9 rounds
            # sub byte
            myhexstring = resultbv.get_bitvector_in_hex()
            temp1=subbyte(myhexstring)

            # shift rows
            temp2=shiftrow(temp1)

            # mix column
            bv3 = BitVector(hexstring=temp2)
            newbvashex=mixcolumn(bv3)
            newbv=BitVector(hexstring=newbvashex)

            #add roundkey for current round
            bv1 = BitVector(bitlist=newbv)
            bv2 = BitVector(hexstring=roundkeys[x-1])
            resultbv = bv1 ^ bv2
            myhexresult = resultbv.get_bitvector_in_hex()

        #start round 10
        # sub byte round 10
        myhexstring = resultbv.get_bitvector_in_hex()
        temp1=subbyte(myhexstring)

        # shift rows round 10
        temp2=shiftrow(temp1)

        # add round key round 10
        newbv = BitVector(hexstring=temp2)
        bv1 = BitVector(bitlist=newbv)
        bv2 = BitVector(hexstring=roundkeys[9])
        resultbv = bv1 ^ bv2
        myhexstring = resultbv.get_bitvector_in_hex()

        #set encrypted hex segement of message to output string
        outputhextemp = resultbv.get_hex_string_from_bitvector()
        FILEOUT.write(outputhextemp)
        start = start + 16 #increment start pointer
        end = end + 16 #increment end pointer

    # encrypted output hex string to specified cipherhex file
    FILEOUT.close()

# file2=open(sys.argv[2], "r")
# print("The output hex value for the entire message is:\n%s\n" % file2.read())
# file2.close()
# encrypt()
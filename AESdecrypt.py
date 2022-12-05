from AESdecryptfunc import * #import AESdecryptfunc module to use functions created for this program
import math #import math module to use function such as ceiling
import io
from cryptography.fernet import Fernet

#check that script is running with the two text files as the two parameters or else quit
# if len(sys.argv) is not 3:#takes in two arguments for the ciphertext.txt file name and plainhex.txt file name
#     sys.exit("Error, script needs two command-line arguments. (Ciphertext.txt File and plainhex.txt File)")
def decrypt():
    PassPhrase="thisiskeyforaess"

    while(len(PassPhrase)!=16):
        # print("Enter in the 16 character passphrase to decrypt your text file %s" %sys.argv[1])
        # PassPhrase=input()#takes in user input of char, eg. "Iwanttolearnkung"
        if(len(PassPhrase)<16):#check if less than 16 characters, if so add one space character until 16 chars
            while(len(PassPhrase)!=16):
                PassPhrase=PassPhrase+"\00"
        if(len(PassPhrase)>16):#check if bigger than 16 characters, if so then truncate it to be only 16 chars from [0:16]
            print("Your passphrase was larger than 16, truncating passphrase.")
            PassPhrase=PassPhrase[0:16]

    #open ciphertext.txt file to read and decrypt
    file=open("ciphertext.txt", "r")
    message=(file.read())
    print("Inside your ciphertext message is:\n%s\n" % message)
    file.close()

    #set up some parameters
    start=0#set starting pointer for the part to decrypt of the ciphertext
    end=32#set ending pointer for the part to decrypt of the plaintex
    length=len(message)#check the entire size of the message
    loopmsg=0.00#create a decimal value
    loopmsg=math.ceil(length/32)+1#use formula to figure how long the message is and how many 16 character segmentss must be decrypted
    outputhex=""#setup output message segment in hex
    asciioutput=""#setup compilation of output message in ascii

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

    FILEOUT = io.open("plaintext2.txt", 'w', encoding='utf-8')

    # set up the segement message loop parameters
    for y in range(1, loopmsg): # loop to encrypt all segments of the message
        plaintextseg = message[start:end]

        # add round key
        bv1 = BitVector(hexstring=plaintextseg)
        bv2 = BitVector(hexstring=roundkeys[9])
        resultbv = bv1 ^ bv2
        myhexstring = resultbv.get_bitvector_in_hex()

        #inverse shift row
        myhexstring=invshiftrow(myhexstring)

        #inverse subbyte
        myhexstring=invsubbyte(myhexstring)

        for x in range(8, -1, -1):
            # add roundkey for current round
            bv1 = BitVector(hexstring=myhexstring)
            bv2 = BitVector(hexstring=roundkeys[x])
            resultbv = bv1 ^ bv2
            myhexstring = resultbv.get_bitvector_in_hex()

            # mix column
            bv3 = BitVector(hexstring=myhexstring)
            myhexstring=invmixcolumn(bv3)

            # shift rows
            myhexstring = invshiftrow(myhexstring)

            # sub byte
            myhexstring = invsubbyte(myhexstring)

        #add initial round key
        bv1 = BitVector(hexstring=myhexstring)
        bv2 = PassPhrase
        resultbv = bv1 ^ bv2
        myhexstring = resultbv.get_bitvector_in_hex()

        start = start + 32 #increment start pointer
        end = end + 32 #increment end pointer

        replacementptr = 0
        while (replacementptr < len(myhexstring)):
            if (myhexstring[replacementptr:replacementptr + 2] == '0d'):
                myhexstring = myhexstring[0:replacementptr] + myhexstring[replacementptr+2:len(myhexstring)]
            else:
                replacementptr = replacementptr + 2

        outputhex = BitVector(hexstring=myhexstring)
        # print(outputhex)
        asciioutput = outputhex.get_bitvector_in_ascii()
        # print(asciioutput)
        # print(asciioutput)
        # asciioutput=asciioutput.replace('\x00','')
        # print("ascii")
        # print(asciioutput)
        # p1=""
        # # for i in 
        # for i in range(0,len(asciioutput)-1,2):
        #     remainder=ord(asciioutput[i])
        #     quotient=ord(asciioutput[i+1])
        #     # if(k==13):
        #     #     continue
        #     # print(remainder, quotient)
        #     quotient-=122
        #     c1=(122*quotient)+remainder
        #     # print(c1)
        #     p1+=chr(c1)
        # FILEOUT.write(p1)
        FILEOUT.write(asciioutput)
        # print(asciioutput)

    FILEOUT.close()
    # f = open("plaintext2.txt", "r")
    # print(f.read())
    f1 = open('key.txt', 'r')
    p11 = f1.read()
    res = bytes(p11, 'utf-8')
    fernet=Fernet(p11)
    file2=io.open("plaintext2.txt", "r", encoding='utf-8')
    mes=file2.read()
    mes.replace('\x00','')
    res = bytes(mes, 'utf-8')

    decMessage = fernet.decrypt(res).decode()
    final_out = open("output.txt", "w", encoding='utf-8')
    final_out.write(decMessage)
    final_out.close()
    # print("The decrypted message for the entire ciphertext is:\n%s\n" % decMessage)
    file2.close()
# decrypt()
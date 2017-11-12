def to_byte(text):
    btext=""
    for c in text:
        b=str(bin(ord(c)))[2:]
        while(len(b)<8):
            b="0"+b
        btext+=b
    return btext

def to_ascii(btext):
    text=""
    i=0
    for counter in range(int((len(btext))/8)):
        bc=btext[i:(8*(counter+1))]
        c=chr(int(bc,2))
        i=i+8
        text=text+c
    return text
def to_base10(binNum):
    return (int(binNum,2))
def to_base2(decNum):
    b2=bin(decNum)[2:]
    while(len(b2)%8!=0):
        b2="0"+b2
    return b2
bt=to_byte("Ciao Mondo!")
print(bt)
b10=to_base10(bt)
print(b10)
b2=to_base2(b10)
print(b2)
nt=to_ascii(bt)
print(nt)

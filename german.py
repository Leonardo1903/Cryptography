import math
keysquare = {'Q':'VX', 'C':'AG', '3':'AV', 'T':'DD', '6':'GF', 'W':'FF',
            'M':'DX', 'O':'DV', 'E':'FA', 'H':'AX', 'N':'AA', 'L':'VV',
            '8':'DA', 'A':'AD', '4':'GA', '2':'DG', '1':'AF', 'I':'GX',
            'G':'GG', 'B':'DF', '5':'FD', 'Z':'XX', 'R':'FG', '7':'GV',
            'S':'XA', 'X':'XG', '9':'VA', 'V':'XF', 'U':'XD', 'P':'FV',
            '0':'VF', 'K':'VG', 'J':'VD', 'F':'GD', 'D':'FX', 'Y':'XV'}


swapped_keysquare = {
    'VX': 'Q', 'AG': 'C', 'AV': '3', 'DD': 'T', 'GF': '6', 'FF': 'W',
    'DX': 'M', 'DV': 'O', 'FA': 'E', 'AX': 'H', 'AA': 'N', 'VV': 'L',
    'DA': '8', 'AD': 'A', 'GA': '4', 'DG': '2', 'AF': '1', 'GX': 'I',
    'GG': 'G', 'DF': 'B', 'FD': '5', 'XX': 'Z', 'FG': 'R', 'GV': '7',
    'XA': 'S', 'XG': 'X', 'VA': '9', 'XF': 'V', 'XD': 'U', 'FV': 'P',
    'VF': '0', 'VG': 'K', 'VD': 'J', 'GD': 'F', 'FX': 'D', 'XV': 'Y'
}



def keyGen():
    flag = True
    while (flag):
        flag=False
        code = input("Enter a Key: ")
        code=code.upper()
        i=0
        while (i<len(code)):
            j=i+1
            while (j<len(code) and flag == False):
                if (code[i]==code[j]):
                    flag = True
                    print("Bad Key!")

                j=j+1
            i=i+1
    return code

#encrypts plaintext
def Encrypt1():
    plaintext = input("Enter a string to encrypt: ")
    plaintext = plaintext.upper()
    ciphertext=""
    for letter in plaintext:
        if letter in keysquare:
            ciphertext+=keysquare[letter]
    print("YES:", ciphertext)
    return ciphertext

#returns matrix with configured list of ciphertext
def Encrypt2_Setup(key,ciphertext):
    width = len(key)
    height = math.ceil(len(ciphertext)/width)
    matrix= [["X" for x in range(width)] for y in range(height)]
    r=0
    c=0
    index=0
    while (r<height):
        while(c<width):
            if(index==len(ciphertext)):
                break
            matrix[r][c]=ciphertext[index]
            index=index+1
            c=c+1
        r=r+1
        c=0
        print(matrix)
    return matrix

# transposes a matrix
def Encrypt2_Transpose(key,matrix):
    width = len(key)
    height = len(matrix)
    skey = sorted(key)
    transposed=[["X" for x in range(width)] for y in range(height)]
    c = 0
    for letter in skey:
        into= key.index(letter)
        r=0
        while(r<height):
            transposed[r][c]=matrix[r][into]
            r=r+1
        c=c+1
    ciphertext=""
    for list in transposed:
        for char in list:
            ciphertext+=char
    return ciphertext



def main():
    thekey = keyGen()
    print(thekey)
    ciphertext = Encrypt1()
    e_matrix = Encrypt2_Setup(thekey,ciphertext)
    f_ciphertext = Encrypt2_Transpose(thekey,e_matrix)
    print("Ciphertext is: "+ f_ciphertext)

main()
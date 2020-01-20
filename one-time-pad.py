#Made by Jason Van Bladel

import png
import random
from PIL import Image
from PIL import ImageColor
import datetime
import time
import math

def turnInto256(charInt):
    if charInt < 69:
        return charInt + (94*random.randint(0,2))
    if charInt < 94:
        return charInt + (94*random.randint(0,1))
    else:
        return charInt
    
def Two56IntoCharInt(Int):
    return Int%94

def convertCharacterToASSKEY(char):
    return ord(char)-32

def convertASSKEYToChar(ASKEY):
    return chr(ASKEY+32)
def chooseRandomChar():
    return random.randint(0,93)

def encryptCharacter(char, key):
    return ((char + key)%94)

def decyrptCharacter(char, key):
    output = char - key
    if output < 0:
        return 94+output
    else:
        return output
    
def createSmallKey():
    return int(time.time())

def creatBigKey():
    small = 1
    for x in range(4096):
        small *= 2
    large = 1
    for x in range(8192):
        large *= 2
    value1 = random.randint(small, large)
    value2 = int(time.time()*100000000000000000000000000000000000000000000000000000000000000000000000000000)
    
    return  (value1* value2 + random.randint(1, 9))
    

def turnListIntoColorList(myList):
    outputList = list()
    aList = myList
    while len(aList)%4 != 0:
        aList.insert(len(aList),256)
    while len(aList) > 0:
        outputList.append([aList.pop(0),aList.pop(0),aList.pop(0),aList.pop(0)])
    return outputList

def createEncrytion(string, imageName, s):
    encryptionSize = 255
    key = 1
    if s == "b":
        key = createBigKey()
    else:
        key = createSmallKey()
    random.seed(key)
    myList = list()
    for char in string:
        rand = chooseRandomChar()
        myList.append(encryptCharacter(convertCharacterToASSKEY(char), rand))
 
    img = Image.new('RGBA', (encryptionSize, encryptionSize), color = 'white')

    colorList = turnListIntoColorList(myList)
    
    cordinateList = list()
    for x in range(encryptionSize):
        for y in range(encryptionSize):
            cordinateList.append([x,y])
            
    pixelList = list()
    for pixel in colorList:
        pixelList.append([cordinateList.pop(random.randint(0, len(cordinateList)-1)),pixel])

    for pixel in pixelList:
        for x in range(pixel[1].count(256)):
            pixel[1].remove(256)
            pixel[1].append(random.randint(0,255))

    for pixel in pixelList:
        for i in range(len(pixel[1])):
            item = pixel[1].pop(i)
            changeValue = turnInto256(item)
            pixel[1].insert(i, changeValue)

    while len(cordinateList) > 0:
        newPixel = list()
        for x in range(4):
            newPixel.append(random.randint(0,255))
        pixelList.append([cordinateList.pop(),newPixel])

    pixelMap = img.load()
    
    for pixel in pixelList:
        img.putpixel((pixel[0][0], pixel[0][1]),(pixel[1][0], pixel[1][1], pixel[1][2], pixel[1][3]))

    img.save(imageName)
    
    return([key,len(string),encryptionSize])
    
def decrypt(filename, key):
    pixelList = list_of_pixels_in(filename)
    print(key[0])
    random.seed(key[0])
    randomList = list()
    for elem in range(key[1]):
        randomList.append(chooseRandomChar())

    cordinateList = list()
    for x in range(key[2]):
        for y in range(key[2]):
            cordinateList.append([x,y])
            
    pixelOrderList = list()
    for pixel in range(math.ceil(key[1]/4)):
        pixelOrderList.append(cordinateList.pop(random.randint(0, len(cordinateList)-1)))
    
    myList = list()
    for elem in pixelOrderList:
        for i in pixelList:
            if i[0] == elem:
                for elem in i[1]:
                   myList.append(elem)
    decryptionOutput = ""
    pos = 0
    for rand in randomList:
        letterToDecrypt = Two56IntoCharInt(myList[pos])
        decryptionOutput = decryptionOutput + convertASSKEYToChar(decyrptCharacter(letterToDecrypt, rand))
        pos += 1
        
    return decryptionOutput[:key[1]]

def list_of_pixels_in(filename):
    image = Image.open(filename)
    listOfPixels = list()
    width, height = image.size
    
    for x in range(width):
        for y in range(height):
            r, g, b, a = image.getpixel((x,y))
            listOfPixels.append([[x,y],[r, g, b, a]])
    return listOfPixels
def main():
    while 1:
        print("Welcome to the one-time pad Encryption Program!")
        print("Would you like to Encrypt(E) or Decrypt(D) a message?")
        option = input("E or D?" )
        if option == "E":
            response = input("Enter Secret Message: ")
            s = input("Would you like a small key or a big key? \nEnter: s or b: ")
            imageName = input("Enter Image File Name, Exclude extention: ")
            imageName +=".png"
            key = createEncrytion(response, imageName, s)
            print("Secret Key: ", key[0])
            print("Length Key: ", key[1])
            print("Size Key:", key[2])
        if option == "D":
            imageName = input("Enter Image File Name, Exclude extention: ")
            key1 = input("Enter Secret Key: ")
            key1 = int(key1)
            key2 = input("Enter Length: ")
            key2 = int(key2)
            key3 = input("Enter Size: ")
            key3 = int(key3)
            imageName += ".png"
            print(decrypt(imageName,[key1, key2, key3]))
    
main()





from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
import functools 
from collections import Counter


def createExamples():
    numberArrayExamples = open('numArEx.txt','a')
    numberWeHave = range(0,10)
    versionWeHave = range(1,10)

    for eachNum in numberWeHave:
        for eachVer in versionWeHave:
            #print (str(eachNum)+'.'+str(eachVer))
            imgFilePath = 'C:/Users/Bolaji Ayeni/Documents/images/numbers/'+str(eachNum)+'.'+str(eachVer)+'.png'
            examp_img = Image.open(imgFilePath)
            examp_img_array = np.array(examp_img)
            examp_img_list = str(examp_img_array.tolist())

            lineToWrite = str(eachNum)+'::'+examp_img_list+'\n'
            numberArrayExamples.write(lineToWrite)
            

def threshold(imageArray):
    balanceAr = []
    newAr = imageArray

    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = functools.reduce(lambda x, y: x + y, eachPix[:3])/len(eachPix[:3])
            balanceAr.append(avgNum)
        balance = functools.reduce(lambda x, y: x + y, balanceAr)/len(balanceAr)

        for eachRow in newAr:
            for eachPix in eachRow:
                if functools.reduce(lambda x, y: x + y, eachPix[:3])/len(eachPix[:3]) > balance:
                    eachPix[0] = 255
                    eachPix[1] = 255
                    eachPix[2] = 255
                    eachPix[3] = 255

                else:
                    eachPix[0] = 0
                    eachPix[1] = 0
                    eachPix[2] = 0
                    eachPix[3] = 255
        return newAr


def imagerec(filePath):
    matchedAr = []
    loadExamps = open('numArEx.txt','r').read()
    loadExamps = loadExamps.split('\n')

    i = Image.open(filePath)
    iar = np.array(i)
    iar1 = iar.tolist()

    inQuestion = str(iar1)

    for eachExample in loadExamps:
        if len(eachExample) > 3:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]

            eachPixEx = currentAr.split('],')

            eachPixInQ = inQuestion.split('],')

            x = 0

            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))
                x += 1
    print (matchedAr)
    x = Counter(matchedAr)
    print (x)
                
imagerec('C:/Users/Bolaji Ayeni/Documents/images/test.png')   

"""    
i = Image.open('C:/Users/Bolaji Ayeni/Documents/images/numbers/0.1.png')
iar = np.array(i)

i2 = Image.open('C:/Users/Bolaji Ayeni/Documents/images/numbers/y0.4.png')
iar2 = np.array(i2)
 
i3 = Image.open('C:/Users/Bolaji Ayeni/Documents/images/numbers/y0.5.png')
iar3 = np.array(i3)

i4 = Image.open('C:/Users/Bolaji Ayeni/Documents/images/sentdex.png')
iar4 = np.array(i4)

"""
'''
threshold(iar4)
threshold(iar3)
threshold(iar2)

fig = plt.figure()
ax1 = plt.subplot2grid ((8,6), (0,0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid ((8,6), (4,0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid ((8,6), (0,3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid ((8,6), (4,3), rowspan=4, colspan=3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()

'''

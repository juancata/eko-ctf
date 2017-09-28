#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt

def inputData(stValue, isbody, jump = 0, startlt = 0, nwValue = []):

    for idx in stValue:
        try:
            if isbody:
                nwValue.append(int(hex(ord(idx)), 16))
            else:
                jump = int(idx)
                isbody = True

        except ValueError:
            startlt = int(hex(ord(idx)), 16)

    return startlt, jump, nwValue

def createMatrix(startlt, jump, lst, im, rowim, pos):

    for idx in lst:
        nwStart = startlt
        while(nwStart > idx):
            im[rowim, pos] = 1
            pos += 1
            nwStart += jump
        im[rowim, pos] = 0
        pos += 1

    return im

def createImage(im):
    #ONA{im}
    plt.figure(figsize=(5, 5))
    plt.imshow(im, cmap=plt.cm.gray)
    plt.axis('of')
    plt.show()

def iterateCodes(ltCodes, rowim = 1):

    im = np.zeros(((len(ltCodes)*2), len(ltCodes[0])*2))

    for mCode in ltCodes:
        startlt, jump, nwValue = inputData(mCode, False)
        im = createMatrix(startlt, jump, nwValue, im, rowim, 1)
        print(im)
        rowim += 2

    createImage(im)

ltCodes = ["J1LKKKK", "B3EEEHH", "M2QQQQO", "M2OQQQQ", "A9SSSSS", "L3RORO", "V1WXXXX", "A2CCCCE", "R1TSSSS", "O4SSSSS", "E2IIGGG", "I3OOOLL", "C2EGGGG", "O1PPPQQ", "N1OOOOO", "A5KKKKF", "P1QQQQQ", "S1T", "I2K", "S2WWUUU", "H3NKKK", "H1IIIIJ", "I2MMMMK", "N3TQQQQ", "N1OOOOO", "O2QQQSS", "V1XWXW", "A4IIIEE", "T2XXXXV", "I4MMMQQ", "O3R", "N2RRRRR", "L2NNNNN", "A1CBBB", "B5LGGGG", "B3EEEEE", "D6PJJ", "Q1RRRSS", "J2L", "W1XXXYY"]
iterateCodes(ltCodes)


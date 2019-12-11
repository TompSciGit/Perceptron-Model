from PIL import Image, ImageColor
import matplotlib
import numpy as np
import random as rnd
import colorsys

def output(vals, widthofpic, heightofpic, picName):

    #normalise
    valsrgb = []
    maxNum = max(map(max, vals))
    for y in range(0, len(vals)):
        valsrgb.append([])
        for x in range(0, len(vals[0])):
            
            valsrgb[y].append([360, 0, (vals[y][x] / maxNum) * 100])

    #do colour alterations here....

    #re-normalise & RGB convert
    for y in range(0, len(valsrgb)):
        for x in range(0, len(valsrgb[0])):
            valsrgb[y][x][0] = valsrgb[y][x][0] / 360
            valsrgb[y][x][1] = valsrgb[y][x][1] / 100
            valsrgb[y][x][2] = valsrgb[y][x][2] / 100
            valsrgb[y][x] = list(colorsys.hsv_to_rgb(valsrgb[y][x][0], valsrgb[y][x][1], valsrgb[y][x][2]))
            valsrgb[y][x][0] = round(valsrgb[y][x][0] * 255)
            valsrgb[y][x][1] = round(valsrgb[y][x][1] * 255)
            valsrgb[y][x][2] = round(valsrgb[y][x][2] * 255)
    
    #enlarges the image
    pixels = []
    for y in range(0, len(valsrgb)):
        for smally in range(0, round(heightofpic / len(valsrgb))):
            pixels.append([])
            for x in range(0, len(valsrgb[0])):
                for smallx in range(0, round(widthofpic / len(valsrgb[0]))):
                    pixels[(y * round(heightofpic / len(valsrgb))) + smally].append(valsrgb[y][x])

    #saves the image
    im = Image.fromarray(np.asarray(pixels, dtype=np.uint8), 'RGB')
    rgb_im = im.convert('RGB')
    rgb_im.save(picName)
    
    

# makes random sample data
vals2 = []
for y in range(0, 20):
    vals2.append([])
    for x in range(0, 10):
        vals2[y].append(rnd.random())

# calls the subroutine
output(vals2, 500, 1000, "smellyBumBum.jpg")
print("Done.")

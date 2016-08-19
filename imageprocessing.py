import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import time
import functools as ft
from collections import Counter

'''def  createex():
    exfile=open('numberex.txt','a')
    number=range(0,10)
    version=range(1,10)
    for eachnum in number:
        for eachver in version:
            impath='images/numbers/'+str(eachnum)+'.'+str(eachver)+'.png'
            im=Image.open(impath)
            imarray=np.array(im)
            imlist=str(imarray.tolist())
            exfile.write(str(eachnum)+'::'+imlist+'\n')
#createex()
i0=Image.open('images/numbers/y0.4.png')
iar0=np.array(i0)
iarray=np.array(i0)
ia=iarray
print (iarray)
def th(ia):
    newar=ia
    balancear=[]
    for eachrow in ia:
        for eachpix in eachrow:
            balancear.append(ft.reduce(lambda x,y:x+y, eachpix[0:3])/len(eachpix))
            count=0
            for e in eachpix[0:3]:
                
                
                if(e==0):
                    eachpix[count]=255
                    count=count+1
                else:
                    
                    eachpix[count]=0
                    count=count+1
                
            balanceno=ft.reduce(lambda x,y:x+y ,balancear)/len(balancear)
    for eachrow in newar:
        for eachpix in eachrow:
            if (ft.reduce(lambda x,y:x+y, eachpix[0:3])/len(eachpix) > balanceno):
                eachpix[0]=255
                eachpix[1]=255
                eachpix[2]=255
                eachpix[3]=255
            else:
                eachpix[0]=0
                eachpix[1]=0
                eachpix[2]=0
                eachpix[3]=255
            #eachpix.insert(0,0)
    return newar
im=th(ia)
print('\n \n')
print (im)
#plt.imshow(im)
#plt.show()

i1=Image.open('images/numbers/1.1.png')
iar1=np.asarray(i1)
i2=Image.open('images/numbers/2.1.png')
iar2=np.asarray(i2)
i3=Image.open('images/numbers/3.1.png')
iar3=np.asarray(i3)
ax1=plt.subplot2grid((8,6),(0,0),rowspan=4,colspan=3)
ax1.imshow(iar0)
ax2=plt.subplot2grid((8,6),(4,0),rowspan=4,colspan=3)
ax2.imshow(iar1)
ax3=plt.subplot2grid((8,6),(0,3),rowspan=4,colspan=3)
ax3.imshow(iar2)
ax4=plt.subplot2grid((8,6),(4,3),rowspan=4,colspan=3)
ax4.imshow(iar3)
plt.show()'''
def numberrecog(fpath):
    matched=[]
    loadexamps=open('numberex.txt','r').read()
    loadexamps=loadexamps.split('\n')
    i=Image.open(fpath)
    iar=np.array(i)
    iarl=iar.tolist()

    inquestion=str(iarl)
    for eachexample in loadexamps:
        if(len(eachexample)>3):
            splitex=eachexample.split('::')
            numberis=splitex[0]
            pixarris=splitex[1]
            eachpixex=pixarris.split('],')
            eachpixinq=inquestion.split('],')
            x=0
            while(x<len(eachpixex)):
                if(eachpixex[x]==eachpixinq[x]):
                    matched.append(int(numberis))
                x += 1
    #print(matched)
    c=Counter(matched)
    print(c)
    print(max(c.values()))
    xaxis=[]
    yaxis=[]
    for eachno in c:
        xaxis.append(eachno)
        yaxis.append(c[eachno])
    ax1=plt.subplot2grid((4,4),(0,0), rowspan=1, colspan=4)
    ax2=plt.subplot2grid((4,4),(1,0), rowspan=3, colspan=4)
    ax1.imshow(iar)
    ax2.bar(xaxis,yaxis, align="center")
    plt.ylim(350)
    plt.show()
numberrecog('test.png')
    
                

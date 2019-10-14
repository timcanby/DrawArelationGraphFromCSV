import matplotlib.pyplot as plt
import csv
import requests
import numpy as np
from bs4 import BeautifulSoup
''''''
from matplotlib import pyplot
import numpy
from mpl_toolkits.mplot3d import Axes3D
from wikidata.client import Client
from matplotlib.font_manager import FontProperties
fp = FontProperties(fname=r'ipag.ttf', size=7)
'''
def getNamelist(dataPath):
    f = open(dataPath, 'r')
    csvreader = csv.reader(f)
    final_list = list(csvreader)
    return final_list

namelist=getNamelist("distinct_artist_pair_simple.csv")
Name=[]
for item in namelist:
    Name.append(item[2])

'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



def generateNode(Number):
    data = np.random.randint(0, Number*10, (3, Number))

    return data


def marching(Id,list):
    pairID=[]
    return pairID

def findAliases(id):

    result=[]
    if id=='':
        return ''
    else:
        client = Client()
        result=[]
        entity = client.get(id, load=True)

def getNamelist(dataPath):
    f = open(dataPath, 'r')
    csvreader = csv.reader(f)
    final_list = list(csvreader)
    return final_list
import re

fig = plt.figure()
ax = Axes3D(fig)

data=getNamelist('data.csv')

zdirs=[]
result=[]

for item in data[1:]:

    zdirs.append(item[0])



nodes = generateNode(len(zdirs))


x = nodes[0]
y = nodes[1]
z = nodes[2]


ax.scatter(x, y, z)
CounterST=0
for item in data[1:]:
    CounterST+=1
    counterED=0
    for student in data[1:]:
        counterED+=1
        if item[1].replace(' ','') in student[2].replace(' ',''):
            if item[1]!='':
                ax.plot((x[CounterST],x[counterED]),(y[CounterST],y[counterED]), (z[CounterST],z[counterED]), 'r:')

CounterST = 0
for item in data[1:]:
    CounterST += 1
    counterED = 0
    for student in data[1:]:
        counterED += 1
        if item[1].replace(' ', '') in student[3].replace(' ', ''):
            if item[1] != '':
                ax.plot((x[CounterST], x[counterED]), (y[CounterST], y[counterED]),
                        (z[CounterST], z[counterED]), 'b:')
#================================

#---============================================

zdirs=tuple(zdirs)




for zdir, x, y, z in zip(zdirs, x, y, z):

    label = zdir
    ax.text(x, y, z, label,fontproperties=fp)

plt.show()
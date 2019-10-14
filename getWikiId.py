import wikipedia
# -*- coding: UTF-8 -*-
import sys
#sysとmecab-python3を呼び出します。
import csv
import requests
from bs4 import BeautifulSoup
import re
def FindidentifiedCode(targetTxT):
    target_url = 'http://www.wikidata.org/wiki/Special:ItemByTitle/jawiki/'+str(targetTxT)+''
    r = requests.get(target_url)
    soup = BeautifulSoup(r.text)

    for a in soup.find_all('a'):

          if '/wiki/Special:SetLabelDescriptionAliases/'in str(a):
              for x in str(a).split('/'):
                  if "Q"in x and x.split('Q')[1].isdigit():
                      return x

def getNamelist(dataPath):
    f = open(dataPath, 'r')
    csvreader = csv.reader(f)
    final_list = list(csvreader)
    return final_list




namelist=getNamelist("distinct_artist_pair_simple.csv")
Name=[]
for item in namelist:
    Name.append(item[2])
Qcode=[]
c=set(Name)
for item in Name[1:]:
    CODE=FindidentifiedCode(str(item).replace(' ',''))
    print(item)
    print(CODE)
    Qcode.append(str(CODE))

#with open("Artistnamelist.txt", "w") as f:
    #f.write(str(c))
print (set(Qcode))
#!/usr/bin/python                                                            
from pprint import pprint
import sys                                                
import os                                              
import urllib.request
import html2text
import time
import re
from sh import tail

urllib.request.urlretrieve (sys.argv[1], "foo.txt")                                  
                                                                             
file=open("foo.txt","r+")                                                     
html = open("foo.txt").read()                                                 
text = html2text.html2text(html)

# Set defaults
minLength = 0
numWords = 10

minLength = int(os.environ['MinLength'])

wordcount={}                                                                  
for word in text.split():

    word = re.sub('[^A-Za-z0-9]+', '', word)

    if len(word) == 0 or len(word) < minLength:
      continue

    if word not in wordcount:   
        wordcount[word] = 1             
    else:                                            
        wordcount[word] += 1
sortedList = sorted(wordcount.items(), key=lambda item: item[1], reverse=True)
                                                                              
numWords = int(os.environ['NumWords'])                                        
top10 = sortedList[:numWords]                                                
pprint(top10)                                                                
file.close();

tail("-f", "/dev/null")

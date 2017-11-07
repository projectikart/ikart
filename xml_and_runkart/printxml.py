import sys
import os
from lxml import etree
import urllib.request as ur
import xml.etree.ElementTree as et

with open('file.xml', 'r') as f:
    xml=f.read();
price=[]
name=[]
ids=[]

tree = et.fromstring(xml)
counts = tree.findall('.//productprice')
for count in counts:
    price.append(count.text)
    print(count.text)

tree = et.fromstring(xml)
counts = tree.findall('.//productname')
for count in counts:
    name.append(count.text)
    print(type(count.text))

    
print(range(0 ,len(price)))
for i in range(0 ,len(price)):
    print(price[i]," : ",name[i])

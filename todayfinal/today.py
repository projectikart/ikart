'''setting up encoding'''
import sys
import lcd
reload(sys)
sys.setdefaultencoding("utf-8")


'''import statements'''
import requests
import os
import time
import socket
from qrtools import QR
from lxml import etree
import xml.etree.ElementTree as et

class runkart:

    def update_xml(self,m):
        m='ak:56:fghh'
    
        m=m.split(":")
        brand=m[0]
        price=m[1]
        proid=m[2]
        self.totprice=self.totprice + int(price)
        
        lcd.add(brand)
        lcd.add('Item added')
        
        self.product = etree.Element(proid)


        productid=etree.Element('productid')
        productid.text=proid

        productp=etree.Element('productprice')
        productp.text=price

        productn=etree.Element('productname')
        productn.text=brand


        self.product.append(productid)
        self.product.append(productn)
        self.product.append(productp)
        self.root.append(self.product)
        lcd.price('Amount',str(self.totprice))

        pass

    def send_product(self):



        with open('file.xml', 'w') as f:
            f.write(etree.tostring(self.root).decode("ascii"))
            f.close()

        with open('file.xml', 'r') as f:
            xml=f.read();
            f.close()
        price=[]
        name=[]
        ids=[]

        tree = et.fromstring(xml)
        counts = tree.findall('.//productprice')
        for count in counts:
            price.append(count.text)

        tree = et.fromstring(xml)
        counts = tree.findall('.//productname')
        for count in counts:
            name.append(count.text)

        tree = et.fromstring(xml)
        counts = tree.findall('.//productid')
        for count in counts:
            ids.append(count.text)

        #r = requests.get('http://127.0.0.1:1234/hinterface/additem', params={'key1':'Britania','key2':'55465','key3':'BIS_BRI100','key4':'ikart_s101'})


        for i in range(0 ,len(price)):
            r = requests.get('http://172.20.5.12:1234/hinterface/additem', params={'key1':name[i],'key2':price[i],'key3':ids[i],'key4':'ikart_s101'})
            print(ids[i]," : ",name[i]," : ",price[i])




        r="received"
        print str(r)
        if str(r)=="received":
            return 1
        pass


        self.turn_green()
        ''' initiate xml'''
        pass


    def displaydetails(self):
        '''code for displaying details on lED'''
        pass


    def turn_green(self):
        '''code for turning green light on'''
        pass


    def turn_red(self):
        '''code for turning red light on'''
        pass


    def __init__(self):
        self.root = etree.Element('products')
        self.totprice=0

        pass
    def __del__(self):

        pass



    def takein(self):

        self.update_xml('')
        return




        self.turn_red()

        '''try:
            find=os.remove("/home/pi/Desktop/project/ikart/qw.jpeg")
        except OSError:
            pass'''

        ''' capture image'''
        try :
            '''fswebcam -d /dev/video0  -S 2 -s brightness=60% -s Contrast=15%  -s Gamma=50%  -p YUYV -r 1280x720 --jpeg 80 -s Sharpness=40% -s Saturation=15%   --title "New Zealand - Wellington - Tawa"  $DIR/$filename'''
            os.system('fswebcam -r 100x100  --jpeg 1000 qw.jpeg')

        except IOError:
            time.sleep(1)
            os.system('fswebcam -r 300x300 --jpeg 500 kqrcode.jpeg')

        '''sleep to recover image'''
        time.sleep(4)

        '''extract qrcode'''
        try :
            myCode = QR(filename="/home/pi/Desktop/project/ikart/kqrcode.jpeg")
            if myCode.decode():
                print myCode.data
                print myCode.data_type
                print myCode.data_to_string()

                m=myCode.data_to_string()
                print (m)

                '''update xml '''
                self.update_xml(m)



                '''display details on lED'''
                self.displaydetails()
        except IOError as e:
            print(e,'sfhgdfhsdhdsh',myCode,str(myCode))
            return 0
        pass


    def takeout(self):
        ''' send product with negation'''
        '''update xml'''
lcd.ready()
kart= runkart()
ask=raw_input('any more()y/n')
while True:
    ron=kart.takein()
    ask=raw_input('any more()y/n')
    if(ask=='n'):
        kart.send_product()

        break

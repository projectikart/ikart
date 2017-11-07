'''setting up encoding'''
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


'''import statements'''
import os
import time
import socket
from qrtools import QR

class runkart:
    
    def update_xml(self):
        pass
    
    def send_product(self,m):
        '''connect to server '''
        self.client=socket.socket()
        ip='172.20.5.12'
        print (ip)
        self.client.connect((ip,1234))
        self.client=socket.socket()
        ip='172.20.5.12'
        print (ip)
        self.client.connect((ip,1234))
        
        '''send product to server'''
        m=m.encode('utf-8')
        self.client.send(m)
        r=self.client.recv(1024)
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
        pass
    def __del__(self):
        self.client.close()
        pass
    
    
    
    def takein(self):
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
            os.system('fswebcam -r 300x300 --jpeg 500 qw.jpeg')
        
        '''sleep to recover image'''
        time.sleep(4)
        
        
        '''extract qrcode'''
        try :
            myCode = QR(filename="/home/pi/Desktop/project/ikart/qw.jpeg")
            if myCode.decode():
                print myCode.data
                print myCode.data_type
                print myCode.data_to_string()
                
                m=myCode.data_to_string()
                print (m)
                '''send product'''
                ''' ron:recieved or not'''
                ron=self.send_product(m)
                '''update xml '''
                self.update_xml()
                
                
                '''display details on lED'''
                self.displaydetails()
                return ron
        except IOError as e:
            print(e,'sfhgdfhsdhdsh',myCode,str(myCode))
            return 0
        pass
    
    
    def takeout(self):
        ''' send product with negation'''
        '''update xml'''
        
kart= runkart()
while True:
    ron=kart.takein()
    ask=raw_input('any more()y/n')
    if(ask=='n'):
        kart.client.close()
        break
    
        
        

    
        
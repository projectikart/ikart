'''import statements'''
import os
import time
from qrtools import QR

class runkart:
    
    def update_xml(self):
        pass
    
    def send_product(self):
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
        
        '''connect to server '''
        client=socket.socket()
        ip='172.20.5.12'print (ip)
        client.connect((ip,1234))
        while True:
            m=str(raw_input("<data>"))
            client.send(m.encode('ascii'))
            r=client.recv(1024)
            print str(r)
            if str(m)=="lince":
                client.close()
                break;
        
        self.turn_green()
        ''' initiate xml'''
        pass
    
    
    def takein(self):
        self.turn_red()
        ''' capture image'''
        os.system('fswebcam -r 1024x786  --jpeg 500 qw.jpeg')
        
        '''sleep to recover image'''
        time.sleep(5)
        
        '''extract qrcode'''
        myCode = QR(filename="/home/pi/Desktop/project/ikart/qw.jpeg")
        if myCode.decode():
            print myCode.data
            print myCode.data_type
            print myCode.data_to_string()
            
             '''send product'''
             self.send_product()
             
             
             '''update xml '''
             self.update_xml()
             
             
             '''display details on lED'''
             self.displaydetails()

       
        pass
    
    
    def takeout(self):
        ''' send product with negation'''
        '''update xml'''
        
kart= runkart()
kart.takein()
    
        
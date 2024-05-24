import json
from time import sleep
from pyscript import document, fetch,window

## remove load banner
__terminal__.resize(100,100)
player=document.getElementById('xxx')
xx=document.getElementById('load')
xx.remove()
bred='\033[1;31m'
bblue='\033[1;34m'
bgreen='\033[1;32m'
yellow='\033[0;33m'
red='\033[0;31m'
blue='\033[0;34m'
green='\033[0;32m'
reset='\033[0m'

commands=["music","clear","toolkit","help","learn","about","extensions","coffee","joke","exit","blog","social"]
extensions=["AutoRepeater", "Js Link Finder", "GAP", "Piper", "Reflection", "Hackverter"]
learn_list={"TomNomNom":"TomNomNomDotCom","NahamSec":"nahamsec","Jason Haddix":"jhaddix","IppSec":"ippsec","John Hammond":"_JohnHammond","LiveOverflow ":"LiveOverflow","g0lden":"g0lden1"}
headers={'Accept':'application/json'}
BASE_URL = "https://crt.sh/?q={}&output=json"
subdomains = set()
wildcardsubdomains = set()

def banner():
    print(f"Hello World !! Welcome to the matrix. Enter {bgreen}help{reset} to check available commands")
#     print(f"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠛⠛⠛⠛⠛⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⣄⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⠀Hello World !! Welcome to the matrix⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀I am Rohit a.k.a {red}rohsec{reset}. I am a full time
# ⠀⠀⠀⠀⠀⠀⢀⡿⠀⠀⢀⣀⣤⡴⠶⠶⢦⣤⣀⡀⠀⠀⢻⡆⠀⠀⠀BugBounty Hunter and HackerOne Ambassador.⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠘⣧⡀⠛⢻⡏⠀⠀⠀⠀⠀⠀⠉⣿⠛⠂⣼⠇⠀⠀⠀I like identifying vulnerabilities and helping⠀⠀⠀
# ⠀⠀⠀⠀⢀⣤⡴⠾⢷⡄⢸⡇⠀⠀⠀⠀⠀⠀⢀⡟⢀⡾⠷⢦⣤⡀⠀organizations reinforce their defenses.⠀⠀⠀
# ⠀⠀⠀⢀⡾⢁⣀⣀⣀⣻⣆⣻⣦⣤⣀⣀⣠⣴⣟⣡⣟⣁⣀⣀⣀⢻⡄⠀⠀⠀
# ⠀⠀⢀⡾⠁⣿⠉⠉⠀⠀⠉⠁⠉⠉⠉⠉⠉⠀⠀⠈⠁⠈⠉⠉⣿⠈⢿⡄⠀Enter {bgreen}help{reset} to check available commands
# ⠀⠀⣾⠃⠀⣿⠀⠀⠀⠀⠀⠀⣠⠶⠛⠛⠷⣤⠀⠀⠀⠀⠀⠀⣿⠀⠈⢷⡀⠀
# ⠀⣼⠃⠀⠀⣿⠀⠀⠀⠀⠀⢸⠏⢤⡀⢀⣤⠘⣧⠀⠀⠀⠀⠀⣿⠀⠀⠈⣷⠀
# ⢸⡇⠀⠀⠀⣿⠀⠀⠀⠀⠀⠘⢧⣄⠁⠈⣁⣴⠏⠀⠀⠀⠀⠀⣿⠀⠀⠀⠘⣧
# ⠈⠳⣦⣀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠻⠶⠶⠟⠀⠀⠀⠀⠀⠀⠀⣿⠀⢀⣤⠞⠃
# ⠀⠀⠀⠙⠷⣿⣀⣀⣀⣀⣀⣠⣤⣤⣤⣤⣀⣤⣠⣤⡀⠀⣤⣄⣿⡶⠋⠁⠀⠀
# ⠀⠀⠀⠀⠀⢿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⠀⠀⠀⠀⠀""")
    # 
def help():
    print(f"{yellow}[{bgreen} *{yellow} ]{reset} Available Commands :")
    print(f"""\t{bblue}|--{bgreen} help{reset} -- displays available commands    
    \t{bblue}|--{bgreen} toolkit{reset} -- BugBounty Tool Kit
    \t{bblue}|--{bgreen} joke{reset} -- Get a dad joke from icanhazdadjoke
    \t{bblue}|--{bgreen} music{reset} -- Play an AI generated Hacking Song
    \t{bblue}|--{bgreen} extensions{reset} -- Prints My Burp Suit Exetnsions
    \t{bblue}|--{bgreen} learn{reset} -- Resources to get started in BugBounties ;)
    \t{bblue}|--{bgreen} blog{reset} -- My blog post
    \t{bblue}|--{bgreen} about{reset} -- About Me 
    \t{bblue}|--{bgreen} coffee{reset}  -- Buy me a Coffee
    \t{bblue}|--{bgreen} social{reset}  -- My Social Handles
    \t{bblue}|--{bgreen} clear{reset} -- Clear the console screen
    \t{bblue}|--{bgreen} exit{reset} -- Exit the app
""")

def music():
    print(" ===========================")
    print(f" |{bgreen}    Music Center {bblue}v1.0{reset}    |")
    print(" ===========================")
    print(""" ░░█▀▀▀▀▀▀▀▀▀▀▀▀▀▀█   ♫ ♪ ♫ ♪
 ██▀▀▀██▀▀▀▀▀▀██▀▀▀██
 █▒▒▒▒▒█▒▀▀▀▀▒█▒▒▒▒▒█
 █▒▒▒▒▒█▒████▒█▒▒▒▒▒█
 ██▄▄▄██▄▄▄▄▄▄██▄▄▄██""")
    ch=input(f"\n {bred}0.{bblue}Play\n {bred}1.{bblue}Pause{reset}\n Enter choice: ")
    if(ch=="0"):
        print(f" {yellow}[{bgreen} * {yellow}]{reset} Playing some music for you...")
        print(f""" {green}» {yellow}[Lost Connections]{green} «
 {reset}0:00{blue} ─〇─────{reset} 1:40
 {blue}⇄   ◃◃   ⅠⅠ   ▹▹   ↻{reset}""")
        player.play()
    elif(ch=="1"):
        print(f" {yellow}[{bgreen} * {yellow}]{reset} Stoping the music...")
        print(f""" {green}» {yellow}[Lost Connections]{green} «
 {reset}0:00{blue} ─〇─────{reset} 1:40
 {blue}⇄   ◃◃   ⅠⅠ   ▹▹   ↻{reset}""")
        player.pause()
    else:
        print("Wrong Choice!!")

def tools():
    # async def crtsh():
    # BASE_URL = "https://crt.sh/?q={}&output=json"
    # subdomains = set()
    # wildcardsubdomains = set()
    # domain=input(f"{blue}Enter a domain:{reset} ")
    # if(domain!=""):
    #     try:
    #         print(f" {yellow}[ {bgreen}+{yellow} ]{reset} Fetching Domains...")
    #         subdomains.clear()
    #         wildcardsubdomains.clear()
    #         response = fetch(BASE_URL.format(domain), timeout=25)
    #         if response.ok:
    #             content = await response.content.decode('UTF-8')
    #             jsondata = json.loads(content)
    #             for i in range(len(jsondata)):
    #                 name_value = jsondata[i]['name_value']
    #                 if name_value.find('\n'):
    #                     subname_value = name_value.split('\n')
    #                     for subname_value in subname_value:
    #                         if subname_value.find('*'):
    #                             if subname_value not in subdomains:
    #                                 subdomains.add(subname_value)
    #                         else:
    #                             if subname_value not in wildcardsubdomains:
    #                                 wildcardsubdomains.add(subname_value)
    #             print("Fetched Subdomains\n============", '\n'.join(sorted(subdomains)))
    #             print("WildCard Subdomains\n============", '\n'.join(sorted(wildcardsubdomains)))
    #     except:
    #         print("Opps!! Techincial error occured. Please run the command again")
    # else:
    #     print(f"{yellow}[ {bred}!{yellow} ]{reset} Invalid input !!")
    def dorker():
        domain_pattern = r"^(?![0-9]+$)(?!-)(?:[a-zA-Z0-9-]{0,62}[a-zA-Z0-9]\.)+(?:[a-zA-Z]{2,})$"
        print(f"{bblue}=+=+=+ {bgreen}Google Dorks Generator{bblue} =+=+=+{reset}")
        domain=input("Enter your domain: ")
        with open('dorks.txt', "r") as f1:
            x1=f1.readlines()
        f1.close()
        if(domain!=""):
            for i in x1:
                if(i.startswith("#")):
                    print(f" {yellow}[ {bgreen}* {yellow}] {bblue}{i[4:]}{reset}")
                elif(i.startswith('>')):
                    print(f"\t{bblue}|-- {green}https://google.com/search?q={i.replace('example.com',domain)[2:]}")
        else:
            print(f"{yellow}[{bred} !{yellow} ]{reset} Invalid input !!")

    def replacer():
        print(f"{bblue}=+=+=+ {bgreen}Word Replacer{bblue} =+=+=+{reset}")
        print(f"{yellow}[{bgreen} *{yellow} ]{reset} Paste URL list below :")
        urls=input("")
        orig=input(f"{yellow}[{bgreen} *{yellow} ]{reset} Enter word to be replaced : ")
        rep=input(f"{yellow}[{bgreen} *{yellow} ]{reset} Enter Replacment word : ")
        if(urls!="" and orig!="" and rep!=""):
            print(f"{yellow}[{bgreen} *{yellow} ]{reset} Output : ")
            out=urls.replace(orig,rep)
            print(out)
        else:
            print(f"{yellow}[{bred} !{yellow} ]{reset}Please validate your inputs !! ")

    def bulk_url():
        print(f"{bblue}=+=+=+ {bgreen}Word Replacer{bblue} =+=+=+{reset}")
        print(f"{bgreen}Note: {bblue}Make sure your browser is not blocking pop up windows.{reset}")
        print(f"{yellow}[{bgreen} *{yellow} ]{reset} Paste URL list below :")
        urls=input("")
        if(urls!=""):
            for i in urls.splitlines():
                window.open(i,"_blank")
        else:
            print(f"{yellow}[{bred} !{yellow} ]{reset}Please validate your inputs !! ")
    print(" ===========================")
    print(f" |{bgreen} BugBounty Tool Kit {bblue}v1.0{reset} |")
    print(" ===========================")
    tool_choice=input(f" {bred}0. {bblue}Google Dorker\n {bred}1. {bblue}Word Replacer\n {bred}2. {bblue}Bulk URL Open\n {bred}3. {bblue}Exit Tool Kit{reset}\n Enter Choice: ")
    if(tool_choice=="0"):
        dorker()
    elif(tool_choice=="1"):
        replacer()
    elif(tool_choice=="2"):
        bulk_url()
    elif(tool_choice=="3"):
        print(f"{yellow}[{bgreen} *{yellow} ]{reset} Terminating Tool Kit...")
    else:
        print(f" {yellow}[{bred} !{yellow} ]{reset} Invalid Input !!")
        print(f" {yellow}[{bgreen} *{yellow} ]{reset} Terminating Tool Kit...")
    


def social():
    print(f"{yellow}[{bgreen} *{yellow} ]{reset} My Social Handles :")
    print(f"\t{bblue}|-- https://twitter.com/rohsec{reset}")
    print(f"\t{bblue}|-- https://linkedin.com/in/rohity264{reset}")
    print(f"\t{bblue}|-- https://github.com/rohsec{reset}")


def extension():
    print(f"{yellow}[{bgreen} *{yellow} ]{reset} My current Burp Extensions are :")
    for i in extensions:
        print(f"\t{bblue}|-- {green}{i}{reset}")
def learn():
    print(f"{yellow}[{bgreen} *{yellow} ]{reset} Resources to get started :\n\t{bblue}|-- {yellow}PortSwigger Academy : {bblue}https://portswigger.net/web-security\n\t{bblue}|-- {yellow}Hacker101 : {bblue}https://hacker101.com{reset}")

    print(f"{yellow}[{bgreen} *{yellow} ]{reset} Content Creators to check out :")
    for key in learn_list:
        print(f"\t{bblue}|-- {yellow}{key} : {bblue}https://youtube.com/@{learn_list[key]}" )

def about():
    print(f"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠛⠛⠛⠛⠛⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⣄⠀⠀⠀⠀ ╔═════════════════════════════════════════════════╗⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀ ║      Hello World !! Welcome to the matrix       ║
⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀║  I am Rohit a.k.a {red}rohsec{reset}. I am a full time      ║
⠀⠀⠀⠀⠀⠀⢀⡿⠀⠀⢀⣀⣤⡴⠶⠶⢦⣤⣀⡀⠀⠀⢻⡆⠀⠀⠀║    BugBounty Hunter and HackerOne Ambassador.   ║
⠀⠀⠀⠀⠀⠀⠘⣧⡀⠛⢻⡏⠀⠀⠀⠀⠀⠀⠉⣿⠛⠂⣼⠇⠀⠀⠀║  I like identifying vulnerabilities and helping ║
⠀⠀⠀⠀⢀⣤⡴⠾⢷⡄⢸⡇⠀⠀⠀⠀⠀⠀⢀⡟⢀⡾⠷⢦⣤⡀⠀║    organizations reinforce their defenses.      ║
⠀⠀⠀⢀⡾⢁⣀⣀⣀⣻⣆⣻⣦⣤⣀⣀⣠⣴⣟⣡⣟⣁⣀⣀⣀⢻⡄╚═════════════════════════════════════════════════╝⠀⠀
⠀⠀⢀⡾⠁⣿⠉⠉⠀⠀⠉⠁⠉⠉⠉⠉⠉⠀⠀⠈⠁⠈⠉⠉⣿⠈⢿⡄⠀
⠀⠀⣾⠃⠀⣿⠀⠀⠀⠀⠀⠀⣠⠶⠛⠛⠷⣤⠀⠀⠀⠀⠀⠀⣿⠀⠈⢷⡀⠀
⠀⣼⠃⠀⠀⣿⠀⠀⠀⠀⠀⢸⠏⢤⡀⢀⣤⠘⣧⠀⠀⠀⠀⠀⣿⠀⠀⠈⣷⠀
⢸⡇⠀⠀⠀⣿⠀⠀⠀⠀⠀⠘⢧⣄⠁⠈⣁⣴⠏⠀⠀⠀⠀⠀⣿⠀⠀⠀⠘⣧
⠈⠳⣦⣀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠻⠶⠶⠟⠀⠀⠀⠀⠀⠀⠀⣿⠀⢀⣤⠞⠃
⠀⠀⠀⠙⠷⣿⣀⣀⣀⣀⣀⣠⣤⣤⣤⣤⣀⣤⣠⣤⡀⠀⣤⣄⣿⡶⠋⠁⠀⠀
⠀⠀⠀⠀⠀⢿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⠀⠀⠀⠀⠀""")
    # print(f" Hi 👋! I am Rohit a.k.a {red}rohsec{reset}. I am a full time BugBounty Hunter and HackerOne Ambassador. I like identifying vulnerabilities and helping organizations reinforce their defenses.")
    # print(f" You can connect with me at {bblue}https://twitter.com/rohsec{reset}")

def coffee():
    print(f"{yellow}[{bgreen} *{yellow} ]{reset} Yayy!! Coffee Time :")
    print(" If you appreciate the work I do, consider supporting my work! Your small contribution can help me continue my work for the community.")
    print(f"{yellow} Buy Me a Coffee{reset} 🙌{yellow} : {bblue}https://buymeacoffee.com/rohsec{reset}")

async def jokes():
    print(f"{yellow}[ {bblue}+{yellow} ]{reset} Fetching a joke for you...")
    resp= await fetch("https://icanhazdadjoke.com/",headers=headers)
    if(resp.ok):
        respjson=json.loads(await resp.text())
        print(f"{respjson['joke']}")
    else:
        print("Opps !! Techincal error occured, maybe try after some time !")

def clear():
    __terminal__.clear()

def exitapp():
    print(f"{yellow}[{bgreen} *{yellow} ]{reset} See you later :")
    print(" Thank you for stopping by !! You will be now redirected to my twitter, connect to get in touch :)")
    sleep(2)
    document.location="https://x.com/rohsec"

def blog():
    print(f"{yellow}[{bgreen} *{yellow} ]{reset} You can find my blog at :")
    print(f"{yellow}\t{bblue}|-- {yellow}https://blog.rohsec.com{reset}")

def choice():
#     inp=input("""┌──(root㉿kali)-[~]
# └─# """)
    inp=input(f"""{blue}┌──({bred}root㉿rohsec{blue}){green}-{blue}[{bgreen}~{blue}]{blue}
└─{bred}#{reset} """)
    if(inp in commands):
        if(inp =="help"):
            help()
        elif(inp == "extensions"):
            extension()
        elif(inp == "learn"):
            learn()
        elif(inp== "about"):
            about()
        elif(inp=="coffee"):
            coffee()
        elif(inp=="joke"):
            await jokes() 
        elif(inp=="exit"):
            exitapp()
        elif(inp=="blog"):
            blog()
        elif(inp=="clear"):
            clear()
        elif(inp=="social"):
            social()
        elif(inp=="toolkit"):
            tools()
        elif(inp=="music"):
            music()
    else:
        print("Command not found !! Run the help command to get a list of available commands")

async def main():
    banner()
    while True:
        await choice()

await main()

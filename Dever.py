try:
    import dhooks
    import threading
    from colorama import Fore,init
    import fade
except ImportError:
    import os
    os.system("pip install dhooks")
    os.system("pip install fade")
    os.system("pip install threading")
    os.system("pip install colorama")




banner = """
+----------------------------------------------------+
|                                                    |
|                                                    |
|       ▓█████▄  ▓█████ ██▒   █▓ ▓█████ ██▀███       |
|       ▒██▀ ██▌ ▓█   ▀▓██░   █▒ ▓█   ▀▓██ ▒ ██▒     |
|       ░██   █▌ ▒███   ▓██  █▒░ ▒███  ▓██ ░▄█ ▒     |
|      ▒░▓█▄   ▌ ▒▓█  ▄  ▒██ █░░ ▒▓█  ▄▒██▀▀█▄       |
|      ░░▒████▓ ▒░▒████   ▒▀█░  ▒░▒████░██▓ ▒██▒     |
|      ░ ▒▒▓  ▒ ░░░ ▒░    ░ ▐░  ░░░ ▒░ ░ ▒▓ ░▒▓░     |
|        ░ ▒  ▒ ░ ░ ░     ░ ░░  ░ ░ ░    ░▒ ░ ▒      |
|        ░ ░  ░     ░        ░      ░    ░░   ░      |
|          ░    ░   ░        ░  ░   ░     ░          |
|                                                    |
+------------------+-----------------+---------------+
|        1         |        2        |       3       |
| Webhook Deleter  | Webhook Spammer | Webhook Nuker |
+------------------+-----------------+---------------+
|        4         |        5        |       6       |
| Webhook Modifier |  Webhook Info   |      Quit     |
+------------------+-----------------+---------------+
"""
banner = fade.water(banner)

fade.system("title Dever | Discord Webhook Utility Tool")

def cls():
    fade.system("cls")

def attach_webhook(webhook):
    whook = dhooks.Webhook(webhook)
    return whook
def delete_webhook(whook):
    whook.delete()
def send_msg(whook, message):
    whook.send(message)
    print(f"{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}]{Fore.LIGHTCYAN_EX} Sent Post Request With Msg: {message}{Fore.WHITE} ")
def spam_webhook(whook, message):
    while True:
        try:
            send_msg(whook, message)
            print(f"{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}]{Fore.LIGHTCYAN_EX} Sent Post Request With Msg: {message}{Fore.WHITE} ")
        except Exception:
            break
def nuke_webhook(whook, msg, name):
    threads = []
    
    whook.modify(name)
    print(f"\n{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}]{Fore.LIGHTCYAN_EX} Changed Webhook Name To: {name}{Fore.WHITE}\n")
    
    
    for i in range(25):
        t = threading.Thread(target=send_msg, args=(whook, msg,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
    whook.delete()
    print(f"\n{Fore.GREEN}[{Fore.WHITE}?{Fore.GREEN}]{Fore.LIGHTCYAN_EX} Deleted The Webhook{Fore.WHITE} ")
def modify_webhook(whook, name):
    whook = dhooks.Webhook()
    whook.modify(name)
    print(f"{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}]{Fore.LIGHTCYAN_EX} Successfully Changed Name To: {name}")
def webhook_info(whook):
    info = whook.get_info()
    info = [
f"Avatar Url: {info.avatar_url}",
f"Channel ID: {info.channel_id}",
f"Default Avatar: {info.default_avatar}",
f"Default Name: {info.default_name}",
f"Guild ID: {info.guild_id}",
f"Token: {info.token}",
f"ID: {info.id}",
f"Username: {info.username}"
    ]
    return info


def main():
    cls()
    print(f"{banner}\n{Fore.YELLOW}[{Fore.WHITE}?{Fore.YELLOW}]{Fore.LIGHTCYAN_EX} Webhook:{Fore.WHITE} ", end="")
    webhook = input("")
    
    print(f"\n\n{Fore.YELLOW}[{Fore.WHITE}!{Fore.YELLOW}]{Fore.LIGHTCYAN_EX} Attempting To Attach...")
    whook = attach_webhook(webhook)
    print(f"{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}]{Fore.LIGHTCYAN_EX} Successfully Attached!")
    input("\n(Press Enter To Continue)")
    
    while True:
        cls()
        print(banner)
        print(f"\n{Fore.YELLOW}[{Fore.WHITE}?{Fore.YELLOW}]{Fore.LIGHTCYAN_EX} Choose:{Fore.WHITE} ", end="")
        choose = input("")

        if choose == "1":
            delete_webhook(whook)
            print(f"{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}]{Fore.LIGHTCYAN_EX} Successfully Deleted Webhook!")
            input("\n(Press Enter To Continue)")
        if choose == "2":
            threads = []
            print(f"\n{Fore.YELLOW}[{Fore.WHITE}?{Fore.YELLOW}]{Fore.LIGHTCYAN_EX} Threads:{Fore.WHITE} ", end="")
            threadss = int(input(""))
            
            print(f"{Fore.YELLOW}[{Fore.WHITE}?{Fore.YELLOW}]{Fore.LIGHTCYAN_EX} Message:{Fore.WHITE} ", end="")
            msg = input("")
            
            for i in range(threadss):
                t = threading.Thread(target=spam_webhook, args=(whook, msg,))
                threads.append(t)
                t.start()
                
            for t in threads:
                t.join()
        if choose == "3":
            print(f"{Fore.YELLOW}[{Fore.WHITE}?{Fore.YELLOW}]{Fore.LIGHTCYAN_EX} Message:{Fore.WHITE} ", end="")
            msg = input("")
            print(f"{Fore.YELLOW}[{Fore.WHITE}?{Fore.YELLOW}]{Fore.LIGHTCYAN_EX} Name:{Fore.WHITE} ", end="")
            name = input("")
            print(Fore.LIGHTCYAN_EX)
            
            nuke_webhook(whook, msg, name)
            input("\n(Press Enter To Continue)")
        if choose == "4":
            print(f"\n{Fore.YELLOW}[{Fore.WHITE}?{Fore.YELLOW}]{Fore.LIGHTCYAN_EX} Name:{Fore.WHITE} ", end="")
            name = input("")
            print(Fore.LIGHTCYAN_EX)
            modify_webhook(whook, name)
            input("\n(Press Enter To Continue)")
        if choose == "5":
            info = webhook_info(whook)      
            for data in info:
                print(f"\n{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}]{Fore.LIGHTCYAN_EX} Found {data}{Fore.LIGHTCYAN_EX} ", end="")
            input("\n(Press Enter To Continue)")
        if choose == "6":
            whook.close()
            quit()
        
main()
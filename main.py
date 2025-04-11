from colorama import Style, Fore
import random
from time import sleep
import subprocess
import threading
import os


# Formatting For Better Code Maybe

class logger:
    @staticmethod
    def info(msg): print(f"{Fore.BLUE}[INFO] {Style.RESET_ALL}{msg}")
    @staticmethod
    def error(msg): print(f"{Fore.RED}{Style.BRIGHT}[ERR] {Style.RESET_ALL}{msg}")
    @staticmethod
    def warning(msg): print(f"{Fore.YELLOW}[WARN] {Style.RESET_ALL}{msg}")
    @staticmethod
    def success(msg): print(f"{Fore.GREEN}[SUC] {Style.RESET_ALL}{msg}")

# Directory list

def check_dir():

    print(f"{Fore.BLUE}Checking for Directories, Please wait{Style.RESET_ALL}")
    output_dir = {
        "output": "output",
        "xss": "output/xss",
        "sqli": "output/sqli",
        "dig": "output/dig",
        "nmap": "output/nmap",
        "temp": "output/temp"
    }

    for key, path in output_dir.items():
        if not os.path.isdir(path):
            logger.warning(f"'{path}' does not exist! Creating one for u.")
            os.makedirs(path, exist_ok=True)
            sleep(.05)
        else:
            logger.info(f"'{path} OK!'")
            sleep(.05)



slapsh_text = f"{Style.BRIGHT}Did you know:"
def tips():
    
    tip1 = f'''{Fore.GREEN}{Style.BRIGHT}You can type "exit" to exit!{Style.RESET_ALL}'''
    tip2 = f'''{Fore.GREEN}{Style.BRIGHT}This is 2nd tip!{Style.RESET_ALL}'''
    tips = [tip1, tip2]
    return random.choice(tips)

def main():
    check_dir()

    while True:
        print(f"{Style.BRIGHT}Welcome to Fast Uhh idk")
        sleep (0.2)
        print(f"{slapsh_text} {tips()}\n\n")
        sleep (3)
        print("Enter your nmap target: (e.g: www.google.com or 8.8.8.8)")
        target = input("> ")
        if target.lower() == "exit":
            print(f"{Fore.GREEN}Ba Bye!{Style.RESET_ALL}")
            exit()

        parallel1(target)


def dig_scan(target):
    print(f"Target: {Fore.GREEN}{target}")
    subprocess.run(["dig", target])

def nmap_scan(target):
    print(f"Target: {Fore.GREEN}{target}")
    subprocess.run(["nmap", "-sV", target])


def parallel1(targeted):
    global nmap_thread, dig_thread
    nmap_thread = threading.Thread(target=nmap_scan, args=(targeted,))
    dig_thread = threading.Thread(target=dig_scan, args=(targeted,))

    nmap_thread.start()
    dig_thread.start()

    nmap_thread.join()
    dig_thread.join()

main()

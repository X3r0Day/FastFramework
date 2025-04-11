from lib.format import log
from back import profiles
from back import settings

intro = '''

            Welcome to this framework!

'''
'''
# Settings list
nmap_opt = []

def nmap_settings():
    global nmap_opt
    print("NMAP Settings configuration")
    while True:
        nmap_arg = input("Vulnerability Scanning Engine:\n1 = No    2 = Yes     3 = Default Engine\n> ")
        if nmap_arg == "1" or "2" or "3":
            print("Settings Applied!")
            nmap_opt.append(nmap_arg)
            break
        else:
            logger.err("error Try again!")


    while True:
        nmap_arg = input("Scanning mode level: (1-4)\n> ")
        if nmap_arg == "1" or "2" or "3" or "4":
            print("Settings Applied!")
            nmap_opt.append(nmap_arg)
            break
        else:
            logger.err("Error! Try again")

    while True:
        nmap_arg = input("")

def main():

    print(intro)
    nmap_settings()
    
main()

print(nmap_opt)
'''

intro = '''
    Welcome to Framework
'''


def start():
    print("Test")

def main():
    log.info(intro)
    while True:
        print("1. Configure Profiles")
        print("2. Start")
        print("99. Exit")
        opt = input("> ")
        if opt == "1":
            profiles.main()
        elif opt == "2":
            start()
        elif opt == "99":
            exit()
        else:
            pass

if __name__ == "__main__":
    main()

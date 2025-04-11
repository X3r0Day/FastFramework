from colorama import Style,Fore


class log:
    @staticmethod
    def warn(msg): print(f"{Fore.YELLOW}[!] {Style.RESET_ALL}{msg}")
    @staticmethod
    def err(msg):  print(f"{Fore.RED}{Style.BRIGHT}[x] {Style.RESET_ALL}{msg}")
    @staticmethod
    def suc(msg):  print(f"{Fore.GREEN}{Style.BRIGHT}[] {Style.RESET_ALL}{msg}")
    @staticmethod
    def info(msg): print(f"{Fore.BLUE}[i] {Style.RESET_ALL}{msg}")

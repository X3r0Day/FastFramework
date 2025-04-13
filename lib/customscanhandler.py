import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from engine import selected_opt
import main2 as sel_target

target = sel_target.main()

def nmap():
    print("Starting NMAP Scan")
    print(target)
    

def main():
    # NMAP Scan
    nmap()


if __name__ == "__main__":
    main()
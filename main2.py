import threading
import subprocess
import json
import os
import sys
from back.profiles import curr_prof


profile = curr_prof()
print(f"profiles/{profile}")

def load_prof():
    with open(f"profiles/{profile}") as file:
        data = json.load(file)
        nmap_args = data["nmap"]["options"]
        print(f"Arguments to use for nmap: {nmap_args}")
        return nmap_args

print(profile)

def main():
    print("Selecting All Scan")

    target = input("Enter Your Target\n> ")
    print(f"Selected Target: '{target}'")
    scanning(target)
    return target


def scanning(targeted):
    print("Starting NMAP and DIG Scan") 
    nmap_scan = subprocess.run(["nmap", *load_prof(), targeted])
    print(nmap_scan.stdout)

if __name__ == "__main__":
    main()
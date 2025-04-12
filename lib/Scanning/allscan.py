import threading
import subprocess
import json
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ..back.profiles import curr_prof


profile = curr_prof()
print(profile)

def main():
    print("Selecting All Scan")

    target = input("Enter Your Target\n> ")
    print(f"Selected Target: '{target}'")


def scanning():
    print("Starting NMAP and DIG Scan")
    nmap_scan = subprocess.run(["nmap", "-sV", "-A"])


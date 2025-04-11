import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lib.format import log

settings_file = "settings/settings.json"
profiles_dir = "profiles"
prof_list = []

def curr_prof():
    with open(settings_file, "r") as settings:
        data = json.load(settings)
    return data["profile"]["current_profile"]

def total_prof():
    return len([
        f for f in os.listdir(profiles_dir)
        if os.path.isfile(os.path.join(profiles_dir, f))
    ])

def list_profiles():
    return [
        f for f in os.listdir(profiles_dir)
        if os.path.isfile(os.path.join(profiles_dir, f))
    ]

def update_settings(profile_name):
    try:
        with open(settings_file, "r") as file:
            data = json.load(file)
    except(json.JSONDecodeError, FileNotFoundError):
        data = {"profile": {}}

    data["profile"]["current_profile"] = profile_name

    with open(settings_file, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Updated Current Profile Successfully!")    

def options():
    print("1. Select Profile")
    print("2. List Profile")
    print("99. Exit")

def select_prof():
    select_prof = input("Enter Profile You Want to select\n> ")
    print(f"Selecting the profile {select_prof}")
    if select_prof in prof_list:
        print(f"Selected Profile: '{select_prof}'")
        update_settings(select_prof)
    else:
        log.err("Profile Not Found! Try Again.")

def list_prof():
    print("🗂 Available Profiles:")
    global prof_list
    for i, profile in enumerate(list_profiles(), 1):
        print(f"  {i}. {profile}")
        prof_list.append(profile)





def main():
    print("=== ⚙️ Configure Profile ===\n")
    
    log.info(f"Current Selected Profile: {curr_prof()}")
    log.info(f"Total Profiles: {total_prof()}\n")

    options()
    while True:
        opt = input("> ")
        if opt == "1":
            select_prof()
        elif opt == "2":
            list_prof()
        elif opt == "99":
            print("Exiting...")
            exit()
        else:
            print("Error! Try again!")
        

if __name__ == "__main__":
    main()

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

def main():
    print("=== ⚙️ Configure Profile ===\n")
    
    log.info(f"Current Selected Profile: {curr_prof()}")
    log.info(f"Total Profiles: {total_prof()}\n")
    
    print("🗂 Available Profiles:")
    for i, profile in enumerate(list_profiles(), 1):
        print(f"  {i}. {profile}")
        prof_list.append(profile)
    
    print(prof_list)
    while True:
        select_prof = input("Enter Profile You Want to select\n> ")
        print(f"Selecting the profile {select_prof}")
        if select_prof in prof_list:
            print(f"Selected Profile: '{select_prof}'")
            update_settings(select_prof)
        else:
            log.err("Profile Not Found! Try Again.")

if __name__ == "__main__":
    main()

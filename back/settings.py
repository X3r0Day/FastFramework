import json

settings_file = "settings/settings.json"

def main():
    print("Settings")
    with open(settings_file, "r") as file:
        data = json.load(file)

        print(data)

main()

if __name__ == "__main__":
    main()
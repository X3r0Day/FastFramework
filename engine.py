from lib.format import log

def options():
    print("1. All scans")
    print("2. Custom Scan")
    print("99. Exit")


def main():
    print("Welcome to the main engine!")
    options()
    while True:
        opt = input("> ")
        if opt == "1":
            print("All Scans")
            

        elif opt == "2":
            print("Custom Scan")


        elif opt == "99":
            print("Exiting..")
            exit()
        else:
            log.err("Error Occured! Please Again!")


if __name__ == "__main__":
    main()
from lib.format import log

selected_opt = []

def options():
    print("1. All scans")
    print("2. Custom Scan")
    print("99. Exit")

def sel_cust_scan():
    global selected_opt
    opt1 = input("Do you want to run NMAP Scan? (Y/n): ")
    if opt1.lower() == "Y" or "":
        selected_opt.append("NMAP Scan")

    opt2 = input("Do you want to run SQLi Scan? (Y/n): ")
    if opt1.lower() == "Y" or "":
        selected_opt.append("SQLi Scan")

    opt3 = input("Do you want to run Dig Scan? (Y/n): ")
    if opt1.lower() == "Y" or "":
        selected_opt.append("Dig Scan")



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
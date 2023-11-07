#----------------------------Phone Tester------------------------------
import time
import sys
#------------------------------Inputing-------------------------------
print("    ____  __                        ______          __               ")
print("   / __ \/ /_  ____  ____  ___     /_  __/__  _____/ /____  _____    ")
print("  / /_/ / __ \/ __ \/ __ \/ _ \     / / / _ \/ ___/ __/ _ \/ ___/    ")
print(" / ____/ / / / /_/ / / / /  __/    / / /  __(__  ) /_/  __/ /        ")
print("/_/   /_/ /_/\____/_/ /_/\___/    /_/  \___/____/\__/\___/_/         ")
print("                                                                     ")
print("                                                                     ")
print("Turn On The Bluetooth And Wifi Before You Test Your Device")
print("                                                                     ")
print("                                                                     ")
print("Chose Any Options \n 1. Test A New Phone \n 2. Test A Old Phone \n 3. Test a Smart Watch \n 4. Update This Tool \n 5. Exit")
inp = input("Enter Any Option--> ")
#--------------------------------Coding---------------------------------
if inp == "1":
    def print_slow(text, delay=0.02):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    print_slow("                Testing...             ")
    print_slow("  ______          __  _                ")
    print_slow(" /_  __/__  _____/ /_(_)___  ____ _    ")
    print_slow("  / / / _ \/ ___/ __/ / __ \/ __ `/    ")
    print_slow(" / / /  __(__  ) /_/ / / / / /_/ /     ")
    print_slow("/_/  \___/____/\__/_/_/ /_/\__, /      ")
    print_slow("                          /____/       ")
    print_slow("Camara Ok.")
    print_slow("Ram Ok.")
    print_slow("Rom Ok.")
    print_slow("Internet Ok.")
    print_slow("Speed Ok.")
    print_slow("Phone Is Original And Official!!!")
elif inp == "2":
    def print_slow(text, delay=0.02):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    print_slow("                Testing...             ")
    print_slow("  ______          __  _                ")
    print_slow(" /_  __/__  _____/ /_(_)___  ____ _    ")
    print_slow("  / / / _ \/ ___/ __/ / __ \/ __ `/    ")
    print_slow(" / / /  __(__  ) /_/ / / / / /_/ /     ")
    print_slow("/_/  \___/____/\__/_/_/ /_/\__, /      ")
    print_slow("                          /____/       ")
    print_slow("Camara Ok.")
    print_slow("Ram Ok.")
    print_slow("Rom Ok.")
    print_slow("Internet Ok.")
    print_slow("Speed Ok.")
    print_slow("Phone Is Original And Official!!!")
elif inp == "3":
    def print_slow(text, delay=0.02):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    print_slow("                Testing...             ")
    print_slow("  ______          __  _                ")
    print_slow(" /_  __/__  _____/ /_(_)___  ____ _    ")
    print_slow("  / / / _ \/ ___/ __/ / __ \/ __ `/    ")
    print_slow(" / / /  __(__  ) /_/ / / / / /_/ /     ")
    print_slow("/_/  \___/____/\__/_/_/ /_/\__, /      ")
    print_slow("                          /____/       ")
    print_slow("Camara Ok.")
    print_slow("Ram Ok.")
    print_slow("Rom Ok.")
    print_slow("Internet Ok.")
    print_slow("Speed Ok.")
    print_slow("Phone Is Original And Official!!!")
elif inp == "4":
    print("No Need To Update Your Tool. You Are Up To Date!!!")
elif inp == "5":
    sys.exit()
else:
    print("Opps You Enter A Unvalid Number😣😣😣")
# ██╗░░░░░██╗██████╗░  ██╗░░░██╗███████╗░█████╗░██████╗░
# ██║░░░░░██║██╔══██╗  ╚██╗░██╔╝██╔════╝██╔══██╗██╔══██╗
# ██║░░░░░██║██████╔╝  ░╚████╔╝░█████╗░░███████║██████╔╝
# ██║░░░░░██║██╔═══╝░  ░░╚██╔╝░░██╔══╝░░██╔══██║██╔══██╗
# ███████╗██║██║░░░░░  ░░░██║░░░███████╗██║░░██║██║░░██║
# ╚══════╝╚═╝╚═╝░░░░░  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝

year = int(input("Which year do you want to check? "))

if (year / 4) == int(year / 4):
    if (year / 100) == int(year / 100):
        if (year / 400) == int(year / 400):
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
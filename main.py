from os import path, system
from colorama import Fore, init
from Plugins.api_list import handler
from Plugins.functions import Functions
from pystyle import Col, Center, System

init(autoreset=True)

g = "\033[1m"
r = "\033[1m"
reset = "\033[0m"

def install_requirements():
    if path.exists("./requirements.txt"):
        with open("./requirements.txt") as file:
            libs = [i.split("==")[0] for i in file.readlines()]
        
        for lib in libs:
            try:
                __import__(lib)
            except ModuleNotFoundError:
                system("pip install " + lib)

install_requirements()

def display_logo():
    logo = f'''
     {g}█████{reset}╗ {g}██{reset}╗     {g}███████{reset}╗{g}██████{reset}╗  {g}███████{reset}╗  {g}████████{reset}╗   {g}█████{reset}╗
    {r}██╔══██{reset}╗{r}██║     ██╔════╝██╔══██{reset}╗ {r}██╔════╝  ╚════╗██{reset}║  {r}██╔══██{reset}╗
    {g}███████{reset}║{g}██║     █████╗  ██████╔╝ █████╗       ███╔═╝  ███████{reset}║
    {r}██╔══██{reset}║{r}██║     ██╔══╝  ██╔══██{reset}╗ {r}██╔══╝    ███╔══╝    ██╔══██{reset}║
    {g}██║  ██║███████╗███████{reset}╗{g}██║  ██║ ███████╗  ███████{reset}╗   {g}██║  ██║
    ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝ ╚══════╝  ╚══════╝   ╚═╝  ╚═╝

    {g}██████{reset}╗  {g}█████{reset}╗ {g}███{reset}╗   {g}███{reset}╗{g}██████{reset}╗ {g}███████{reset}╗{g}██████{reset}╗ 
    {g}██{reset}╔══{g}██{reset}╗{g}██{reset}╔══{g}██{reset}╗{g}████{reset}╗ {g}████{reset}║{g}██{reset}╔══{g}██{reset}╗{g}██╔════╝{g}██{reset}╔══{g}██{reset}╗
    {g}██████{reset}╦╝{g}██{reset}║  {g}██{reset}║{g}██{reset}╔{g}████{reset}╔{g}██{reset}║{g}██████{reset}╦╝{g}█████{reset}╗  {g}██████{reset}╔╝
    {g}██{reset}╔══{g}██{reset}╗{g}██{reset}║  {g}██{reset}║{g}██{reset}║╚{g}██{reset}╔╝{g}██{reset}║{g}██╔══{reset}{g}██{reset}╗{g}██╔══╝  {g}██╔══{reset}{g}██{reset}╗
    {g}██████{reset}╦╝╚{g}█████{reset}╔╝{g}██{reset}║ ╚═╝ {g}██{reset}║{g}██████{reset}╦╝{g}███████{reset}╗{g}██{reset}║  {g}██{reset}║
    {r}╚═════╝  ╚════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

                    Alireza.Nasiri_py
     {reset}
    '''
    System.Clear()
    print(Center.XCenter(logo))

def main():
    while True:
        display_logo()
        try:
            proxy_state = Fore.GREEN + "Enabled" if Functions.proxy_state() else Fore.RED + "Disabled"
            choices = {
                "1": "call",
                "2": "sms"
            }
            print(f"{Col.yellow}[!]{Col.gray} Proxies are {proxy_state}")
            print(f"{Col.yellow}[!]{Fore.CYAN} Choices: ")

            for ch in choices:
                print(f"   {Fore.CYAN}{ch}- {Fore.GREEN}{choices[ch].capitalize()} Bomber ")
            
            print()
            choice = Functions.get_input(f"{Fore.CYAN}[=]{Col.gray} Enter Your Choice: {Col.green}", lambda x: x in [str(i) for i in choices])
            number = Functions.get_input(f"{Fore.CYAN}[=]{Col.gray} Enter the phone number {Fore.CYAN}[9xxxxxxxxx]{Col.gray}: {Col.green}", 
                                         checker=lambda x: x != "" and x.isnumeric() and x.startswith("9") and len(x) == 10)
            count = Functions.get_input(f"{Fore.CYAN}[=]{Col.gray} Enter spam count: {Col.green}", lambda x: x.isnumeric() and int(x) >= 0)

            Functions.start(choices[choice], number, int(count))
        except KeyboardInterrupt:
            print("\n" + Fore.BLUE, "Exiting...")
            break

if __name__ == "__main__":
    main()
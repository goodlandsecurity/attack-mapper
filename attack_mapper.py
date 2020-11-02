import json
from os import system, name


def load_attack_mapping():
    try:
        with open('attack_mapping.json') as attack_map:
            attack_json = json.load(attack_map)

        return attack_json

    except FileNotFoundError:
        print("[*] ERROR: Please put attack_mapping.json in the same directory as this script! "
              "(https://github.com/MITRECND/mitrecnd.github.io/blob/master/_data/attack_mapping.json)")
        exit()


def main():
    attack_mapping = load_attack_mapping()
    while True:
        clear_screen()
        prCastle()
        first_input = input("[*] Would you like to search by ATT&CK Technique Name or ID?\n")

        if first_input.lower() == 'quit' or first_input.lower() == 'exit':
            prWarning("[+] Goodbye!")
            exit()
        elif first_input.lower() == 'name':
            search_technique_name(attack_mapping)
        elif first_input.lower() == 'id':
            search_technique_id(attack_mapping)


def search_technique_name(attack_mapping):
    clear_screen()
    prCastle()
    technique_search = input("[*] Enter ATT&CK Technique name:\n")
    for techniques in attack_mapping:
        tactic_list = []
        technique_list = []
        dtactic_list = []
        procedure_list = []
        if technique_search in techniques['attack_technique']['name'].lower():
            map_attack(techniques, tactic_list, technique_list, dtactic_list, procedure_list)


def search_technique_id(attack_mapping):
    clear_screen()
    prCastle()
    technique_search = input("[*] Enter ATT&CK Technique ID: \n")
    for techniques in attack_mapping:
        tactic_list = []
        technique_list = []
        dtactic_list = []
        procedure_list = []
        if technique_search.upper() == techniques['attack_technique']['id']:
            map_attack(techniques, tactic_list, technique_list, dtactic_list, procedure_list)


def map_attack(techniques, tactic_list, technique_list, dtactic_list, procedure_list):
    clear_screen()
    for tactic in techniques['attack_tactics']:
        tactic_list.append([tactic['name'], tactic['id']])
    technique_list.append([techniques['attack_technique']['name'], techniques['attack_technique']['id']])
    prRed(f"ATT&CK Tactic(s):")
    for i in tactic_list:
        print(f"[+] {[i][0][0]} ({i[1]})")
    prRed(f"\nATT&CK Technique:")
    print(f"[+] {technique_list[0][0]} ({technique_list[0][1]})\n")

    prWarning(f"Active Defense Opportunity:")
    print(f"[+] {techniques['opportunity']['description']} ({techniques['opportunity']['id']})\n")

    for dtactic in techniques['tactics']:
        dtactic_list.append([dtactic['name'], dtactic['id'], dtactic['long_description']])
    prCyan(f"Active Defense Tactic:")
    print(f"[+] {dtactic_list[0][0]} ({dtactic_list[0][1]})\n"
          f"[*] {dtactic_list[0][2]}\n")

    prCyan(f"Active Defense Technique:")
    print(f"[+] {techniques['technique']['name']} ({techniques['technique']['id']})\n"
          f"[*] {techniques['technique']['long_description']}\n")

    prWarning(f"Active Defense Use Case:")
    print(f"[+] {techniques['use_case']['description']} ({techniques['use_case']['id']})\n")

    for procedure in techniques['procedures']:
        procedure_list.append([procedure['id'], procedure['description']])
    prCyan(f"Active Defense Procedure(s):")
    for i in procedure_list:
        print(f"[+] {[i][0][1]} ({i[0]})")

    enter = input(f"\nPress enter to continue")


def prGreen(skk):
    print("\033[92m {}\033[00m".format(skk))


def prRed(skk):
    print("\033[91m {}\033[00m" .format(skk))


def prCyan(skk):
    print("\033[96m {}\033[00m" .format(skk))


def prWarning(skk):
    print("\033[93m {}\033[00m" .format(skk))


def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def prCastle():
    print("\n                                    *//////\n"
          "                                    *//////\n"
          "                                    *//////\n"
          "                                    *\n"
          "                                  .***\n"
          "           *///                  */////*                   *///\n"
          "           *///                *////////**                 *///\n"
          "           *             .((#%**/&&@@&%/**%#(/             *\n"
          "          ///.           .((#%***&&@@&%***%#(/           ////\n"
          "        */////*          .((#%%&&&&@@&&&&%%#((          */////*\n"
          "      ***********          ///(((((#(((((//*          **********,\n"
          "   *(#%&&&&@&&&%#(/        (##%&&&...&&%%##(        /(#%&&&@&&&%#(\n"
          "    ,(#%%&&&&%%#(*         (##%%&.....&%%##(         /(#%%&&&%%#(\n"
          "    ,(#%&&&@&&%#(*         (##%&&*****&%%##(         /(%%&&@&&%#(\n"
          "    ,(#%......%#(*         (##%%&(((((&%%##(         /(%(.....%#(\n"
          "    ,(#%,,,,,,%#(*  .####  (#%%%%&&&&&%%%%#(  ####.  /(%(,,,,,%#(\n"
          "    ,(#%//////%#(*  .####  (#%%%%&&&&&%%%%#(  ####.  /(%#/////%#(\n"
          "    ,(#%&&@@&&%#((#####%%%%%%%%&&&&&&&&&%%%%%%%%#####/(%%&&@&&%#(\n"
          "    ,(#%&&@@&&%#((####%%%%%%%&&%#######%&&&%%%%%%%###/(%%&&@&&%#(\n"
          "    ,(#%&&@@&&%#((###%%%%%%&%##/*..*..*(##&&%%%%%%###/(%%&&@&&%#(\n"
          "    ,(#%&&@@&&%#((##%%%%%%&###.,*,,*,,*,.##%&%%%%%%##/(%%&&@&&%#(\n"
          "    ,(#%&&@@&&%#((##%%%%%&&##*,,*,,*,,*,,*##&&%%%%%%#/(%%&&@&&%#(\n"
          "    ,(#%&&@@&&%#((##%%%%%%&##*,,*,,*,,*,,*##&%%%%%%##/(%%&&@&&%#(\n"
          "    ,(#%&&@@&&%#((###%%%%%&##*,,*,,*,,*,,*##&%%%%%%##/(%%&&@&&%#(\n"
          "    ,(#%&&@@&&%#((###%%%%%%##*,,*,,*,,*,,*##%%%%%%###/(%%&&@&&%#(\n"
          "    ,(#%&&@@&&%#((####%%%%%##*,,*,,*,,*,,*##%%%%%####/(%%&&@&&%#(")

    prCyan("▄▀█ █▀▀ ▀█▀ █ █░█ █▀▀   █▀▄ █▀▀ █▀▀ █▀▀ █▄░█ █▀ █▀▀   ▀█▀ ▀█▀ █▀█ █▀\n"
           " █▀█ █▄▄ ░█░ █ ▀▄▀ ██▄   █▄▀ ██▄ █▀░ ██▄ █░▀█ ▄█ ██▄   ░█░ ░█░ █▀▀ ▄█\n")

if __name__ == "__main__":
    main()

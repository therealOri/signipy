import os
import sys
import beaupy
from pystyle import Colors, Colorate




def banner():
    banner = """
                ███████╗██╗ ██████╗ ███╗   ██╗██╗██████╗ ██╗   ██╗
                ██╔════╝██║██╔════╝ ████╗  ██║██║██╔══██╗╚██╗ ██╔╝
                ███████╗██║██║  ███╗██╔██╗ ██║██║██████╔╝ ╚████╔╝
                ╚════██║██║██║   ██║██║╚██╗██║██║██╔═══╝   ╚██╔╝
                ███████║██║╚██████╔╝██║ ╚████║██║██║        ██║
                ╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝        ╚═╝

          Made by Ori#6338 | @therealOri_ | https://github.com/therealOri
    """
    colored_banner = Colorate.Horizontal(Colors.purple_to_blue, banner, 1)
    return colored_banner



def clear():
    os.system("clear||cls")



def execmd(cmd):
    #os.system will return command code for when the command was successful, failed, interrupted, etc.
    #I am not returning anything rn but have left room for that possibilty in the future.
    os.system(cmd)





def main():
    clear()
    while True:
        main_options = ["Keygen?", "Sign file?", "Verify file?", "Exit?"]
        print(f'{banner()}\n\nWhat would you like to do?\n-----------------------------------------------------------\n')
        main_option = beaupy.select(main_options, cursor_style="#ffa533")


        if not main_option:
            clear()
            exit("Keyboard Interuption Detected!\nGoodbye <3")

        if main_options[0] in main_option:
            clear()
            passphrase_check = beaupy.confirm("Do you want to have a passphrase? - (to protect the secret key)")
            if passphrase_check == None:
                clear()
                continue
            if passphrase_check == True:
                print("Generating keypair...")
                execmd("signify -G -p keyname.pub -s keyname.sec")
            else:
                print("Generating keypair...")
                execmd("signify -n -G -p keyname.pub -s keyname.sec")
            clear()
            input('Keys have been generated! - (feel free to rename them.)\n\nPress "enter" to continue...')
            clear()
            continue

        if main_options[1] in main_option:
            clear()
            file_to_sign = beaupy.prompt("Please provide file to sign. - (drag & drop)")
            if not file_to_sign:
                clear()
                continue
            else:
                file_to_sign = file_to_sign.replace("\\", " ").strip()

            sec_key_file = beaupy.prompt("Please provide your .sec key file. - (drag & drop)")
            if not sec_key_file:
                clear()
                continue
            else:
                sec_key_file = sec_key_file.replace("\\", " ").strip()

            tar_check = beaupy.confirm("Is this a .tar.gz archive file?")
            if tar_check == None:
                clear()
                continue

            if tar_check == True:
                execmd(f"signify -z -S -s {sec_key_file} -m {file_to_sign}")
            else:
                execmd(f"signify -S -s {sec_key_file} -m {file_to_sign}")
            clear()
            input('File has been signed!\n\nPress "enter" to continue...')
            clear()
            continue

        if main_options[2] in main_option:
            clear()
            pub_key_file = beaupy.prompt("Please provide your .pub key file. - (drag & drop)")
            if not pub_key_file:
                clear()
                continue
            pub_key_file = pub_key_file.replace("\\", " ").strip()

            signature_file = beaupy.prompt("Please provide the .sig file for the file you want to verify. - (drag & drop)")
            if not signature_file:
                clear()
                continue
            signature_file = signature_file.replace("\\", " ").strip()

            file_to_verify = beaupy.prompt("Please provide the file you want to verify. - (drag & drop)")
            if not file_to_verify:
                clear()
                continue
            file_to_verify = file_to_verify.replace("\\", " ").strip()

            clear()
            tar_check = beaupy.confirm("Is this a .tar.gz archive file?")
            if tar_check == None:
                clear()
                continue

            if tar_check == True:
                execmd(f"signify -z -V -p {pub_key_file} -x {signature_file} -m {file_to_verify}")
            else:
                execmd(f"signify -V -p {pub_key_file} -x {signature_file} -m {file_to_verify}")
            input('\n\nPress "enter" to continue...')
            clear()
            continue

        if main_options[3] in main_option:
            clear()
            exit("Goodbye! <3")





if __name__ == '__main__':
    clear()
    main()

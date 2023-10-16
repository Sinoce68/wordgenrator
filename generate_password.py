import itertools
import colorama
import random
import time
import sys
import os

class color():
    cl = colorama.Fore
    gr = cl.GREEN
    rd = cl.RED
    bl = cl.BLUE
    cy = cl.CYAN
    yl = cl.YELLOW
    mg = cl.MAGENTA
    lgr = cl.LIGHTGREEN_EX
    lrd = cl.LIGHTRED_EX
    lbl = cl.LIGHTBLUE_EX
    lcy = cl.LIGHTCYAN_EX
    lyl = cl.LIGHTYELLOW_EX
    lmg = cl.LIGHTMAGENTA_EX

def prc(start:int=0, end:int=7, list_string:list=list('abcdefghijklmnopqrstuvwxyz' + 'abcdefghijklmnopqrstuvwxyz'.upper() + "0123456789" + "@$~-_\/.")):
    passwords = []
    for i in range(start, end + 1):
        for char in itertools.product(list_string, repeat=i):
            passwords.append("".join(char))
    return passwords



def random_password():
    password_expair = []
    range_password = int(input("Enter Number Password: "))
    length_password = int(input("Enter Length Password: "))
    char = input('Character Passwrdlist Default [y/n]')
    if char.lower() == "y":
         char_default = "qwertyuiopasdfghjklzxcvbnm" + "qwertyuiopasdfghjklzxcvbnm".upper() + "0123456789" + "!@$~()"
    else:
         char_default = input("Enter Character: ")
    save_output = True if input("Save Output File [y/n]").lower() == 'y' else False

    if save_output:
         file_name = input("Enter The Output: ")
         if os.path.isfile(file_name):
             print("Found -> "+file_name.strip())
             for password in range(range_password):
                 passwd = "".join(random.choices(list(char_default), k=length_password))
                 if passwd not in password_expair:
                     password_expair.append(passwd)
                     open(file_name, "a").write(passwd + "\n")
                 else:pass

         else:
             open(file_name, "w")
             TM = time.localtime()
             DATE = str(TM.tm_hour) + ":" + str(TM.tm_min) + ":" + str(TM.tm_sec)
             print(f"File ->({file_name}) Created ({DATE})")
             for password in range(range_password):
                 passwd = "".join(random.choices(list(char_default), k=length_password))
                 if passwd not in password_expair:
                     password_expair.append(passwd)
                     open(file_name, "a").write(passwd + "\n")
                 else:pass
    else:
         for password in range(range_password):
                 print("".join(random.sample(char_default, length_password)))

def password_high():
    LEN = int(input("Enter Length Passwords: "))
    OUTPUT = input("Enter Output: ")
    CHAR = input("Example: reza:mohamad:2012\n \tEnter CHARS : ").split(":")
    PASS = prc(0, LEN, CHAR)
    open(OUTPUT, "w").write("\n".join(PASS))

ask = input("Random [r] High[h]: ")
if ask == 'h':
    password_high()
elif ask == 'r':
    random_password()
else:
    print("Invalid Input !")

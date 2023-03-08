import string
import random
from random import randint, choice
import tkinter
from tkinter import *
import os



                                                                               
# variable
fronttext = f"PASSWORLD generator "+ "1.0.0"
bgcolor= '#413E44'

# fonction
def ERREUR_LOGIN(erreur_message):
    #errorlogin
    windows = Tk()
    windows.title("ERROR")
    windows.geometry("502x126")
    windows.maxsize(502, 126)
    windows.minsize(502, 126)
    windows.iconbitmap("icone.ico.ico")
    windows.config(background='white')
    frame = Frame(windows,bg='white', bd=1, relief=SUNKEN  )
    label_error = Label(frame, text="ERROR: function {generate_opt} is not call, please call the administrator if is an error", font=("Arial", 10),bg='white', fg='Red' )
    label_error.pack()
    frame.pack(expand=YES)
    windows.mainloop()


def Generateur_script():
    #générer code
    password_min = 6
    password_max = 12
    all_char = string.ascii_letters + string.punctuation + string.digits
    password= "" .join(choice(all_char) for x in range(randint(password_min, password_max)))
    pass_entry.delete(0,END)
    pass_entry.insert(0,password)
    # open file
    with open("password.pass","a+") as file:
        file.write("ans= "+ str(password)+"\n")
        file.close()

    


def reset_entry():
    pass_entry.delete(0,END)

def generate_opt():
    all_char = string.ascii_letters + string.digits

#windows
windows = Tk()
windows.title("Passworld generator")
windows.geometry("802x430")
# windows.iconbitmap('icone.ico')
windows.config(background=bgcolor)

def read():
    net = 1
    with open("password.pass", "a+") as file:
       net = file.read()
    if net == str(file.read):
            print("True")
    else:
            print("False")
            print(net)

read()
# frame_main
frame_main = Frame(windows, bg=bgcolor, bd=1, relief=SUNKEN  )


#labeltitle


label_title = Label(frame_main, text="PASSWORLD GENERATOR "+ "1.0.0",background=bgcolor, font=("helvestica",20), bg= bgcolor, fg='white')

#Fird frame
fird_frame = Frame(frame_main, bg=bgcolor, bd=1, relief=SUNKEN)
#sous frame
second_frame = Frame(frame_main, bg=bgcolor, bd=1, relief=SUNKEN)


#imput
pass_entry = Entry(second_frame,background=bgcolor, font=("helvestica",20), bg= 'white', fg='black')


#button generator
pass_botton = Button(fird_frame,text="GENERER",background=bgcolor, font=("helvestica",20), fg='white',command=Generateur_script)

#menubar
menu_bar = Menu(windows, bg=bgcolor)


#fenetre 1 menu
file_menu_option = Menu(menu_bar, tearoff=0)
file_menu_option.add_command(label="option_géneration", command= ERREUR_LOGIN)
file_menu= Menu(menu_bar, tearoff=0)
file_menu.add_command(label="NOUVEAU", command=Generateur_script)
file_menu.add_command(label="RESET", command=reset_entry)
file_menu.add_command(label="QUITTER", command=windows.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)
menu_bar.add_cascade(label="Option", menu= file_menu_option)


#configurer windows
windows.config(menu=menu_bar)


#package

fird_frame.grid(row=1,column=2,sticky=W)
second_frame.grid(row=0,column=2,sticky=W)
pass_botton.pack(side=BOTTOM, fill=X)
pass_entry.pack()
frame_main.pack(expand=YES)
label_title.grid(row=0,column=1,sticky=W)



#windows
windows.mainloop()

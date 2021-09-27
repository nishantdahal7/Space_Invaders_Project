import tkinter
from tkinter import *
from tkinter import messagebox
import sys
from rootPackage.Credit import open_credit
from rootPackage.Setting import open_setting
from game.project import sponngebob

def Our_game():
    root = tkinter.Toplevel()
    root.title("KRUSTY KRAB")
    root.iconbitmap("sponge.ico")
    root.geometry("800x600")
    root.resizable(width=False, height=False)
    bg_img = PhotoImage(file="island.png")

    Label(root, text="WELCOME TO KRUSTY KRAB", font=("courier", 25, "bold"), bg="yellow").pack(side=TOP, fill=X)
    # Creating Canvas
    my_canvas = Canvas(root, width=800, height=600, highlightthickness=0)
    my_canvas.pack(fill="both", expand=False)

    #Setting Canvas Image
    my_canvas.create_image(0,0, image=bg_img, anchor="nw")
    #n, ne, e, se, s, sw, w, nw, or center

    #Defining Exit Button
    def alert():
        sure_exit = messagebox.askyesno("Exit", "Are You Sure To Exit The Game?")

        if sure_exit == 1:
            sys.exit()

        else:
            pass


    #Creating Start Button
    start_button = Button(root, text="START", bg="#CCFFCC", bd=0, fg="black", font=("arial", 22, 'bold'), width=15, height=2, command = sponngebob)
    start_window = my_canvas.create_window(280, 150, anchor="nw", window=start_button)


    #Creating Setting Button
    setting_button = Button(root, text="SETTINGS", bg="#CCFFCC", bd=0, fg="black", font=("arial", 22, 'bold'), width=15, height=2, command=open_setting)
    setting_window = my_canvas.create_window(280, 250, anchor="nw", window=setting_button)


    #Creating Credit Button
    credit_button = Button(root, text="CREDIT", bg="#CCFFCC",bd=0, fg="black", font=("arial", 22, 'bold'), width=15, height=2, command=open_credit)
    credit_window = my_canvas.create_window(280, 350, anchor="nw", window=credit_button)

    #Creating Exit Button
    exit_button = Button(root, text="EXIT", bg="#CCFFCC",bd=0, fg="black", font=("arial", 22, 'bold'), width=15, height=2, command=alert)
    exit_window = my_canvas.create_window(280, 450, anchor="nw", window=exit_button)

    root.mainloop()

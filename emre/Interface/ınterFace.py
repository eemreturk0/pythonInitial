import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from emre.school.fileManager import readFromFile
from emre.school.printer import printList

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 470

master = Tk()
master.title('SCHOOL SYSTEM')
master.title('Resizable')
master.resizable(False, False)


# pack
# place
# grid

class NewWindow(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("New Window")
        self.geometry("200x200")
        label = Label(self, text="This is a new Window")
        label.pack()


def on_enter(e):
    e.widget.config(foreground="white")


def on_leave(e):
    e.widget.config(foreground='black')


def main_menu():
    frame_canvas = Frame(frame_alt_sag)
    submenuFrames["main"] = frame_canvas
    frame_canvas.grid(row=0, column=0, pady=(5, 0), sticky='nw')
    frame_canvas.grid_rowconfigure(0, weight=1)
    frame_canvas.grid_columnconfigure(0, weight=1)
    # Set grid_propagate to False to allow 5-by-5 buttons resizing later
    frame_canvas.grid_propagate(False)

    canvas = Canvas(frame_canvas, bg="#8FA2CA")
    canvas.grid(row=0, column=0, sticky="news")
    vsb = Scrollbar(frame_alt_sag, orient="vertical", command=canvas.yview)
    vsb.grid(row=0, column=1, sticky='ns')
    canvas.configure(yscrollcommand=vsb.set)
    frame_buttons = Frame(canvas, bg="blue")
    canvas.create_window((0, 0), window=frame_buttons, anchor='nw')
    for i, text in enumerate(subMenuMain):
        Button1 = Button(frame_buttons, text=text, width=20, height=2, bg='#B5C6B8', activebackground="#eee8aa")
        Button1.grid(row=i, column=0, padx=5, pady=5, sticky='nwes')
    frame_buttons.update_idletasks()
    frame_canvas.config(width=200 + vsb.winfo_width(), height=SCREEN_HEIGHT)
    canvas.config(scrollregion=canvas.bbox("all"))

    # Button2 = Button(frame_alt_sag, text="Öğretmenleri Göster",  width=20, height=2, bg='#B5C6B8',activebackground="#eee8aa")
    # Button2.grid(row=1, column=0,  padx = 5, pady = 5)

    # Button3 = Button(frame_alt_sag, text="Sınıfları Göster", width=20, height=2, bg='#B5C6B8',activebackground="#eee8aa")
    # Button3.grid(row=2, column=0,  padx = 5, pady = 5)

    # Button4 = Button(frame_alt_sag, text="Dersleri Göster",  width=20, height=2, bg='#B5C6B8',activebackground="#eee8aa")
    # Button4.grid(row=3, column=0,  padx = 5, pady = 5)

    Button1.bind('<Enter>', on_enter)
    Button1.bind('<Leave>', on_leave)
    # Button2.bind('<Enter>', on_enter)
    # Button2.bind('<Leave>', on_leave)


# Button3.bind('<Enter>', on_enter)
# Button3.bind('<Leave>', on_leave)
# Button4.bind('<Enter>', on_enter)
# Button4.bind('<Leave>', on_leave)
def myPrinter(text="bu test deneme"):
    print(text)


vsb = None
frame_buttons = None
submenuFrames = {}
subMenuMain = [{"func":  lambda: showStudentList(), "text": "Öğrencileri göster"}]

subMenuStudents = [{"func":  lambda : NewWindow(master), "text": "Öğrenci EKle"} ]

subMenuTeacher = [{"func":  lambda: myPrinter("öğrencileri gostere basıldı"), "text": "Öğretmen ekle"}]

subMenuLesson = [{"func":  lambda: myPrinter("öğrencileri gostere basıldı"), "text": "Dersleri göster"}]



def submenuCreator(menu_name,subMenuItems:[]):
    frame_canvas = Frame(frame_alt_sag)
    submenuFrames[menu_name] = frame_canvas
    frame_canvas.grid(row=0, column=0, pady=(5, 0), sticky='nw')
    frame_canvas.grid_rowconfigure(0, weight=1)
    frame_canvas.grid_columnconfigure(0, weight=1)
    # Set grid_propagate to False to allow 5-by-5 buttons resizing later
    frame_canvas.grid_propagate(False)

    canvas = Canvas(frame_canvas, bg="#8FA2CA")
    canvas.grid(row=0, column=0, sticky="news")
    vsb = Scrollbar(frame_alt_sag, orient="vertical", command=canvas.yview)
    vsb.grid(row=0, column=1, sticky='ns')
    canvas.configure(yscrollcommand=vsb.set)
    frame_buttons = Frame(canvas, bg="blue")
    canvas.create_window((0, 0), window=frame_buttons, anchor='nw')
    for i, obj in enumerate(subMenuItems):
        Button1 = Button(frame_buttons, text=obj["text"],command=obj["func"], width=20, height=2, bg='#B5C6B8', activebackground="#eee8aa")
        Button1.grid(row=i, column=0, padx=5, pady=5, sticky='nwes')
    frame_buttons.update_idletasks()
    frame_canvas.config(width=200 + vsb.winfo_width(), height=SCREEN_HEIGHT)
    canvas.config(scrollregion=canvas.bbox("all"))


def showStudentList():

     printList("student", schoolObj.student_list)
     liste = ttk.Treeview(frame_alt_sag2, columns=(1), show="headings", height="5")
     liste.pack()

     liste.heading(1, text="Öğrenci Adı")




def createPanels():
    global frame_alt_sol, frame_alt_sag, frame_alt_sag2
    canvasMain = Canvas(master, height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
    canvasMain.pack()

    frame_ust = Frame(master, bg='#8FA2CA')
    frame_ust.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.15)

    frame_alt_sol = Frame(master, bg='#8FA2CA')
    frame_alt_sol.place(relx=0.02, rely=0.2, relwidth=0.31, relheight=0.77)

    frame_alt_sag = Frame(master, bg='#8FA2CA')
    frame_alt_sag.place(relx=0.34, rely=0.2, relwidth=0.32, relheight=0.77)

    frame_alt_sag2 = Frame(master, bg='#8FA2CA')
    frame_alt_sag2.place(relx=0.68, rely=0.2, relwidth=0.30, relheight=0.77)

    school_system_etiket = Label(frame_ust, bg='#B5C6B8', text='SchoolSystem', font="Verdana 12 bold")
    school_system_etiket.pack(padx=10, pady=10, side=LEFT)


def createMenu():
    main_menu_btn = Button(frame_alt_sol, text="Main Menu", command=lambda: changeMenu(1), width=20, height=2, bg='#B5C6B8',activebackground="#eee8aa")
    main_menu_btn.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.12)

    student_menu_btn = Button(frame_alt_sol, text="Student Menu", command=lambda: changeMenu(2), width=20, height=2,  bg='#B5C6B8', activebackground="#eee8aa")
    student_menu_btn.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.12)

    exeButton3 = Button(frame_alt_sol, text="Teacher Menu", command=lambda: changeMenu(3), width=20, height=2, bg='#B5C6B8',activebackground="#eee8aa")
    exeButton3.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.12)

    exeButton4 = Button(frame_alt_sol, text="Lesson Menu", command=lambda: changeMenu(4), width=20, height=2, bg='#B5C6B8', activebackground="#eee8aa")
    exeButton4.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.12)

    main_menu_btn.bind('<Enter>', on_enter)
    main_menu_btn.bind('<Leave>', on_leave)
    student_menu_btn.bind('<Enter>', on_enter)
    student_menu_btn.bind('<Leave>', on_leave)
    exeButton3.bind('<Enter>', on_enter)
    exeButton3.bind('<Leave>', on_leave)
    exeButton4.bind('<Enter>', on_enter)
    exeButton4.bind('<Leave>', on_leave)


def changeMenu(toChange):
    if toChange == 1:
        if "main" not in submenuFrames.keys():
            print("Craetiong main")
            submenuCreator("main",subMenuMain)
        submenuFrames["main"].tkraise()
    elif toChange == 2:
        if "student" not in submenuFrames.keys():
            print("creating studentmenu")
            submenuCreator("student",subMenuStudents)
        submenuFrames["student"].tkraise()
    elif toChange == 3:
        if "teacher" not in submenuFrames.keys():
            print("Creationg teachermenu")
            submenuCreator("teacher",subMenuTeacher)
        submenuFrames["teacher"].tkraise()
    elif toChange == 4:
        if "lesson" not in submenuFrames.keys():
            print("Creationg lessonmenu")
            submenuCreator("lesson",subMenuLesson)
        submenuFrames["lesson"].tkraise()

if __name__ == "__main__":
    global schoolObj
    schoolObj = readFromFile()
    createPanels()
    createMenu()
    master.mainloop()

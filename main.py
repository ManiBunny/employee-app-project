

""""libraries used in program"""
import File_manager
import Employee_class
from tkinter import *
from tkinter import filedialog


"""constant variables"""
BUTTON_COLOR = '#FFAEC9'
BACKGROUND_COLOR= '#C8BFE7'
BUTTON_FONT= 'Arial 12 bold'
TITLE_FONT='Cambria 20 bold'


"""opening main window and initializing/constructing it"""
main_window = Tk()
main_window.title("Employee App")
main_window.geometry("440x360")
main_window.configure(bg=BACKGROUND_COLOR)

"""all gui and ui functions(buttons and labels etc.)"""


def open_add_employee():
    """when button clicked on the main window this function is called
    opens a new window with the nececery inputs to put on an employee
    and adds then to the employee txt file"""
    top = Toplevel()
    top.configure(bg=BACKGROUND_COLOR)
    id= StringVar()
    name = StringVar()
    age =StringVar()
    phone =StringVar()
    Label(top, text="Add Employee",fg='white',bg=BACKGROUND_COLOR,font=TITLE_FONT).grid(row=0, column=1)
    Label(top, text="ID: ",fg='white',bg=BACKGROUND_COLOR,font=BUTTON_FONT).grid(row=1, column=0)
    Entry(top,textvariable = id ,width=50, borderwidth=5).grid(row=1, column=1)
    Label(top, text="Name: ",fg='white',bg=BACKGROUND_COLOR,font=BUTTON_FONT).grid(row=2, column=0)
    Entry(top,textvariable = name , width=50, borderwidth=5).grid(row=2, column=1)
    Label(top, text="Age: ",fg='white',bg=BACKGROUND_COLOR,font=BUTTON_FONT).grid(row=3, column=0)
    Entry(top,textvariable = age , width=50, borderwidth=5).grid(row=3, column=1)
    Label(top, text="Phone Number: ",fg='white',bg=BACKGROUND_COLOR,font=BUTTON_FONT).grid(row=4, column=0)
    Entry(top,textvariable = phone , width=50, borderwidth=5).grid(row=4, column=1)

    def add_new():
        File_manager.add_employee(Employee_class.Employee(name.get(), id.get(), age.get(), phone.get()))
        top.destroy()
    Button(top, text="Add Employee", padx=50, pady=20, command = add_new ,fg='white',bg=BUTTON_COLOR,bd='10',font=BUTTON_FONT).grid(row=5, column=1)


def open_employee_file():
    """opens when the button clicked and there are two ways to select a file
    first is to write the name of the file on the blank space
    second is to choose from computer
    and then adds all the employees from file"""
    top = Toplevel()
    top.configure(bg=BACKGROUND_COLOR)
    file = StringVar()
    Label(top, text="Add Employees from File   ",fg='white',bg=BACKGROUND_COLOR,font=TITLE_FONT).grid(row=0, column=1)
    Label(top, text="Name of the File: ",fg='white',bg=BACKGROUND_COLOR,font=BUTTON_FONT).grid(row=1, column=0)
    Entry(top, textvariable=file, width=50, borderwidth=5).grid(row=1, column=1)
    Label(top, text="Or choose file from computer: ", fg='white', bg=BACKGROUND_COLOR, font=BUTTON_FONT).grid(row=2, column=0)

    def ask_file():
        top.filename = filedialog.askopenfilename(initialdir="/C", title="Select a file",filetypes=(("txt files", "*.txt"), ("csv files", "*.csv"),("py files", "*.py")))
        file.set(top.filename)
    Button(top, text="Choose File", command=ask_file, fg='white', bg=BUTTON_COLOR, font=BUTTON_FONT).grid(row=2, column=1)

    def add_new():
        File_manager.add_employee_file(file.get())
        top.destroy()
    Button(top, text="Add Employees", padx=50, pady=20, command= add_new,fg='white',bg=BUTTON_COLOR,bd='10',font=BUTTON_FONT).grid(row=3, column=1)


def open_delete_employee():
    """opens when the button clicked and ases the id number of the employee they wish to delete"""
    top = Toplevel()
    top.configure(bg=BACKGROUND_COLOR)
    id = StringVar()
    Label(top, text="Delete Employee using ID   ",fg='white',bg=BACKGROUND_COLOR,font=TITLE_FONT).grid(row=0, column=1)
    Label(top, text="Employee ID: ",fg='white',bg=BACKGROUND_COLOR,font=BUTTON_FONT).grid(row=1, column=0)
    Entry(top, textvariable=id, width=50, borderwidth=5).grid(row=1, column=1)

    def add_new():
        File_manager.delete_employee(id.get())
        top.destroy()

    Button(top, text="Delete Employee", padx=50, pady=20, command=add_new,fg='white',bg=BUTTON_COLOR,bd='10',font=BUTTON_FONT).grid(row=2, column=1)


def open_delete_employee_file():
    """opens when the button clicked and there are two ways to select a file
    first is to write the name of the file on the blank space
    second is to choose from computer
    and then deletes all the employees from file"""
    top = Toplevel()
    top.configure(bg=BACKGROUND_COLOR)
    file = StringVar()
    Label(top, text="Delete Employees from File   ",fg='white',bg=BACKGROUND_COLOR,font=TITLE_FONT).grid(row=0, column=1)
    Label(top, text="Name of the File: ",fg='white',bg=BACKGROUND_COLOR,font=BUTTON_FONT).grid(row=1, column=0)
    Entry(top, textvariable=file, width=50, borderwidth=5).grid(row=1, column=1)
    Label(top, text="Or choose file from computer: ", fg='white', bg=BACKGROUND_COLOR, font=BUTTON_FONT).grid(row=2,column=0)

    def ask_file():
        top.filename = filedialog.askopenfilename(initialdir="/C", title="Select a file", filetypes=(("txt files", "*.txt"), ("csv files", "*.csv"), ("py files", "*.py")))
        file.set(top.filename)

    Button(top, text="Choose File", command=ask_file, fg='white', bg=BUTTON_COLOR, font=BUTTON_FONT).grid(row=2,column=1)

    def add_new():
        File_manager.delete_employee_file(file.get())
        top.destroy()

    Button(top, text="Delete Employees", padx=50, pady=20, command=add_new,fg='white',bg=BUTTON_COLOR,bd='10',font=BUTTON_FONT).grid(row=3, column=1)


def open_attendance_mark():
    """opens when button clicked, asks the id number of the employee that attending"""
    top = Toplevel()
    top.configure(bg=BACKGROUND_COLOR)
    id = StringVar()
    Label(top, text="Mark Attendance using ID   ", fg='white', bg=BACKGROUND_COLOR, font=TITLE_FONT).grid(row=0, column=1)
    Label(top, text="Employee ID: ", fg='white', bg=BACKGROUND_COLOR, font=BUTTON_FONT).grid(row=1, column=0)
    Entry(top, textvariable=id, width=50, borderwidth=5).grid(row=1, column=1)

    def add_new():
        File_manager.attendance_check(id.get())
        top.destroy()

    Button(top, text="Mark Attendance", padx=50, pady=20, command=add_new, fg='white', bg=BUTTON_COLOR, bd='10',
           font=BUTTON_FONT).grid(row=2, column=1)


def open_attendance_report():
    """opens when button clicked and provides the attendance of the provided id of employee """
    top = Toplevel()
    top.configure(bg=BACKGROUND_COLOR)
    id = StringVar()
    Label(top, text="Attendance Report  ", fg='white', bg=BACKGROUND_COLOR, font=TITLE_FONT).grid(row=0, column=1)
    Label(top, text="Employee ID: ", fg='white', bg=BACKGROUND_COLOR, font=BUTTON_FONT).grid(row=1, column=0)
    Entry(top, textvariable=id, width=50, borderwidth=5).grid(row=1, column=1)

    def add_new():
        attended = File_manager.attendance_report(id.get())
        if (attended):
            Label(top, text=attended, fg='white', bg=BACKGROUND_COLOR, font=BUTTON_FONT).grid(row=3, column=1)
        #top.destroy()

    Button(top, text="Attendance Report", padx=50, pady=20, command=add_new, fg='white', bg=BUTTON_COLOR, bd='10',
           font=BUTTON_FONT).grid(row=2, column=1)


def open_report_month():
    """opens when button clicked and provides data of all employees that attended this month"""
    top = Toplevel()
    top.configure(bg=BACKGROUND_COLOR)

    Label(top, text="Attendance Month Report  ", fg='white', bg=BACKGROUND_COLOR, font=TITLE_FONT).grid(row=0, column=1)

    attended = File_manager.report_month()
    if (attended):
        Label(top, text=attended, fg='white', bg=BACKGROUND_COLOR, font=BUTTON_FONT).grid(row=3, column=1)


def open_late_report():
    """opens when button clicked, provides data of all employees that came late then 9:30 in the morning"""
    top = Toplevel()
    top.configure(bg=BACKGROUND_COLOR)

    Label(top, text="Report Late Employees  ", fg='white', bg=BACKGROUND_COLOR, font=TITLE_FONT).grid(row=0, column=1)

    attended = File_manager.report_late()
    if (attended):
        Label(top, text=attended, fg='white', bg=BACKGROUND_COLOR, font=BUTTON_FONT).grid(row=3, column=1)


"""the opening main window buttons and titels"""
opening_label = Label(main_window, text = "What action would you like to do?", fg='white',bd='10',bg=BACKGROUND_COLOR,font=TITLE_FONT).grid(row=0, column=0)
add_employee_button = Button(main_window, text = "Add Employee",command = open_add_employee, fg='white',bg=BUTTON_COLOR,font=BUTTON_FONT).grid(row=1, column=0)
add_employee_file_button = Button(main_window, text = "Add Employee from File", command = open_employee_file, fg='white',bg=BUTTON_COLOR,font=BUTTON_FONT).grid(row=2, column=0)
delete_employee_button = Button(main_window, text = "Delete Employee", command=open_delete_employee, fg='white',bg=BUTTON_COLOR,font=BUTTON_FONT).grid(row=3, column=0)
delete_employee_file_button = Button(main_window, text = "Delete Employees from File",command=open_delete_employee_file, fg='white',bg=BUTTON_COLOR,font=BUTTON_FONT).grid(row=4, column=0)
Label(main_window, text = "----------------------------------------------------------", fg='white',bg=BACKGROUND_COLOR,font=BUTTON_FONT).grid(row=5, column=0)
mark_attendance_button = Button(main_window, text = "Mark Attendance", command =open_attendance_mark ,fg='white',bg=BUTTON_COLOR,font=BUTTON_FONT).grid(row=6, column=0)
attendance_report_button = Button(main_window, text = "Attendance Report of an Employee",command=open_attendance_report, fg='white',bg=BUTTON_COLOR,font=BUTTON_FONT).grid(row=7, column=0)
report_month_button = Button(main_window, text = "Report of Current Month" ,command= open_report_month, fg='white',bg=BUTTON_COLOR,font=BUTTON_FONT).grid(row=8, column=0)
late_report_button = Button(main_window, text = "Late Employees Attendance Report",command= open_late_report, fg='white',bg=BUTTON_COLOR,font=BUTTON_FONT).grid(row=9, column=0)


main_window.mainloop()


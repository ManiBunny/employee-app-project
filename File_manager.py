

""""libraries used in program"""
from datetime import datetime
from tkinter import messagebox

"""constant variables"""
employee_file = "Employee.txt"
attendance_file = "Attendance_log.txt"


def id_in_file(id):
    """finds if id is in the file"""
    file_r = open(employee_file, "r")
    for line in file_r:
        if (id == line.split(",")[0]):
            messagebox.showinfo("Error!", "Theres already an identical ID.")
            file_r.close()
            return 1
    file_r.close()
    return 0


def add_employee(newEmployee):
    '''
    adds an given employee
    if theres already an employee with same id then trows exception
    '''
    try:
        id = int(newEmployee.id)
        name = str(newEmployee.name)
        age = int(newEmployee.age)
        phone = str(newEmployee.phone)
        for character in phone:
            if character < '0' or character > '9':
                raise ValueError
    except ValueError:
        messagebox.showinfo("Error!", "The ID, Age and Phone number should be numbers.")
        return
    if id_in_file(str(newEmployee.id)):
        return
    file = open(employee_file, "a")
    file.write(str(id) + ", " + name + ", " + str(age) + ", " + str(phone) + "\n")
    file.close()


def add_employee_file(file):
    '''adds employee from user file
    if there no such file then it trows an exception and asks to reenter file name'''
    try:
        file_1 = open(file, "r")
    except FileNotFoundError:
        messagebox.showinfo("Error!", "Theres no such file.")
        return
    file_2 = open(employee_file, "a")
    for employee in file_1:
        if not id_in_file(employee.split(",")[0]):
            file_2.write(employee)
    file_2.write("\n")
    file_1.close()
    file_2.close()


def delete_employee(id):
    '''given an id deletes it from the file
    this function rewrites all before the deleted item and after
    our id is always the first in line
    when id is not found it asks to renter the id'''
    with open(employee_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            if(str(id) ==line.split(",")[0]):
                break
        else:
            messagebox.showinfo("Error!", "Theres no such ID, please re-enter ID.")
            return
    with open(employee_file, "w") as f:
        for line in lines:
            if line.split(",")[0] != str(id):
                f.write(line)


def delete_employee_file(file):
    '''all given ids from file is deleted from employee file
    if there no such file then it asks to renter file name'''
    try:
        file_1 = open(file, "r")
    except FileNotFoundError:
            messagebox.showinfo("Error!", "Theres no such file.")
            return
    file_2 = open(employee_file, "a")
    for line in file_1:
        id = line.split(",")[0]
        delete_employee(id)
    file_1.close()
    file_2.close()


def attendance_check(id):
    '''askes the user for id and marking the employee in the attendance file
    if employee not found it asks to re-enter the id'''
    fileEmployee = open(employee_file, "r")
    fileAttendance = open(attendance_file, "a")
    now = datetime.now()
    found =0
    for line in fileEmployee:
        if(id == line.split(",")[0]):
            found =1
            fileAttendance.write(line + "attended in date and time: " +now.strftime("%d/%m/%Y %H:%M:%S")+ "\n")
    fileEmployee.close()
    fileAttendance.close()
    if not found:
        messagebox.showinfo("Error!", "Theres no such ID.")
        return


def attendance_report(report_id):
    '''for given employee it prints all his attendance data'''
    fileAttendance = open(attendance_file, "r")
    found =0
    report=""
    for line in fileAttendance:
        if(report_id ==line.split(",")[0]):
            found=1
            report += next(fileAttendance)
    fileAttendance.close()
    if not found:
        messagebox.showinfo("Error!", "Theres no such ID.")
    return report


def report_month():
    '''report attendance in current month '''
    now =datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    fileAttendance = open(attendance_file, "r")
    count = 0
    prev = ""
    report=""
    for line in fileAttendance:
        if (count % 2 == 0):
            prev = line.strip("\n")
        if (count%2 != 0):
            if (dt_string.split("/")[1] == line.split("/")[1]):
                report+= prev+ ": " + line
        count = count+1
    fileAttendance.close()
    if not count:
        messagebox.showinfo("Error!", "No one attended this month.")
    return report


def report_late():
    '''if employee is late then this function prints when and who was late '''
    fileAttendance = open(attendance_file, "r")
    count = 0
    prev = ""
    nine =9
    thirty =30
    report =""
    for line in fileAttendance:
        if (count % 2 == 0):
            prev = line.strip("\n")
        if (count % 2 != 0):
            hour =int(line.split(" ")[6].split(":")[0])
            minutes = int(line.split(" ")[6].split(":")[1])
            if ((hour == nine) and (minutes > thirty)) or (hour > nine):
                report+= prev+ ": " + line
        count = count + 1
    fileAttendance.close()
    if not count:
        messagebox.showinfo("Error!", "No one was late!.")
    return report

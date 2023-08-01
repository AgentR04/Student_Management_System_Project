# importing packages
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
from tkinter import messagebox, filedialog
import datetime
import mysql.connector
import tkinter as tk
import os

# database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rutu1234",
    database="studentsdb",
)

mycursor = mydb.cursor()

python_script = "student_management_system.py"

# background window
root = Tk()
root.title("Student Management System")
root.config(bg="white")
root.geometry("1350x700+200+50")
root.resizable(False, False)

# function for dynamic header
def IntroLabelTick():
    global count, text
    if count >= len(header):
        count = 0
        text = ""
        movingheader.config(text=text)
    else:
        text = text + header[count]
        movingheader.config(text=text)
        count += 1
    movingheader.after(200, IntroLabelTick)

# header
header = "Student Management System"
count = 0
text = ""
movingheader = Label(
    root,
    text=header,
    font=("Times New Roman", 30, "bold"),
    relief=RIDGE,
    borderwidth=4,
    width=25,
    bg="lightblue",
)
movingheader.place(x=350, y=0)
IntroLabelTick()

# frames for content
Frame1 = Frame(root, bg="blue", relief=GROOVE, borderwidth=8)
Frame1.place(x=10, y=80, width=500, height=600)

Frame2 = Frame(root, bg="blue", relief=GROOVE, borderwidth=8)
Frame2.place(x=520, y=80, width=800, height=600)

# functions for buttons
# search function
def searchStudent():
    keyword = searchentry.get()
    # Replace 'your_database.db' with the actual name of your SQLite database file
    # connection = sqlite3.connect('your_database.db')
    # cursor = connection.cursor()
    sql = 'SELECT * FROM personal WHERE fname = "' + keyword + '"'

    print(sql)

    root.destroy()

    os.system(f"python {python_script}")

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    # Assuming you have a table named 'your_table' with a column named 'search_column'
    # Replace 'search_column' with the actual name of the column you want to search
    # cursor.execute(f"SELECT * FROM your_table WHERE search_column LIKE '%{keyword}%'")
    # results = cursor.fetchall()
    # connection.close()

    # Clear the previous search results
    # trv.delete(*trv.get_children())

    # # Display the search results in the Treeview
    # for result in results:
    #     trv.insert('', 'end', values=result)

# add function
def addStudent():
    def submitadd():
        roll_no = entry_vars[0].get()
        name = entry_vars[1].get()
        mobile_no = entry_vars[2].get()
        email = entry_vars[3].get()
        course = entry_vars[4].get()
        gender = entry_vars[5].get()
        dob = entry_vars[6].get()

        sql = "INSERT INTO personal VALUES(%s, %s, %s, %s, %s, %s, %s)"

        val = (name, roll_no, dob, mobile_no, email, course, gender)

        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

        mycursor.execute("SELECT * FROM personal;")

        myresult = mycursor.fetchall()

        root.destroy()

        os.system(f"python {python_script}")

        print("Student added:")
        print(f"Roll No: {roll_no}")
        print(f"Name: {name}")
        print(f"Mobile No: {mobile_no}")
        print(f"Email: {email}")
        # print(f"Address: {address}")
        print(f"Gender: {gender}")
        print(f"DOB: {dob}")

    addroot = Toplevel(master=Frame2)
    addroot.grab_set()
    addroot.geometry("620x500+200+200")
    addroot.title("Student Management System")
    addroot.config(bg="white")
    addroot.resizable(False, False)

    # Labels
    labels = [
        "Enter Roll No:",
        "Enter Name:",
        "Enter Mobile No:",
        "Enter Email:",
        "Enter Course:",
        "Enter Gender:",
        "Enter DOB:",
    ]
    entry_vars = [StringVar() for _ in range(len(labels))]

    for i, label_text in enumerate(labels):
        label = Label(
            addroot,
            text=label_text,
            bg="lightblue",
            font=("Ariel", 20, "bold"),
            relief=GROOVE,
            borderwidth=3,
            width=15,
            anchor="w",
        )
        label.grid(row=i, column=0, padx=5, pady=5, sticky="w")

        entry = Entry(
            addroot, font=("Ariel", 15, "bold"), bd=5, textvariable=entry_vars[i]
        )
        entry.grid(row=i, column=1, padx=5, pady=5, sticky="e")

    # Submit Button
    submit_button = Button(
        addroot,
        text="Submit",
        font=("Ariel", 15, "bold"),
        bg="lightblue",
        activebackground="white",
        activeforeground="blue",
        command=submitadd,
    )
    submit_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

# updation function
def updateStudent():
    def submitupdate():
        roll_no = entry_vars[0].get()
        name = entry_vars[1].get()
        mobile_no = entry_vars[2].get()
        email = entry_vars[3].get()
        course = entry_vars[4].get()
        gender = entry_vars[5].get()
        dob = entry_vars[6].get()

        sql = f"UPDATE personal SET fname='{name}', roll_no={roll_no}, dob='{dob}', phone_no={mobile_no}, email='{email}', course='{course}', gender='{gender}' WHERE roll_no={roll_no}"
        print(sql)

        mycursor.execute(sql)

        mydb.commit()

        root.destroy()

        os.system(f"python {python_script}")

    addroot = Toplevel(master=Frame2)
    addroot.grab_set()
    addroot.geometry("620x500+200+200")
    addroot.title("Student Management System")
    addroot.config(bg="white")
    addroot.resizable(False, False)

    # Labels
    labels = [
        "Update Roll No:",
        "Update Name:",
        "Update Mobile No:",
        "Update Email:",
        "Update Course:",
        "Update Gender:",
        "Update DOB:",
    ]
    entry_vars = [StringVar() for _ in range(len(labels))]

    for i, label_text in enumerate(labels):
        label = Label(
            addroot,
            text=label_text,
            bg="lightblue",
            font=("Ariel", 20, "bold"),
            relief=GROOVE,
            borderwidth=3,
            width=15,
            anchor="w",
        )
        label.grid(row=i, column=0, padx=5, pady=5, sticky="w")

        entry = Entry(
            addroot, font=("Ariel", 15, "bold"), bd=5, textvariable=entry_vars[i]
        )
        entry.grid(row=i, column=1, padx=5, pady=5, sticky="e")

    # Update Button
    update_button = Button(
        addroot,
        text="Update",
        font=("Ariel", 15, "bold"),
        bg="lightblue",
        activebackground="white",
        activeforeground="blue",
        command=submitupdate,
    )
    update_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

# delete function
def deleteStudent():
    def submitdelete():
        roll_no = entry_var.get()

        print(f"Student with Roll No {roll_no} deleted.")

        sql = "Delete from personal where roll_no = " + roll_no

        mycursor.execute(sql)

        mydb.commit()

        root.destroy()

        os.system(f"python {python_script}")

    deleteroot = Toplevel(master=Frame2)
    deleteroot.grab_set()
    deleteroot.geometry("500x150+300+300")
    deleteroot.title("Delete Student")
    deleteroot.config(bg="white")
    deleteroot.resizable(False, False)

    # Labels
    label = Label(
        deleteroot,
        text="Enter Roll No:",
        bg="lightblue",
        font=("Ariel", 20, "bold"),
        relief=GROOVE,
        borderwidth=3,
        width=15,
        anchor="w",
    )
    label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    entry_var = StringVar()
    entry = Entry(
        deleteroot, font=("Ariel", 15, "bold"), bd=5, width=10, textvariable=entry_var
    )

    entry.grid(row=0, column=1, padx=5, pady=5, sticky="e")

    # Delete Button
    delete_button = Button(
        deleteroot,
        text="Delete",
        font=("Ariel", 15, "bold"),
        bg="red",
        fg="white",
        command=submitdelete,
    )
    delete_button.grid(row=1, column=0, columnspan=2, pady=10)


# export function
def exportStudent():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV File", "*.csv")],
        initialdir="/",
        title="Export Data",
    )
    if file_path:
        with open(file_path, "w") as f:
            headers = ["Name", "Roll No", "Time", "Phone No.", "Email", "Class", "Gender"]
            f.write(",".join(headers) + "\n")
            for item in trv.get_children():
                values = trv.item(item)["values"]
                f.write(",".join(map(str, values)) + "\n")
     
# exit function
def exit():
    res = messagebox.askyesnocancel("notification", "Do you want to EXIT?")
    if res == True:
        root.destroy()

# buttons in frame 1
add = Button(
    Frame1,
    text="1. ADD STUDENT",
    width=20,
    font=("Times New Roman", 18, "bold"),
    bd=0,
    bg="lightblue",
    activebackground="skyblue",
    relief=RIDGE,
    activeforeground="white",
    command=addStudent,
)
add.pack(side=TOP, expand=True)

update = Button(
    Frame1,
    text="2. UPDATE STUDENT",
    width=20,
    font=("Times New Roman", 18, "bold"),
    bd=0,
    bg="lightblue",
    activebackground="skyblue",
    relief=RIDGE,
    activeforeground="white",
    command=updateStudent,
)
update.pack(side=TOP, expand=True)

delete = Button(
    Frame1,
    text="3. DELETE STUDENT",
    width=20,
    font=("Times New Roman", 18, "bold"),
    bd=0,
    bg="lightblue",
    activebackground="skyblue",
    relief=RIDGE,
    activeforeground="white",
    command=deleteStudent,
)
delete.pack(side=TOP, expand=True)

export = Button(
    Frame1,
    text="5. EXPORT DATA",
    width=20,
    font=("Times New Roman", 18, "bold"),
    bd=0,
    bg="lightblue",
    activebackground="skyblue",
    relief=RIDGE,
    activeforeground="white",
    command=exportStudent
)
export.pack(side=TOP, expand=True)

exit = Button(
    Frame1,
    text="6. EXIT",
    width=20,
    font=("Times New Roman", 18, "bold"),
    bd=0,
    bg="lightblue",
    activebackground="skyblue",
    relief=RIDGE,
    activeforeground="white",
    command=exit,
)
exit.pack(side=TOP, expand=True)

# search button and entry in frame 2
search = Frame(Frame2, bg="white", bd=10, relief=GROOVE, width=50)
search.pack(side=TOP, fill=X)

searchentry = Entry(search, text="Search Item", font=("Ariel", 14), width=40)
searchentry.grid(row=0, column=1, padx=10, pady=2)

searchbutton = Button(
    search,
    text="SEARCH",
    font=("Times New Roman", 13),
    bd=9,
    width=14,
    bg="lightblue",
    command=searchStudent,
)
searchbutton.grid(row=0, column=2, padx=10, pady=2)

# Display window

scroll_y = Scrollbar(Frame2, orient=VERTICAL)
scroll_x = Scrollbar(Frame2, orient=HORIZONTAL)

mycursor.execute("""SELECT * FROM personal;""")

myresult = mycursor.fetchall()

# print(myresult)
mydb.commit()

trv = ttk.Treeview(
    root,
    selectmode="browse",
    height=290
)

trv.grid(row=1, column=1, padx=530, pady=180)

trv["columns"] = ("1", "2", "3", "4", "5", "6", "7")

trv["show"] = "headings"

trv.column("1", width=111, anchor="c")
trv.column("3", width=111, anchor="c")
trv.column("4", width=111, anchor="c")
trv.column("5", width=111, anchor="c")
trv.column("6", width=111, anchor="c")
trv.column("2", width=111, anchor="c")
trv.column("7", width=111, anchor="c")

trv.heading("1", text="Name")
trv.heading("2", text="Roll No")
trv.heading("3", text="Time")
trv.heading("4", text="Phone No.")
trv.heading("5", text="Email")
trv.heading("6", text="Class")
trv.heading("7", text="Gender")

for dt in myresult:
    trv.insert(
        "",
        "end",
        iid=dt[0],
        values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6]),
    )

root.mainloop()
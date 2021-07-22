from tkinter import *
root = Tk()

root.geometry("655x333")

def get_value():
    with open("file/entries", "a") as data:
        data.write("\n\nName: " + str(name.get()))
        data.write("\nAge: " + str(age.get()))
        data.write("\nContact Number: " + str(con.get()))
        data.write("\nGuardian Name: " + str(guardian.get()))
        data.write("\nSelected Language: " + str(language.get()))
    pass

message = Label(root, text="Welcome to Jay Coding Classes", bg="black", fg="white", width=200, font="Consolas 12 bold")
message.pack(fill=X)

enter = Label(root, text="Enter the below form to join the Coding Classes", bg="yellow", fg="black", width=50, font="Consolas 10 bold")
enter.pack(pady=20)

# pack

user = Label(root, text="Name")
password = Label(root, text="Age")
lang = Label(root, text="Language")
contact = Label(root, text="Contact No.")
guardian_name = Label(root, text="Guardian Name")

name = StringVar()
age = StringVar()
language = StringVar()
con = StringVar()
guardian = StringVar()

name_entry = Entry(root, textvariable=name)
age_entry = Entry(root, textvariable=age)
contact_entry = Entry(root, textvariable=con)
guardian_entry = Entry(root, textvariable=guardian)
language_entry = Entry(root, textvariable=language)

# Name
user.pack()
name_entry.pack()
# Age
password.pack()
age_entry.pack()
# Contact
contact.pack()
contact_entry.pack()
# Guardian Name
guardian_name.pack()
guardian_entry.pack()
# Language
lang.pack()
language_entry.pack()

Button(text="Submit", command=get_value, padx=20).pack(pady=10)
# Button(text="End", command=Tk.destroy(root), padx=20).pack(pady=10)


root.mainloop()

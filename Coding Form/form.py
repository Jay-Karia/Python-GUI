from tkinter import *
root = Tk()

root.geometry("655x333")

def get_value():
    with open("file/entries", "a") as data:
        data.write("\n\nName: " + str(name.get()))
        data.write("\nAge: " + str(age.get()))
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

name = StringVar()
age = StringVar()
language = StringVar()

name_entry = Entry(root, textvariable=name)
age_entry = Entry(root, textvariable=age)
language_entry = Entry(root, textvariable=language)

user.pack()
name_entry.pack()
password.pack()
age_entry.pack()
lang.pack()
language_entry.pack()

Button(text="Submit", command=get_value, padx=20).pack(pady=10)
# Button(text="End", command=Tk.destroy(root), padx=20).pack(pady=10)


root.mainloop()

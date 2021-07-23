from tkinter import *
root = Tk()

# Set Title
root.title("Window Resizer")

height = "353"
width = "855"

# Method
def resize(event):
    try:
        print(f"Reset Height: {H.get()}")
        print(f"Reset Width: {W.get()}")
        global height
        height = H.get()
        print(height)
        root.geometry(f"{W.get()}x{H.get()}")
    except:
        print("\nAn Error Occurred!")
    H.set("")
    W.set("")

# Set Height and Width of the Window
root.geometry(f"{width}x{height}")

# Display the Dimensions
# display = Label(root, text="Current Dimensions of the Window is\nHeight: " + H.get() + "\nWidth: " + W.get(), bg="yellow",  font="Consolas 15 bold")
# display.pack(pady=20)

# Intro of the GUI
intro = Label(root, text="Welcome to Tkinter Window Resizer Developed -- By Jay", bg="black", fg="white", font="Consolas 20 bold")
intro.pack(fill=X)

# Display "Set the Height"
w = Label(root, text="Set Width", bg="orange",  font="Consolas 15 bold")

# Display "Set the Width"
h = Label(root, text="Set Height", bg="orange",  font="Consolas 15 bold")

# Create Variables
H = StringVar()
W = StringVar()

# Create Entries
h_entry = Entry(textvariable=H)
w_entry = Entry(textvariable=W)

# Pack Entries and Displays
h.pack()
h_entry.pack(pady=5)
w.pack()
w_entry.pack(pady=5)

# Create a Button "Apply"
apply = Button(text="Apply",  font="Consolas 10 bold", bg="red")
apply.bind('<Button-1>', resize)
apply.pack()

# Create a Button "Quit"
apply = Button(text="Quit",  font="Consolas 10 bold", bg="blue")
apply.bind('<Button-1>', quit)
apply.pack(pady=10)

root.mainloop()

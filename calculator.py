import webbrowser
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# create object tkinter
root = Tk()
root.title("Calculator")
root.resizable(width=False, height=False)


# logics calculator
def calc(key):
    global memory
    if key == "=":
        # don't write word
        str1 = "-+0123456789.*/%@"
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "First number not number!")
            messagebox.showerror("Error", "You enter not number")

        # try data
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.delete(0, END)

            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Don't true data")

    # brush enter
    elif key == "C":
        calc_entry.delete(0, END)

    # github code
    elif key == "@":
        webbrowser.open('http://example.com')

    # change + and -
    elif key == "-/+":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)

        calc_entry.insert(END, key)


# create buttons
btn_list = [
    "7", "8", "9", "+", "-",
    "4", "5", "6", "*", "/",
    "1", "2", "3", "-/+", "=",
    "0", ".", "C", "%", "@",
]
r = 1
c = 0

for i in btn_list:
    rel = ""
    cmd = lambda x=i: calc(x)
    ttk.Button(root, text=i, command=cmd).grid(row=r, column=c)
    c += 1
    if c > 4:
        c = 0
        r += 1

calc_entry = Entry(root, width=62)
calc_entry.grid(row=0, column=0, columnspan=5)

# create window
root.mainloop()

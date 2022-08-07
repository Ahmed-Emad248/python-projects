import sqlite3
from tkinter import *
from tkinter import messagebox, ttk
from random import choice, shuffle, randint

# ---------------------------- connect DB ------------------------------- #
connect = sqlite3.connect("PasswordGenerator")
create_sql = "CREATE TABLE IF NOT EXISTS password(website text not null,email text not null,password text not null)"
cursor = connect.cursor()
cursor.execute(create_sql)
connect.commit()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    passowrd_letters = [choice(letters) for _ in range(randint(4, 6))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_numbers + passowrd_letters

    shuffle(password_list)
    password = "".join(password_list)
    # print(f"Your password is: {password}")
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD to DB ------------------------------- #
def save():
    global website_entry
    global email_entry
    global password_entry

    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showwarning(title="Empty fileds", message="please don't leave any field empty!!!!!")
    else:
        is_ok = messagebox.askyesnocancel(title="save password",
                                          message=f"ara you sure to save? \n your website is {website_entry.get()} \n,Email is: {email_entry.get()} \n , and your password is: {password_entry.get()}")
        if is_ok:
            cursor.execute("INSERT INTO password VALUES (?,?,?)",
                           (website_entry.get(), email_entry.get(), password_entry.get()))
            connect.commit()
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            email_entry.delete(0, 'end')


# ------------------------------------------------------------------------------------------#
# ---------------------------------show records from DB-------------------------------------#
def show():
    show_window = Tk()
    show_window.title("your passwords")
    show_window.minsize(500, 400)

    show_sql = cursor.execute("SELECT * FROM password")
    columns = ("website", "email", "password")
    show_label = ttk.Treeview(show_window, columns=columns, show="headings")
    i = 0
    for passwords in show_sql:
        for column in columns:
            show_label.heading(column, text=column)
            show_label.grid(row=1, column=0, columnspan=3)
        show_label.insert('', 'end', values=(passwords))
    i += 1

    show_window.mainloop()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("password generator")
# window.minsize(400,250)
window.config(padx=30, pady=30)
# ---------------------------------------------------#

# -------------------logo----------------------------#
canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=2, row=0)
# ----------------------website name Label & Entry--------#
website_label = Label(text="website:", font=("arial", 16))
website_label.grid(column=1, row=1)

website_entry = Entry(width=40, font=("arial", 12))
website_entry.grid(column=2, row=1, columnspan=2)
website_entry.focus()
# ----------------email Label & Entry----------------------#
email_label = Label(text="Email:", font=("arial", 16))
email_label.grid(column=1, row=2)

email_entry = Entry(width=40, font=("arial", 12))
email_entry.grid(column=2, row=2, columnspan=2)
# --------------------password Label & generator & generate button------------#
password_label = Label(text="Password:", font=("arial", 16))
password_label.grid(column=1, row=3)

password_entry = Entry(width=21, font=("arial", 12))
password_entry.grid(column=2, row=3)

generate_button = Button(text="Generate Password", command=generate_password, font=("arial", 12, "italic"))
generate_button.grid(column=3, row=3)
# -------------------------------------save button---------------------------#
save_button = Button(text="save password", command=save, width=35, font=("arial", 14, "italic"))
save_button.grid(column=2, row=4, columnspan=2)

# ------------------------------------show passwords----------------------------#
show_button = Button(text="show passwords", command=show, width=35, font=("arial", 14, "italic"))
show_button.grid(column=2, row=5, columnspan=2)

window.mainloop()

cursor.close()

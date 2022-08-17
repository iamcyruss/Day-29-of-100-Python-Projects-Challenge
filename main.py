from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)
    password_char = ""
    for char in password_list:
        password_char += char
    password_entry.delete(0, END)
    password_entry.insert(END, string=password_char)
    pyperclip.copy(password_char)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_info():
    website, email, password = website_entry.get(), email_user_entry.get(), password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(message="One of the entries is blank and it cannot be blank. \nPlease try again.")
    elif len(website) > 0 and len(email) > 0 and len(password) > 0:
        save_check = messagebox.askyesno(message=f"Are you sure you want to add?\nWebsite: {website}\nEmail: "
                                                 f"{email}\nPassword: {password}",
                                         icon='question', title='Install')
        if save_check:
            with open('passwords.txt', 'a') as f:
                f.write(f"{website} | {email} | {password}\n")
                reset()
        else:
            pass
    else:
        pass


def reset():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

image = PhotoImage(file="logo.png")
# this stupid line above is what is needed to add an image to the canvas
canvas = Canvas(width=200, height=200)
# below you can not enter the path of the image. it would make toooo much sense for that
# instead you have to do something stupid which is the above
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)
website_entry = Entry(width=44)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_user = Label(text="Email/Username:")
email_user.grid(column=0, row=2)
email_user_entry = Entry(width=44)
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(END, string="russnicosia@gmail.com")
password = Label(text="Password:")
password.grid(column=0, row=3)
password_entry = Entry(width=25)
password_entry.grid(column=1, row=3)
passwords_button = Button(text="Generate Password", command=generate_password)
passwords_button.grid(column=2, row=3)
add_button = Button(text="Add", width=32, command=save_info)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()

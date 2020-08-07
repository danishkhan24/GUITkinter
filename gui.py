from tkinter import *
from PIL import Image, ImageTk

global y_var, m_var, d_var, h_var, min_var
y_var = 2030
m_var = 1
d_var = 0
h_var = 0
min_var = 0


def increment_year():
    global y_var
    if y_var < 2030:
        y_var += 1
    year.config(text=y_var)


def decrement_year():
    global y_var
    if y_var > 2020:
        y_var -= 1
    year.config(text=y_var)


def increment_month():
    global m_var
    if m_var < 12:
        m_var += 1
    month.config(text=m_var)


def decrement_month():
    global m_var
    if m_var > 1:
        m_var -= 1
    month.config(text=m_var)


def increment_day():
    global d_var
    d_var += 1
    day.config(text=d_var)


def decrement_day():
    global d_var
    if d_var > 0:
        d_var -= 1
    day.config(text=d_var)


def increment_hour():
    global h_var
    if h_var < 23:
        h_var += 1
    hour.config(text=h_var)


def decrement_hour():
    global h_var
    if h_var > 0:
        h_var -= 1
    hour.config(text=h_var)


def increment_min():
    global min_var
    min_var += 1
    minute.config(text=min_var)


def decrement_min():
    global min_var
    if min_var > 0:
        min_var += 1
    minute.config(text=min_var)


def update():
    # TODO
    print("This one is left for You Sir! 😃")


tk = Tk()
tk.title("Set Time")
tk.geometry("700x300")
tk.resizable(0, 0)

# Header
head = Label(tk, text="Set Time", width=9, height=1, font=("Courier", 25))
head.grid(row=0, column=2, columnspan=2)

# Load Images
# Increment Image
up_image = Image.open("up.png")
up_image = up_image.resize((110, 70), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(up_image)

# Decrement Image
down_image = Image.open("down.png")
down_image = down_image.resize((110, 70), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(down_image)

# Update/Set Image
update_image = Image.open("update.png")
update_image = update_image.resize((110, 70), Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(update_image)

# Labels
year = Label(tk, text=y_var, relief=RAISED, width=5, height=2, font=("Courier", 20))
month = Label(tk, text=m_var, relief=RAISED, width=2, height=1, font=("Courier", 50))
day = Label(tk, text=d_var, relief=RAISED, width=2, height=1, font=("Courier", 50))
hour = Label(tk, text=h_var, relief=RAISED, width=2, height=1, font=("Courier", 50))
minute = Label(tk, text=min_var, relief=RAISED, width=2, height=1, font=("Courier", 50))

year.grid(row=2, column=0, pady=2)
month.grid(row=2, column=1, pady=2)
day.grid(row=2, column=2, pady=2)
hour.grid(row=2, column=3, pady=2)
minute.grid(row=2, column=4, pady=2)

# increment buttons
year_btn = Button(tk, image=photo, command=increment_year)
month_btn = Button(tk, image=photo, command=increment_month)
day_btn = Button(tk, image=photo, command=increment_day)
hour_btn = Button(tk, image=photo, command=increment_hour)
min_btn = Button(tk, image=photo, command=increment_min)
set_btn = Button(tk, image=photo3, command=update)

year_btn.grid(row=1, column=0, sticky=W, pady=2)
month_btn.grid(row=1, column=1, sticky=W, pady=2)
day_btn.grid(row=1, column=2, sticky=W, pady=2)
hour_btn.grid(row=1, column=3, sticky=W, pady=2)
min_btn.grid(row=1, column=4, sticky=W, pady=2)
set_btn.grid(row=3, column=5, sticky=W, pady=2)

# decrement buttons
year_btn_down = Button(tk, image=photo2, command=decrement_year)
month_btn_down = Button(tk, image=photo2, command=decrement_month)
day_btn_down = Button(tk, image=photo2, command=decrement_day())
hour_btn_down = Button(tk, image=photo2, command=decrement_hour)
min_btn_down = Button(tk, image=photo2, command=decrement_min)

year_btn_down.grid(row=3, column=0, sticky=W, pady=2)
month_btn_down.grid(row=3, column=1, sticky=W, pady=2)
day_btn_down.grid(row=3, column=2, sticky=W, pady=2)
hour_btn_down.grid(row=3, column=3, sticky=W, pady=2)
min_btn_down.grid(row=3, column=4, sticky=W, pady=2)

tk.mainloop()

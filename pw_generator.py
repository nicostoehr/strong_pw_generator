def main() -> None:
    from tkinter import Tk, Label, Checkbutton, IntVar, BooleanVar, Spinbox, Entry, Button
    from helper import gen_pw

    mw = Tk()
    mw.title("Password generator")
    mw.geometry('265x240')
    font_main = ("Helvetica", 16)

    # Generation Settings
    pw_length = IntVar(value=12)
    pw_cap = BooleanVar(value=True)
    pw_num = BooleanVar(value=True)
    pw_sym = BooleanVar(value=True)

    # Functions
    def gen_pw_internal() -> None:
        pw = gen_pw(int(pw_length.get()), pw_cap.get(), pw_num.get(), pw_sym.get())

        # Entry field output
        e1.configure(state="normal")
        e1.delete(0, "end")
        e1.insert(0, pw)
        e1.configure(state="readonly")

    # Widget Inits
    l1 = Label(mw, text="Password length:", font=font_main)
    l2 = Label(mw, text="Capital letters:", font=font_main)
    l3 = Label(mw, text="Numbers:", font=font_main)
    l4 = Label(mw, text="Symbols:", font=font_main)

    sb1 = Spinbox(mw, from_=4, to=18, width=4, font=font_main, textvariable=pw_length) 

    cb1 = Checkbutton(mw, variable=pw_cap, onvalue=True, offvalue=False)
    cb2 = Checkbutton(mw, variable=pw_num, onvalue=True, offvalue=False)
    cb3 = Checkbutton(mw, variable=pw_sym, onvalue=True, offvalue=False)
    cb1.select(), cb2.select(), cb3.select()

    b1 = Button(mw, text="Generate Password", font=font_main, command=gen_pw_internal)

    e1 = Entry(mw, font=font_main, state="readonly", justify="center")


    # Widget positioning
    l1.place(x=10, y=10)
    l2.place(x=35, y=40)
    l3.place(x=82, y=70)
    l4.place(x=85, y=100)

    sb1.place(x=180, y=12)

    cb1.place(x=180, y=44)
    cb2.place(x=180, y=74)
    cb3.place(x=180, y=104)

    b1.place(x=30, y=140)

    e1.place(x=10, y=200)


    # Mainloop
    mw.mainloop()
if __name__ == "__main__": main()
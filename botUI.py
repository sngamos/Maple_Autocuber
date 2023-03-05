from tkinter import*

OPTIONS = ["Bossing Potentials","Drop Rate Potentials"]
root = Tk()
root.title("Familiar Cubing Bot")
root.geometry('400x400')
empty_space = Label(root, text = "          ")
line_1_label = Label(root, text= "Choose 1st Line:").grid(row=0,column=0)
line_2_label = Label(root, text= "Choose 2nd Line:").grid(row=1,column=0)
empty_space = Label(root, text = "          ").grid(row=0,column=2)
empty_space = Label(root, text = "          ").grid(row=1,column=2)
line_1_var = StringVar()
line_2_var = StringVar()


def apply():
    line_1_dropdown.configure(state='disable')

    first_line_label= Label(root,text ="1st Line selected:").grid(row=0, column=0)
    second_line_label = Label(root,text ="2nd Line selected:").grid(row=1, column=0)
line_1_dropdown = OptionMenu(root, line_1_var, *OPTIONS).grid(row=0,column=3)
line_2_dropdown = OptionMenu(root, line_2_var, *OPTIONS).grid(row=1,column=3)

Apply_selections = Button(root, text="Apply Selection",command=apply).grid(row=5,column=0)
root.mainloop()





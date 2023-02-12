from tkinter import *
from tkinter import messagebox
import string
from random import *
import webbrowser

def generate_code():
	all_chars = string.digits
	pass_code = "".join(choice(all_chars) for x in range(14))
	code_entry.delete(0, END)
	code_entry.insert(0, pass_code)

def insta_dev():
	webbrowser.open_new('https://www.instagram.com/h4ck3rm4n04/?next=%2F')

def message_error():
	messagebox.showinfo('Erreur', "Votre machine va exploser dans exactement 5 minutes il est recommandé d'éteindre votre ordinateur pendant une journée")
		


fenetre = Tk()

fenetre.geometry('1080x720')
fenetre.minsize(300, 300)
fenetre.config(background = '#002d50')
fenetre.iconbitmap('téléchargement.ico')
fenetre.title('GCC')

frame_1 = Frame(fenetre, bg = '#002d50')

#insertion d'une deuxième image
w = 500
h = 250
deux_image = PhotoImage(file = '480537.png').zoom(3).subsample(5)
deux_canvas = Canvas(fenetre, width = w, height = h, bg = '#002d50', bd = 0, highlightthickness = 0)
deux_canvas.create_image(w/2, h/2, image = deux_image)
deux_canvas.pack()


#insertion d'une image

width = 300
height = 300
prem_image = PhotoImage(file = '480537.png').zoom(5).subsample(15)
prem_canvas = Canvas(frame_1, width = width, height = height, bg = '#002d50', bd = 0, highlightthickness = 0)
prem_canvas.create_image(width/2, height/2, image = prem_image)
prem_canvas.grid(row = 0, column = 0, sticky = W)


#sous boîte
right_frame = Frame(frame_1, bg = '#002d50')

#création d'un premier titre

titre_1 = Label(right_frame, text = 'Générateur de code de crédit', font = ('CommercialScript BT', 30), bg = '#002d50', fg = 'white')
titre_1.pack()


#création de l'entrée de l'user
code_entry = Entry(right_frame, font = ('Arial', 30), bg = '#002d50', fg = 'white')
code_entry.pack()

#création d'un bouton de génération

button = Button(right_frame, text = 'GENERATE', font =('MD thaitype A', 20), bg = '#002d50', fg = 'white', command = generate_code)
button.pack(fill = X)


right_frame.grid(row = 0, column = 1, sticky = W)
frame_1.pack(expand = YES)

button_error = Button(fenetre, text = "Don't click", font = ('Old English Text MT', 25), bg = '#002d50',fg = 'red',bd = 1, highlightthickness = 0, command = message_error)
button_error.pack(side = RIGHT)

#création d'une barre de menu

menu_bar = Menu(fenetre)
#créer un premier menu

file_menu = Menu(menu_bar, tearoff = 0)
file_menu.add_command(label = 'Nouveau code', command = generate_code)
file_menu.add_command(label = 'Follow developper', command = insta_dev)
file_menu.add_command(label = 'Alt f4', command = fenetre.quit)
menu_bar.add_cascade(label = 'Menu', menu = file_menu)
fenetre.config(menu = menu_bar)



fenetre.mainloop()
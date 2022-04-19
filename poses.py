	# -*- encoding: UTF-8 -*-
from telnetlib import IP
from Tkinter import *
from naoqi import ALProxy
import unicodedata


root = Tk()
# Mesures de la interficia grafica del equip
root.geometry("300x300")
# Nom del programa
root.title(" NAO - Poses ")

l = Label(text = "Tria la pose d'en NAO")
p1 = Button(root, height = 2,
				width = 20,
				text = "Pose 1")

				
p2 = Button(root, height = 2,
				width = 20,
				text ="Pose 2")

p3 = Button(root, height = 2,
				width = 20,
				text = "Pose 3")
p4 = Button(root, height = 2,
				width = 20,
				text ="Pose 4")

p5 = Button(root, height = 2,
				width = 20,
				text ="Pose 5")

tr = Button(root, height = 2,
				width = 20,
				text ="Tornar inici")


l.pack()
p1.pack()
p2.pack()
p3.pack()
p4.pack()
p5.pack()
tr.pack()

mainloop()

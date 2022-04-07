from telnetlib import IP
from tkinter import *


root = Tk()
# Mesures de la interficia grafica del equip
root.geometry("300x300")
# Nom del programa
root.title(" NAO - INS PLA DE L'ESTANY ")

def Take_input():
	IP = inputtxt.get("1.0", "end-1c")
	print(IP)   
    


	
l = Label(text = "INDICA LA IP DEL ROBOT NAO")
iptxt = Text(root, height = 1,
				width = 25,
				bg = "light yellow")

mv = Label(text = "MOVIMENTS")
bracdret = Button(root, height = 2,
				width = 20,
				text ="AIXECAR EL BRAC",
				command = lambda:Take_input())

prl = Label(text = "Indica que vols que digui el robot")
inputtxt = Text(root, height = 1,
				width = 25,
				bg = "light green")
parla = Button(root, height = 2,
				width = 20,
				text ="parla",
				command = lambda:Take_input())

l.pack()
iptxt.pack()
mv.pack()
bracdret.pack()
prl.pack()
inputtxt.pack()
parla.pack()

mainloop()

from telnetlib import IP
from tkinter import *
from netaddr import IPNetwork, IPAddress 


root = Tk()
# Mesures de la interficia grafica del equip
root.geometry("300x300")
# Nom del programa
root.title(" NAO - INS PLA DE L'ESTANY ")

def Take_input():
	IP = inputtxt.get("1.0", "end-1c")
	print(IP)   
    


	
l = Label(text = "INDICA LA IP DEL ROBOT NAO")
inputtxt = Text(root, height = 1,
				width = 25,
				bg = "light yellow")


Display = Button(root, height = 2,
				width = 20,
				text ="AIXECAR EL BRAÇ",
				command = lambda:Take_input())

l.pack()
inputtxt.pack()
Display.pack()

mainloop()

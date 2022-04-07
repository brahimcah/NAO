from telnetlib import IP
from Tkinter import *
from naoqi import ALProxy
import unicodedata


root = Tk()
# Mesures de la interficia grafica del equip
root.geometry("300x300")
# Nom del programa
root.title(" NAO - INS PLA DE L'ESTANY ")





def Xarxa():
    IP = iptxt.get("1.0","end-1c")
    return IP

def Parlar():
    #IP = iptxt.get("1.0", "end-1c")
	l = Xarxa()
	ls = l.encode('ascii','replsce')
	print(type(ls))
	print(ls)
	tts = ALProxy("ALTextToSpeech",ls, 9559)
	
	txt = inputtxt.get("1.0", "end-1c")
	strtxt = txt.encode('ascii','replsce')
	tts.say(strtxt)
    


	
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
				command = lambda:[Parlar(),Xarxa()])


l.pack()
iptxt.pack()
mv.pack()
bracdret.pack()
prl.pack()
inputtxt.pack()
parla.pack()

mainloop()

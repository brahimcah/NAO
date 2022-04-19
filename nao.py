	# -*- encoding: UTF-8 -*-
from telnetlib import IP
from Tkinter import *
from naoqi import ALProxy
import unicodedata


root = Tk()
# Mesures de la interficia grafica del equip
root.geometry("300x600")
# Nom del programa
root.title(" NAO - INS PLA DE L'ESTANY ")





def Xarxa():
    IP = iptxt.get("1.0","end-1c")
    return IP

def Parlar():
    
	txt = inputtxt.get("1.0", "end-1c")
	strtxt = txt.encode('ascii','replsce')

	ip = iptxt.get("1.0", "end-1c")
	with open('.\data\ip.txt', 'w') as f:
		f.write(ip)
	with open('.\data\stext.txt', 'w') as f:
		f.write(txt)
	execfile(".\_talk\parlar.py")
    

def Japan():
	ip = iptxt.get("1.0", "end-1c")
	with open('.\data\ip.txt', 'w') as f:
		f.write(ip)
	execfile("prova.py")
	



l = Label(text = "INDICA LA IP DEL ROBOT NAO")
iptxt = Text(root, height = 1,
				width = 25,
				bg = "light yellow")

				
##from naoqi import ALProxy
##tts = ALProxy("ALTextToSpeech", "172.16.251.86", 9559)
##tts.say("hola a tots!")
##tts.setLanguage("Japanese")
##tts.say("こんにちは")

mv = Label(text = "MOVIMENTS")
bracdret = Button(root, height = 2,
				width = 20,
				text ="AIXECAR EL BRAC",
				command = lambda:equilibri())

prl = Label(text = "Indica que vols que digui el robot")
inputtxt = Text(root, height = 1,
				width = 25,
				bg = "light green")
parla = Button(root, height = 2,
				width = 20,
				text ="parla",
				command = lambda:[Parlar(),Xarxa()])

prlJpn = Button(root, height = 2,
				width = 20,
				text ="Parlar amb Japones",
				command = lambda:Japan())


l.pack()
iptxt.pack()
mv.pack()
bracdret.pack()
prl.pack()
inputtxt.pack()
parla.pack()
prlJpn.pack()

mainloop()

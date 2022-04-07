from telnetlib import IP
from tkinter import *
from naoqi import ALProxy



root = Tk()
# Mesures de la interficia grafica del equip
root.geometry("300x300")
# Nom del programa
root.title(" NAO - INS PLA DE L'ESTANY ")

def Take_input():
	IP = inputtxt.get("1.0", "end-1c")
	print(IP)   

def Parlar():
    IP = iptxt.get("1.0", "end-1c")
    txt = inputtxt.get("1.0", "end-1c")
	print(IP)   
    motion = ALProxy("ALMotion", IP , 9559)
    tts    = ALProxy("ALTextToSpeech", IP, 9559)
    motion.moveInit()
    motion.post.moveTo(0.5, 0, 0)
    tts.say("I'm walking")


	
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
				command = lambda:Parlar())

l.pack()
iptxt.pack()
mv.pack()
bracdret.pack()
prl.pack()
inputtxt.pack()
parla.pack()

mainloop()

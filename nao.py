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
	execfile(".\_pose\pos_sentat.py")
	


def equilibri():

	"""Example: Whole Body Motion - Enable Balance Constraint"""

	import qi
	import argparse
	import sys
	import math


	def main(session):
		"""
		Example of a whole body Enable Balance Constraint.
		Warning: Needs a PoseInit before executing.
			Whole body balancer must be deactivated at the end of the script.
		This example is only compatible with NAO.
		"""
		# Get the services ALMotion & ALRobotPosture.

		motion_service = session.service("ALMotion")
		posture_service = session.service("ALRobotPosture")

		# Wake up robot
		motion_service.wakeUp()

		# Send robot to Stand Init
		posture_service.goToPosture("StandInit", 0.5)

		# Activate Whole Body Balancer
		isEnabled  = True
		motion_service.wbEnable(isEnabled)

		# Legs are constrained in a plane
		stateName  = "Fixed"
		supportLeg = "Legs"
		motion_service.wbFootState(stateName, supportLeg)

		# Constraint Balance Motion
		isEnable   = True
		supportLeg = "Legs"
		motion_service.wbEnableBalanceConstraint(isEnable, supportLeg)

		# KneePitch angleInterpolation
		# Without Whole Body balancer, foot will fall down
		names      = ["LKneePitch", "RKneePitch"]
		angleLists = [ [0.0, 40.0*math.pi/180.0], [0.0, 40.0*math.pi/180.0]]
		timeLists  = [ [5.0, 10.0], [5.0, 10.0]]
		isAbsolute = True
		try:
			motion_service.angleInterpolation(names, angleLists, timeLists, isAbsolute)
		except Exception.errorMsg:
			print (str(errorMsg))
			print ("This example is not allowed on this robot.")
			exit()

		# Deactivate Whole Body Balancer
		isEnabled  = False
		motion_service.wbEnable(isEnabled)

		# Go to rest position
		motion_service.rest()


	if __name__ == "__main__":
		parser = argparse.ArgumentParser()
		parser.add_argument("--ip", type=str, default="172.16.252.90",
							help="Robot IP address. On robot or Local Naoqi: use '172.16.252.90'.")
		parser.add_argument("--port", type=int, default=9559,
							help="Naoqi port number")

		args = parser.parse_args()
		session = qi.Session()
		try:
			session.connect("tcp://" + args.ip + ":" + str(args.port))
		except RuntimeError:
			print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
				"Please check your script arguments. Run with -h option for help.")
			sys.exit(1)
		main(session)



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

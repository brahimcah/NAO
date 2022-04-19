# -*- encoding: UTF-8 -*-
from naoqi import ALProxy
fitxer = open('ip.txt')
l = fitxer.readline()
ls = l.encode('ascii','replsce')
print(type(ls))

tts = ALProxy("ALTextToSpeech", ls , 9559)
tts.say("hola a tots!")
tts.setLanguage("Japanese")
tts.say("こんにちは")
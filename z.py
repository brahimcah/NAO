# -*- encoding: UTF-8 -*-
from naoqi import ALProxy
fitxer = open('.\data\ip.txt')
l = fitxer.readline()
ls = l.encode('ascii','replsce')

tts = ALProxy("ALTextToSpeech", ls , 9559)
tts.say("hola a tots!")
tts.setLanguage("Japanese")
tts.say("こんにちは")
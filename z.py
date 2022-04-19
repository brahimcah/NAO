# -*- encoding: UTF-8 -*-
from naoqi import ALProxy
l = open('hola.txt')
print(type(l))

ls = l.encode('ascii','replsce')
print(type(ls))

tts = ALProxy("ALTextToSpeech", ls , 9559)
tts.say("hola a tots!")
tts.setLanguage("Japanese")
tts.say("こんにちは")
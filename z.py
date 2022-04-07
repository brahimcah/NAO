# -*- encoding: UTF-8 -*-
from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "172.16.252.90", 9559)
tts.say("hola a tots!")
tts.setLanguage("Japanese")
tts.say("こんにちは")
#!/usr/bin/python
def speak(tex):
	"""
	converts the text recieved to speech
	using google text to speech
	"""
	from gtts import gTTS
	import commands
	import os
	tts = gTTS(text=tex,lang='en')
	print tex
	tts.save('reply.mp3')
	out = 'mpg321 reply.mp3'
	a = commands.getoutput(out)
	# os.system('mpg321 reply.mp3')
	# webbrowser.open('reply.mp3')
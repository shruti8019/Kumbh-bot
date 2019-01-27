from googletrans import Translator


trans = Translator()
text=input("Give input")	
ttext = trans.translate(text).text
pron = trans.translate(text).pronunciation
if pron == None:
	pron = ttext
message = "**" + ttext + "**"
message += "(" + pron + ")"
print(message)

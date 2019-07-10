'''If in future if we add more translateable languages, we could make own file to language lists and import them and make own files too to translate processes.'''
MorseList = {
" " : " ","A" : "._", "B" : "_...",
"C" : "_._.", "D" : "_..", "E" : ".",
"F" : ".._.", "G" : "__.", "H" : "....",
"I" : "..", "J" : ".___", "K" : "_._",
"L" : "._..", "M" : "__", "N" : "_.",
"O" : "___", "P" : ".__.", "Q" : "__._",
"R" : "._.", "S" : "...", "T" : "_",
"U" : ".._", "V" : "..._", "W" : ".__",
"X" : "_.._", "Y" : "_.__", "Z" : "__..",
"." : "._._._", "," : "__.._", "?" : "..__..",
"/" : "_.._.", "@" : ".__._.", "1" : ".____",
"2" : "..___", "3" : "...__", "4" : "...._",
"5" : ".....", "6" : "_....", "7" : "__...",
"8" : "___..", "9" : "____.", "0" : "_____"
} #MorseList contains defined letters, numbers and symbols, and their equivalents morsecodes.

	
def englishtomorse(contents): #Translate english to morse
	message = "" #message = Resultmessage 
	try:
		for char in contents: #char = One readed character
			if char != " ":
				message += MorseList[char.upper()]+ " " #Checks if character is in MorseList and adds it equivalents morsecode to message.
			else:
				message += " "
		f=open("Output.txt", "w") #Opens Output.txt-file
		f.write(message) #And writes message to it.
		f.close() #Then closes Output.txt-file
		print("Completed!")
	except KeyError: #If readed character from Input.txt-file isn't in MorseList. Print error message.
		print("Input contains unavailable character(s). Availabe letters are A-Z, numbers 0-9 and symbols .,?@")

def morsetoenglish(contents): #Translate morse to english 
	message = "" #message = Resultmessage 
	citext = "" #citext = One readed morsecode
	try:
		for char in contents: #char = One readed character
			if (char != " "): 
				i = 0
				citext += char	
			else:
				i += 1	
				if i == 2:
					message += " " #
				else:
					message += list(MorseList.keys())[list(MorseList.values()).index(citext)] #Checks if morsecode is in MorseList and adds it equivalents character to message.
					citext = ""
		f=open("Output.txt", "w")
		f.write(message)
		f.close()
		print("Completed!")
	except ValueError: #If readed morsecode from Input.txt-file isn't in MorseList. Print error message.
		print("Input contains unavailable character(s) or morsecode. Remember to separate morsecodes with a space. Availabe symbols are . and _")

def main(): #This is main process, which greets user and asks what language user wants translate.
	print("WELCOME! \n Choose what language you wanna translate: \n A) English to Morse \n B) Morse to English")
	answ = input("Answer (A or B):")
	if answ.upper() == "A": #If user choose answer A. Read Input.txt and start translating it from english to morse.
		f=open("Input.txt", "r")
		contents = f.read()
		f.close()
		englishtomorse(contents)
	elif answ.upper() == "B": #If user choose answer B. Read Input.txt and start translating it from morse to english.
		f=open("Input.txt", "r")
		contents = f.read()
		f.close()
		morsetoenglish(contents)
	
if __name__ == '__main__': 
    main() 


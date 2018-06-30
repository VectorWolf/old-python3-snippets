#from deutschliste import wb
wortbuch = open('de_neu.dic', 'rb').read()
wb = wortbuch.decode('latin1')
wb2 = wb.lower()
wb = wb.split("\r\n")
wb2 = wb2.split("\r\n")
wort = list(input("Bitte geben Sie ein bis zu 10-stelliges Anagramm ein : "))
liste = list()
a = len(wort)
for buchstabe in wort[-10:]:
	if a>= 10:
		del wort[-10]
		wort.append(buchstabe)
	for buchstabe in wort[-9:]:
		if a>= 9:
			del wort[-9]
			wort.append(buchstabe)
		for buchstabe in wort[-8:]:
			if a>= 8:
				del wort[-8]
				wort.append(buchstabe)
			for buchstabe in wort[-7:]:
				if a>= 7:
					del wort[-7]
					wort.append(buchstabe)
				for buchstabe in wort[-6:]:
					if a>= 6:
						del wort[-6]
						wort.append(buchstabe)
					for buchstabe in wort[-5:]:
						if a>= 5:
							del wort[-5]
							wort.append(buchstabe)
						for buchstabe in wort[-4:]:
							if a>= 4:
								del wort[-4]
								wort.append(buchstabe)
							for buchstabe in wort[-3:]:
								if a>= 3:
									del wort[-3]
									wort.append(buchstabe)
								for buchstabe in wort[-2:]:
									del wort[-2]
									wort.append(buchstabe)
									vorliste = ''.join(wort)
									if vorliste in wb2 == True:
										liste.append(wb2.index(vorliste))
#print("\n" + str(len(liste)) + " Wortvariationen gefunden\n")
input("Die Wörter " + str(wb(liste)) + " sind im Wörterbuch enthalten")					

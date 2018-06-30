wortbuch = open('de_neu.dic', 'rb').read()
wb = wortbuch.decode('latin1')
wb = wb.lower()
wb = wb.split("\r\n")
wb = set(wb)
wort = list(input("\nBitte geben Sie ein bis zu 10-stelliges Anagramm in Kleinbuchstaben ein : \n\n"))
liste = set()
a = len(wort)
for buchstabe in wort[-11:]:
	if a>= 11:
		del wort[-11]
		wort.append(buchstabe)
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
										liste.add(vorliste)
input("\n" + str(len(liste)) + " Wortvariationen gefunden\n")
print("Die Wörter " + str(wb.intersection(liste)) + " sind im Wörterbuch enthalten")

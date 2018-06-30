wortbuch = open('de_neu.dic', 'rb').read()
wb = wortbuch.decode('latin1')
wb = wb.lower()
wb = wb.split("\r\n")
wb = set(wb)
wort = list(input("\nBitte geben Sie bis zu 10 Kleinbuchstaben ohne Leerschritte ein : \n\n"))
liste = set()
a = len(wort)
if a > 10:
	input("\nWillst du mich umbringen?\nIch dachte ich hätte mich klar genug ausgedrückt, \nNICHT MEHR ALS 10 ZEICHEN!\n")
	exit()
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
print("\n" + str(len(liste)) + " Wortvariationen gefunden\n")
cliste = set()
while a > 2:
	cliste.clear()
	print("Die " + str(a) + "-stelligen Wörter " + str(wb.intersection(liste)) + " sind im Wörterbuch enthalten\n")
	for zähler in liste:
		cliste.add(zähler[1:])
	a -= 1
	liste = cliste.copy()
input("Fertig!")

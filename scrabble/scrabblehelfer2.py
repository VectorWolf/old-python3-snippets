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
for i in range(10):
	if a>= 10:
		wort.append(wort.pop(-10))
	for i in range(9):
		if a>= 9:
			wort.append(wort.pop(-9))
		for i in range(8):
			if a>= 8:
				wort.append(wort.pop(-8))
			for i in range(7):
				if a>= 7:
					wort.append(wort.pop(-7))
				for i in range(6):
					if a>= 6:
						wort.append(wort.pop(-6))
					for i in range(5):
						if a>= 5:
							wort.append(wort.pop(-5))
						for i in range(4):
							if a>= 4:
								wort.append(wort.pop(-4))
							for i in range(3):
								if a>= 3:
									wort.append(wort.pop(-3))
								for i in range(2):
									wort.append(wort.pop(-2))
									vorliste = ''.join(wort)
									liste.add(vorliste)
print("\n" + str(len(liste)) + " Wortvariationen gefunden\n")
while a > 2:
	print("Die " + str(a) + "-stelligen Wörter " + str(wb.intersection(liste)) + " sind im Wörterbuch enthalten\n")	
	liste = list(liste)
	a -= 1
	liste = [ x[:a] for x in liste ]
	liste = set(liste)
input("Fertig!")

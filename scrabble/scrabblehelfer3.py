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
def tausch(länge):
	for buchstabe in wort[-länge:]:
		del wort[-länge]
		wort.append(buchstabe)
		if länge == 2:
			vorliste = ''.join(wort)
			liste.add(vorliste)
		else:
			tausch(länge-1)
tausch(a)
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

wörterbuch = {"Ulm","ist","und","nun"}
eingabe = list(input())
liste = list()
wort = eingabe
for buchstabe in eingabe[0:]:
	del wort[0]
	wort.append(buchstabe)
	for buchstabe in eingabe[1:]:
		del wort[1]
		wort.append(buchstabe)
		for buchstabe in eingabe[2:]:
			del wort[2]
			wort.append(buchstabe)
			vorliste = ''.join(wort)
			liste.append(vorliste)
			eingabe = wort
print (liste)
input()
					

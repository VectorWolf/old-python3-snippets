wörterbuch = {"Ulm","ist","und","nun"}
wort = list(input())
liste = list()
for buchstabe in wort[0:]:
	del wort[0]
	wort.append(buchstabe)
	for buchstabe in wort[1:]:
		del wort[1]
		wort.append(buchstabe)
		for buchstabe in wort[2:]:
			del wort[2]
			wort.append(buchstabe)
			for buchstabe in wort[3:]:
				del wort[3]
				wort.append(buchstabe)
				vorliste = ''.join(wort)
				liste.append(vorliste)
print (liste)
input()
					

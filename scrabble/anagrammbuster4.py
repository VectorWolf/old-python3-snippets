wörterbuch = {"Ulm","ist","und","nun"}
wort = list(input())
liste = list()
for buchstabe in wort[-4:]:
	del wort[-4]
	wort.append(buchstabe)
	for buchstabe in wort[-3:]:
		del wort[-3]
		wort.append(buchstabe)
		for buchstabe in wort[-2:]:
			del wort[-2]
			wort.append(buchstabe)
			vorliste = ''.join(wort)
			liste.append(vorliste)
print (liste)
input()
					

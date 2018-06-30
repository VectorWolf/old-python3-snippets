wordbook = open('de_neu.dic', 'rb').read()
wordbook = wordbook.decode('latin1')
wordbook = wordbook.lower()
wordbook = wordbook.split("\r\n")
wordbook = {word for word in wordbook if len(word) > 2 and len(word) <= 10}
searched_word = str(input("\nBitte geben Sie bis zu 10 Kleinbuchstaben "
                          "ohne Leerschritte ein : \n\n"))
word_length = len(searched_word)

if word_length > 10:
    input("\nWillst du mich umbringen?\nIch dachte ich hätte mich "
          "klar genug ausgedrückt, \nNICHT MEHR ALS 10 ZEICHEN!\n")
    exit()

elif word_length <= 2:
    input("\nZu kurz!\nErwartest du wirklich ein so kurzes Wort?")
    exit()

elif not searched_word.isalpha():
    input("\nDas Wort ist nicht rein alphabetisch!")
    exit()

searched_word = list(searched_word.lower())
liste = set()


def interchange(word_length):
    for buchstabe in searched_word[-word_length:]:
        del searched_word[-word_length]
        searched_word.append(buchstabe)
        if word_length == 2:
            changed_word = ''.join(searched_word)
            liste.add(changed_word)
        else:
            interchange(word_length - 1)

interchange(word_length)

print("\n" + str(len(liste)) + " Wortvariationen gefunden\n")
while word_length > 2:
    found_words = wordbook.intersection(liste)
    if found_words:
        if len(found_words) == 1:
            print("Das " + str(word_length) + "-stellige Wort "
                  + str(found_words).strip("{}")
                  + " ist im Wörterbuch enthalten.\n")
        else:
            print("Die " + str(word_length) + "-stelligen Wörter "
                  + str(found_words).strip("{}")
                  + " sind im Wörterbuch enthalten.\n")
    word_length -= 1
    liste = {x[:word_length] for x in liste}
input("Fertig!")

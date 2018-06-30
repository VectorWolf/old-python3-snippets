# -*- coding: UTF-8 -*-

# Pygame-Modul importieren.
import pygame     

# Überprüfen, ob die optionalen Text- und Sound-Module geladen werden konnten.
if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')
if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden!')     

def main():
    # Initialisieren aller Pygame-Module und    
    # Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repräsentiert).
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    # Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendrücke wiederholt senden.
    pygame.display.set_caption("Pygame-Tutorial: Grundlagen")
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 30)

    # Clock-Objekt erstellen, das wir benötigen, um die Framerate zu begrenzen.
    clock = pygame.time.Clock()
 
    # Die Schleife, und damit unser Spiel, läuft solange running == True.
    running = True
    bg_color = (0,0,0)
    while running:
        # Framerate auf 30 Frames pro Sekunde beschränken.
        # Pygame wartet, falls das Programm schneller läuft.
        clock.tick(30) 

        # screen-Surface mit Schwarz (RGB = 0, 0, 0) füllen.
        screen.fill((bg_color))

        # Alle aufgelaufenen Events holen und abarbeiten.
        for event in pygame.event.get():
            # Spiel beenden, wenn wir ein QUIT-Event finden.
            if event.type == pygame.QUIT:
                running = False 

            # Wir interessieren uns auch für "Taste gedrückt"-Events.
            if event.type == pygame.KEYDOWN:
                # Wenn Escape gedrückt wird, posten wir ein QUIT-Event in Pygames Event-Warteschlange.
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                if event.key == pygame.K_UP:
                    bg_color = (0,0,0)
                if event.key == pygame.K_LEFT:
                    bg_color = (255,0,0)                    
                if event.key == pygame.K_DOWN:
                    bg_color = (0,255,0)                   
                if event.key == pygame.K_RIGHT:
                    bg_color = (0,0,255)
                if event.key == pygame.K_SPACE:
                    bg_color = (255,255,255)
                                                            
        # Inhalt von screen anzeigen.
        pygame.display.flip()
 

# Überprüfen, ob dieses Modul als Programm läuft und nicht in einem anderen Modul importiert wird.
if __name__ == '__main__':
    # Unsere Main-Funktion aufrufen.
    main()
    print("Tja, zuende, näch?")

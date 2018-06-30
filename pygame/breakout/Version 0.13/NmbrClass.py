import pygame


class NmbrObj:
    """This class implements a standard Number Object"""
    _oblist = []
    _dellist = []
    dirty = []

    space = 180

    def __init__(self, number, x, y, mlength):
        self.number = number
        self.y = y
        self.x = x
        self.pos = []
        self.nmbr = []
        self.mlength = mlength
        self.rect = pygame.Rect(x + self.space, y, self.space, 50)

        for i in range(10):
            self.nmbr.append(pygame.Surface.convert(pygame.image.load
                                                    (str(i) + ".png")))
            self.nmbr[i].set_colorkey((255, 0, 255))

        for i in range(1, mlength + 1):
            self.pos.append(pygame.Rect(self.x - (i * (self.space / mlength)),
                                        self.y, self.space / mlength, 50))

        type(self)._oblist.append(self)
        type(self).dirty.append(self.rect)

    """Returns the list with all objects of the class"""
    @classmethod
    def get_oblist(cls):
        return cls._oblist

    """Given object gets drawn at given screen"""
    def draw(self, screen):
        wnumber = self.number
        for i in range(self.mlength):
            screen.blit(self.nmbr[wnumber % 10], self.pos[i])
            if wnumber > 0:
                wnumber = int(wnumber / 10)

    """All objects in _oblist get drawn at given screen"""
    @classmethod
    def draw_all(cls, screen):
            for i in cls._oblist:
                i.draw(screen)

    """Object --> append to _dellist and gets deleted at cleanup()"""
    def destroy(self):
        type(self).dirty.append(self.rect)
        type(self)._dellist.append(self)

    """All objects are appended to _dellist"""
    @classmethod
    def destroy_all(cls):
        for i in cls._oblist:
            cls._dellist.append(i)

    """Deletes all objects in _dellist"""
    @classmethod
    def cleanup(cls):
        for i in cls._dellist:
            if i in cls._oblist:
                cls._oblist.remove(i)
        cls._dellist = []

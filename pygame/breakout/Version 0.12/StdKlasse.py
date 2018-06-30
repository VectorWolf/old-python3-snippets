import pygame
import random


class StdObj:
    """This class implements a standard collideable object"""
    _oblist = []
    _dellist = []

    def __init__(self, pic, x, y):
        self.obj = pygame.image.load(pic)
        self.rect = self.obj.get_rect()
        self.rect.top = y
        self.rect.left = x

        type(self)._oblist.append(self)

    """Returns the list with all objects of the class"""
    @classmethod
    def get_oblist(cls):
        return cls._oblist

    """Should call certain functions when in collision"""
    def collision(self, purge):
        pass

    """Given object gets drawn at given screen"""
    def draw(self, screen):
        screen.blit(self.obj, self.rect)

    """All objects in _oblist get drawn at given screen"""
    @classmethod
    def draw_all(cls, screen):
            for i in cls._oblist:
                screen.blit(i.obj, i.rect)

    """Object --> append to _dellist and gets deleted at cleanup()"""
    def destroy(self):
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
            cls._dellist.remove(i)
            del i


class StaticObj(StdObj):
    """Obj which merely exists and vanishes upon impact"""
    _oblist = []
    _dellist = []

    def collision(self, purge):
        self.destroy()


class PaddelObj(StdObj):
    """Generates a movable Paddle"""
    _oblist = []
    _dellist = []

    def __init__(self, pic, x, y, lbord, rbord, mspeed=8):
        StdObj.__init__(self, pic, x, y)
        self.speed = 0
        self.leftborder = lbord
        self.rightborder = rbord
        self.maxspeed = mspeed

    """Upon collision x speed partly gets added to the dyn. obj"""
    def collision(self, obj):
        if obj.speed[0] > 0 and self.speed > 0:
            obj.speed[0] += int(self.speed / 2 / self.maxspeed
                                * ((self.maxspeed + 2) - obj.speed[0]))
        elif obj.speed[0] < 0 and self.speed < 0:
            obj.speed[0] += int(self.speed / 2 / self.maxspeed
                                * ((self.maxspeed + 2) + obj.speed[0]))
        else:
            obj.speed[0] += self.speed // 2
        if obj.speed[0] == 0:
            obj.speed[0] = random.choice([-1, 1])

    def move_left(self):
        if self.speed > -self.maxspeed:
            self.speed -= 3

    def move_right(self):
        if self.speed < self.maxspeed:
            self.speed += 3

    """Checks for collision with borders and moves by speed"""
    def update_pos(self=None):
        if self is None:
            for i in PaddelObj._oblist:
                i.update_pos()
        else:
            if self.rect.left <= self.leftborder and self.speed < 0:
                self.speed = -self.speed

            elif self.rect.right > self.rightborder and self.speed > 0:
                self.speed = -self.speed

            if self.speed > 0:
                self.speed -= 1

            elif self.speed < 0:
                self.speed += 1

            self.rect = self.rect.move(self.speed, 0)


class BounceObj(StdObj):
    _oblist = []
    _dellist = []
    _width = [0, 0]
    _height = [0, 0]

    def __init__(self, pic, x, y, xspeed, yspeed):
        StdObj.__init__(self, pic, x, y)
        self.speed = [xspeed, yspeed]

    """Sets the borders for whole class"""
    @classmethod
    def set_borders(cls, x, y):
        cls._width = x
        cls._height = y

    """Checks for collision with other BounceObj Instances and swaps speed"""
    @classmethod
    def collide_dyn_self(cls):
        obj = cls._oblist
        for i in range(len(obj)):
            for j in range(i + 1, len(obj)):
                if obj[i].rect.colliderect(obj[j].rect):
                    obj[i].collision(obj[j])
                    obj[j].collision(obj[i])
                    # saves all x and y points of objs. in seperate lists
                    ballho = set(range(obj[i].rect.top,
                                       obj[i].rect.bottom))
                    ballbr = set(range(obj[i].rect.left,
                                       obj[i].rect.right))
                    ball2ho = set(range(obj[j].rect.top,
                                        obj[j].rect.bottom))
                    ball2br = set(range(obj[j].rect.left,
                                        obj[j].rect.right))
                    # determines x-, and y-center of indiv. obj.
                    avballho = sum(ballho) / len(ballho)
                    avballbr = sum(ballbr) / len(ballbr)
                    avball2ho = sum(ball2ho) / len(ball2ho)
                    avball2br = sum(ball2br) / len(ball2br)
                    # checks wether x or y intersects less
                    if (len(ballho.intersection(ball2ho))
                          > len(ballbr.intersection(ball2br))):
                        # is a left or right of b
                        if (avballbr < avball2br):
                            # is b moving towards a or a towards b
                            if (obj[i].speed[0] >= 0 or obj[j].speed[0] <= 0):
                                # swap x speed and send collision event
                                obj[i].speed[0], obj[j].speed[0] \
                                  = obj[j].speed[0], obj[i].speed[0]

                        elif (avballbr > avball2br):
                            if (obj[i].speed[0] <= 0 or obj[j].speed[0] >= 0):
                                obj[i].speed[0], obj[j].speed[0] \
                                  = obj[j].speed[0], obj[i].speed[0]

                    else:
                        # is a above or below b
                        if (avballho < avball2ho):
                            # is b moving towards a or a towards b
                            if (obj[i].speed[1] >= 0 or obj[j].speed[1] <= 0):
                                # swap y speed and send collision event
                                obj[i].speed[1], obj[j].speed[1] \
                                  = obj[j].speed[1], obj[i].speed[1]

                        elif (avballho > avball2ho):
                            if (obj[i].speed[1] <= 0 or obj[j].speed[1] >= 0):
                                obj[i].speed[1], obj[j].speed[1] \
                                  = obj[j].speed[1], obj[i].speed[1]

    """Checks for collision with other BounceObj Instances and revs. speed"""
    @classmethod
    def collide_rev_self(cls):
        obj = cls._oblist
        for i in range(len(obj)):
            for j in range(len(obj)):
                if obj[i].rect.colliderect(obj[j].rect):
                    obj[j].collision(obj[i])
                    # saves all x and y points of objs. in seperate lists
                    ballho = set(range(obj[i].rect.top,
                                       obj[i].rect.bottom))
                    ballbr = set(range(obj[i].rect.left,
                                       obj[i].rect.right))
                    ball2ho = set(range(obj[j].rect.top,
                                        obj[j].rect.bottom))
                    ball2br = set(range(obj[j].rect.left,
                                        obj[j].rect.right))
                    # determines x-, and y-center of indiv. obj.
                    avballho = sum(ballho) / len(ballho)
                    avballbr = sum(ballbr) / len(ballbr)
                    avball2ho = sum(ball2ho) / len(ball2ho)
                    avball2br = sum(ball2br) / len(ball2br)
                    # checks wether x or y intersects less
                    if (len(ballho.intersection(ball2ho))
                          > len(ballbr.intersection(ball2br))):
                        # is a left or right of b
                        if (avballbr < avball2br
                              and obj[i].speed[0] >= 0
                              or avballbr > avball2br
                              and obj[i].speed[0] <= 0):
                            obj[i].speed[0] = -obj[i].speed[0]
                    else:

                        if (avballho < avball2ho
                              and obj[i].speed[1] >= 0
                              or avballho > avball2ho
                              and obj[i].speed[1] <= 0):
                            obj[i].speed[1] = -obj[i].speed[1]

    @classmethod
    def collide_rev(cls, oblist):
        obj = cls._oblist
        for i in range(len(obj)):
            for j in range(len(oblist)):
                if obj[i].rect.colliderect(oblist[j].rect):
                    oblist[j].collision(obj[i])
                    # saves all x and y points of objs. in seperate lists
                    ballho = set(range(obj[i].rect.top,
                                       obj[i].rect.bottom))
                    ballbr = set(range(obj[i].rect.left,
                                       obj[i].rect.right))
                    ball2ho = set(range(oblist[j].rect.top,
                                        oblist[j].rect.bottom))
                    ball2br = set(range(oblist[j].rect.left,
                                        oblist[j].rect.right))
                    # determines x-, and y-center of indiv. obj.
                    avballho = sum(ballho) / len(ballho)
                    avballbr = sum(ballbr) / len(ballbr)
                    avball2ho = sum(ball2ho) / len(ball2ho)
                    avball2br = sum(ball2br) / len(ball2br)
                    # checks wether x or y intersects less
                    if (len(ballho.intersection(ball2ho))
                         > len(ballbr.intersection(ball2br))):

                        if (avballbr < avball2br
                              and obj[i].speed[0] >= 0
                              or avballbr > avball2br
                              and obj[i].speed[0] <= 0):
                            obj[i].speed[0] = -obj[i].speed[0]
                    else:

                        if (avballho < avball2ho
                              and obj[i].speed[1] >= 0
                              or avballho > avball2ho
                              and obj[i].speed[1] <= 0):
                            obj[i].speed[1] = -obj[i].speed[1]

    def update_pos(self=None):
        if self is None:
            for i in BounceObj._oblist:
                i.update_pos()
        else:
            if (self.rect.left < BounceObj._width[0]) \
                  and (self.speed[0] < 0) \
                  and (BounceObj._width[0] != -1):
                self.speed[0] = -self.speed[0]

            elif (self.rect.right > BounceObj._width[1]) \
                  and (self.speed[0] > 0) \
                  and (BounceObj._width[1] != -1):
                self.speed[0] = -self.speed[0]

            if (self.rect.top < BounceObj._height[0]) \
                  and (self.speed[1] < 0) \
                  and (BounceObj._height[0] != -1):
                self.speed[1] = -self.speed[1]

            elif (self.rect.bottom > BounceObj._height[1]) \
                  and (self.speed[1] > 0) \
                  and (BounceObj._height[1] != -1):
                self.speed[1] = -self.speed[1]

            self.rect = self.rect.move(self.speed)

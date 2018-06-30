import pygame
import random
class StdObj:
    _oblist = []
    _dellist = []
    
    def __init__(self, pic, x, y):
        self.obj = pygame.image.load(pic)
        self.rect = self.obj.get_rect()
        self.rect.top = y
        self.rect.left = x
        
        type(self)._oblist.append(self)
        
    @classmethod        
    def GetOblist(cls):
        return cls._oblist
        
    def Collosion(self,purge):
        self.Destroy()
            
    def Draw(self,screen):
        screen.blit(self.obj, self.rect)

    @classmethod
    def DrawAll(cls,screen):
            for i in cls._oblist:
                screen.blit(i.obj, i.rect)
                
    def Destroy(self):
        type(self)._dellist.append(self)
            
    @classmethod        
    def DestroyAll(cls):
        for i in cls._oblist:
            cls._dellist.append(i)

    @classmethod                    
    def Cleanup(cls):
        for i in cls._dellist:
            if i in cls._oblist:
                cls._oblist.remove(i)
            cls._dellist.remove(i)
            del i

class StaticObj(StdObj):
    _oblist = []
    _dellist = []
    pass
    
    
class PaddelObj(StdObj):
    _oblist = []
    _dellist = []
       
    def __init__(self, pic, x, y, lbord, rbord, mspeed=8):
        StdObj.__init__(self, pic, x, y)
        self.speed = 0
        self.leftborder = lbord
        self.rightborder = rbord
        self.maxspeed = mspeed
        
    def Collosion(self,obj):
        if obj.speed[0] > 0 and self.speed > 0:
            obj.speed[0] += int(self.speed / 2 / self.maxspeed * (self.maxspeed - obj.speed[0]))
        elif obj.speed[0] < 0 and self.speed < 0:
            obj.speed[0] += int(self.speed / 2 / self.maxspeed * (self.maxspeed + obj.speed[0]))
        else:            
            obj.speed[0] += self.speed // 2
        if obj.speed[0] == 0:
            obj.speed[0] = random.choice([-1,1])
        
    def MoveLeft(self):
        if self.speed > -self.maxspeed:
            self.speed -= 3
            
    def MoveRight(self):
        if self.speed < self.maxspeed:
            self.speed += 3
                                                
    def UpdatePos(self=None):
        if self == None:
            for i in PaddelObj._oblist:
                i.UpdatePos()    
        else:                                
            if self.rect.left <= self.leftborder and self.speed < 0:
                self.speed = -self.speed
                
            elif self.rect.right > self.rightborder and self.speed > 0:
                self.speed = -self.speed
                
            if self.speed > 0:
                self.speed -= 1
                
            elif self.speed < 0:            
                self.speed += 1
                
            self.rect = self.rect.move(self.speed,0)            
            
            
class BounceObj(StdObj):
    _oblist = []
    _dellist = []
    _width = [0,0]
    _height = [0,0]
    
    def __init__(self, pic, x, y, xspeed, yspeed):
        StdObj.__init__(self, pic, x, y)
        self.speed = [xspeed,yspeed]

    @classmethod        
    def SetBorders(cls, x, y):
        cls._width = x
        cls._height = y
                
    @classmethod    
    def Collide(cls,oblist=None):
        if oblist==None:    
            for i in range(len(cls._oblist)):
                for j in range(i+1, len(cls._oblist)):
                    if cls._oblist[i].rect.colliderect(cls._oblist[j].rect):            
                        ballho = set(range(cls._oblist[i].rect.top,cls._oblist[i].rect.bottom))
                        ballbr = set(range(cls._oblist[i].rect.left,cls._oblist[i].rect.right))
                        ball2ho = set(range(cls._oblist[j].rect.top,cls._oblist[j].rect.bottom))
                        ball2br = set(range(cls._oblist[j].rect.left,cls._oblist[j].rect.right))
                        
                        avballho = sum(ballho)/len(ballho)
                        avballbr = sum(ballbr)/len(ballbr)
                        avball2ho = sum(ball2ho)/len(ball2ho)
                        avball2br = sum(ball2br)/len(ball2br)                
                        
                        if len(ballho.intersection(ball2ho)) > len(ballbr.intersection(ball2br)):
                            if avballbr < avball2br and cls._oblist[i].speed[0] >= 0 or avballbr > avball2br and cls._oblist[i].speed[0] <= 0:
                                cls._oblist[i].speed[0], cls._oblist[j].speed[0] = cls._oblist[j].speed[0], cls._oblist[i].speed[0]
                                
                            elif avballbr < avball2br and cls._oblist[j].speed[0] <= 0 or avballbr > avball2br and cls._oblist[j].speed[0] >= 0:
                                cls._oblist[i].speed[0], cls._oblist[j].speed[0] = cls._oblist[j].speed[0], cls._oblist[i].speed[0]
                                
                        else:
                        
                            if avballho < avball2ho and cls._oblist[i].speed[1] >= 0 or avballho > avball2ho and cls._oblist[i].speed[1] <= 0:
                                cls._oblist[i].speed[1], cls._oblist[j].speed[1] = cls._oblist[j].speed[1], cls._oblist[i].speed[1]
                                
                            elif avballho < avball2ho and cls._oblist[j].speed[1] <= 0 or avballho > avball2ho and cls._oblist[j].speed[1] >= 0:
                                cls._oblist[i].speed[1], cls._oblist[j].speed[1] = cls._oblist[j].speed[1], cls._oblist[i].speed[1]                        
        else:
            for i in range(len(cls._oblist)):
                for j in range(len(oblist)):
                    if cls._oblist[i].rect.colliderect(oblist[j].rect):            
                        ballho = set(range(cls._oblist[i].rect.top,cls._oblist[i].rect.bottom))
                        ballbr = set(range(cls._oblist[i].rect.left,cls._oblist[i].rect.right))
                        ball2ho = set(range(oblist[j].rect.top,oblist[j].rect.bottom))
                        ball2br = set(range(oblist[j].rect.left,oblist[j].rect.right))
                        
                        avballho = sum(ballho)/len(ballho)
                        avballbr = sum(ballbr)/len(ballbr)
                        avball2ho = sum(ball2ho)/len(ball2ho)
                        avball2br = sum(ball2br)/len(ball2br)                
                        
                        if len(ballho.intersection(ball2ho)) > len(ballbr.intersection(ball2br)):

                            if avballbr < avball2br and cls._oblist[i].speed[0] >= 0 or avballbr > avball2br and cls._oblist[i].speed[0] <= 0:
                                cls._oblist[i].speed[0] = -cls._oblist[i].speed[0]
                                oblist[j].Collosion(cls._oblist[i])
                        else:
                        
                            if avballho < avball2ho and cls._oblist[i].speed[1] >= 0 or avballho > avball2ho and cls._oblist[i].speed[1] <= 0:
                                cls._oblist[i].speed[1] = -cls._oblist[i].speed[1]
                                oblist[j].Collosion(cls._oblist[i])
                                                
    def UpdatePos(self=None):
        if self == None:
            for i in BounceObj._oblist:
                i.UpdatePos()    
        else:                                
            if self.rect.left < BounceObj._width[0] and self.speed[0] < 0 and BounceObj._width[0] != -1:
                self.speed[0] = -self.speed[0]
                
            elif self.rect.right > BounceObj._width[1] and self.speed[0] > 0 and BounceObj._width[1] != -1:
                self.speed[0] = -self.speed[0]
                
            if self.rect.top < BounceObj._height[0] and self.speed[1] < 0 and BounceObj._height[0] != -1:
                self.speed[1] = -self.speed[1]
                
            elif self.rect.bottom > BounceObj._height[1] and self.speed[1] > 0 and BounceObj._height[1] != -1:
                self.speed[1] = -self.speed[1]
                
            self.rect = self.rect.move(self.speed)            


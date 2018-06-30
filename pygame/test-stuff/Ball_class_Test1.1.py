import sys, pygame, time

pygame.init()

start_time = time.time()

size = width, height = 666, 450
color = 40, 20, 20

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

class BounceObj:
    __oblist = []
    
    def __init__(self, pic, x, y, xspeed, yspeed):
        self.obj = pygame.image.load(pic)
        self.rect = self.obj.get_rect()
        self.speed = [xspeed,yspeed]
        self.rect.top = y
        self.rect.left = x
        
        type(self).__oblist.append(self)
        
    def GetOblist():
        return BounceObj.__oblist
        
    def Collide(oblist=None):
        if oblist==None:    
            for i in range(len(BounceObj.__oblist)):
                for j in range(i+1, len(BounceObj.__oblist)):
                    if BounceObj.__oblist[i].rect.colliderect(BounceObj.__oblist[j].rect):            
                        ballho = set(range(BounceObj.__oblist[i].rect.top,BounceObj.__oblist[i].rect.bottom))
                        ballbr = set(range(BounceObj.__oblist[i].rect.left,BounceObj.__oblist[i].rect.right))
                        ball2ho = set(range(BounceObj.__oblist[j].rect.top,BounceObj.__oblist[j].rect.bottom))
                        ball2br = set(range(BounceObj.__oblist[j].rect.left,BounceObj.__oblist[j].rect.right))
                        
                        avballho = sum(ballho)/len(ballho)
                        avballbr = sum(ballbr)/len(ballbr)
                        avball2ho = sum(ball2ho)/len(ball2ho)
                        avball2br = sum(ball2br)/len(ball2br)                
                        
                        if len(ballho.intersection(ball2ho)) > len(ballbr.intersection(ball2br)):

                            if avballbr < avball2br and BounceObj.__oblist[i].speed[0] > 0 or avballbr > avball2br and BounceObj.__oblist[i].speed[0] < 0:
                                BounceObj.__oblist[i].speed[0] = -BounceObj.__oblist[i].speed[0]
                                
                            if avballbr < avball2br and BounceObj.__oblist[j].speed[0] < 0 or avballbr > avball2br and BounceObj.__oblist[j].speed[0] > 0:
                                BounceObj.__oblist[j].speed[0] = -BounceObj.__oblist[j].speed[0]
                                
                        else:
                        
                            if avballho < avball2ho and BounceObj.__oblist[i].speed[1] > 0 or avballho > avball2ho and BounceObj.__oblist[i].speed[1] < 0:
                                BounceObj.__oblist[i].speed[1] = -BounceObj.__oblist[i].speed[1]
                                
                            if avballho < avball2ho and BounceObj.__oblist[i].speed[1] < 0 or avballho > avball2ho and BounceObj.__oblist[i].speed[1] > 0:
                                BounceObj.__oblist[j].speed[1] = -BounceObj.__oblist[j].speed[1]
        else:
            for i in range(len(BounceObj.__oblist)):
                for j in range(len(oblist)):
                    if BounceObj.__oblist[i].rect.colliderect(oblist[j].rect):            
                        ballho = set(range(BounceObj.__oblist[i].rect.top,BounceObj.__oblist[i].rect.bottom))
                        ballbr = set(range(BounceObj.__oblist[i].rect.left,BounceObj.__oblist[i].rect.right))
                        ball2ho = set(range(oblist[j].rect.top,oblist[j].rect.bottom))
                        ball2br = set(range(oblist[j].rect.left,oblist[j].rect.right))
                        
                        avballho = sum(ballho)/len(ballho)
                        avballbr = sum(ballbr)/len(ballbr)
                        avball2ho = sum(ball2ho)/len(ball2ho)
                        avball2br = sum(ball2br)/len(ball2br)                
                        
                        if len(ballho.intersection(ball2ho)) > len(ballbr.intersection(ball2br)):

                            if avballbr < avball2br and BounceObj.__oblist[i].speed[0] > 0 or avballbr > avball2br and BounceObj.__oblist[i].speed[0] < 0:
                                BounceObj.__oblist[i].speed[0] = -BounceObj.__oblist[i].speed[0]
                                
                            if avballbr < avball2br and oblist[j].speed[0] < 0 or avballbr > avball2br and oblist[j].speed[0] > 0:
                                oblist[j].speed[0] = -oblist[j].speed[0]
                                
                        else:
                        
                            if avballho < avball2ho and BounceObj.__oblist[i].speed[1] > 0 or avballho > avball2ho and BounceObj.__oblist[i].speed[1] < 0:
                                BounceObj.__oblist[i].speed[1] = -BounceObj.__oblist[i].speed[1]
                                
                            if avballho < avball2ho and BounceObj.__oblist[i].speed[1] < 0 or avballho > avball2ho and BounceObj.__oblist[i].speed[1] > 0:
                                oblist[j].speed[1] = -oblist[j].speed[1]
        
    def UpdatePos(self=None):
        if self == None:
            for i in BounceObj.__oblist:
                i.UpdatePos()    
        else:                                
            if self.rect.left < 0 and self.speed[0] < 0:
                self.speed[0] = -self.speed[0]
                
            if self.rect.right > width and self.speed[0] > 0:
                self.speed[0] = -self.speed[0]
                
            if self.rect.top < 0 and self.speed[1] < 0:
                self.speed[1] = -self.speed[1]
                
            if self.rect.bottom > height and self.speed[1] > 0:
                self.speed[1] = -self.speed[1]
                
            self.rect = self.rect.move(self.speed)
            
    def Draw(self=None):
        if self == None:
            for i in BounceObj.__oblist:
                screen.blit(i.obj, i.rect)
        else:
            screen.blit(self.obj, self.rect)
            
            
if __name__ == '__main__':            
    
    arsch = BounceObj("eckball.png",300,20,3,3)

    arsch2 = BounceObj("ball.png",1,20,3,3)

    arsch3 = BounceObj("paddel.png",2,20,3,3)

    arsch4 = BounceObj("eckball.png",3,20,3,3)

    arsch5 = BounceObj("paddel.png",4,20,3,3)

    arsch6 = BounceObj("ball.png",5,20,3,3)

    arsch7 = BounceObj("eckball.png",6,20,3,3)

    arsch8 = BounceObj("eckball.png",7,20,3,3)

    arsch9 = BounceObj("ball.png",8,20,3,3)

    pimmel = BounceObj("eckball.png",300,300,-3,-3)

    sack = BounceObj("ball.png",550,100,-2,3)

    sack = BounceObj("eckball.png",450,100, 2,-3)

    sack = BounceObj("paddel.png",350,100,-3,2)

    sack = BounceObj("eckball.png",250,100,1,-2)

    anal = BounceObj("Dick.gif",100,100,2,-1)

    rektal = BounceObj("Dick.gif",400,200,1,-2)

    while True:
      
        clock.tick(120) 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            
        oblist=BounceObj.GetOblist()          
                
        BounceObj.Collide()            
            
        BounceObj.UpdatePos()
            
        screen.fill(color)        
        BounceObj.Draw()
        
        pygame.display.flip()

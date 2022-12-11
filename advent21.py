import copy
class Player():
    def __init__(self,start):
        self.pos=start -1
        self.score=0
        
    def roll(self,dice):
        self.pos=(self.pos+dice)%10
        self.score += self.pos +1
    
    def Won(self):
        return self.score >= 21
    
def Universe(p1,p2,player2,dice):
    c=0
    d=0
    new={3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    if dice>0:
        if player2:
            p2.roll(dice)
            #print(2,num,p2.pos)
            if p2.Won():
                return (0,1)
            player2=False
        else:
            p1.roll(dice)
            #print(1,num,p1.pos)
            if p1.Won():
                return (1,0)
            player2=True
    for i in new:
        cp1=copy.copy(p1)
        cp2=copy.copy(p2)
        a,b = Universe(cp1,cp2,player2,i)
        c += a *new[i]
        d += b *new[i]
    #print(a,b)
    return (c,d)

ans=444356092776315+341960390180808
Dice = -1
is2=False
p1 = Player(4)
p2 = Player(1)
print(Universe(p1,p2,False,0))
#print(3**rols,rols,p1.score,p2.score)
print(ans)

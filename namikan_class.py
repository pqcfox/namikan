import math, curses

global foodstore
global Space
global SpaceDirtiness
global Namikans
global GoodSoulCatch
Space = 0
SpaceDirtiness
foodstore = 0

def CPrint(text, y ,x):
    scr.addstr(y, x, text, curses.A_REVERSE)

def twodify(x,y):
    name = []
    for row in xrange(x): name +=[[0]*y]
    return name

class Namikan():
    def __init__(self, size, growth, growthrate, food, clean, sick, form, life, abilityone, abilitytwo, attackone, attacktwo, attackthree, speed, breed, mate):
        self.size = size
        self.growth = growth
        self.growthrate = growthrate
        self.food = food
        self.sick = sick
        self. clean = clean
        self.breed = breed
        self.mate = mate
        self.form = form
        self.life = life
        self.abilityone = abilityone
        self.abilitytwo = abilitytwo
        self.attackone = attackone
        self.attacktwo = attacktwo
        self.attackthree = attackthree
        self.speed = speed
        

    def Goodnight(Namikan, index, Namikans):
        global foodstore
        global SpaceDirtiness
        global Space
        if foodstore > Namikan.size-Namikan.food:
            foodstore -= Namikan.size-Namikan.food
            Namikan.food = Namikan.size
        if Namikan.size < Namikan.growth and Namikan.food > Namikan.growthrate:
            Namikan.size += Namikan.growthrate
            Namikan.food -= Namikan.growthrate
        if Namikan.food < 0:
            Namikan.sick -= 40
        Namikan.clean -= int(math.ceil(len(Namikans)/Space))
        Namikan.clean -= int(math.floor(SpaceDirtiness/10))
        Namikan.clean -= int(math.floor(Namikan.sick/10))
        if Namikan.clean < 100 and Namikan.sick < 70:
            Namikan.clean += 3
        Namikan.sick += int(math.floor(len(Namikans)/Space))
        for OtherNamikan in Namikans:
            Namikan.sick += int(math.floor(OtherNamikan.sick/20))
        if random.randint(1,20) == 20:
            Namikan.sick += random.randint(0,40)
        Namikan.sick -= random.randint(0,5)
        if (Namikan.sick == 100 and Namikan.clean == 0) or (Namikan.food == 0 and Namikan.clean == 0) or (Namikan.sick == 100 and Namikan.food == 0):
            del Namimans[index]
        if Namikan.breed < 0 and Namikan.growth == Namikan.size:
            Namikan.breed += 1
        if Namikan.food >= Namikan.size and Namikan.clean > 95 and Namikan.sick < 5 and Namikan.breed == 0 and Namikan.growth == Namikan.size and random.randint(0,1) == 1:
            while(True):
                Mate = random.select(Namikans)
                if Mate.growth == Mate.size:
                    Namikan.mate = Mate
                    Namikan.breed = 1
                    break
        if Namikan.breed == 0:
            Namikan.breed = -15
        elif Namikan.breed > 0:
            Namikan.breed += int(math.ceil((Namikan.growthrate+Namikan.mate.growthrate)/2))
        elif Namikan.breed == Namikan.size:
            Birth(Namikan, Namikan.mate)
            Namikan.breed = -40

        def Birth(Namikan0, Namikan1):
            global Namikans
            if random.randint(0,1) == 0:
                NewGrowth = Namikan0.growth
                if Namikan0.growth > Namikan1.growth:
                    NewGrowth -= random.randing(0,30)
                if Namikan0.growth < Namikan1.growth:
                    NewGrowth += random.randing(0,30)
            else:
                NewGrowth = Namikan1.growth
                if Namikan0.growth > Namikan1.growth:
                    NewGrowth -= random.randing(0,30)
                if Namikan0.growth < Namikan1.growth:
                    NewGrowth += random.randing(0,30)
            if random.randint(0,1) == 0:
                NewGrowthRate = Namikan0.growthrate
                if Namikan0.growthrate > Namikan1.growthrate:
                    NewGrowthRate -= random.randing(0,1)
                if Namikan0.growthrate < Namikan1.growthrate:
                    NewGrowthRate += random.randing(0,1)
            else:
                NewGrowthRate = Namikan1.growthrate
                if Namikan0.growthrate > Namikan1.growthrate:
                    NewGrowthRate -= random.randing(0,1)
                if Namikan0.growthrate < Namikan1.growthrate:
                    NewGrowthRate += random.randing(0,1)
            if random.randint(0,1) == 0:
                NewForm = Namikan0.form
            else:
                NewForm = Namikan1.form
            if random.randint(0,1) == 0:
                NewSpeed = Namikan0.speed
                if Namikan0.speed > Namikan1.speed:
                    NewSpeed -= random.randing(0,1)
                if Namikan0.speed < Namikan1.speed:
                    NewSpeed += random.randing(0,1)
            else:
                NewSpeed = Namikan1.Speed
                if Namikan0.speed > Namikan1.speed:
                    NewSpeed -= random.randing(0,1)
                if Namikan0.speed < Namikan1.speed:
                    NewSpeed += random.randing(0,1)
            if NewSpeed < 1:
                NewSpeed = 1
            PotentialAbilities = []
            PotentialAbilities.append(Namikan0.abilityone)
            PotentialAbilities.append(Namikan0.abilitytwo)
            PotentialAbilities.append(Namikan1.abilityone)
            PotentialAbilities.append(Namikan1.abilitytwo)
            random.shuffle(PotentialAbilities)
            NewAbilityOne = PotentialAbilities.pop()
            NewAbilityTwo = PotentialAbilities.pop()
            PotentialAttacks = []
            PotentialAttacks.append(Namikan0.attackone)
            PotentialAttacks.append(Namikan0.attacktwo)
            PotentialAttacks.append(Namikan0.attackthree)
            PotentialAttacks.append(Namikan1.attackone)
            PotentialAttacks.append(Namikan1.attacktwo)
            PotentialAttacks.append(Namikan1.attackthree)
            random.shuffle(PotentialAttacks)
            NewAttackOne = PotentialAbilities.pop()
            NewAttackTwo = PotentialAbilities.pop()
            NewAttackThree = PotentialAbilities.pop()
            NewNamikan = Namikan(1, NewGrowth, NewGrowthRate, 100, 100, 0, NewForm, 100, NewAbilityOne, NewAbilityTwo, NewAttackOne, NewAttackTwo, NewAttackThree, NewSpeed, -40, None)
            Namikans.append(NewNamikan)





Forms = ["Occult", "Nostalgic", "Enigmatic", "Unearthly", "Heraldic", "Divine", "Bionic"]

Abilities = ["Terrifying", "Animated", "Apothecary", "Healer", "Maternal"]

Attacks = ["Soul Catch", "Ditty", "Teleport", "Force Beam", "Circle Cut"]

Feed(Namikan, Amount):
    if foodstore > Amount:
        foodstore -= Amount
        Namikan.food += Amount

MuckOut():
    global SpaceDirtiness
    if SpaceDirtiness > 50:
        SpaceDirtiness -= 50
    else:
        SpaceDirtiness = 0

Wash(Namikan):
    Namikan.clean += 20

CheckBelly(Namikan):
    if ciel(Namikan.food/Namikan.size) > 1:
        CPrint("The Namikan lolls, its stomach distended with a more-than-full full meal.",0,0)
    elif Namikan.food/Namikan.size > 0.9:
        CPrint("The Namikan is content on a full stomach.",0,0)
    elif Namikan.food/Namikan.size > 0.5:
        CPrint("The Namikan appears satiated.",0,0)
    elif Namikan.food/Namikan.size > 0.2:
        CPrint("The Namikan growls as it begins to feel hunger pangs.",0,0)
    elif Namikan.food/Namikan.size > 0.1:
        CPrint("The Namikan appears agitated, its hunger apparent.",0,0)
    else:
        CPrint("The Namikan is weak with starvation.",0,0)

CheckCleanliness(Namikan):
    if Namikan.clean > 100:
        CPrint("The Namikan's coat is lustrous. These creatures possess a beauty you didn't know could exist in an animal.",0,0)
    elif Namikan.clean > 90:
        CPrint("The Namikan gleams with cleanliness. Enter it in a Namikan Fair?",0,0)
    elif Namikan.clean > 50:
        CPrint("The Namikan could probably use a bath, but it's nothing major.",0,0)
    elif Namikan.clean > 20:
        CPrint("The Namikan is quite dirty. Still, muddy Namikans have their own sort of cuteness.",0,0)
    elif Namikan.clean > 10:
        CPrint("You can hardly see the Namikan through the dust cloud that envelops it. The smell is also starting to become a concern.",0,0)
    else:
        CPrint("The sight of the Namikan encrusted with dirt and smelling like filth is almost to much to bear.",0,0)

CheckSickness(Namikan):
    if Namikan.sick > 100:
        CPrint("The Namikan gives you a feeble glance, its eyes glazed over with weakness. Its belly heaves in uncomfortable, irregular motions.",0,0)
    elif Namikan.sick > 90:
        CPrint("The Namikan tries to lift its head, but pain shoots through its body and it falls back to the ground.",0,0)
    elif Namikan.sick > 80:
        CPrint("The Namikan has become lethargic and has a dangerously high fever.",0,0)
    elif Namikan.sick > 50:
        CPrint("The Namikan is coming down with something major. It's lost interest in its normal activities.",0,0)
    elif Namikan.sick > 10:
        CPrint("The Namikan seems to be falling ill, but it still makes an effort to be its normal self.",0,0)
    else:
        CPrint("The Namikan appears to be in perfect health, gallivating around energetically.",0,0)

CheckBreeding(Namikan):
    if Namikan.size != Namikan.growth:
        CPrint("The Namikan isn't mature enough to breed yet.",0,0)
    elif Namikan.breed/Namikan.size > 0.7:
        CPrint("The Namikan's belly is swollen with its unborn offspring.",0,0)
    elif Namikan.breed/Namikan.size > 0.3:
        CPrint("The Namikan's belly has become increasingly full lately.",0,0)
    elif Namikan.breed > 0:
        CPrint("Nothing much can be determined about the Namikan's reproductive state right now.",0,0)
    elif Namikan.breed > -4:
        CPrint("The Namikan appears to be nearing its breeding state.",0,0)
    elif Namikan.breed > -21:
        CPrint("Nothing much can be determined about the Namikan's reproductive state right now.",0,0)

CheckLife(Namikan):
    if Namikan.life > 100:
        CPrint("There is something unnatural about the Namikan's extraordinary vitality.",0,0)
    elif Namikan.life > 90:
        CPrint("The Namikan is in perfect health. You seem to be doing something right.",0,0)
    elif Namikan.life > 50:
        CPrint("The Namikan has suffered some injuries, but is bearing them with a cheerful resoluteness.",0,0)
    elif Namikan.life > 20:
        CPrint("The Namikan is seriously hurt. Its performance is starting to flag.",0,0)
    elif Namikan.life > 10:
        CPrint("The Namikan's valor in the face of its cuts, wounds, and various other injuries is amazing, but you doubt it can last much longer.",0,0)
    else:
        CPrint("The Namikan can barely go on. It might not make it too much farther.",0,0)


CheckGeneral(Namikan):
    CPrint("Current Size: "+Namikan.size)
    CPrint("Full Size: "+Namikan.growth)
    CPrint("Form: "+Namikan.growth)
    CPrint("Ability One: "+Namikan.abilityone)
    CPrint("Ability Two: "+Namikan.abilitytwo)
    CPrint("Attack One: "+Namikan.attackone)
    CPrint("Attack Two: "+Namikan.attacktwo)
    CPrint("Attack Three: "+Namikan.attackthree)

class BattleNamikan():
    def __init__(self, size, attack, defence, life, abilityone, abilitytwo, attackone, attacktwo, attackthree, speed, status, x, y):
        self.size = size
        self.attack = attack
        self.defense = defense
        self.life = life
        self.abilityone = abilityone
        self.abilitytwo = abilitytwo
        self.attackone = attackone
        self.attacktwo = attacktwo
        self.attackthree = attackthree
        self.speed = speed
        self.status = status
        self.x = x
        self.y = y

    def ReadyforBattle(Namikan):
        Size = Namikan.size
        Attack = 100
        Defense = 100
        Life = 100
        Attack += int(math.ceil(Namikan.size/10))
        Defense -= int(math.ceil(Namikan.size/15))
        Defense += Namikan.speed*20
        Attack -= int(math.ceil(Namikan.sick/3))
        Defense -= int(math.ceil(Namikan.sick/3))
        Life -= int(math.ceil(Namikan.sick/1.5))
        Attack += int(math.ceil(Namikan.food/5))
        Defense += int(math.ceil(Namikan.food/5))
        Attack -= 10
        Defense -= 10
        Defense += int(math.ceil(Namikan.clean/10))
        Defense -= int(math.ceil(Namikan.breed/10))
        return BattleNamikan(Size,Attack,Defense,Life,Namikan.abilityone,Namikan.abilitytwo,Namikan.attackone,Namikan.attacktwo,Namikan.attackthree,Namikan.speed, None, 0, 0)
        
    

class Battle():
#      def __init__(self, size, growth, growthrate, food, clean, sick, form, life, abilityone, abilitytwo, attackone, attacktwo, attackthree, speed, breed, mate):

    def Battle(GNamOne,GNamTwo,BNamOne,BNamTwo):
        global GoodSoulCatch
        Arena = [][]
        for i in range (9):
            for j in range (9):
                Arena[i][j] = Ground
        GNamOne.x = 2
        GNamOne.y = 6
        GNamTwo.x = 6
        GNamTwo.y = 6
        BNamOne.x = 2
        BNamOne.y = 2
        BNamTwo.x = 6
        BNamTwo.y = 2
        while(BattleOn == True):

            #UseItem

            if GNamOne.life < 1:
                GNamOne = None
            if GNamTwo.life < 1:
                GNamTwo = None
            if BNamOne.life < 1:
                BNamOne = None
            if BNamTwo.life < 1:
                BNamTwo = None

            if GNamOne != None:
                for i in range (9):
                    for j in range (9):
                        Arena[i][j] = Ground
                GLoc1 = (GNamOne.x,GNamOne.y)
                GLoc2 = (GNamTwo.x,GNamTwo.y)
                GLoc3 = (BNamOne.x,BNamOne.y)
                GLoc4 = (BNamTwo.x,BNamTwo.y)
                Arena[GNamOne.y][GNamOne.x] = GNamOne
                Arena[GNamTwo.y][GNamTwo.x] = GNamTwo
                Arena[BNamOne.y][BNamOne.x] = BNamOne
                Arena[GNamTwo.y][GNamTwo.x] = BNamTwo
                TurnsLeft = GNamOne.speed
                while(TurnsLeft > 0):
                    if std.scr.getch() == w and GNamOne.x != 0:
                        GNamOne.x -= 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
                    elif std.scr.getch() == s and GNamOne.x != 8:
                        GNamOne.x += 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
                    elif std.scr.getch() == a and GNamOne.x != 0:
                        GNamOne.y -= 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
                    elif std.scr.getch() == d and GNamOne.x != 8:
                        GNamOne.y += 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
                    elif std.scr.getch() == 1:
                        UseAttack(GNamOne.attackone,GNamOne.x,GNamOne.y,GNamOne)
                        TurnsLeft = 0
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
                    elif std.scr.getch() == 2: 
                        UseAttack(GNamOne.attacktwo,GNamOne.x,GNamOne.y,GNamOne)
                        TurnsLeft = 0
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
                    elif std.scr.getch() == 3: 
                        UseAttack(GNamOne.attackthree,GNamOne.x,GNamOne.y,GNamOne)
                        TurnsLeft = 0
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):


            if GNamTwo != None:
                for i in range (9):
                    for j in range (9):
                        Arena[i][j] = Ground
                GLoc1 = (GNamOne.x,GNamOne.y)
                GLoc2 = (GNamTwo.x,GNamTwo.y)
                GLoc3 = (BNamOne.x,BNamOne.y)
                GLoc4 = (BNamTwo.x,BNamTwo.y)
                Arena[GNamOne.y][GNamOne.x] = GNamOne
                Arena[GNamTwo.y][GNamTwo.x] = GNamTwo
                Arena[BNamOne.y][BNamOne.x] = BNamOne
                Arena[GNamTwo.y][GNamTwo.x] = BNamTwo
                TurnsLeft = GNamTwo.speed
                while(TurnsLeft > 0):
                    if std.scr.getch() == w and GNamTwo.x != 0:
                        GNamTwo.x -= 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
                    elif std.scr.getch() == s and GNamTwo.x != 8:
                        GNamTwo.x += 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
                    elif std.scr.getch() == a and GNamTwo.x != 0:
                        GNamTwo.y -= 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
                    elif std.scr.getch() == d and GNamTwo.x != 8:
                        GNamTwo.y += 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
                    elif std.scr.getch() == 1:
                        UseAttack(GNamTwo.attackone,GNamTwo.x,GNamTwo.y,GNamTwo)
                        TurnsLeft = 0
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
                    elif std.scr.getch() == 2: 
                        UseAttack(GNamTwo.attacktwo,GNamTwo.x,GNamTwo.y,GNamTwo)
                        TurnsLeft = 0
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
                    elif std.scr.getch() == 3: 
                        UseAttack(GNamTwo.attackthree,GNamThree.x,GNamThree.y,GNamTwo)
                        TurnsLeft = 0
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):

            #Use Item

            if BNamOne != None:
                for i in range (9):
                    for j in range (9):
                        Arena[i][j] = Ground
                GLoc1 = (GNamOne.x,GNamOne.y)
                GLoc2 = (GNamTwo.x,GNamTwo.y)
                GLoc3 = (BNamOne.x,BNamOne.y)
                GLoc4 = (BNamTwo.x,BNamTwo.y)
                Arena[GNamOne.y][GNamOne.x] = GNamOne
                Arena[GNamTwo.y][GNamTwo.x] = GNamTwo
                Arena[BNamOne.y][BNamOne.x] = BNamOne
                Arena[GNamTwo.y][GNamTwo.x] = BNamTwo
                TurnsLeft = BNamOne.speed
                while(TurnsLeft > 0):
                    Decision = random.randint(0, 6)
                    if Decision == 0 and BNamOne.x != 0:
                        BNamOne.x -= 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
                    elif Decision == 1 and BNamOne.x != 8:
                        BNamOne.x += 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
                    elif Decision == 2 and BNamOne.x != 0:
                        BNamOne.y -= 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
                    elif Decision == 3 and BNamOne.x != 8:
                        BNamOne.y += 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
                    elif Decision == 4:
                        UseAttack(BNamOne.attackone,BNamOne.x,BNamOne.y,BNamOne)
                        TurnsLeft = 0
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
                    elif Decision == 5: 
                        UseAttack(BNamOne.attacktwo,BNamOne.x,BNamOne.y,BNamOne)
                        TurnsLeft = 0
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
                    elif Decision == 6:
                        UseAttack(BNamOne.attackthree,BNamOne.x,BNamOne.y,BNamOne)
                        TurnsLeft = 0
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
        
         


            if BNamTwo != None:
                for i in range (9):
                    for j in range (9):
                        Arena[i][j] = Ground
                GLoc1 = (GNamOne.x,GNamOne.y)
                GLoc2 = (GNamTwo.x,GNamTwo.y)
                GLoc3 = (BNamOne.x,BNamOne.y)
                GLoc4 = (BNamTwo.x,BNamTwo.y)
                Arena[GNamOne.y][GNamOne.x] = GNamOne
                Arena[GNamTwo.y][GNamTwo.x] = GNamTwo
                Arena[BNamOne.y][BNamOne.x] = BNamOne
                Arena[GNamTwo.y][GNamTwo.x] = BNamTwo
                TurnsLeft = GNamTwo.speed
                while(TurnsLeft > 0):
                    Decision = random.randint(0, 6)
                    if Decision == 0 and BNamTwo.x != 0:
                        BNamTwo.x -= 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
                    elif Decision == 1 and BNamTwo.x != 8:
                        BNamTwo.x += 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
                    elif Decision == 2 and BNamTwo.x != 0:
                        BNamTwo.y -= 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
                    elif Decision == 3 and BNamTwo.x != 8:
                        BNamTwo.y += 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
                    elif Decision == 4:
                        UseAttack(BNamTwo.attackone,BNamTwo.x,BNamTwo.y,BNamTwo)
                        TurnsLeft = 0
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
                    elif Decision == 5: 
                        UseAttack(BNamTwo.attacktwo,BNamTwo.x,BNamTwo.y,BNamTwo)
                        TurnsLeft = 0
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
                    elif Decision == 6: 
                        UseAttack(BNamTwo.attackthree,BNamTwo.x,BNamTwo.y,BNamTwo)
                        TurnsLeft = 0
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):





    def UseAttack(Attack,x,y,ANamikan):
        global GoodSoulCatch
        if Attack == "Force Projection":
            if std.scr.getch() == w:
                for i in range (9):
                    if type(Arena[y-i][x]) == BattleNamikan:
                        Namikan.life -= int(math.ceil(20*(ANamikan.attack/Arena[y-i][x].defense)))
            elif std.scr.getch() == s:
                for i in range (9):
                    if type(Arena[y+i][x]) == BattleNamikan:
                        Namikan.life -= int(math.ceil(20*(ANamikan.attack/Arena[y+i][x].defense)))
            elif std.scr.getch() == a:
                for i in range (9):
                    if type(Arena[y][x-i]) == BattleNamikan:
                        Namikan.life -= int(math.ceil(20*(ANamikan.attack/Arena[y][x-i].defense)))
            elif std.scr.getch() == d:
                for i in range (9):
                    if type(Arena[y][x+i]) == BattleNamikan:
                        Namikan.life -= int(math.ceil(20*(ANamikan.attack/Arena[y][x+i].defense)))
        if Attack == "Circle Cut":
            if type(Arena[y][x-1]) == BattleNamikan:
                        Namikan.life -= int(math.ceil(30*(ANamikan.attack/Arena[y][x-1].defense)))
            if type(Arena[y][x+1]) == BattleNamikan:
                        Namikan.life -= int(math.ceil(30*(ANamikan.attack/Arena[y][x+1].defense)))
            if type(Arena[y-1][x]) == BattleNamikan:
                        Namikan.life -= int(math.ceil(30*(ANamikan.attack/Arena[y-1][x].defense)))
            if type(Arena[y+1][x]) == BattleNamikan:
                        Namikan.life -= int(math.ceil(30*(ANamikan.attack/Arena[y+1][x].defense)))
            if type(Arena[y+1][x-1]) == BattleNamikan:
                        Namikan.life -= int(math.ceil(30*(ANamikan.attack/Arena[y+1][x-1].defense)))
            if type(Arena[y-1][x+1]) == BattleNamikan:
                        Namikan.life -= int(math.ceil(30*(ANamikan.attack/Arena[y-1][x+1].defense)))
            if type(Arena[y-1][x-1]) == BattleNamikan:
                        Namikan.life -= int(math.ceil(30*(ANamikan.attack/Arena[y-1][x-1].defense)))
            if type(Arena[y+1][x+1]) == BattleNamikan:
                        Namikan.life -= int(math.ceil(30*(ANamikan.attack/Arena[y+1][x+1].defense))
        if Attack == "Ditty":
            if random.randint(0,2) == 0:
                if ANamikan == GNamOne:
                    GNamTwo.status = "Sleep"
                else:
                    GNamOne.status = "Sleep"
            elif random.randing(0,1) = 0:
                BNamOne.status = "Sleep"
            else:
                BNamTwo.status = "Sleep"
        if Attack == "Teleport":
            while(True):
                i = random.randint(0,8)
                j = random.randint(0,8)
                if Arena[i][j] == Ground:
                    ANamikan.x = i
                    ANamikan.y = j
                    break
        if Attack == "Soul Catch":
            if random.randint(0,3) != 3:
                GoodSoulCatch = True

    def ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo):
        CPrint(0,0,"+---------+")
        CPrint(1,0,"|.........|")
        CPrint(2,0,"|.........|")
        CPrint(3,0,"|.........|")
        CPrint(4,0,"|.........|")
        CPrint(5,0,"|.........|")
        CPrint(6,0,"|.........|")
        CPrint(7,0,"|.........|")
        CPrint(8,0,"|.........|")
        CPrint(9,0,"|.........|")
        CPrint(10,0,"+---------+")
        CPrint(GnamOne.y+1,GNamOne.x+1,"%")
        CPrint(GnamTwo.y+1,GNamTwo.x+1,"&")
        CPrint(BnamOne.y+1,BNamOne.x+1,"#")
        CPrint(BnamTwo.y+1,BNamTwo.x+1,"$")
                                                
                                            
                                            
                
                                
                

                
            
                
                
                
        
    
    
    

    
        
                        
        

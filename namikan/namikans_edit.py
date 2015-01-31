import math, curses, random

global foodstore
global Space
global SpaceDirtiness
global Namikans
global GoodSoulCatch
Space = 0
SpaceDirtiness = 0
foodstore = 0

def CPrint(text, y ,x):
    scr.addstr(y, x, text, curses.A_REVERSE)

def twodify(x,y):
    name = []
    for row in xrange(x): name +=[[0]*y]
    return name

class Namikan():
    def __init__(self, size, growth, growthrate, food, clean, sick, form, life, maxlife, abilityone, abilitytwo, attackone, attacktwo, attackthree, speed, status, breed, mate):
        self.size = size
        self.growth = growth
        self.growthrate = growthrate
        self.food = food
        self.sick = sick
        self.clean = clean
        self.breed = breed
        self.mate = mate
        self.form = form
        self.life = life
        self.maxlife = maxlife
        self.abilityone = abilityone
        self.abilitytwo = abilitytwo
        self.attackone = attackone
        self.attacktwo = attacktwo
        self.attackthree = attackthree
        self.speed = speed
        self.status = status

    def goodnight(Namikan, index, Namikans):
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
        if Namikan.life > Namikan.maxlife:
            Namikan.life = Namikan.maxlife
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
        if Namikan.abilityone or Namikan.abilitytown == "Apothecary":
            ANamikan.sick = random.choice(Namikans)
            for i in range (30):
                TNamikan = random.choice(Namikans)
                if TNamikan.sick > ANamikan.sick:
                    ANamikan = TNamikan
            ANamikan.sick -= 15
            if ANamikan.sick < 0:
                ANamikan.sick = 0
        if Namikan.abilityone or Namikan.abilitytwo == "Healer":
            ANamikan.life = random.choice(Namikans)
            for i in range (30):
                TNamikan = random.choice(Namikans)
                if TNamikan.life < ANamikan.life:
                    ANamikan = TNamikan
            ANamikan.life += 15
        if Namikan.abilityone or Namikan.abilitytwo == "Maternal":
            ANamikan = random.choice(Namikans)
            for i in range (30):
                TNamikan = random.choice(Namikans)
                if ((TNamikan.size/TNamikan.growth)*(TNamikan.Food/2)) < ((ANamikan.size/ANamikan.growth)*(TNamikan.Food/2)):
                    ANamikan = TNamikan
            if ANamikan.size < ANamikan.growth:
                ANamikan.food += 50
                Namikan.food -= 15
        
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
        NewNamikan = Namikan(1, NewGrowth, NewGrowthRate, 100, 100, 0, NewForm, 100, 100, NewAbilityOne, NewAbilityTwo, NewAttackOne, NewAttackTwo, NewAttackThree, NewSpeed, None, -40, None)
        Namikans.append(NewNamikan)





Forms = ["Occult", "Nostalgic", "Enigmatic", "Extraterrestrial", "Heraldic", "Seraph", "Bionic", "Ethereal", "Archtypal", "Beastiary"]

Abilities = ["Terrifying", "Apothecary", "Healer", "Maternal"]

Attacks = ["Soul Catch", "Ditty", "Teleport", "Velocity Turn", "Joust", "Healing Light", "Stabilize", "Spin Kick", "Diversion", "Spit Venom", "Circle Cut", "Force Projection"]

Items = ["Vital Potion", "Deionized Water", "Energetic Essence", "Firebloom Petals","Water"]

def UseBasicEquipment(Item):
    if Item == "Water":
        CPrint("You deionized some water.",0,0)
        return "Deionized Water"
    elif Item == "Firebloom Petals":
        CPrint("You grind the petals into a sparkly powder that seems to glow with energy.",0,0)
        return "Energetic Essence"
def UseBasicEquipmentTwo(ItemOne, ItemTwo):
    if (ItemOne == "Deionized Water" and ItemTwo == "Energetic Essence") or (ItemTwo == "Deionized Water" and ItemOne == "Energetic Essence"):
        CPrint("The powder dissolves in the water, imbuing it with a strange sense of vitality.",0,0)
        return "Vital Potion"

def UseItemOnNamikan(Item, Namikan):
    if Item == "Vital Potion":
        CPrint("The potion gives the Namikan a fleeting positive energy. It starts to heal.")
        Namikan.life += 10

def Feed(Namikan, Amount):
    if foodstore > Amount:
        foodstore -= Amount
        Namikan.food += Amount

def MuckOut():
    global SpaceDirtiness
    if SpaceDirtiness > 50:
        SpaceDirtiness -= 50
    else:
        SpaceDirtiness = 0

def Wash(Namikan):
    Namikan.clean += 20

def BullyTown(Namikan, Town, Ask):
    Town.fear += Namikan.size
    Town.fear += Namikan.clean
    Town.fear -= Namikan.sick
    Town.fear += (Namikan.life*2)
    Town.fear -= 100
    Town.anger += (town.population)*5
    if Namikan.form == "Occult" or "Beastiary":
        Town.fear += 75
        Town.fear -= Namikan.life
    if Namikan.form == "Nostalgic" or "Archtypal":
        Town.anger -= 50
    if Namikan.form == "Extraterrestrial":
        Town.fear += 125
    if Namikan.form == "Heraldic":
        Town.anger += 50
    if Namikan.form == "Seraph":
        Town.anger += 250
    if Namikan.abilityone == "Terrifying" or Namikan.abilitytwo == "Terrifying":
        Town.fear += 125
    if Town.anger < Town.fear:
        if Ask == "Choc":
            if Town.store > Town.fear:
                Player.Namichoc += Town.fear
                Town.store -= Town.fear
            elif Town.store <= Town.fear:
                Player.Namichoc += Town.store
                Town.store = 0
                Town.anger += 1000
        if Ask == "Coin":
            if (Town.population)*5 > Town.fear:
                Player.Namicoin += Town.population
                Town.fear -= (Town.population)*5
            elif (Town.population)*5 < Town.fear:
                Player.Namicoin += Town.population
                Town.fear -= (Town.population)*5
                Town.agner += 1000
    

def CheckBelly(Namikan):
    if ciel(Namikan.food/Namikan.size) > 1:
        CPrint("The Namikan lolls, its stomach distended with a more-than-full full meal.",0,0)
    elif Namikan.food/Namikan.size > 0.9:
        CPrint("The Namikan is content on a full stomach.",0,0)
    elif Namikan.food/Namikan.size > 0.5:
        CPrint("The Namikan appears satiated.",0,0)
    elif Namikan.food/Namikan.size > 0.2:
        CPrint("The Namikan growls as it begins to feel hunger.",0,0)
    elif Namikan.food/Namikan.size > 0.1:
        CPrint("The Namikan is agitated, its hunger apparent.",0,0)
    else:
        CPrint("The Namikan is weak with starvation.",0,0)

def CheckCleanliness(Namikan):
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

def CheckSickness(Namikan):
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

def CheckBreeding(Namikan):
    if Namikan.size != Namikan.growth:
        CPrint("The Namikan isn't mature enough to breed yet.",0,0)
    elif Namikan.breed/Namikan.size > 0.7:
        CPrint("The Namikan's belly is swollen with its unborn offspring.",0,0)
    elif Namikan.breed/Namikan.size > 0.3:
        CPrint("The Namikan's belly has appeared increasingly full lately.",0,0)
    elif Namikan.breed > 0:
        CPrint("Nothing much can be determined about the Namikan's reproductive state right now.",0,0)
    elif Namikan.breed > -4:
        CPrint("Nothing much can be determined about the Namikan's reproductive state right now.",0,0)
    elif Namikan.breed > -21:
        CPrint("Nothing much can be determined about the Namikan's reproductive state right now.",0,0)

def CheckLife(Namikan):
    if Namikan.life > 100:
        CPrint("There is something unnatural about the Namikan's extraordinary vitality.",0,0)
    elif Namikan.life > 90 or (Namikan.form == "Occult" and Namikan.life > 70) or (Namikan.form == "Nostalgic" and Namikan.life > 65):
        CPrint("The Namikan is in perfect health. You seem to be doing something right.",0,0)
    elif Namikan.life > 50:
        CPrint("The Namikan has suffered some injuries, but is bearing them with a cheerful resoluteness.",0,0)
    elif Namikan.life > 20:
        CPrint("The Namikan is seriously hurt. Its performance is starting to flag.",0,0)
    elif Namikan.life > 10:
        CPrint("The Namikan's valor in the face of its cuts, wounds, and various other injuries is amazing, but you doubt it can last much longer.",0,0)
    else:
        CPrint("The Namikan can barely go on. It might not make it too much farther.",0,0)


def CheckGeneral(Namikan):
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
        Status = Namikan.status
        return BattleNamikan(Size,Attack,Defense,Life,Namikan.abilityone,Namikan.abilitytwo,Namikan.attackone,Namikan.attacktwo,Namikan.attackthree,Namikan.speed, Status, 0, 0)

    def LeaveBattle(BattleNamikan, Namikan):
        Namikan.status = BattleNamikan.status
        Namikan.life = BattleNamikan.life
        
        
    

class Battle():
#      def __init__(self, size, growth, growthrate, food, clean, sick, form, life, abilityone, abilitytwo, attackone, attacktwo, attackthree, speed, breed, mate):

    def Battle(GNamOne,GNamTwo,BNamOne,BNamTwo):
        global GoodSoulCatch
        Arena = twodify(Arena)
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

            if GNamOne.life < 1 and GoodSoulCatch == False:
                GNamOne = None
            if GNamTwo.life < 1 and GoodSoulCatch == False:
                GNamTwo = None
            if BNamOne.life < 1 and BadSoulCatch == False:
                BNamOne = None
            if BNamTwo.life < 1 and BadSoulCatch == False:
                BNamTwo = None
            if GNamOne.life < 1 and GoodSoulCatch == True:
                GNamOne.life = 1
                GoodSoulCatch = False
            if GNamTwo.life < 1 and GoodSoulCatch == True:
                GNamTwo.life = 1
                GoodSoulCatch = False
            if BNamOne.life < 1 and BadSoulCatch == True:
                BNamOne.life = 1
                BadSoulCatch = False 
            if BNamTwo.life < 1 and BadSoulCatch == True:
                BNamTwo.life = 1
                BadSoulCatch = False

            
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
                if GNamOne.status == "Sleep":
                    if random.randint(0,1) == 0:
                        TurnsLeft = 0
                    else:
                        GNamOne.status = None
                if GNamOne.status == "Poisoned":
                    GNamOne.life -= random.randint(0,10)
                    if random.randint(0,3) == 3:
                        GNamOne.status = None
                while(TurnsLeft > 0):
                    if std.scr.getch() == w and GNamOne.x != 0:
                        GNamOne.x -= 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
                    elif std.scr.getch() == s and GNamOne.x != 8:
                        GNamOne.x += 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
                    elif std.scr.getch() == a and GNamOne.x != 0:
                        GNamOne.y -= 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
                    elif std.scr.getch() == d and GNamOne.x != 8:
                        GNamOne.y += 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
                    elif std.scr.getch() == 1:
                        UseAttack(GNamOne.attackone,GNamOne.x,GNamOne.y,GNamOne)
                        TurnsLeft = 0
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
                    elif std.scr.getch() == 2: 
                        UseAttack(GNamOne.attacktwo,GNamOne.x,GNamOne.y,GNamOne)
                        TurnsLeft = 0
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
                    elif std.scr.getch() == 3: 
                        UseAttack(GNamOne.attackthree,GNamOne.x,GNamOne.y,GNamOne)
                        TurnsLeft = 0
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)


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
                if GNamTwo.status == "Sleep":
                    if random.randint(0,1) == 0:
                        TurnsLeft = 0
                    else:
                        GNamTwo.status = None
                if GNamTwo.status == "Poisoned":
                    GNamTwo.life -= random.randint(0,10)
                    if random.randint(0,3) == 3:
                        GNamTwo.status = None
                while(TurnsLeft > 0):
                    if std.scr.getch() == w and GNamTwo.x != 0:
                        GNamTwo.x -= 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
                    elif std.scr.getch() == s and GNamTwo.x != 8:
                        GNamTwo.x += 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
                    elif std.scr.getch() == a and GNamTwo.x != 0:
                        GNamTwo.y -= 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
                    elif std.scr.getch() == d and GNamTwo.x != 8:
                        GNamTwo.y += 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
                    elif std.scr.getch() == 1:
                        UseAttack(GNamTwo.attackone,GNamTwo.x,GNamTwo.y,GNamTwo)
                        TurnsLeft = 0
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
                    elif std.scr.getch() == 2: 
                        UseAttack(GNamTwo.attacktwo,GNamTwo.x,GNamTwo.y,GNamTwo)
                        TurnsLeft = 0
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
                    elif std.scr.getch() == 3: 
                        UseAttack(GNamTwo.attackthree,GNamThree.x,GNamThree.y,GNamTwo)
                        TurnsLeft = 0
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)

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
                if BNamOne.status == "Sleep":
                    if random.randint(0,1) == 0:
                        TurnsLeft = 0
                    else:
                        BNamOne.status = None
                if BNamOne.status == "Poisoned":
                    BNamOne.life -= random.randint(0,10)
                    if random.randint(0,3) == 3:
                        BNamOne.status = None
                while(TurnsLeft > 0):
                    Decision = random.randint(0, 6)
                    if Decision == 0 and BNamOne.x != 0:
                        BNamOne.x -= 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
                    elif Decision == 1 and BNamOne.x != 8:
                        BNamOne.x += 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
                    elif Decision == 2 and BNamOne.x != 0:
                        BNamOne.y -= 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
                    elif Decision == 3 and BNamOne.x != 8:
                        BNamOne.y += 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
                    elif Decision == 4:
                        UseAttack(BNamOne.attackone,BNamOne.x,BNamOne.y,BNamOne)
                        TurnsLeft = 0
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
                    elif Decision == 5: 
                        UseAttack(BNamOne.attacktwo,BNamOne.x,BNamOne.y,BNamOne)
                        TurnsLeft = 0
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
                    elif Decision == 6:
                        UseAttack(BNamOne.attackthree,BNamOne.x,BNamOne.y,BNamOne)
                        TurnsLeft = 0
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
        
         


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
                if BNamTwo.status == "Sleep":
                    if random.randint(0,1) == 0:
                        TurnsLeft = 0
                    else:
                        BNamTwo.status = None
                if BNamTwo.status == "Poisoned":
                    BNamTwo.life -= random.randint(0,10)
                    if random.randint(0,3) == 3:
                        BNamTwo.status = None
                while(TurnsLeft > 0):
                    Decision = random.randint(0, 6)
                    if Decision == 0 and BNamTwo.x != 0:
                        BNamTwo.x -= 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
                    elif Decision == 1 and BNamTwo.x != 8:
                        BNamTwo.x += 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
                    elif Decision == 2 and BNamTwo.x != 0:
                        BNamTwo.y -= 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
                    elif Decision == 3 and BNamTwo.x != 8:
                        BNamTwo.y += 1
                        TurnsLeft -= 1
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
                    elif Decision == 4:
                        UseAttack(BNamTwo.attackone,BNamTwo.x,BNamTwo.y,BNamTwo)
                        TurnsLeft = 0
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
                    elif Decision == 5: 
                        UseAttack(BNamTwo.attacktwo,BNamTwo.x,BNamTwo.y,BNamTwo)
                        TurnsLeft = 0
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)
                    elif Decision == 6: 
                        UseAttack(BNamTwo.attackthree,BNamTwo.x,BNamTwo.y,BNamTwo)
                        TurnsLeft = 0
                        ShowBattle(Arena,GNamOne,GNamTwo,BNamOne,BNamTwo)




#Attacks = ["Soul Catch", "Ditty", "Teleport", "Velocity Turn", "Joust", "Healing Light", "Stabilize", "Spin Kick", "Diversion", "Spit Venom", "Circle Cut", "Force Projection"]

    def UseAttack(Attack,x,y,ANamikan, AONamikan):
        global GoodSoulCatch
        if Attack == "Force Projection":
            if std.scr.getch() == w:
                for i in range (1,9):
                    if type(Arena[y-i][x]) == BattleNamikan:
                        Damage(ANamikan,Arena[y-i][x],20,None,0)
                        break
            elif std.scr.getch() == s:
                for i in range (1,9):
                    if type(Arena[y+i][x]) == BattleNamikan:
                        Damage(ANamikan,Arena[y+i][x],20,None,0)
                        break
            elif std.scr.getch() == a:
                for i in range (1,9):
                    if type(Arena[y][x-i]) == BattleNamikan:
                        Damage(ANamikan,Arena[y][x-i],20,None,0)
                        break
            elif std.scr.getch() == d:
                for i in range (1,9):
                    if type(Arena[y][x+i]) == BattleNamikan:
                        Damage(ANamikan,Arena[y][x+i],20,None,0)
                        break
        elif Attack == "Circle Cut":
            if type(Arena[y][x-1]) == BattleNamikan:
                        Damage(ANamikan,Arena[y][x-1],30,None,0)
            if type(Arena[y][x+1]) == BattleNamikan:
                        Damage(ANamikan,Arena[y][x+1],30,None,0)
            if type(Arena[y-1][x]) == BattleNamikan:
                        Damage(ANamikan,Arena[y-1][x],30,None,0)
            if type(Arena[y+1][x]) == BattleNamikan:
                        Damage(ANamikan,Arena[y+1][x],30,None,0)
            if type(Arena[y+1][x-1]) == BattleNamikan:
                        Damage(ANamikan,Arena[y+1][x-1],30,None,0)
            if type(Arena[y-1][x+1]) == BattleNamikan:
                        Damage(ANamikan,Arena[y-1][x+1],30,None,0)
            if type(Arena[y-1][x-1]) == BattleNamikan:
                        Damage(ANamikan,Arena[y-1][x-1],30,None,0)
            if type(Arena[y+1][x+1]) == BattleNamikan:
                        Damage(ANamikan,Arena[y+1][x+1],30,None,0)
        elif Attack == "Ditty":
            if ANamikan == GNamOne or GNamTwo:
                if random.randint(0,2) == 0:
                    if ANamikan == GNamOne:
                        GNamTwo.status = "Sleep"
                    else:
                        GNamOne.status = "Sleep"
                elif random.randing(0,1) == 0:
                    BNamOne.status = "Sleep"
                else:
                    BNamTwo.status = "Sleep"
            if ANamikan == BNamOne or BNamTwo:
                if random.randint(0,2) == 0:
                    if ANamikan == BNamOne:
                        BNamTwo.status = "Sleep"
                    else:
                        BNamOne.status = "Sleep"
                elif random.randing(0,1) == 0:
                    GNamOne.status = "Sleep"
                else:
                    GNamTwo.status = "Sleep"
        elif Attack == "Teleport":
            while(True):
                i = random.randint(0,8)
                j = random.randint(0,8)
                if Arena[i][j] == Ground:
                    ANamikan.x = i
                    ANamikan.y = j
                    break
        elif Attack == "Soul Catch":
            if random.randint(0,3) != 3 and ANamikan == (GNamOne or GNamTwo):
                GoodSoulCatch = True
            elif random.randint(0,3) != 3 and ANamikan == (BNamOne or BNamTwo):
                BadSoulCatch = True
        elif Attack == "Velocity Turn":
            ANamikan.status = "Velocity Turn"
        elif Attack == "Joust":
            Done = False
            if std.scr.getch() == w:
                for i in range (1,9):
                    if type(Arena[y-i][x]) == Ground:
                        ANamikan.y -= 1
                        if type(Arena[y-i][x+1]) == BattleNamikan and Done == False:
                            Damage(ANamikan,Arena[y-i][x+1],40,None,0)
                            Done = True
                            break
                        elif type(Arena[y-i][x-1]) == BattleNamikan and Done == False:
                            Damage(ANamikan,Arena[y-i][x-1],40,None,0)
                            Done = True
                            break
            elif std.scr.getch() == s:
                for i in range (1,9):
                    if type(Arena[y+i][x]) == Ground:
                        ANamikan.y -= 1
                        if type(Arena[y+i][x-1]) == BattleNamikan and Done == False:
                            Damage(ANamikan,Arena[y+i][x+1],40,None,0)
                            Done = True
                            break
                        elif type(Arena[y+i][x-1]) == BattleNamikan and Done == False:
                            Damage(ANamikan,Arena[y+i][x-1],40,None,0)
                            Done = True
                            break
            elif std.scr.getch() == a:
                for i in range (1,9):
                    if type(Arena[y][x-i]) == Ground:
                        ANamikan.y -= 1
                        if type(Arena[y-1][x-i]) == BattleNamikan and Done == False:
                            Damage(ANamikan,Arena[y-1][x-i],40,None,0)
                            Done = True
                            break
                        elif type(Arena[y+1][x-i]) == BattleNamikan and Done == False:
                            Damage(ANamikan,Arena[y+1][x-i],40,None,0)
                            Done = True
                            break
            elif std.scr.getch() == d:
                for i in range (1,9):
                    if type(Arena[y][x+i]) == Ground:
                        ANamikan.y -= 1
                        if type(Arena[y-1][x+i]) == BattleNamikan and Done == False:
                            Damage(ANamikan,Arena[y+1][x+i],40,None,0)
                            Done = True
                            break
                        elif type(Arena[y+1][x+i]) == BattleNamikan and Done == False:
                            Damage(ANamikan,Arena[y-1][x+i],40,None,0)
                            Done = True
                            break
        elif Attack == "Healing Light":
            if random.randint(0,3) != 3:
                ANamikan.life -= 10
                AONamikan.life += int(30*(AONamikan.attack/ANamikan.defense))
        elif Attack == "Stabilize":
            ANamikan.status = "Stabilized"
        elif Attack == "Spin Kick":
            if type(Arena[y-1][x-1]) == BattleNamikan:
                        Damage(ANamikan,Arena[y-1][x-1],35,None,0)
            if type(Arena[y+1][x+1]) == BattleNamikan:
                        Damage(ANamikan,Arena[y+1][x+1],35,None,0)
            if type(Arena[y-1][x+1]) == BattleNamikan:
                        Damage(ANamikan,Arena[y-1][x+1],35,None,0)
            if type(Arena[y+1][x-1]) == BattleNamikan:
                        Damage(ANamikan,Arena[y+1][x-1],35,None,0)
            if type(Arena[y-2][x-2]) == BattleNamikan:
                        Damage(ANamikan,Arena[y-2][x-2],35,None,0)
            if type(Arena[y+2][x+2]) == BattleNamikan:
                        Damage(ANamikan,Arena[y+2][x+2],35,None,0)
            if type(Arena[y-2][x+2]) == BattleNamikan:
                        Damage(ANamikan,Arena[y-2][x+2],35,None,0)
            if type(Arena[y+2][x-2]) == BattleNamikan:
                        Damage(ANamikan,Arena[y+2][x-2],35,None,0)
        elif Attack == "Diversion":
            if ANamikan == GNamOne:
                GNamTwo.status = "Diverted"
            if ANamikan == BNamOne:
                BNamTwo.status = "Diverted"
            if ANamikan == GNamTwo:
                GNamOne.status = "Diverted"
            if ANamikan == BNamTwo:
                BNamOne.status = "Diverted"
        elif Attack == "Spit Venom":
            if std.scr.getch() == w:
                for i in range (1,2):
                    if type(Arena[y-i][x]) == BattleNamikan:
                        Damage(ANamikan,Arena[y-i][x],10,"Poisoned",70)
                        break
            elif std.scr.getch() == s:
                for i in range (1,2):
                    if type(Arena[y+i][x]) == BattleNamikan:
                        Damage(ANamikan,Arena[y+i][x],10,"Poisoned",70)
                        break
            elif std.scr.getch() == a:
                for i in range (1,2):
                    if type(Arena[y][x-i]) == BattleNamikan:
                        Damage(ANamikan,Arena[y][x-i],10,"Poisoned",70)
                        break
            elif std.scr.getch() == d:
                for i in range (1,2):
                    if type(Arena[y][x+i]) == BattleNamikan:
                        Damage(ANamikan,Arena[y][x+i],10,"Poisoned",70)
                        break

    def Damage(ANamikan, DNamikan, Power, Status, Probability):
            if DNamikan.status == "Velocity Turn":
                ANamikan.life -= int(Power*1.5*(DNamikan.attack/ANamikan.defense))
            elif ANamikan.status == "Stabilized":
                DNamikan.life -= int(Power*((ANamikan.attack+15)/DNamikan.defense))
                ANamikan.status = None
            elif DNamikan.status == "Stabilized":
                DNamikan.life -= int(Power*(ANamikan.attack/(DNamikan.defense+15)))
                ANamikan.status = None
            elif DNamikan.status == "Diverted":
                if DNamikan == GNamOne and GNamTwo.status != "Diverted":
                    Damage(ANamikan, GNamTwo, Power, Status, Probability)
                if DNamikan == GNamTwo and GNamOne.status != "Diverted":
                    Damage(ANamikan, GNamOne, Power, Status, Probability)
                if DNamikan == BNamOne and BNamTwo.status != "Diverted":
                    Damage(ANamikan, BNamTwo, Power, Status, Probability)
                if DNamikan == BNamTwo and BNamOne.status != "Diverted":
                    Damage(ANamikan, BNamOne, Power, Status, Probability)
            else:
                DNamikan.life -= int(Power*(ANamikan.attack/DNamikan.defense))
            if random.randint(0,100) <= Probability and Status != None:
                DNamikan.status = Status
                            

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

#Manaris and Girgis CRP
#FreeRunner
#Nicholas,David
#avoid the upcoming enemies by jumping over the enemies
#objects and intitial settings

from gamelib import*

game = Game(1000,600,"Free Runner")

#bk stuff
bk=Image("bkgame.png",game)
bk.resizeTo(game.width,game.height)
game.setBackground(bk)

#platform stuff
platform=Image("platform.png",game)
platform.resizeBy(-75)
platform.x=900
platform.y=365
platform.setSpeed(3,90)
onplatform= False
jumping = False #Used to check to see if you are jumping
landed = False  #Used to check to see if you have landed on the "ground" (platform)
factor = 1  #Used for a slowing effect of the jumping

#james stuff
james=Animation("Walksequence_spritesheet.png.",30,game,1440/6,1480/5)
james.resizeBy(-60)
james.x=100
james.y=525
james.setSpeed(3,270)
jumping = False #Used to check to see if you are jumping
landed = False  #Used to check to see if you have landed on the "ground" (platform)
factor = 1  #Used for a slowing effect of the jumping

#street stuff
#street=Image("street.jpg",game)
#street.moveTo(game.width,game.height-50)
#street.resizeBy(-60)
#street.x=100
#street.y=585

#bottle stuff
bottle=Image("gbottle.png",game)

#enemy stuff
enemy1=Animation("Enemy1.png",40,game,1298/5,2070/8)
enemy1.resizeBy(-60)
enemy1.x=900
enemy1.y=525
enemy1.setSpeed(3,90)

enemy2=Animation("Enemy2.png",12,game,1380/3,1380/4)
enemy2.resizeBy(-100)
enemy2.x=700
enemy2.y=450
enemy2.setSpeed(3,450)

enemy3=Animation("Enemy 3.png",9,game,1380/3,1035/3)
enemy3.resizeBy(-60)
enemy3.x=800
enemy3.y=525
enemy3.setSpeed(3,450)

#bystander stuff
bystander=Animation("bystander.png",12,game,1380/3,1840/4)
bystander.resizeBy(-44)
bystander.x=1000
bystander.y=525
bystander.setSpeed(22,450)

#titlescreen stuff
titlescreen=Image("Titlescreen.PNG",game)
titlescreen.resizeTo(game.width,game.height)

#game...lol
while not game.over:
        game.processInput()
        game.scrollBackground("left",4)
        #street.draw()
        platform.move()
        james.draw()
        if james.y< 525 and not onplatform:#value of y is based on your object's y position
                landed = False#not landed

        else:
                landed = True
   
            
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
                jumping = True

        if jumping:
   
                james.y -=27*factor#adjust for the drop
                #Make the character go up.  Factor creates a slowing effect to the jump
                factor*=.95#fall slowly
                landed = False
                #Since you are jumping you are no longer staying on land
                if factor < .18:
                    jumping = False
                    #Stop jumping once the slowing effect finishes
                    factor = 1
            
        if not landed: #is jumping
                james.y +=6#adjust for the height of the jump - lower number higher jump

        if james.collidedWith(platform,"rectangle")and james.x>platform.left and james.x<platform.right and james.y>platform.top and james.y<platform.y+30:
                onplatform = True

    #After landing, added if the object moves off the platform from the right or left   
        if onplatform and james.x>platform.right and not jumping:#character has landed on ramp and moves off to the right and is not jumping (to start tbe jumping test again)
                onplatform = False
                james.y +=6 #adjust as needed (lower number higher jump)


        if platform.isOffScreen("left"):
                y = randint(300,400)
                platform.moveTo(game.width,y)
                platform.speed +=0
                platform.visible = True

        if enemy1.isOffScreen("left"):
                y =525
                enemy1.moveTo(game.width,y)
                enemy1.speed +=0
                enemy1.visible = True

        enemy1.move()
        enemy2.move()
        enemy3.move()
        bystander.move()

        if keys.Pressed[K_RIGHT]:
                james.x+=3

        if keys.Pressed[K_LEFT]:
                james.x-=3

        game.update(30)

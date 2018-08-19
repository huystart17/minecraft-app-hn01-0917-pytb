from mcpi import minecraft
from lib import Building
from lib import Player
from lib import Goods
from lib import Nature

mc =minecraft.Minecraft.create('10.15.0.194')
mc.postToChat("hello")
pl = Player.MinePLayer(mc,"mai")
# pl.setPos(100,200,100)
x,y,z = pl.getPos()
# Building.bao_house(mc,x,y,z)
# Nature.volcano(mc,x,y,z)  
bd = Building.Building(mc,x,y,z)

while True:
           chatEvents = mc.events.pollChatPosts()
           for chatEvent in chatEvents:
               print (chatEvent.message)
               msg = chatEvent.message
               msg =msg.split(' ')
               thing = msg[0]
               length = msg[1]
               if thing =='house':
                      pl = Player.MinePLayer(minecraft_connect=mc,id=chatEvent.entityId)
                      x,y,z = pl.getMySight(int(length))
                      bd = Building.Building(mc,x,y,z)
                      bd.big_house(155)
               elif thing =='tree':
                      pl = Player.MinePLayer(minecraft_connect=mc,id=chatEvent.entityId)
                      x,y,z = pl.getMySight(int(length))
                      Nature.treeKien(mc,x,y,z)
           

# Goods.door(mc,x,y,z)

from mcpi import minecraft
from lib import Building
from lib import Player
from lib import Goods
from lib import Nature
from mcpi import vec3
import time
import math

mc =minecraft.Minecraft.create()
mc.postToChat("hello ")
mc.postToChat("Neu ban tien len 10 buoc nua, thi mot ngoi nha se xuat hien ")

pl = Player.MinePLayer(mc,"gg")
x_root,y_root,z_root = pl.getPos() 
# pl.setPos(100,200,100)
print(pl.id)
def firecurse ():
    while True: 
        x,y,z = pl.getPos()
        dt =mc.getBlockWithData(x,y-1,z)
        if dt.id == 155:
            Building.fireroad(mc,x-10,y,z-10)
        time.sleep(0.5)
        mc.postToChat("{}".format(dt.id))
        chatEvents = mc.events.pollChatPosts()
        for chatEvent in chatEvents:
            if chatEvent.message == 'forgiveme':
                mc.events.clearAll()
                return True

def chatPower(): 
    while True : 
        chatEvents = mc.events.pollChatPosts()
        for chatEvent in chatEvents:
            if chatEvent.message == 'house':
                x,y,z = pl.getMySight()
                Building.bao_house(mc,x,y,z)
                mc.postToChat("da xay xong")
                mc.events.clearAll()
            elif chatEvent.message =='tree':
                x,y,z = pl.getMySight()
                Nature.treeKien(mc,x,y,z)
                mc.events.clearAll()
            elif chatEvent.message =='volcano':
                x,y,z = pl.getMySight()
                Nature.volcano(mc,x,y,z)
                mc.events.clearAll()
            elif chatEvent.message =='fence':
                x,y,z = pl.getMySight()
                Goods.fence_z(mc,x,y,z)
                mc.events.clearAll()
            elif chatEvent.message =='fireroad':
                x,y,z = pl.getMySight()
                Building.fireroad(mc,x,y,z)
                mc.events.clearAll()
            elif chatEvent.message =='firecurse':
                mc.events.clearAll()
                firecurse()

chatPower() 
# Nature.volcano(mc,x,y,z)  
# bd = Building.Building(mc,x,y,z)
# bd.change_material(40)x
# bd.small_house()

# Goods.door(mc,x,y,z)
# x= x-5
# z = z-5
# mc.setBlocks(x+1,y,z,x+1,y+10,z,1)
# mc.setBlocks(x-1,y,z,x-1,y+10,z,1)
# mc.setBlocks(x,y,z,x,y+10,z-1,1)

# mc.setBlocks(x,y,z,x,y+10,z,65,3)



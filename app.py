from mcpi import minecraft
from lib import Building
from lib import Player
from lib import Goods
from lib import Nature

mc =minecraft.Minecraft.create('10.15.0.175')
mc.postToChat("hello")
pl = Player.MinePLayer(mc,"gg")
# pl.setPos(100,200,100)
x,y,z = pl.getPos()
# Building.bao_house(mc,x,y,z)
# Nature.volcano(mc,x,y,z)  
# bd = Building.Building(mc,x,y,z)
# bd.change_material(40)
# bd.small_house()

# Goods.door(mc,x,y,z)
x= x-5
z = z-5
# mc.setBlocks(x+1,y,z,x+1,y+10,z,1)
# mc.setBlocks(x-1,y,z,x-1,y+10,z,1)
# mc.setBlocks(x,y,z,x,y+10,z-1,1)

# mc.setBlocks(x,y,z,x,y+10,z,65,3)



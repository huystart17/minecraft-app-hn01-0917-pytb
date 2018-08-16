from mcpi import minecraft
from lib import Building
from lib import Player
from lib import Goods
from lib import Nature

mc =minecraft.Minecraft.create()
mc.postToChat("hello")
pl = Player.MinePLayer(mc,"gg")
# pl.setPos(100,200,100)
x,y,z = pl.getPos()

Nature.volcano(mc,x,y,z)  
bd = Building.Building(mc,x,y,z)
bd.small_house()

Goods.door(mc,x,y,z)
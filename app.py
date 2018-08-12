from mcpi import minecraft
from lib import Building
from lib import Player
from lib import Goods
from lib import Nature

mc =minecraft.Minecraft.create("10.15.0.75")
mc.postToChat("hello")
pl = Player.MinePLayer(mc,"123")
x,y,z = pl.getPos()

Nature.waterfall(mc,x,y,z)

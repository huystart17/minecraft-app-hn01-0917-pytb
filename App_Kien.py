from mcpi import minecraft
from lib import Nature

mc = minecraft.Minecraft.create('10.15.0.202')
x,y,z = mc.player.getPos()
Nature.lake(mc,x,y,z)
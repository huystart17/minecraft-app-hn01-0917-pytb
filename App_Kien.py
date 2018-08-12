from mcpi import minecraft
from lib import Nature


mc = minecraft.Minecraft.create('10.15.0.75')
x,y,z = mc.player.getPos()
mc.postToChat("ádfsad")
Nature.lake(mc,x,y,z)   

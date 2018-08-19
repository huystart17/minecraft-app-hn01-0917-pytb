from mcpi import minecraft
from lib import Building
from lib import Player
from lib import Goods
from lib import Nature

mc = minecraft.Minecraft.create('10.15.0.194')
mc.postToChat("hello")
pl = Player.MinePLayer(mc, "aaaaa")

while True:
    chatEvents = mc.events.pollChatPosts()
    for chatevent in chatEvents:
        if (chatevent.message == "pillar"):
            pl = Player.MinePLayer(minecraft_connect=mc, id=chatevent.entityId)
            x, y, z = pl.getMySight(10)
            Building.pillars(mc, x, y, z)
            mc.events.clearAll()

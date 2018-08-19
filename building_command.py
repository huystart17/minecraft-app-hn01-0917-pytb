from mcpi import minecraft
from lib import Building
from lib import Player
from lib import Goods
from lib import Nature
from lib import SimpleBuilding

mc =minecraft.Minecraft.create('10.15.0.194')

while True:
    chats=mc.events.pollChatPosts()
    for chat in chats:
        if chat.message=='firecurse':
            pl=Player.MinePLayer(minecraft_connect=mc,id=chat.entityId)
            x,y,z=pl.getMySight(5)
            SimpleBuilding.Lhouse(mc,x,y,z)
            print(chat)

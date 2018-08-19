from mcpi import minecraft
from lib import Building
from lib import Player
from lib import Goods
from lib import Nature

mc =minecraft.Minecraft.create('10.15.0.194')

while True:
    chats=mc.events.pollChatPosts()
    for chat in chats:
        if chat.message!='':
            pl=Player.MinePLayer(minecraft_connect=mc,id=chat.entityId)
            x,y,z=pl.getMySight(10)
            Nature.island(mc,x,y,z)
            print(chat)

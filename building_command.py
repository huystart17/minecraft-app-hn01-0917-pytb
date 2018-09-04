from mcpi import minecraft
from lib import Building
from lib import Player
from lib import Goods
from lib import Nature
from lib import SimpleBuilding
from lib import Game
mc =minecraft.Minecraft.create()

while True:
    chats=mc.events.pollChatPosts()
    for chat in chats:
        if chat.message!='':
            pl=Player.MinePLayer(minecraft_connect=mc,id=chat.entityId)
            x,y,z=pl.getMySight(15)
            Game.arena(mc,x,y,z)
            print(chat)

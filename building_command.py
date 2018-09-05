from mcpi import minecraft
import time
from lib import Game
from lib import Player
mc =minecraft.Minecraft.create()
a=0
while True:
    chats=mc.events.pollChatPosts()
    for chat in chats:
        if chat.message=='game':
            pl=Player.MinePLayer(minecraft_connect=mc,id=chat.entityId)
            x,y,z=pl.getMySight(15)
            Game.arena(mc,x,y,z)
            print(chat)
            a=1
            break
    if a==1:
        break

print('aaaaaa')
ids=mc.getPlayerEntityIds()
pls=[]
for id in ids:
    pl=Player.MinePLayer(minecraft_connect=mc,id=id)
    pls.append(pl)

while True:
    time.sleep(4)
    for p in pls:
        x,y,z=p.getPos()
        if mc.getBlock(x,y-1,z)==57:
            mc.setBlock(x,y-1,z,0)
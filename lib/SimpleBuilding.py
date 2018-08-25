from lib import Goods
def Lhouse(mc,x,y,z):
    mc.setBlocks(x-10,y-1,z-10,x+10,y+6,z+10,57)
    mc.setBlocks(x-9,y-1,z-9,x+9,y-1,z+9,169)
    mc.setBlocks(x-10,y-1,z-10,x-1,y+6,z-1,0)
    mc.setBlocks(x+1,y,z-9,x+9,y+5,z+9,0)
    mc.setBlocks(x-9,y,z+1,x+9,y+5,z+9,0)
    Goods.bed(mc,x+9,y,z+8)
    Goods.table(mc,x+3,y,z+3)
    Goods.door(mc,x+10,y,z+1)
    mc.setBlocks(x+1,y,z-9,x+9,y+5,z-9,47)


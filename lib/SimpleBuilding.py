from lib import Goods
def Lhouse(mc,x,y,z):
    mc.setBlocks(x-10,y-1,z-10,x+10,y+6,z+10,57)
    mc.setBlocks(x-9,y-1,z-9,x+9,y-1,z+9,169)
    mc.setBlocks(x-10,y-1,z-10,x-1,y+6,z-1,0)
    mc.setBlocks(x+1,y,z-9,x+9,y+5,z+9,0)
    mc.setBlocks(x-9,y,z+1,x+9,y+5,z+9,0)
    Goods.bed(mc,x+9,y,z+8)
    for a in range(4):
        Goods.table(mc,x+2+a*2,y,z-5)
    Goods.door(mc,x+10,y,z+1)
    mc.setBlocks(x+1,y,z-9,x+9,y+5,z-9,47)
    mc.setBlocks(x-9,y,z+1,x-8,y+5,z+9,41)
    mc.setBlocks(x-8,y+1,z+2,x-8,y+4,z+8,20)
    mc.setBlocks(x-9,y+1,z+2,x-9,y+4,z+8,10)




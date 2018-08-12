import random

def tree(mc,x,y,z):
    mc.setBlocks(x+2,y,z,x+2,y+4,z,17)
    mc.setBlocks(x-1,y+4,z-3,x+5,y+4,z+3,18)
    mc.setBlocks(x,y+5,z-2,x+4,y+5,z+2,18)
    mc.setBlocks(x+1,y+6,z-1,x+3,y+6,z+1,18)
    mc.setBlocks(x-1,y+4,z-3,x+5,y+6,z+3,18)

def treeKien(mc,x,y,z):
    mc.setBlocks(x,y+3,z,x+4,y+4,z+4,18)
    mc.setBlocks(x+1,y+5,z+1,x+3,y+6,z+3,18)
    mc.setBlock(x,y+3,z,0)
    mc.setBlock(x+4,y+3,z,0)
    mc.setBlock(x,y+3,z+4,0)
    mc.setBlock(x+4,y+3,z+4,0)
    mc.setBlock(x+1,y+6,z+1,0)
    mc.setBlock(x+3,y+6,z+1,0)
    mc.setBlock(x+1,y+6,z+3,0)
    mc.setBlock(x+3,y+6,z+3,0)
    mc.setBlocks(x+2,y,z+2,x+2,y+4,z+2,17)
def lake(mc,x,y,z):
    for i in range(10):
        mc.setBlocks(x - random.randint(3,5),y,z+i
        ,x + random.randint(3,5),y+10,z+i,46)


def volcano(mc,x,y,z):
    for i in range(10):
        mc.setBlocks(x+1+i,y,z+1+i,x+31-i,y,z+31-i,1)

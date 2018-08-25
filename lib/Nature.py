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
#Dirt
    mc.setBlocks(x,y+10,z,x+20,y+10,z+20,2)
    mc.setBlocks(x,y+11,z,x+2,y+11,z+21)
    mc.setBlocks(x,y,z,x+20,y+9,z+20,3)
#Water
    mc.setBlocks(x+12,y+10,z+4,x+8,y+10,z+4,8)
    mc.setBlocks(x+13,y+10,z+5,x+7,y+10,z+5,8)
    mc.setBlocks(x+14,y+10,z+6,x+6,y+10,z+6,8)
    mc.setBlocks(x+15,y+10,z+7,x+5,y+10,z+7,8)
    mc.setBlocks(x+16,y+10,z+8,x+4,y+10,z+8,8)
    


def volcano(mc,x,y,z):
    for i in range(16):
        mc.setBlocks(x+1+i,y+i,z+1+i,x+31-i,y+i,z+31-i,1)
    mc.setBlock(x+16,y+16,z+16,10)
    tree(mc,x+5,y+5,z+5)
 
def forest(mc,x,y,z):
    for i in range (0,15,5):
        for j in range (0,15,5):
            tree(mc,x-5+ i,y,z -5 +j)

def island (mc,x,y,z):
    mc.setBlocks(x-10,y-5,z-10,x+10,y,z+10,2)
    mc.setBlocks(x-5,y-4,z-5,x+5,y,z+5,9)
    mc.setBlocks(x-6,y-3,z-4,x-6,y,z+4,9)
    mc.setBlocks(x+6,y-3,z-4,x+6,y,z+4,9)
    mc.setBlocks(x-4,y-3,z-6,x-4,y,z-6,9)
    mc.setBlocks(x+4,y-3,z+6,x+4,y,z+6,9)
    mc.setBlocks(x-1,y-1,z-1,x+1,y+1,z+1,2)
    treeKien(mc,x-2,y+2,z-2)

#fix lỗi
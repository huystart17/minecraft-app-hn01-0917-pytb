def book(mc,x,y,z):
    mc.setBlocks( x,y,z, x,y,z, 47)
def bed(mc,x,y,z):
    mc.setBlocks( x+10,y,z, x+12,y,z, 355)
    mc.setBlock(x, y, z, 26, 0)
    mc.setBlock(x, y, z + 1, 26, 8)
def door(mc,x,y,z):
    x =int(x)
    y = int(y)
    z= int(z)
    mc.setBlock(x,y,z,64,0)
    mc.setBlock(x, y+1, z, 64, 8)
def Furnace(mc,x,y,z):
    mc.setBlocks(x,y,z,x,y,z,61)

def table(mc,x,y,z):
    mc.setBlocks(x,y+1,z,x,y+1,z,72)
    mc.setBlocks(x,y,z,x,y,z,85)

def fence_z (mc,x,y,z):
    mc.setBlocks(x,y,z,x,y,z+10,113 )

def lavapool(mc,x,y,z):
    mc.setBlocks(x-5,y-5,z-5,x+1,y,z+1,1)
    mc.setBlocks(x-4,y-4,z-4,x,y-1,z,10)
    mc.setBlocks(x-2,y+1,z-2,46)

def beacon(mc,x,y,z):
    mc.setBlocks(x-1,y,z-1,x+1,y,z+1,57)
    mc.setBlock(x,y+1,z,138)


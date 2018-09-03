import math
def distance(mc,x1,y1,z1,x2,y2,z2):
    dis=math.sqrt((x1-x2)^2+(y1-y2)^2+(z1-z2)^2)
    return dis

def midpoint(mc,x1,y1,z1,x2,y2,z2):
    x=(x1+x2)/2
    y=(y1+y2)/2
    z=(z1+z2)/2
    return[x,y,z]
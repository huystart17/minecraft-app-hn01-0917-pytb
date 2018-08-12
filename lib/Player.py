class MinePLayer ():
  def __init__(self, minecraft_connect, player_name):
    self.conn = minecraft_connect
    self.name = player_name
    self.id = minecraft_connect.getPlayerEntityId(player_name)

  def setPos (self,x,y,z):
    sc = self.conn
    sc.entity.setPos(self.id, x,y,z)

  def getPos (self):
    sc = self.conn
    x,y,z = sc.entity.getPos(self.id)
    return (x,y,z)

  def getMySight(self):
    sc = self.conn
    x,y,z = sc.entity.getPos(self.id)
    x1, y1, z1 = sc.entity.getDirection(self.id)
    return (x + x1 * 2, y + y1* 2, z +z1*2 )

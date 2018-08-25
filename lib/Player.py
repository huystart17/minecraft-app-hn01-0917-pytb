class MinePLayer ():
  def __init__(self, minecraft_connect, player_name='unname', id =''):
    self.conn = minecraft_connect
    self.name = player_name
    if(len(str(id)) > 0):
      self.id = id
    else:
      self.id = minecraft_connect.getPlayerEntityId(player_name)

  def setPos (self,x,y,z):
    sc = self.conn
    sc.entity.setPos(self.id, x,y,z)

  def getPos (self):
    sc = self.conn
    x,y,z = sc.entity.getPos(self.id)
    return (x,y,z)

  def getMySight(self,length =3 ):
    sc = self.conn
    x,y,z = sc.entity.getPos(self.id)
    x1, y1, z1 = sc.entity.getDirection(self.id)

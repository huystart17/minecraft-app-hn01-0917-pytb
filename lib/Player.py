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
<<<<<<< HEAD
    return (x + x1 * 10, y + y1* 10, z +z1*10 )
=======
    return (x + x1 * length, y + y1* length, z +z1*length )

>>>>>>> 57c53a6fd181408c2526471a0063ba7c21d5f28a

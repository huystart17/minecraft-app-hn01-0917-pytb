class Building():

    def __init__(self,mc,x,y,z):

        self.mc=mc

        self.x=x

        self.y=y

        self.z=z

    def small_house(self):

        x=self.x

        y=self.y

        z=self.z

        mc =self.mc

        mc.setBlocks(x,y-1,z,x+10,y+5,z+10,155)

        mc.setBlocks(x+1,y,z+1,x+9,y+4,z+9,0)



        #den

        mc.setBlocks(x+9,y,z+1,x+9,y,z+1,89)

        mc.setBlocks(x+7,y,z+9,x+9,y+4,z+9,89)

        #cua

        mc.setBlocks(x,y,z+5,x,y+1,z+5,0)

        mc.setBlocks(x,y+1,z+5,x,y+1,z+5,64,8)

        mc.setBlocks(x,y,z+5,x,y,z+5,64)

        mc.setBlocks(x-1,y-1,z+5,x-1,y-1,z+5,156)

        #cua so

        mc.setBlocks(x,y+2,z+2,x,y+3,z+3,102)

        mc.setBlocks(x,y+2,z+7,x,y+3,z+8,102)



        #ruong

        mc.setBlocks(x+4,y,z+9,x+3,y,z+9,54)

        mc.setBlocks(x+7,y,z+1,x+8,y,z+1,54)

        mc.setBlocks(x+7,y+1,z+1,x+8,y+1,z+1,96,1)

        #ban che tao

        mc.setBlocks(x+6,y,z+9,x+6,y,z+9,58)



        #lo ren

        mc.setBlocks(x+5,y,z+9,x+5,y+1,z+9,61)



        #giuong

        mc.setBlocks(x+7,y+1,z+2,x+7,y+1,z+2,26,7)

        mc.setBlocks(x+8,y+1,z+2,x+8,y+1,z+2,26,11)

        mc.setBlocks(x+7,y,z+3,x+9,y,z+2,5,5)

        mc.setBlocks(x+6,y,z+3,x+6,y,z+1,53)



        #ban

        mc.setBlocks(x+4,y,z+3,x+4,y,z+1,126,2)



        #sach

        mc.setBlocks(x+7,y+1,z+9,x+9,y+3,z+9,47)

   
    def big_house(self,block):

        x=self.x

        y=self.y

        z=self.z

        mc =self.mc

        #1

        mc.setBlocks(x,y-1,z,x+7,y+4,z+7,block)
        mc.setBlocks(x+2,y+2,z,x,y+1,z+4,95,3)#window
        mc.setBlocks(x+1,y,z+1,x+6,y+3,z+6,0)


        #2...

        mc.setBlocks(x,y+4,z,x+7,y+9,z+7,block)
        mc.setBlocks(x+2,y+6,z,x,y+7,z+4,95,3)#window
        mc.setBlocks(x+1,y+5,z+1,x+6,y+8,z+6,0)

        


        #ban cong
        mc.setBlocks(x,y+4,z,x-4,y+4,z+7,block)
        mc.setBlocks(x-4,y+5,z,x-1,y+5,z+7,102)
        mc.setBlocks(x-3,y+5,z+1,x-1,y+5,z+6,0)
        mc.setBlocks(x-4,y,z,x-4,y+4,z,block)



        #cua2
        mc.setBlocks(x,y+6,z+5,x,y+6,z+5,64,8)
        mc.setBlocks(x,y+5,z+5,x,y+5,z+5,64)


        #cua1

        mc.setBlocks(x,y,z+5,x,y+1,z+5,0)

        mc.setBlocks(x,y+1,z+5,x,y+1,z+5,64,8)

        mc.setBlocks(x,y,z+5,x,y,z+5,64)

        #khác

        mc.setBlocks(x-1,y-1,z+4,x-1,y+8,z+6,block)
        mc.setBlocks(x-1,y-1,z+5,x-1,y+8,z+5,0)
        mc.setBlocks(x-1,y+8,z-1,x+8,y+8,z+8,block)
        mc.setBlocks(x,y+4,z,x-4,y+4,z+7,block)

        #be boi
        mc.setBlocks(x,y-5,z-5,x-7,y-1,z+2,155)

        x=self.x

        y=self.y

        z=self.z

        mc =self.mc

        #1

        mc.setBlocks(x,y-1,z,x+10,y+5,z+10,155)

        mc.setBlocks(x+1,y,z+1,x+9,y+4,z+9,0)



        #2...

        mc.setBlocks(x+3,y+6,z,x+10,y+11,z+10,1)

        mc.setBlocks(x+1,y+6,z+1,x+8,y+10,z+9,0)

        #ban cong

        mc.setBlocks(x,y+6,z,x+1,y+6,z+10,85)









        #cua

        mc.setBlocks(x,y,z+5,x,y+1,z+5,0)

        mc.setBlocks(x,y+1,z+5,x,y+1,z+5,64,8)

        mc.setBlocks(x,y,z+5,x,y,z+5,64)


def bao_house(mc,x,y,z):
        

        #1

        mc.setBlocks(x,y-1,z,x+10,y+5,z+10,155)

        mc.setBlocks(x+1,y,z+1,x+9,y+4,z+9,0)
        mc.setBlocks(x+4,y+5,z+4,x+6,y+5,z+6,169)




        #ban cong

        mc.setBlocks(x,y+6,z,x,y+6,z+10,113)


        #thang
        # mc.setBlocks(x+9,y,z+4,x+9,y+5,z+4,49)
        mc.setBlocks(x+9,y,z+5,x+9,y+5,z+5,65)
        mc.setBlocks(x+9,y,z+6,x+9,y+5,z+6,49)






        #cua

        mc.setBlocks(x,y,z+5,x,y+1,z+5,0)

        mc.setBlocks(x,y+1,z+5,x,y+1,z+5,64,8)

        mc.setBlocks(x,y,z+5,x,y,z+5,64)

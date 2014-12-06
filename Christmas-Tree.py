from mcpi import minecraft, block
from time import sleep
mc = minecraft.Minecraft.create()

mc.postToChat("Hello")

# mc.postToChat("Your Coords are: "+str(x)+":"+str(y)+":"+str(z))

#flower = 38
#while True:
#	x,y,z = mc.player.getPos()
#	mc.setBlock(x,y,z,flower)
#	sleep(0.2)


tree = 17
leaves = 18
x,y,z = mc.player.getPos()
for i in range(0,7):
	if (i==2):
		for ii in range(0,5):
			mc.setBlock(x-4-ii,y+i,z,leaves)
			mc.setBlock(x-4+ii,y+i,z,leaves)
	if (i==3):
		for ii in range(0,4):
			mc.setBlock(x-4-ii,y+i,z,leaves)
			mc.setBlock(x-4+ii,y+i,z,leaves)
	if (i==4):
		for ii in range(0,3):
			mc.setBlock(x-4-ii,y+i,z,leaves)
			mc.setBlock(x-4+ii,y+i,z,leaves)
	if (i==5):
		for ii in range(0,2):
			mc.setBlock(x-4-ii,y+i,z,leaves)
			mc.setBlock(x-4+ii,y+i,z,leaves)
	if (i==6):
		for ii in range(0,1):
			mc.setBlock(x-4-ii,y+i,z,leaves)
			mc.setBlock(x-4+ii,y+i,z,leaves)
	
	if (i!=6):
		mc.setBlock(x-4,y+i,z,tree)
	else:
		mc.setBlock(x-4,y+i+1,z,leaves)

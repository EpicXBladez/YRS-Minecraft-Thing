from mcpi import minecraft, block
from time import sleep
mc = minecraft.Minecraft.create()

mc.postToChat("Hello")

# mc.postToChat("Your Coords are: "+str(x)+":"+str(y)+":"+str(z))

flower = 38
while True:
	x,y,z = mc.player.getPos()
	mc.setBlock(x,y,z,flower)
	sleep(0.2)

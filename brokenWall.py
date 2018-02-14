from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

walllength = 100
wallheight = 50

xcounter = 0
ycounter = 0

for height in range(wallheight):
    xcounter = 0
    for length in range(walllength):
        brokenBlocks = [48, 67, 4, 4, 4, 4]
        block = random.choice(brokenBlocks)
        mc.setBlock(x + xcounter, y + ycounter, z, block)
        xcounter += 1
    ycounter += 1
print("You are now property of the plup club")    
    
    

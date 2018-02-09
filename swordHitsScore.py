from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

name = " "
scoreboard = {}

while True:
    name = input("What is your name? ")
    if name =="exit":
        break
    mc.postToChat("Go!")

    time.sleep(20)

    blockHits = mc.events.pollBlockHits()

    blockHitsLength = len(blockHits)
    mc.postToChat("Your score is " + str(blockHitsLength))

    scoreboard = {str(name) + ": " + str(blockHitsLength) + " blocks"}

    print(scoreboard)

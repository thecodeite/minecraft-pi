import minecraft
mc = minecraft.Minecraft.create()
mc.postToChat("Hello Minecraft World!")

import block
import math

start = mc.player.getTilePos()
mc.postToChat("Building at " +  `start.x` + " " + `start.y`)

def buildFloor():
	sx = start.x-5
	sy = start.z-5
	ex = start.x+5
	ey = start.z+5

	mc.setBlocks(sx, start.y-1, sy, ex, start.y-1, ey, block.WOOD_PLANKS)

buildFloor()

def sq(sx, sy, height, blk):
	# mc.postToChat("Building at height height" +  `height`)

	for x in xrange(sx, sx+11):
		for y in xrange(sy, sy+11):
			if x == sx or x == sx+10 or y == sy or y == sy + 10:
				mc.setBlock(x, height, y, blk)
		#else:
		#		mc.setBlock(y, height, x, block.AIR)
def buildWalls():		
	for h in xrange(start.y, start.y + 10):
		
		if h%5 == 0:
			sq(start.x-5, start.z-5, h, block.GLASS)
		else:
			sq(start.x-5, start.z-5, h, block.STONE)
buildWalls()




def drange(start, stop, step):
	r = start
	while r < stop:
		yield r
		r += step


def drawSemiCircle(radius, xc, zc, yc):
	y = yc
	r2 = radius * radius
	for x in drange(-radius, radius, .1):
		
		z = math.sqrt(r2 - x*x) + 0.5

		#mc.postToChat(`xc+x`+ " " + `zc+z` + " " + `y`)
		mc.setBlock(xc+x, zc+z, y, block.WOOL)
		#3mc.setBlock(xc+x, height, yc-y, block.WOOL)

#mc.setBlocks
for z in xrange(start.z-5, start.z+5):
	drawSemiCircle(5, start.x, start.y+10, z)




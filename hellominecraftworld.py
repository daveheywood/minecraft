import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

minecraft_greeting="dad"

mc.postToChat("hello " +  minecraft_greeting)

mc.player.setPos(1,100,1)




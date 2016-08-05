import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

minecraft_greeting="dad"

mc.postToChat("hello " +  minecraft_greeting)

# xyz positions are
mc.player.setPos(8,10,8)




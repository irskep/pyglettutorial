import pyglet
import util

# Tell pyglet where to find the images
pyglet.resource.path = ['../images']
pyglet.resource.reindex()

# Load the three main images and get them to draw centered
player_image = pyglet.resource.image("player.png")
util.center_image(player_image)

bullet_image = pyglet.resource.image("bullet.png")
util.center_image(bullet_image)

asteroid_image = pyglet.resource.image("asteroid.png")
util.center_image(asteroid_image)

# The engine flame should not be centered on the ship. Rather, it should be shown 
# behind it. To achieve this effect, we just set the anchor point outside the
# image bounds.
engine_image = pyglet.resource.image("engine_flame.png")
engine_image.anchor_x = engine_image.width * 1.5
engine_image.anchor_y = engine_image.height / 2
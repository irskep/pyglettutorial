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
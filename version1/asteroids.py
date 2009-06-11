import pyglet, random, math
from game import load, resources

# Set up a window
game_window = pyglet.window.Window(800, 600)

# Set up the two top labels
score_label = pyglet.text.Label(text="Score: 0", x=10, y=575)
level_label = pyglet.text.Label(text="Version 1: Static Graphics", 
                                x=400, y=575, anchor_x='center')

# Initialize the player sprite
playership = pyglet.sprite.Sprite(img=resources.player_image, x=400, y=300)

# Make three sprites to represent remaining lives
player_lives = load.player_lives(3)

# Make three asteroids so we have something to shoot at 
asteroids = load.asteroids(3, (playership.x, playership.y))

@game_window.event
def on_draw():
    game_window.clear()
    
    playership.draw()
    for asteroid in asteroids:
        asteroid.draw()
    for ship_icon in player_lives:
        ship_icon.draw()
    
    level_label.draw()
    score_label.draw()

if __name__ == "__main__":
    # Tell pyglet to do its thing
    pyglet.app.run()

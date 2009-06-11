import pyglet, random
import resources, util

def player_lives(num_icons):
    """Generate sprites for player life icons"""
    player_lives = []
    start_x = 800 - 30 * num_icons
    for i in range(num_icons):
        new_sprite = pyglet.sprite.Sprite(img=resources.player_image, 
                                          x=start_x+i*30, y=585)
        new_sprite.scale = 0.5
        player_lives.append(new_sprite)
    return player_lives

def asteroids(num_asteroids, player_position):
    """Generate asteroid objects with random positions and velocities, not close to the player"""
    asteroids = []
    for i in range(num_asteroids):
        asteroid_x, asteroid_y = player_position
        while util.distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 600)
        new_asteroid = pyglet.sprite.Sprite(img=resources.asteroid_image, 
                                            x=asteroid_x, y=asteroid_y)
        new_asteroid.rotation = random.randint(0, 360)
        asteroids.append(new_asteroid)
    return asteroids

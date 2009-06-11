import pyglet, random, math
from game import load, player, resources

# Set up a window
game_window = pyglet.window.Window(800, 600)

main_batch = pyglet.graphics.Batch()

# Set up the two top labels
score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)
level_label = pyglet.text.Label(text="Version 3: Basic Collision", 
                                x=400, y=575, anchor_x='center', batch=main_batch)

# Initialize the player sprite
playership = player.Player(x=400, y=300, batch=main_batch)

# Make three sprites to represent remaining lives
player_lives = load.player_lives(3, main_batch)

# Make three asteroids so we have something to shoot at 
asteroids = load.asteroids(3, (playership.x, playership.y), main_batch)

# Store all objects that update each frame in a list
game_objects = [playership] + asteroids

# Tell the main window that the player object responds to events
game_window.push_handlers(playership.key_handler)

@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()

def update(dt):
    for obj in game_objects:
        obj.update(dt)
    
    # To avoid handling collisions twice, we employ nested loops of ranges.
    # This method also avoids the problem of colliding an object with itself.
    for i in xrange(len(game_objects)):
        for j in xrange(i+1, len(game_objects)):
            
            obj_1 = game_objects[i]
            obj_2 = game_objects[j]
            
            # Make sure the objects haven't already been killed
            if not obj_1.dead and not obj_2.dead:
                if obj_1.collides_with(obj_2):
                    obj_1.handle_collision_with(obj_2)
                    obj_2.handle_collision_with(obj_1)
    
    # Get rid of dead objects
    for to_remove in [obj for obj in game_objects if obj.dead]:
        # Remove the object from any batches it is a member of
        to_remove.delete()
        
        # Remove the object from our list
        game_objects.remove(to_remove)

if __name__ == "__main__":
    # Get the update() function to run 30 times a second
    pyglet.clock.schedule(update)
    
    # Tell pyglet to do its thing
    pyglet.app.run()

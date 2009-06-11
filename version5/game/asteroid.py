import random
import physicalobject, resources

class Asteroid(physicalobject.PhysicalObject):
    """An asteroid that divides a little before it dies"""
    
    def handle_collision_with(self, other_object):
        super(Asteroid, self).handle_collision_with(other_object)
        
        # Superclass handles deadness already
        if self.dead and self.scale > 0.25:
            num_asteroids = random.randint(2, 3)
            for i in xrange(num_asteroids):
                new_asteroid = Asteroid(resources.asteroid_image, 
                                        x=self.x, y=self.y, batch=self.batch)
                new_asteroid.rotation = random.randint(0, 360)
                new_asteroid.vx, new_asteroid.vy = random.random()*70, random.random()*70
                new_asteroid.vx += self.vx
                new_asteroid.vy += self.vy
                new_asteroid.scale = self.scale * 0.5
                self.new_objects.append(new_asteroid)
    
